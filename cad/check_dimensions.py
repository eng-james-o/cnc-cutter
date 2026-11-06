"""Check KCL layout arithmetic and regenerate the default stock cut list.

No dependencies. This does not execute KCL or check solid collisions/stiffness.
"""
from pathlib import Path
import csv
import math
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'parameters.kcl').read_text()
p = {name: float(value) for name, value in re.findall(
    r'export\s+(\w+)\s*=\s*(-?\d+(?:\.\d+)?)mm\b', source)}

def require(condition, message):
    if not condition:
        raise ValueError(message)

travel = p['linearTravel']
rail = p['railLength']
foot = p['profileWide'] + p['railHeight'] + p['blockHeight'] + p['plateThickness']
center = p['guideSeparation'] / 2 + p['towerOffset']
inner = center - p['railSpacing'] / 2
span_tie = 2 * inner - p['profileNarrow']
short_tie = p['railSpacing'] - p['profileNarrow']
carrier_face = center - p['profileWide'] / 2 - p['railHeight'] - p['blockHeight'] - p['plateThickness']
require(p['foamSpan'] < p['guideSeparation'], 'Foam exceeds guide spacing')
require(carrier_face > p['guideSeparation'] / 2, 'Guide arm has nonpositive reach')
require(p['basePlateWidth'] >= p['railSpacing'] + 27, 'Base plate misses guide blocks')
require(p['baseDepth'] >= travel + p['carriageDepth'], 'Moving plate exceeds bed at full travel')
require(rail >= travel + 45, 'Horizontal blocks exceed rail at full travel')
require(p['endMargin'] + rail <= p['towerHeight'], 'Vertical rail exceeds upright')
require(p['guideAbovePlate'] - 22.5 >= p['endMargin'], 'Vertical block below rail at minimum')
require(p['guideAbovePlate'] + travel + 22.5 <= p['endMargin'] + rail, 'Vertical block exceeds rail at maximum')
for axis in ('x1Position', 'x2Position'):
    require(abs(p[axis]) <= travel / 2, f'{axis} exceeds horizontal travel')
for axis in ('y1Position', 'y2Position'):
    require(0 <= p[axis] <= travel, f'{axis} exceeds vertical travel')

rows = [
    ('E01', '2040 aluminium', 4, p['baseDepth'], 'Bed beams; 40 mm vertical'),
    ('E02', '2040 aluminium', 4, span_tie, 'Span ties; 40 mm vertical'),
    ('E03', '2040 aluminium', 4, short_tie, 'Tower bed end ties; 40 mm vertical'),
    ('E04', '2040 aluminium', 4, p['towerHeight'], 'Moving uprights; 40 mm across span'),
    ('E05', '2040 aluminium', 2, p['railSpacing'] + p['profileNarrow'], 'Tower caps; 20 mm vertical'),
    ('S01', '20 x 4 steel flat', 2, math.hypot(span_tie, p['baseDepth'] - p['profileNarrow']), 'Diagonal centerline lengths; end holes/overlap allowance TBD'),
]
with (ROOT / 'frame_cut_list.csv').open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Stock', 'Quantity', 'Nominal length mm', 'Notes'])
    writer.writerows((a,b,c,f'{d:.2f}',e) for a,b,c,d,e in rows)
print('PASS: nominal guide spacing, foam clearance, full travel, rail fit and guide-arm reach')
print(f'Guide spacing: {p["guideSeparation"]:.0f} mm; foam end clearance: {(p["guideSeparation"]-p["foamSpan"])/2:.0f} mm each')
print(f'Base stock footprint: {2*(center+p["railSpacing"]/2+p["profileNarrow"]/2):.0f} x {p["baseDepth"]:.0f} mm')
print(f'Tower top: {foot+p["towerHeight"]+p["profileNarrow"]:.0f} mm above bed underside')
print(f'Guide height range: {foot+p["guideAbovePlate"]:.0f}..{foot+p["guideAbovePlate"]+travel:.0f} mm')
print(f'2040 total: {sum(q*length for _,stock,q,length,_ in rows if stock=="2040 aluminium")/1000:.2f} m before kerf/waste')
print('Updated frame_cut_list.csv. Solid execution, fasteners, drive packaging and FEA are not checked.')

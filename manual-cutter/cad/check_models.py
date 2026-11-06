"""Offline KCL evaluation and manual-cutter interface checks; no engine token needed.

Install zoo-kcl==0.3.195. Mock evaluation is not a solid-kernel/render test.
"""
import asyncio
import csv
import importlib.metadata
import json
import math
import re
from pathlib import Path

import kcl

ROOT = Path(__file__).resolve().parent


def parameters():
    text = (ROOT / 'parameters.kcl').read_text()
    return {name: float(value) for name, value in re.findall(
        r'export (\w+) = ([0-9.]+)mm', text)}


def interfaces():
    p = parameters()
    gap = (p['span'] - p['foamSpan']) / 2
    assert gap > p['wireClipInset'] + 35, 'Clips need clearance beyond foam/guide ends'
    assert p['pipeOD'] > 2 * p['pipeWall'] > 0
    assert p['pivotZ'] > p['pipeBottom'] and p['pipeTop'] > p['pivotZ']
    assert p['fitClearance'] > 0, 'A positive coupon-calibrated fit clearance is required'
    assert p['pivotSleeveBore'] > p['pivotSleeveOD']
    sleeve_gap = p['pivotSleeveBore'] - p['pivotSleeveOD']
    le = (p['span'] - 2 * p['wireClipInset']) / 1000
    resistance = 1.09 * le / (math.pi * p['wireDiameter'] ** 2 / 4)
    current = 19 / resistance
    assert current < 3.42 * 0.8, 'Baseline adapter current reserve lost'
    manifest = list(csv.DictReader((ROOT / 'parts.csv').open()))
    assert all((ROOT / r['Model']).is_file() for r in manifest)
    entries = {r['Model'] for r in manifest}
    actual = {f.name for f in ROOT.glob('*.kcl') if re.match(r'[PMEO]\d\d_', f.name)}
    assert actual <= entries, f'Unmapped components: {actual - entries}'
    assert all(int(r['Quantity']) > 0 for r in manifest)
    return {'foam_end_clearance_mm': gap,
            'pivot_sleeve_diametral_clearance_mm': round(sleeve_gap, 3),
            'energized_length_mm': round(le * 1000, 3),
            'wire_resistance_ohm': round(resistance, 4),
            'full_on_current_A': round(current, 4),
            'full_on_power_W': round(19 * current, 3),
            'manifest_rows': len(manifest)}


async def main():
    results = []
    for path in sorted(ROOT.glob('*.kcl')):
        # Official parser and offline evaluator; all part constructors are called
        # in standalone files, not merely parsed as function definitions.
        try:
            kcl.parse_code(path.read_text())
            outcome = await kcl.mock_execute(str(path))
            errors = [i.message() for i in outcome.issues() if i.is_err()]
            warnings = [i.message() for i in outcome.issues() if i.is_warning()]
            results.append({'file': path.name, 'passed': not errors,
                            'errors': errors, 'warnings': warnings})
        except Exception as exc:
            results.append({'file': path.name, 'passed': False, 'errors': [str(exc)]})
    report = {'validation_mode': 'offline parse and mock execution; no solid kernel',
              'zoo_kcl_version': importlib.metadata.version('zoo-kcl'),
              'checks': interfaces(), 'files': results,
              'engine_render_validated': False,
              'step_stl_exports_validated': False,
              'prototype_validated': False}
    (ROOT / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    bad = [r for r in results if not r['passed']]
    warning_count = sum(len(r.get('warnings', [])) for r in results)
    print(f'{len(results) - len(bad)}/{len(results)} KCL files passed offline evaluation; '
          f'{warning_count} warnings; solid kernel not run.')
    for item in bad:
        print(item['file'], '\n'.join(item['errors']))
    if bad:
        raise SystemExit(1)


if __name__ == '__main__':
    asyncio.run(main())

# Printed components and template system

The owner has a 3D printer. Use it for custom interfaces and workholding; do not print a hot-wire anchor directly in ordinary filament. All quantities below are for one M1 bow and one guide pair. CAD/STL files are intentionally deferred.

| ID / part | Quantity | Function and detailing requirements |
| --- | --- | --- |
| P01 crossbar-end pivot forks | 2 | Clamp onto measured pipe OD; double-shear M6 pivot with metal spacer/bushing; load-spreading arm saddle; captured nuts and mechanical stops |
| P02 arm pivot saddles | 2 | Spread clamp load over continuous PVC arms; avoid point loading or crushing pipe; replaceable metal sleeve where needed |
| P03 upper tie anchor saddles | 2 | Through-bolted/load-spreading cool cord anchors; no sharp cord bends; one supports preload adjuster |
| P04 lower terminal carrier saddles | 2 | Hold purchased ceramic-insulated terminal hardware outboard; printed body must remain cool; wire force carried through bolts/backing plates, not a small printed hook |
| P05 grips / pinch guards | 2 sets | Non-slip hand position near pivots; fingers cannot enter pivots or spring; do not mechanically lock out required lever movement |
| P06 spring guard | 1 | Ventilated, removable shield or sleeve; allow full spring travel; retains fragments with separate tether |
| P07 template bodies | 2 minimum | Root and tip profile; indexed mounting holes, numbered stations and lead-in/out; split into keyed sections if larger than printer bed |
| P08 template registration brackets | 4 | Two per end; shared datum to foam/support; bolts/pins kept outside wire path; no conductive connection between template edges |
| P09 controller enclosure | 1 | Bench-mounted; rated connector, fuse access, insulated terminals, strain relief and ventilation; do not enclose the sealed laptop adapter inside it |
| P10 cable clips / parking saddles | 6 / 2 | Support cold lead runs; ceramic/metal surface supports the hot wire when parked, never a bare printed wire rest |

## Printing and material assumptions

Start with PETG for cool fittings and template bodies; ASA is an alternative where the printer is equipped for it. PLA may be used for nonloaded fit checks only. Filament choice alone does not establish thermal or structural adequacy. Follow the filament supplier's print and service limits and document the actual material used.

Provisional slicer starting point for loaded cool fittings: 0.20–0.28 mm layers, 5–6 walls, 40–60% infill, broad fillets and washers/backing plates at bolts. Orient forks so the principal tension does not simply peel layers apart. Print a clamp/pivot coupon, measure it and adjust clearances before complete parts. Metal sleeves and bolt shoulders should allow free pivot rotation without loosening the clamp or crushing PVC. Use prevailing-torque nuts or equivalent retention; do not tighten a pivot solid to compensate for poor fit.

Do not assign a universal safe filament temperature. Measure each loaded fitting at the longest expected duty, compare with the actual filament supplier's limits and allow a documented margin for creep under load. If the carrier warms excessively, increase clearance, improve ceramic isolation or replace the interface with suitable metal/ceramic hardware.

## Guide edge development

1. Print a short curved coupon with the proposed groove and fastener arrangement.
2. Fit a smooth 0.3–0.5 mm metal-strip edge as a starting candidate. Mechanically retain it; adhesives alone must not hold the wire contact edge. A contoured sheet-metal profile is another option where a strip cannot follow tight curvature.
3. Deburr/polish the edge and cover all handling surfaces. Retain electrical isolation between the two guides, metal benchwork and hands. No metal bridge may connect points on the energized wire.
4. Test a stationary contact briefly and a moving cut at low duty, then at the intended setting. Inspect for groove growth, edge release, softened carrier, sticking or local hot spots. Bare printed contact edges are not released for use.
5. Compare the resulting foam coupon to a known profile. Record the required geometric offset; include edge thickness and the retained-part side when generating the production template.

Provide a flat registration base, labelled root/tip and left/right orientation, chord datum, incidence reference and matching progression numbers. For unequal end profiles, place corresponding stations by intended geometric correspondence; identical distance spacing does not guarantee a correct loft. Test on a simple untapered shape before progressing to wing taper/twist. Preserve upper/lower template registration between cuts and support the retained foam in its offcut cradle where useful.

## Measurements required before CAD

- Printer usable bed size, nozzle, filament, calibrated hole/slot tolerances.
- Actual PVC OD, wall thickness, straightness and available fitting standard.
- Pivot bushing and bolt dimensions; tested saddle clamp fit.
- Ceramic standoff/anchor geometry, cable connector and electrical clip envelopes.
- Spring free length, initial force, measured spring rate, hook dimensions and rated travel.
- First actual root/tip outline, foam span and required wire endpoint offset.

See [cad/README.md](cad/README.md) for the future modelling deliverables.

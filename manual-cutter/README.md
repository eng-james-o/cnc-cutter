# Manual hot-wire cutter — V2 / M1

Design date: 2026-11-06. Status: architecture proposal; not fabrication release or a tested product. “V2” means the second cutter concept, not a replacement for the CNC design.

Two operators, one at each end of the foam span, move a portable PVC H-frame bow around paired profile templates. A spring-and-cord tie above the crossbar tensions the hot wire below it. The user's 3D printer supplies cool structural fittings, template bodies, fixtures and an enclosure. The heater uses a standard isolated 19 V laptop charger and adjustable DC PWM control; no computer, motors or firmware are needed.

## Documents

| File | Purpose |
| --- | --- |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Requirements, geometry, mechanics, electrical design and calculations |
| [BOM.csv](BOM.csv) | Preliminary purchase/print list; quantities, specifications and unresolved selections |
| [PRINTED_PARTS.md](PRINTED_PARTS.md) | Printable fittings and heat-protected profile guides |
| [BUILD_AND_VALIDATION.md](BUILD_AND_VALIDATION.md) | Assembly, two-person operation, tests and CAD release gates |
| [REFERENCES.md](REFERENCES.md) | Tutorials, material data and how they informed this proposal |
| [cad/README.md](cad/README.md) | Reserved manual CAD location and future modelling scope |

Start with a **1,000 mm foam span**, **1,200 mm nominal wire attachment separation**, **350 mm nominal throat**, **0.40 mm NiCr80 wire**, and an isolated **19 V, at least 3.42 A / 65 W charger**. These are proposed starting values, not confirmed stock dimensions or proven cutting capacity. The exact charger label, pipe dimensions, spring curve and guide profile must be measured before CAD is frozen.

The root architecture/BOM and root `cad/` remain exclusively CNC. Place every future manual CAD model/export under `manual-cutter/cad/`.

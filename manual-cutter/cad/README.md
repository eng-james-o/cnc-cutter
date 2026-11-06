# Manual cutter M1 — Zoo KCL component models

Revision M1-CAD-0.1, 2026-11-06. Preliminary component design and cold assembly; not a fabrication release. All models use KCL 3.0 with millimetres and belong to the manual cutter. The repository root `cad/` still belongs to the CNC cutter.

## Open in Zoo Design Studio

Keep this folder intact with all sibling KCL files. Open:

| Entry point | Contents |
| --- | --- |
| [main.kcl](main.kcl) | Full setup: bow, guides, foam/support references and controller enclosure/electronics |
| [frame.kcl](frame.kcl) | H-frame bow, lever tensioner, wire, hardware, guards and clips |
| [printable_catalogue.kcl](printable_catalogue.kcl) | One of each distinct printed part shape, separated for inspection |
| `Pxx_*.kcl` | Individual printed component candidates, at local part origin |
| `Mxx_*.kcl`, `Exx_*.kcl` | Purchased/fabricated mechanical and electrical reference components |
| [O02_fine_wire.kcl](O02_fine_wire.kcl) | Optional 0.30 mm wire reference |

For individual STL/STEP exports, open the corresponding component entrypoint rather than exporting the full assembly or catalogue. Reorient the part in the slicer; the catalogue is not an arranged print plate. Purchased parts, ceramic parts, wire, spring, electronics and metal contact plates must not be printed as functional substitutes.

[parts.csv](parts.csv) maps each component file to the architecture BOM, assembly quantity and model status. It includes individual clamp halves, guards, enclosure base/lid/carrier, registration brackets, heat-protected demonstration guides, pipe stock, anchors, spring/cord/tether, fasteners and electrical components. Consumables, measuring tools and workshop extraction in the BOM do not require cutter CAD. Optional second pedal O01 uses the E06 reference geometry.

## Parameters and component libraries

- [parameters.kcl](parameters.kcl): principal dimensions, pipe fit, clearances, template and enclosure dimensions.
- [primitives.kcl](primitives.kcl): fresh stock/pin/tube/lead constructors.
- [printed.kcl](printed.kcl): printed fittings with actual bores, holes, splits, openings and mounting features.
- [hardware.kcl](hardware.kcl): generic purchased-part references; threads and vendor internals omitted.
- [guides.kcl](guides.kcl): illustrative upper-profile printed guides and bolted metal face plates.
- [notes.md](notes.md): Zoo AI project memory, coordinates, assumptions, interfaces and outstanding work.

KCL prohibits parent-directory imports, so these modules intentionally remain siblings. Do not reorganize them into subdirectories without designing a compatible module interface.

## Provisional geometry

The assembly keeps the 1,200 mm mechanical wire span, 350 mm pivot-to-wire height and 200 mm upper lever. CAD resolves the arm **PVC cut length to 480 mm**, because ceramic terminal hardware and upper anchor fittings complete the approximately 550 mm overall lever envelope. The crossbar cut is **1,080 mm**. See [pipe_cut_list.csv](pipe_cut_list.csv), which is a fit-check proposal, not a released shop drawing.

The active clip-to-clip length is 1,150 mm, giving approximately 36.2 W at 19 V for the baseline 0.40 mm NiCr80. This is a calculated load, not a measured cutting result. The guides use an example 200 mm upper profile with flat registration base and entry/exit ramps. Actual profiles, lower-surface guides, kerf offsets, numbered stations and any printer-bed splits remain application-specific.

Printed contact edges are recessed below independently isolated, profile-cut 0.4 mm metal face plates. Fit, thermal performance and electrical isolation must be tested. The helical spring is a geometric reference; its dimensions do not establish the required spring rate or allowable extension.

## Validation

See [VALIDATION.md](VALIDATION.md) and [validation.json](validation.json). Run offline checks with Python and `zoo-kcl==0.3.195`:

```bash
python check_models.py
```

This parses and mock-executes every KCL file and checks component coverage and selected interfaces. It does not exercise the solid kernel. Opening/rendering in Zoo, interference checks, STL/STEP generation and prototype tests are still required. No successful render, printable export or hardware test is claimed.

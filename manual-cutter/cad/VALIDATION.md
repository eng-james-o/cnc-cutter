# CAD validation record — M1-CAD-0.1

Date: 2026-11-06. This record distinguishes offline evaluation from solid-kernel and physical verification.

## Completed

- All **67 KCL files** formatted using the official Zoo KCL formatter (`zoo-kcl` Python package 0.3.195).
- All 67 files parsed and mock-executed with the official Zoo offline evaluator: **67 passed, zero errors, zero warnings**. Individual component entrypoints call their constructors, so this checks evaluated function arguments, units, imports and transformations as well as syntax.
- Component manifest checked against all standalone component files; all modelled pieces are mapped to BOM groups with positive quantities.
- Selected numerical interfaces checked: pipe wall/fit assumptions, sleeve clearance, foam-end/clip clearance, and baseline full-on electrical load against 80% of a 3.42 A adapter rating.
- Pipe cut proposal and architectural revisions documented. CNC files remain outside the modification scope.

Detailed machine-readable results are in [validation.json](validation.json). Run [check_models.py](check_models.py) to reproduce these checks after changes.

## Not completed

A live-engine evaluation was attempted on a small component and returned: `No API token found in environment variables. Use ZOO_API_TOKEN`. There was no authenticated Zoo solid-kernel session available.

Consequently, **no successful solid-kernel generation, render, STEP/STL export, mesh/manifold verification, interference sweep, print, thermal test or load test is claimed**. Offline mock evaluation cannot establish any of these results. In particular, a mock-successful union may still fail or produce unexpected topology in the real kernel.

## Next checks in Zoo and on the prototype

1. Open each individual component, beginning with P01 fork and clamp parts; inspect Boolean joins, wall thicknesses, holes and clearances. Inspect the small overlap at the socket/spine and ceramic carrier/web junctions.
2. Open `frame.kcl` and inspect both pivot bearings, running gaps, mechanical stops, clamps, guard screws, spacer stack, wire anchor isolation and spring hook/tie interfaces. Move arms through the intended thermal take-up and common-lean limits; the cold pose does not prove motion clearance.
3. Open `main.kcl`; inspect registration-hole alignment, metal contact-plate attachment, enclosure component clearances and cable slack. The illustrative guide and generic electronics are not final hardware selections.
4. Replace the unverified spring and electrical reference envelopes with measured supplier dimensions. Confirm spring force and take-up independently of its illustrative coil model.
5. Export individual printed candidates in Zoo, inspect their meshes, choose print orientation and print fit coupons before committing a full set. Complete physical checks in [BUILD_AND_VALIDATION.md](../BUILD_AND_VALIDATION.md).

Update this record only when the corresponding checks actually succeed.

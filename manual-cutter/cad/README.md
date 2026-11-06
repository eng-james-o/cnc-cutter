# Reserved CAD directory — manual cutter only

No CAD model is included in this architecture phase. Do not reuse or edit the root `cad/` models: they describe the independent five-axis CNC cutter.

Future deliverables after the validation gates in [BUILD_AND_VALIDATION.md](../BUILD_AND_VALIDATION.md):

- Parametric H-frame assembly with measured pipe dimensions, pivot forks, arm saddles, stops and operator grip envelopes.
- Spring/cord/adjuster model showing cold and hot positions, force ratio and retained travel; verify common arm lean and maximum tilt.
- Ceramic terminal, electrical clip and cable-clearance envelopes, distinguishing raw wire length, energized length and foam span.
- Root/tip guide bodies, replaceable contact edges, registration fixtures, lead-in/out and kerf offsets.
- Bench controller enclosure and nonflammable parking support interfaces.
- Assembly drawing, final pipe cut list, fastener schedule, print orientations and exports.

If KCL/Zoo Design Studio is selected, keep manual `main.kcl`, parameters, parts and `NOTES.md` here. Notes must identify this as M1, reference `../ARCHITECTURE.md`, record assumptions and measured hardware, and avoid importing CNC dimensions. Keep STL/STEP exports clearly named with manual part IDs and revision. No KCL language version is assumed until modelling starts.

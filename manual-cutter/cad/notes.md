# Manual cutter M1 — Zoo Design Studio agent notes

Updated 2026-11-06. This is project memory for the manual bow only. Read this file, `README.md`, `parameters.kcl`, `../ARCHITECTURE.md`, `../PRINTED_PARTS.md` and `../BOM.csv` before editing. Keep notes beside `main.kcl`; update them after substantive design changes. Do not import dimensions from the CNC model in the repository root `cad/`.

## Intent and model status

The user requested a second, non-CNC, two-person cutter. Two operators trace printed guides at the ends of an EPS/XPS blank with a PVC H-frame hot-wire bow. The spring-and-cord tie is above the crossbar and parallel to the wire, outside the electrical path. A sealed 19 V laptop adapter supplies a separate fused, manually controlled PWM heater. The user has a 3D printer and wants component models in Zoo KCL.

All geometry is revision M1-CAD-0.1: a preliminary design, not a fabrication release. The user has authorized CAD development before physical validation; the earlier document instruction to defer CAD is superseded for modelling, not evidence that its prototype tests passed. Printable pieces have bores, splits, holes and mounting features. Purchased pieces are simplified references with no supplier-specific interface guarantee. Reference electronics, springs and electrical connectors must never be printed as working substitutes.

## File organization and KCL rules

- `main.kcl`: full cold setup, frame, demonstration templates, foam/support references and controller box. `frame.kcl`: bow assembly alone. `printable_catalogue.kcl`: one sample of every printable shape, spaced apart for inspection, not a build plate.
- `parameters.kcl`: shared stock sizes, principal dimensions and colours. `primitives.kcl`: basic fresh-body constructors. `printed.kcl`, `hardware.kcl`, `guides.kcl`: functions only, with no top-level geometry. Individual `Pxx_*.kcl`, `Mxx_*.kcl`, `Exx_*.kcl` and `O02_*.kcl` files call these constructors at local origin for inspection/export.
- All KCL uses version 3.0 and millimetres. Imports use `import name, otherName from 'file.kcl'`, without JavaScript braces. Keep KCL files as siblings: KCL forbids `../` imports. Do not introduce cyclic imports or import assembly files into libraries.
- Boolean operations consume their inputs. Use returned bodies, or call constructors again for another instance; do not reuse consumed tools or solids. Keep real components separate rather than unioning an entire assembly.
- Dimension-driven sketch segments are deliberately fixed coordinates in custom functions. Edit their parameters in code; they are not unconstrained drag-editable sketches. `region` uses consecutive boundary segments. A new region is required for each consuming operation.
- Use explicit `global = true` for assembly rotations/translations. Primitive `pin`/`tube` axes start along +Z, `pinX` along +X and `pinY` along +Y. `rodBetween` normalizes squared-length arithmetic into millimetre counts before forming a length.

## Coordinates and frozen-for-now interfaces

World X is the span between operators; Z is up in the H plane; Y is normal to that plane. `frame.kcl` has the wire at Z=0, Y=-14 mm, mechanically anchored at X=±600 mm. The Y offset results from ceramic cross-studs carrying the metal clamps in front of the arm plane, preventing an electrical path through the mounts. In `main.kcl`, the bow is moved to the template entry ramp; it is not a simulated moving cut.

Pivot centres: X=±600, Y=0, Z=350 mm. Upper anchor cord holes: Z=550, Y=21 mm. Both lever arms are initially parallel. No hot/deformed pose, force solution or motion constraints are implemented. The geometry is a cold nominal arrangement. Main geometry follows `span` where practical, but the bench fixtures, clamp detail and reference 200 mm guides have local fixed dimensions; edits require renewed clearance checks.

- Assumed pipe: 33.4 mm OD, 3.4 mm wall. Diametral printed clearance: 0.4 mm. Actual stock and printing tolerances remain unmeasured.
- Crossbar: 1,080 mm cut; ends are 60 mm inboard of pivot centres and clamp in P01 sockets centred 85 mm inboard of each pivot. End sockets do not run into vertical arms.
- Arm pipes: 480 mm, world Z=50 to 530 mm. The initial 550 mm architecture figure represented the complete lower-wire-to-upper-tie envelope; CAD separates that envelope from the shorter PVC stock. Pivot cross-hole is 8.3 mm at 300 mm from the pipe's lower end. Metal sleeves carry M6 bolts through the pipe and split saddles.
- P01 fork cheeks: 8 mm thick, inner faces at Y=±30 mm; saddle halves reach Y=±29 mm. Nominal axial running gap is 1 mm per side. Stops have an approximately 1 mm initial gap to the saddle edge; check actual angular travel and sweep in the real kernel, not by assuming a rated stop angle. The common arm-lean degree of freedom remains unresolved experimentally.
- Split arm saddles use 16 M5 clamp bolts/nuts across fork socket, pivot, upper-anchor and terminal-carrier assemblies. Hardware lengths are examples; `parts.csv` distinguishes assemblies from pieces. Four M3 lid screws and eight M3 guard screws have different required lengths despite sharing one BOM group.
- End closures are internal flush plug references, not external deep socket caps: external caps would collide with collars at the lower ends. Source matching plugs or validate a cool printed alternative separately.
- Lower carrier bridge: Z=40–50 mm. Ceramic blocks: Z=-5 to 35 mm, with 5 mm ceramic spacers up to the bridge. Central wire-clamp studs pass through ceramic along Y. Metal clamps at Y=-14 and Z=0 must stay electrically isolated from mounting bolts, printed parts and PVC. Ceramic parts require sourcing/fabrication and load/heat tests.
- Upper preload eye-rod has an 80 mm M5 reference shank and an M5 wingnut beyond the right anchor. P03 includes a transverse cord eye and an X-axis adjuster passage. Detailed threads, cord knots and preload force are not simulated.
- Modelled spring: 80 mm coil length, 8 mm mean radius, 16 turns, 1.2 mm wire. This is an illustrative purchased-part reference, NOT a spring designed to the specified 0.2–0.4 N/mm rate. Hooks are separate simplified bodies, not a manufacturing-quality spring transition. Replace with measured supplier geometry and force curve. Guard and slack tether are separate bodies.

## Printed guide and enclosure assumptions

`guides.kcl` uses 60 cosine-spaced samples of an illustrative symmetric NACA0012 upper contour at 200 mm chord. Root and tip are identical for the first straight-cut example. The guide includes entry/exit ramps and mounting holes; it is not a final customer wing profile, not a full lower-surface guide, and contains no kerf compensation or engraved progression numbers. Larger final guides will need a printer-bed-aware split and indexed joints; the printer bed is unknown. Replace the example with the intended outlines and matched stations before cutting a production part.

M11 is a **0.4 mm profile-cut metal face plate**, sharing the two mounting holes with the printed guide. The printed upper contour is recessed 0.4 mm vertically so the wire bears on metal. This replaces the initial strip-edge candidate with an attachment that has a retained plate area. It is not a true normal offset, a thermal validation or a kerf correction. Mount the face plates on the outside faces; isolate each end electrically and keep hands clear. Neither a foil wrap nor bare filament is an accepted contact edge. The registration brackets/metal hardware must not bridge both live edges through benchwork. Template numbered stations and final offsets are pending actual profiles and testing.

P09 uses a 150×100×55 mm generic enclosure with 3 mm walls/base, separate 4 mm lid, screw posts, input/output openings, vents, PCB carrier and lid controls. Connector bores, switch cutout and board envelope are assumptions. Confirm all electronics dimensions, standoffs, internal wiring, electrical insulation, fastening and ventilation before printing. The charger remains outside the box. The main model only shows indicative lead segments; it is not a wiring/netlist model and does not show all service loops.

## Electrical and release checks

Mechanical wire span is 1,200 mm. Alligator clips at ±575 mm make **1,150 mm energized length**, with 25 mm unpowered tails. For 0.40 mm NiCr80 and 19 V this calculates to about 9.98 ohm, 1.90 A and 36.2 W cold. The architecture's 1,200 mm electrical calculation was a conservative starting span, not the exact final clip spacing. Unpowered tails still conduct heat. Maintain and test clearance to printed carriers and frame. Clip spring mechanisms and deformation are not modelled; clips are purchased electrical references, not printed fasteners.

Offline parser/mock execution checks evaluate functions, imports, arguments and units. They do not run the Zoo solid kernel, prove boolean manifold results, generate STEP/STL, verify interference, calculate stress or establish printability. A live kernel run was unavailable because there was no Zoo API token. `validation.json` and `VALIDATION.md` record what actually ran. Do not change that status to validated/rendered without evidence. Next: open entrypoints in Zoo, resolve kernel issues, inspect fit and motion, export only individual candidate parts, print fit coupons, then carry out the physical tests in `../BUILD_AND_VALIDATION.md`.

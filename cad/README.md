# Parametric CNC hot-wire cutter frame — KCL

Preliminary engineering layout v0.1, based on repository `ARCHITECTURE.md` v0.2 and `BOM.csv` at commit `28a37b01397c4d52820611e4d7e9827b049c4175`. The repository's newer requirements supersede the original uploaded architecture.

## Open and edit

1. Download/clone the repository. Keep all files in this folder together.
2. In a Zoo Design Studio version supporting **KCL 3.0**, open `cad/main.kcl` for the structural assembly. Open `cad/layout.kcl` for the frame with preliminary carriers, ceramic guide envelopes, foam support, rotary fixture and foam blank.
3. Change dimensions and independent axis positions in `parameters.kcl`, then rerun the entry point. Horizontal positions range from −200 to +200 mm; vertical positions range from 0 to 400 mm. Check the four opposing extreme poses before fixing mechanical details.
4. Run `python cad/check_dimensions.py` from the repository root to check nominal travel arithmetic and regenerate `frame_cut_list.csv` after changing parameters.

`parts.kcl` contains dimension-driven solid helpers. Sketch coordinates are fixed by the input dimensions, without free solver variables. These reusable function sketches are edited through KCL parameters; Zoo's point-and-click sketch tools do not edit function bodies. Each physical member is an independent body, allowing later replacement with a vendor-specific profile or purchased component.

## Files

| File | Purpose |
|---|---|
| `main.kcl` | Bed, ties, underside X straps, moving tower plates, uprights, caps, tower gussets and eight rail envelopes |
| `layout.kcl` | Structural assembly plus vertical carriers, guide locations and workholding/keep-out references |
| `parameters.kcl` | Requirements, provisional dimensions, colors and displayed axis positions |
| `parts.kcl` | Rectangular stock, triangular gusset and circular stock helpers |
| `NOTES.md` | Zoo Studio AI project memory: design intent, coordinates, assumptions, validation status and analysis guidance |
| `frame_cut_list.csv` | Nominal extrusion and diagonal-strap list generated from parameters |
| `check_dimensions.py` | Dependency-free dimension checks and cut-list generation |

## Design basis and coordinate mapping

| Dimension | Default | Basis |
|---|---:|---|
| Separation of ceramic guide center planes | 2,000 mm | Architecture requirement |
| Centered foam span | 1,600 mm | Architecture requirement; nominal 200 mm end clearance |
| Each horizontal and vertical stroke | 400 mm | Architecture requirement |
| Guide rails | 8 × 550 mm | BOM M03; two per axis |
| Tower upright stock | 4 × 620 mm | Preliminary CAD allowance |
| Bed depth | 700 mm | Preliminary allowance for moving plates and end hardware |
| Tower centers | ±1,120 mm | 120 mm outward of each guide plane |
| Tower rail separation | 130 mm | Preliminary; both base and vertical guide pairs |
| Moving base plates | 200 × 200 × 8 mm | Preliminary |
| Tower gussets | 200 mm base × 180 mm height × 6 mm | Preliminary unperforated side webs |
| Base stock footprint | 2,390 × 700 mm | Derived; moving plates increase overall width to 2,440 mm |
| Top of towers | 709 mm above base underside | Derived; excludes feet and future drive hardware |
| Guide height range | 189–589 mm above base underside | Derived |
| Rotary plate | Ø250 × 12 mm | BOM diameter; thickness provisional |
| Tensioner keep-out | 120 × 60 × 40 mm | 120 mm take-up requirement; housing size provisional |

World **X** runs along the hot wire between towers, world **Y** is horizontal cutting travel, and world **Z** is vertical. Firmware X1/X2 therefore move along world Y, and firmware Y1/Y2 move along world Z. `x1Position` and `x2Position` translate the complete towers; `y1Position` and `y2Position` raise their respective guide carriers. B rotates around world Z, but this initial layout does not animate or model its drive.

The nominal extrusion schedule is 4 × 700, 4 × 2090, 4 × 110, 4 × 620, and 2 × 150 mm: **14.38 m** before kerf/waste. Base beams use the 40 mm dimension vertically. Uprights use 40 mm across the wire span. Tower caps sit above upright ends; horizontal ties butt between bed beams. This is a cut-length starting point, not a procurement release.

## Modeled detail and remaining design

- **2040 members are external rectangular envelopes.** Slots, center bores, material area, mass and structural stiffness are not represented. Do not derive mass or deflection from these solid envelopes. Substitute the selected supplier's cross-section before structural analysis.
- Eight rails and eight blocks implement the architecture's minimum arrangement. The four vertical blocks appear only in `layout.kcl`. Their 12/27/45 mm envelope dimensions and rail/block heights are provisional; replace them with the selected rail assembly drawing, including actual stack height and bolt access.
- Bed racking resistance is reserved by two 20 × 4 mm crossed steel straps underneath. They occupy separate levels; the lower strap sits against two modeled 20 × 20 × 4 mm steel packing pads at the end ties. Cut lengths are between nominal joint centerlines; fastening overlap, end holes, tension adjustment and end attachment plates remain to be designed. Allow space below the bed for straps and hardware.
- Tower side webs contact the outside faces of the paired uprights and the moving base plate. Rail screws, M5 T-nuts, angle brackets, gusset holes, base joint plates, alignment slots and tolerances remain unresolved. These unperforated envelopes cannot be sent directly for fabrication.
- Horizontal belt drives, vertical T8 screws, nuts, motors, couplers, bearings and endstop brackets are **not yet modeled**. The rail spacing leaves a central channel for each vertical screw. Verify the motor/belt packaging within the remaining base end clearances before purchasing stock.
- Beige guide discs are ceramic location envelopes without bores. Their center planes define guide separation. The steel arms are layout blocks; actual insulated attachments, current clamps and wire paths require detailing. No wire solid or live electrical assembly is included.
- The orange body is an outboard **keep-out reservation**, not an operating spring. It reserves axial space for 120 mm take-up; pulley routing, electrical isolation, spring housing, force and collision clearance remain to be resolved.
- Green supports and the central rotary pedestal are separate reference volumes, with their lower faces 45 mm above the base underside. A separately supported bench/fixture is required; they do not constitute a finished support structure. Beige foam is a nominal 1,600 × 300 × 300 mm blank. The supports and rotary stack share a top datum 10 mm above the minimum guide center, placing the blank at Z = 199–499 mm. This provisional offset allows the wire to reach both foam faces vertically. The supports and rotary stack share a top datum 10 mm above the minimum guide center, placing the blank at Z = 199–499 mm. Hide/remove its reference body to inspect the carriers.
- Supports under the foam are for stationary wing cutting. They must be repositioned or removed for B-axis rotation. A 1,600 × 300 mm blank has a roughly 1,628 mm planar swept diameter, far exceeding the 700 mm bed depth. The current model does not establish rotary clearance: check the complete workpiece, carriers, supports, bench and surrounding room through every intended indexed angle.
- Long 2040 span ties and tower deflection under 8–10 N wire tension require stiffness analysis and physical validation. No FEA, sag analysis, collision simulation or fabrication approval is implied.

The current architecture limits foam span to **1,600 mm**. For a future 2,000 mm blank, increase `foamSpan` **and** `guideSeparation` (for example 2,400 mm guide spacing to retain 200 mm at each end), then recheck wire geometry, heating, tensioner stroke and frame stiffness. A 2,000 mm guide spacing alone does not accommodate a 2,000 mm blank with fixtures.

## Validation and export

The original four KCL files were parsed/formatted and linted with Zoo CLI 0.2.209. `check_dimensions.py` verifies nominal block containment over the full 400 mm stroke, rail fit, positive guide-arm reach, plate coverage and workpiece end clearance. These are arithmetic checks, not solid execution or collision detection.

A STEP export was attempted but the execution environment had no authenticated Zoo API session. **KCL geometry execution, visual verification and STEP export remain unverified.** No generated STEP file is supplied.

On an authenticated workstation, from the repository root:

```sh
zoo auth login
zoo kcl lint cad/main.kcl
zoo kcl lint cad/layout.kcl
mkdir -p cad/exports
zoo kcl export --output-format=step cad/main.kcl cad/exports
```

Export `main.kcl` for the structural model. `layout.kcl` additionally includes nonmanufacturing reference bodies. Recheck the geometry in Zoo Studio and inspect the exported assembly before using it downstream.

KCL references: [modules](https://zoo.dev/docs/kcl-lang/modules), [sketch blocks](https://zoo.dev/docs/kcl-lang/sketches), [KCL 3.0](https://zoo.dev/docs/kcl-lang/migrating-to-kcl-3).

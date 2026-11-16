# Parametric CNC hot-wire cutter frame — KCL

Preliminary engineering layout v0.2, based on repository `ARCHITECTURE.md` v0.2 and `BOM.csv` at commit `28a37b01397c4d52820611e4d7e9827b049c4175`. The repository's newer requirements supersede the original uploaded architecture.

## Open and edit

1. Download/clone the repository. Keep all files in this folder together.
2. In a Zoo Design Studio version supporting **KCL 3.0**, open `cad/main.kcl` for the structural assembly. Open `cad/layout.kcl` for the frame with motion drives, tensioner, switches, workholding and foam blank.
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
| Tower gussets | 200 mm base × 180 mm height × 6 mm | Drilled side webs |
| Base stock footprint | 2,390 × 700 mm | Derived; moving plates increase overall width to 2,440 mm |
| Top of towers | 709 mm above base underside | Derived; top of extrusion; lift motor reaches 763 mm |
| Guide height range | 189–589 mm above base underside | Derived |
| Rotary plate | Ø250 × 12 mm | BOM diameter; thickness provisional |
| Tensioner | 120 mm usable stroke | Moving spring and redirect layout |

World **X** runs along the hot wire between towers, world **Y** is horizontal cutting travel, and world **Z** is vertical. Firmware X1/X2 therefore move along world Y, and firmware Y1/Y2 move along world Z. `x1Position` and `x2Position` translate the complete towers; `y1Position` and `y2Position` raise their respective guide carriers. The modeled B-axis drive is shown at its home angle about world Z.

The nominal extrusion schedule is 4 × 700, 4 × 2090, 4 × 110, 4 × 620, and 2 × 150 mm: **14.38 m** before kerf/waste. Base beams use the 40 mm dimension vertically. Uprights use 40 mm across the wire span. Tower caps sit above upright ends; horizontal ties butt between bed beams. This is a cut-length starting point, not a procurement release.

## Motion hardware and assembly

Open **layout.kcl** for the assembled cutter. **main.kcl** shows its frame, drilled rails, base carriages and braces. The complete layout adds the four linear drives, rotary drive, switches, corner plates, guide and take-up mechanism, independent workholding and controller enclosure. The beige foam volume is a reference body.

| Module | Contents |
|---|---|
| drive_parts.kcl | Motor, bridges, pulley, belt clamp, perforated gusset, microswitch body, drilled rail, nut and coupling |
| motion.kcl | Two horizontal belt stages, two vertical screw stages, bearing seats, linear switch stands and frame corner plates |
| auxiliary.kcl | Rotary mechanism, home cam, electrical clamps, spring reel and take-up bracket |
| machining.kcl | Local stock and boring primitives |
| fasteners.csv | Installed quantities, diameters, lengths, mating hardware and hole details by joint |
| HARDWARE.md | Drawing references, comparable builds, working assumptions and verification limits |

The visible controller box includes the mounting ears and E-stop operator. The power supplies are excluded. Most purchased items use their mounting geometry and outer dimensions. Threads, belt teeth, motor windings, switch contacts and reducer gearing are omitted. The assembly is a fit study and still requires kernel evaluation and hardware selection before fabrication.

## Verification

From the repository root run `python cad/check_dimensions.py`. For the full parameter sweep install `zoo-kcl==0.3.196` and run `python cad/check_motion.py`. The second check mock-executes every CNC module and the complete assembly at all 16 linear travel corners.

On an authenticated Zoo workstation run `zoo kcl export --output-format=step cad/layout.kcl <output-directory>`. Inspect material around holes and nut seats, insert fasteners, sweep the actual purchased parts, and verify rotary clearance with the chosen workpiece. The 1,600 × 300 mm blank sweeps approximately 1,628 mm in plan. Remove or reposition the stationary supports for indexing.

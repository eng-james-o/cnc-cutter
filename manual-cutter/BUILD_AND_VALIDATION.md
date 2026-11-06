# Build, operation and validation plan

Status: proposed procedure for an unbuilt prototype. A checked box must represent a measured result, not assumed compliance. Record actual parts, conditions and observations below or in a dated test report in this folder.

## 1. Bench preparation and assembly

1. Read the adapter label: confirm isolated 19 V DC, rated current, condition, connector dimensions and polarity. Select the matching DC socket and fuse; do not alter mains wiring.
2. Measure pipe OD/wall and choose one fitting standard. Reserve approximately 1.3 m crossbar stock and two 0.6 m arm blanks; do not cut to final length until pivot/fitting offsets are defined. The 1,200 mm target is pivot/wire geometry, not an automatic pipe cut length.
3. Print a clamp/pivot coupon and prove free rotation, adequate clamp grip and no pipe crushing. Assemble the H with continuous arms, two metal-bushed pivots, stops and lower ceramic terminal assemblies. Keep hands at cool grip locations.
4. Fit the upper cord/spring tie and retention tether. Fit 0.40 mm nichrome mechanically; preload to about 3 N wire tension using a force gauge and the measured lever ratio. Check both ends, spring movement and wire take-up without energizing.
5. Mount the controller, fuse, master switch and hold-to-heat switch in a guarded bench arrangement. Route flexible DC leads along the crossbar to retained alligator clips just inside the anchors. No spring/frame current path; no bare terminal near fingers.
6. Verify wiring, insulation, polarity and cold wire resistance with power disconnected. Calculate full-on current using the measured resistance; reject a load that exceeds the adapter or any component rating even if low PWM duty is planned.
7. Clamp foam and indexed template pair to an independent support. Perform a complete cold trace with both operators and all cables present. Check bow, spring, hands, clips, bench and template clearances, including tilted positions.

## 2. First heating and cut

Start with the wire clear of foam on a nonflammable support, dial at minimum and master off. Connect the charger, enable master, hold heat briefly at low duty and release. Check immediate power removal. Increase duty in small steps, observing tension and contact temperatures. Do not leave the heater latched on unattended.

Cut a scrap EPS coupon first, then the intended foam grade/density. Use only enough power for a smooth cut without forcing or visible glowing wire. If the middle lags, stop and review heat/feed/tension; pulling harder can distort the section. Measure kerf and guide offset rather than assuming the wire diameter equals cut width. Keep extraction effective and keep the path clear of flammable debris.

## 3. Two-person operating sequence

1. Confirm blank/guide registration, known material, cable slack, stable support and a clear parking location. Agree which person leads the count and controls heat.
2. Both say ready. Heat lead holds the normally-open control and establishes the tested setting; enter on matching lead-in ramps.
3. Leader calls corresponding station numbers. Each operator follows the local guide smoothly, reaching matching stations together. Different chords normally mean different local travel speeds.
4. Either operator calls stop if the wire lifts, catches, bows, the guide moves or a clip loosens. Heat lead releases immediately; do not correct a jam with heat held on.
5. Exit together over the lead-out, release heat, switch master off and park the bow. Allow cooling before repositioning guides or removing scraps. Unplug before touching clips, replacing wire or adjusting tension.

For a closed external outline, plan a lead-in slit and support the released offcut. For upper/lower wing cuts, keep the retained section registered and supported between passes. Do not begin with internal cutouts or extreme taper.

## 4. Acceptance record

These are proposed prototype gates, not achieved performance claims.

| Test | Method | Acceptance target |
| --- | --- | --- |
| Geometry | Measure cold wire span, foam end clearance and throat; photograph cold full-profile trace | Baseline 1,000 mm blank fits; no interference throughout intended cut |
| Cold tension | Force gauge and spring curve at assembled lever geometry | Start at 3 N; adjustment can cover intended 3–5 N range without overtravel |
| Take-up | Warm/cool repeatedly and measure movement/tension | Wire stays taut; no spring/arm stop reached; about 15 mm wire-side reserve available cold |
| Frame/joint stability | Hold preload 30 minutes cold; apply representative grip/cutting forces | No cracks, slip, ovalization, uncontrolled lean or progressive span drift; proposed span drift <=1 mm |
| Heated structure | Run staged heating through the longest intended cut duration plus margin; measure fittings and clips | No softening, permanent distortion or rising contact hot spots; measured temperatures below documented material/component service limits with margin |
| Adapter/load | Cold resistance calculation plus actual current/voltage at full allowed setting | No adapter hiccup/cycling; all currents below ratings; proposed sustained adapter use <=80% nameplate |
| Heat release | Test minimum, intermediate and maximum allowed duty; disconnect/reconnect with heat switch released | Release removes heater power immediately; no restart until switch is intentionally held; wire remains hot briefly afterward |
| PWM failure isolation | With power disconnected, inspect series switch arrangement; qualified low-energy continuity check as needed | Hold-to-heat physically opens supply independently of controller electronics; never create a live fault to test this |
| Wire break / clips | Inspect unloaded/released wire routing and retained clip motion | Broken wire cannot pull leads into hands or conductive fixtures; unplug immediately if it occurs |
| Template durability | At least 10 coupon passes; measure edge and inspect carrier | No edge release, sticking or visible profile erosion; proposed profile change <=0.5 mm |
| Straight reference cut | Three cuts with simple matched guides; measure midspan and ends | Provisional <=2 mm deviation from intended profile after kerf correction; revise target if application requires tighter accuracy |
| Taper / twist | Cold clearance trial then sacrificial known geometry | Both guides remain engaged, stations synchronize and geometry meets separately agreed tolerance |

Do not force a low-voltage charger into repeated protection cycles. If the 19 V system cannot achieve useful feed and cut quality, record the result and revise wire/power/span requirements before purchasing final hardware.

## 5. CAD release gates

- [ ] Confirm 1 m foam capacity and actual maximum root/tip profile envelopes.
- [ ] Record exact adapter, connector, controller and switch ratings.
- [ ] Confirm measured pipe and printer dimensions.
- [ ] Demonstrate stable pivoting H behavior; resolve excessive common arm lean/racking.
- [ ] Choose spring from measured force/travel data and finalize stops/guard.
- [ ] Validate insulated anchors, retained clips and printed-guide edge coupons.
- [ ] Demonstrate acceptable 19 V heating on actual foam.
- [ ] Update architecture/BOM with selected parts and measured dimensions.

Only then produce manual CAD, pipe cut list and printable exports inside `manual-cutter/cad/`. Do not modify root CNC CAD to represent this bow.

"""Evaluate the CNC assembly at center and opposing end poses with Zoo's offline evaluator."""
import asyncio
import itertools
import math
from pathlib import Path
import re
import shutil
import tempfile

import kcl

ROOT = Path(__file__).resolve().parent


async def check(path):
    result = await kcl.mock_execute(str(path))
    issues = [issue.message() for issue in result.issues() if issue.is_err() or issue.is_warning()]
    if issues:
        raise ValueError(f"{path.name}: {issues}")


async def main():
    with tempfile.TemporaryDirectory() as directory:
        cad = Path(directory)
        for path in ROOT.glob("*.kcl"):
            shutil.copy2(path, cad)
        params = cad / "parameters.kcl"
        original = params.read_text()
        dims = {k: float(v) for k, v in re.findall(r"export (\w+) = (-?[0-9.]+)mm", original)}
        travel = dims["linearTravel"]
        span = dims["guideSeparation"]
        half = travel / 2
        max_skew = math.hypot(span, travel, travel) - span
        # Architecture thermal allowance 8.5 mm. Fifteen mm cold payout is modeled.
        assert 15 - 8.5 > 0 and 15 + max_skew + 8.5 < dims["takeupTravel"]
        center = dims["baseDepth"] / 2 - 43
        assert center + 42.3 / 2 < dims["baseDepth"] / 2 - dims["profileNarrow"]
        assert 2 * (2 * center) + 40 < 2000, "Two belts exceed the 4 m BOM allowance"
        for path in sorted(cad.glob("*.kcl")):
            await check(path)
        for values in itertools.product((-half, half), (-half, half), (0, travel), (0, travel)):
            text = original
            for axis, value in zip(("x1Position", "x2Position", "y1Position", "y2Position"), values):
                text, count = re.subn(rf"(export {axis} = )-?[0-9.]+mm", rf"\g<1>{value:g}mm", text)
                assert count == 1
            params.write_text(text)
            await check(cad / "layout.kcl")
        print(f"Offline KCL passed at the default pose and all 16 travel corners. Max skew adds {max_skew:.2f} mm.")
        print(f"Nominal belt pitch length per tower: {4 * center + 40:.0f} mm, before clamp allowance.")


if __name__ == "__main__":
    asyncio.run(main())

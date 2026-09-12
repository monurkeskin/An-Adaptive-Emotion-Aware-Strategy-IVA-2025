"""Validate engine identity and run each available or explicitly unavailable target."""

import argparse
import json
from pathlib import Path
from time import perf_counter
from negotiator import __version__
from negotiator.reproduction import run_reproduction
from negotiator.software import runtime_identity

ROOT = Path(__file__).resolve().parent


def verify(output: Path) -> dict:
    metadata = json.loads((ROOT / "framework.json").read_text(encoding="utf-8"))
    if metadata["version"] != __version__:
        raise ValueError("Installed engine version differs from framework.json.")
    actual = runtime_identity()
    expected = metadata.get("package_content_sha256")
    if expected and expected != actual["package_content_sha256"]:
        raise ValueError("Installed engine content differs from the pinned release.")
    output.mkdir(parents=True, exist_ok=False)
    started = perf_counter()
    targets = json.loads(
        (ROOT / "reproduction/targets.json").read_text(encoding="utf-8")
    )["manifests"]
    receipts = []
    for name in targets:
        result = run_reproduction(
            ROOT / "reproduction" / name, output / Path(name).stem
        )
        expected_status = (
            "unavailable" if name == "published-results.json" else "verified"
        )
        if result["status"] != expected_status:
            raise ValueError(f"Unexpected target status: {name}: {result['status']}")
        receipts.append(
            {
                "manifest": name,
                "status": result["status"],
                "manifest_sha256": result["manifest_sha256"],
            }
        )
    receipt = {
        "software": actual,
        "targets": receipts,
        "elapsed_seconds": perf_counter() - started,
    }
    (output / "verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    result = verify(parser.parse_args().output)
    print(json.dumps(result, indent=2))

"""Run only the synthetic configuration and export its independent report."""

import argparse
import json
from time import perf_counter
from pathlib import Path

from negotiator.analysis.report import build_report
from negotiator.application.contracts import StudySpec
from negotiator.application.synthetic import run_study

ROOT = Path(__file__).resolve().parent


def run(output: Path) -> Path:
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = perf_counter()
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/synthetic.json").read_text(encoding="utf-8")
    )
    run_study(spec, output / "records")
    report = build_report(output / "records", output / "report") / "index.html"
    from negotiator.software import runtime_identity

    (output / "timing.json").write_text(
        json.dumps(
            {
                "scope": "synthetic run through report export",
                "elapsed_seconds": perf_counter() - started,
                "software": runtime_identity(),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("demo-output"))
    print(run(parser.parse_args().output))

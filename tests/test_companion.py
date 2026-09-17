import json
from pathlib import Path

from run import run

from negotiator.application.contracts import StudySpec

ROOT = Path(__file__).resolve().parents[1]


def test_all_templates_validate_without_connecting_devices(tmp_path):
    from negotiator.application.studies import StudyStore

    for path in (ROOT / "configs").glob("*.json"):
        spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
        store = StudyStore(tmp_path / path.stem, "test")
        try:
            assert store.create(spec)["plan_id"]
        finally:
            store.shutdown()


def test_complete_independent_example_and_report(tmp_path):
    result = run(tmp_path / "example")
    data = json.loads(result.with_name("analysis.json").read_text(encoding="utf-8"))
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/synthetic.json").read_text(encoding="utf-8")
    )
    assert len(data["sessions"]) == len(spec.conditions)
    assert all(
        s["config"]["synthetic"] and s["status"] == "ended" for s in data["sessions"]
    )
    assert data["independent_unit"] == "participant"
    assert result.with_name("records.xlsx").is_file()
    assert len(data["study_sources"]) == 1


def test_verify_reproduction_pipeline(tmp_path):
    from verify import verify

    receipt = verify(tmp_path / "verification")
    assert receipt is not None

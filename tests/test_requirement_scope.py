"""Protocol startup needs runtime materials, not previous participants' records."""

import hashlib
from pathlib import Path

import pytest

from negotiator.application.contracts import StudySpec
from negotiator.application.protocol import protocol_readiness

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = sorted((ROOT / "configs").glob("protocol*.json"))
REQUIRED = {'execution': ['evidence-2'], 'historical-analysis': ['evidence-1', 'evidence-2-records']}


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_runtime_materials_and_historical_evidence_have_separate_gates(path, tmp_path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    requirements = spec.protocol.requirements
    scopes = {
        scope: sorted(r.id for r in requirements if r.required_for == scope)
        for scope in REQUIRED
    }
    assert scopes == {k: sorted(v) for k, v in REQUIRED.items()}
    # A synthetic file isolates the availability gate; it is not a study asset.
    fixture = tmp_path / "availability-fixture.txt"
    fixture.write_bytes(b"synthetic availability fixture")
    for requirement in requirements:
        if requirement.required_for == "execution":
            requirement.path = str(fixture)
            requirement.sha256 = hashlib.sha256(fixture.read_bytes()).hexdigest()
    assert protocol_readiness(spec) == []
    historical = protocol_readiness(spec, operation="historical-analysis")
    assert sorted(r["id"] for r in historical) == sorted(REQUIRED["historical-analysis"])
    fixture.unlink()
    assert sorted(r["id"] for r in protocol_readiness(spec)) == sorted(REQUIRED["execution"])

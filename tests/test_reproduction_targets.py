"""Each recipe computes from hashed inputs or reports the original-data gap."""

import json
from pathlib import Path
import pytest
from negotiator.reproduction import run_reproduction

ROOT = Path(__file__).resolve().parents[1]
TARGETS = json.loads((ROOT / "reproduction/targets.json").read_text(encoding="utf-8"))[
    "manifests"
]


@pytest.mark.parametrize("name", TARGETS)
def test_reproduction_target(name, tmp_path):
    result = run_reproduction(ROOT / "reproduction" / name, tmp_path / "out")
    if name == "published-results.json":
        assert result["status"] == "unavailable"
        assert result["results"] is None and result["comparisons"] == []
    else:
        assert result["status"] == "verified", result["comparisons"]
        assert (tmp_path / "out/table.tex").is_file()
    assert (tmp_path / "out/ro-crate-metadata.json").is_file()

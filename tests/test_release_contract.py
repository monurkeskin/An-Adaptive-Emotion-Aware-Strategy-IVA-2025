"""Independent documentation, citation and source/test linkage contracts."""

import json
from pathlib import Path
from negotiator.metadata import write_metadata

ROOT = Path(__file__).resolve().parents[1]


def test_metadata_and_readme_use_the_same_paper():
    record = json.loads((ROOT / "citation-metadata.json").read_text(encoding="utf-8"))
    write_metadata(ROOT, record, check=True)
    assert record["paper"]["title"] in (ROOT / "README.md").read_text(encoding="utf-8")
    for path in [
        "README.md",
        "METHOD.md",
        "REPRODUCIBILITY.md",
        "framework.json",
        "paper-map.json",
        "docs/protocol.md",
        "docs/analysis.md",
        "docs/development.md",
        "docs/compatibility.md",
    ]:
        assert (ROOT / path).is_file()


def test_paper_map_has_source_identities_and_existing_local_tests():
    mapping = json.loads((ROOT / "paper-map.json").read_text(encoding="utf-8"))
    assert mapping["requirements"]
    for requirement in mapping["requirements"]:
        assert requirement["sources"]
        for source in requirement["sources"]:
            assert (
                source["label"] and len(source["sha256"]) == 64 and source["line"] > 0
            )
        for test in requirement["tests"]:
            if test["repository"] == "companion":
                assert (ROOT / test["path"]).is_file()


def test_source_package_has_no_copied_engine():
    assert not (ROOT / "src/negotiator").exists()
    assert not (ROOT / "negotiator").exists()
    assert "negotiator-human @ git+" in (ROOT / "requirements.txt").read_text(
        encoding="utf-8"
    )

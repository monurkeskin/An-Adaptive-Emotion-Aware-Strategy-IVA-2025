"""Table 5 wording and Section 4.1 timing, independent of participant records."""

import json
import csv
from pathlib import Path

import pytest

from negotiator.application.contracts import CommandRequest, StudySpec, SurveyRequest
from negotiator.application.studies import StudyStore
from negotiator.analysis.report import build_report

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = (
    "Nao negotiated fairly.",
    "Nao negotiated with me like a human.",
    "Nao determined her next offer according to my emotional state.",
    "Nao tried to find the best deal for us.",
    "Nao cared about my preferences.",
    "Nao considers my behavior.",
    "I'm satisfied with my performance.",
    "Nao often made very unfair offers.",
)


@pytest.mark.parametrize("order", ["solver", "hybrid"])
def test_both_orders_schedule_the_eight_published_items_after_main_sessions(order):
    data = json.loads((ROOT / "configs" / f"protocol-{order}-first.json").read_text())
    spec = StudySpec.model_validate(data)
    assert tuple(q.prompt for q in spec.surveys) == PROMPTS
    assert len({q.id for q in spec.surveys}) == 8
    for item in spec.surveys:
        assert (item.minimum, item.maximum) == (1, 9)
        assert (item.minimum_label, item.maximum_label) == (
            "Strongly disagree", "Strongly agree",
        )
        assert item.phase == "post_session"
        assert item.include_practice is False
        assert item.required is False  # The software permits missing responses.
        assert "10.1145/3717511.3747087" in item.source
        assert "Table 5" in item.source


@pytest.mark.parametrize("order", ["solver", "hybrid"])
def test_two_session_questionnaires_replay_and_export_without_practice_rows(order, tmp_path):
    data = json.loads((ROOT / "configs" / f"protocol-{order}-first.json").read_text())
    # Functional traversal only: no participant, camera, model or robot is run.
    data.update(purpose="demonstration", synthetic=True, output="text")
    for condition in data["conditions"]:
        condition["output"] = "text"
    now = [100.0]
    store = StudyStore(tmp_path / "data", now=lambda: now[0])
    pid = store.create(StudySpec.model_validate(data))["plan_id"]
    expected = []
    try:
        for index in range(1, 4):
            store.start(pid)
            state = store.snapshot(pid)
            sid = state["current"]["config"]["session_id"]
            store.command(pid, CommandRequest(
                request_id=f"end-{index}", session_id=sid, kind="withdraw",
            ))
            store.next(pid, f"after-{index}", store.snapshot(pid)["phase_id"])
            state = store.snapshot(pid)
            if index == 1:
                assert state["phase"] == "break"
            else:
                assert state["phase"] == "survey"
                assert len(state["survey_items"]) == 8
                request = SurveyRequest(request_id=f"survey-{index}", phase_id=state["phase_id"],
                                        answers={"iva2025-q1": 9, "iva2025-q8": 1})
                store.survey(pid, request)
                store.survey(pid, request)  # Same delivery must not add response rows.
                expected.append(sid)
            if index < 3:
                now[0] += 600
                store.next(pid, f"next-{index}", store.snapshot(pid)["phase_id"])
        assert store.snapshot(pid)["phase"] == "complete"
    finally:
        store.shutdown()
    reopened = StudyStore(tmp_path / "data", now=lambda: now[0])
    try:
        assert reopened.snapshot(pid)["phase"] == "complete"
        report = build_report(tmp_path / "data", tmp_path / "report")
        rows = json.loads((report / "analysis.json").read_text())["questionnaires"]
        assert len(rows) == 16
        assert {r["session_id"] for r in rows} == set(expected)
        assert {r["sequence_index"] for r in rows} == {2, 3}
        assert all(r["minimum_label"] == "Strongly disagree" for r in rows)
        assert sum(r["value"] is None for r in rows) == 12
        assert all(r["missing_reason"] == "not_answered" for r in rows if r["value"] is None)
        assert [r["value"] for r in rows if r["item_id"] == "iva2025-q8"] == [1, 1]
        with (report / "questionnaires.csv").open(newline="") as stream:
            exported = list(csv.DictReader(stream))
        assert sum(r["value"] == "" for r in exported) == 12
        assert all(r["value"] != "0" for r in exported)
    finally:
        reopened.shutdown()

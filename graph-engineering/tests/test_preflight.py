"""Offline, fake-GC deterministic intent sanity tests.

These do NOT prove that operator approval, native Bead behavior or agent/model
identity exists in a real Gas City host runtime.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "assets/scripts/checks/graph-preflight.py"
)
SPEC = importlib.util.spec_from_file_location("graph_preflight", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PreflightError = MODULE.PreflightError


@pytest.fixture()
def inputs(tmp_path: Path) -> dict:
    (tmp_path / "goal.md").write_text("# Approved for sample ONLY\n", encoding="utf-8")
    step = {
        "id": "graph.inspect",
        "metadata": {
            "gc.root_bead_id": "graph-run-1",
            "gc.graph.expected_convoy": "convoy-1",
            "gc.graph.goal_path": "goal.md",
            "gc.graph.artifact_root": "artifacts",
            "gc.graph.context_path": "",
        },
    }
    return {
        "step": step,
        "workflow_root": {
            "id": "graph-run-1", "metadata": {"gc.input_convoy_id": "convoy-1"}
        },
        "input_convoy": {"id": "convoy-1", "type": "convoy"},
        "rig": tmp_path,
    }


def test_verified_structure_cannot_claim_approval(inputs: dict) -> None:
    observed = MODULE.validate_preflight(**inputs)
    assert observed["status"] == "INPUT_SANITY_OK_NOT_AUTHORIZED"
    assert observed["approval_verdict"] == "NOT_ESTABLISHED"
    assert observed["host_claim_and_session_provenance"] == "NOT_VERIFIED"
    assert len(observed["goal_sha256"]) == 64


@pytest.mark.parametrize(
    "mutation",
    [
        "missing_root", "stale_root", "wrong_convoy", "fake_convoy", "missing_goal",
        "absolute_goal", "traversal_goal", "directory_goal", "bad_artifact",
        "absolute_artifact", "missing_context", "symlink_goal", "empty_goal",
    ],
)
def test_preflight_falsifiers_fail_closed(inputs: dict, mutation: str) -> None:
    sm = inputs["step"]["metadata"]
    root = inputs["rig"]
    if mutation == "missing_root":
        del sm["gc.root_bead_id"]
    elif mutation == "stale_root":
        sm["gc.root_bead_id"] = "stale-run"
    elif mutation == "wrong_convoy":
        sm["gc.graph.expected_convoy"] = "another-convoy"
    elif mutation == "fake_convoy":
        inputs["input_convoy"]["type"] = "task"
    elif mutation == "missing_goal":
        sm["gc.graph.goal_path"] = "missing.md"
    elif mutation == "absolute_goal":
        sm["gc.graph.goal_path"] = str(root / "goal.md")
    elif mutation == "traversal_goal":
        sm["gc.graph.goal_path"] = "../goal.md"
    elif mutation == "directory_goal":
        sm["gc.graph.goal_path"] = "subdir"
        (root / "subdir").mkdir()
    elif mutation == "bad_artifact":
        sm["gc.graph.artifact_root"] = "goal.md"
    elif mutation == "absolute_artifact":
        sm["gc.graph.artifact_root"] = str(root / "artifacts")
    elif mutation == "missing_context":
        sm["gc.graph.context_path"] = "missing.json"
    elif mutation == "symlink_goal":
        (root / "alias.md").symlink_to(root / "goal.md")
        sm["gc.graph.goal_path"] = "alias.md"
    elif mutation == "empty_goal":
        (root / "goal.md").write_text("")
    with pytest.raises((PreflightError, OSError)):
        MODULE.validate_preflight(**inputs)


def test_missing_metadata_fails_closed(inputs: dict) -> None:
    inputs["step"]["metadata"] = "untrusted-prose"
    with pytest.raises(PreflightError):
        MODULE.validate_preflight(**inputs)


def test_no_external_io_or_second_store_used_by_validator(inputs: dict) -> None:
    original = MODULE.subprocess.run
    def forbid(*args, **kwargs):
        raise AssertionError("pure validator attempted external command")
    MODULE.subprocess.run = forbid
    try:
        assert MODULE.validate_preflight(**inputs)["status"].startswith("INPUT_SANITY_OK")
    finally:
        MODULE.subprocess.run = original

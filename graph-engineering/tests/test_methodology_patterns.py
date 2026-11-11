"""Source-ledger compatibility patterns from actual maintained GasCity methodologies.

These are *offline authoring invariants*, NOT full host compilation or per-method
runtime evidence. Graph engineering is intentionally not the fifth build-base
derivative: it accepts an already-approved existing input convoy.
"""
from __future__ import annotations

import pathlib
import tomllib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
GRAPH = ROOT / "graph-engineering"
METHODS = {
    "bmad": "bmad-build",
    "compound-engineering": "compound-build",
    "superpowers": "superpowers-build",
    "gstack": "gstack-build",
}


def load(path: pathlib.Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("pack,formula", METHODS.items())
def test_proven_build_derivatives_are_explicit(pack: str, formula: str) -> None:
    # The fork's own upstream-derived methodology files are the fixtures.
    manifest = load(ROOT / pack / "pack.toml")
    derived = load(ROOT / pack / "formulas" / f"{formula}.formula.toml")
    assert manifest["pack"]["schema"] == 2
    assert manifest["imports"]["gc"]["source"] == "../gascity"
    assert derived["extends"] == ["build-base"]
    assert derived["target_required"] is True
    metadata = derived["metadata"]["gc"]["methodology"]
    assert set(metadata["interaction_modes"]) == {"interactive", "autonomous", "headless"}
    assert set(metadata["review_modes"]) == {"report", "agent", "interactive"}
    assert set(metadata["allowed_drain_policies"]) == {"separate", "same-session"}
    assert "GC-METH-012" in (ROOT / pack / "REQUIREMENTS.md").read_text()
    ids = [s["id"] for s in derived["steps"]]
    assert len(ids) == len(set(ids))


def test_graph_specialization_does_not_claim_to_implement_build_base() -> None:
    base = load(ROOT / "gascity/formulas/build-base.formula.toml")
    specialized = load(GRAPH / "formulas/graph-long-horizon.formula.toml")
    assert base["formula"] == "build-base"
    assert specialized["formula"] == "graph-long-horizon"
    assert "extends" not in specialized
    assert specialized["target_required"] is True
    assert specialized["steps"][0]["id"] == "inspect"
    assert "GC-METH-012" in (GRAPH / "REQUIREMENTS.md").read_text()


def test_proven_readiness_and_release_gate_anchor_points() -> None:
    bmad = load(ROOT / "bmad/formulas/bmad-build.formula.toml")
    ready = next(s for s in bmad["steps"] if s["id"] == "implementation-readiness")
    assert ready["needs"] == ["decompose"]
    for name in ("implement", "implement-same-session"):
        assert next(s for s in bmad["steps"] if s["id"] == name)["needs"] == ["implementation-readiness"]
    gstack = load(ROOT / "gstack/formulas/gstack-build.formula.toml")
    by = {s["id"]: s for s in gstack["steps"]}
    assert by["qa"]["needs"] == ["review"]
    assert by["release-readiness"]["needs"] == ["qa"]
    assert by["finalize"]["needs"] == ["release-readiness"]


def test_proven_superpowers_native_tdd_not_hidden_subagent() -> None:
    spec = load(ROOT / "superpowers/formulas/superpowers-development.formula.toml")
    steps = {s["id"]: s for s in spec["steps"]}
    chain = [
        "write-failing-test", "verify-test-fails", "implement-change",
        "verify-test-passes", "task-review", "record-item-result"
    ]
    assert spec["extends"] == ["do-work"]
    for a, b in zip(chain, chain[1:]):
        assert steps[b]["needs"] == [a]


def test_proven_compound_plan_review_uses_bounded_native_gate() -> None:
    spec = load(ROOT / "compound-engineering/formulas/compound-plan-review.formula.toml")
    assert spec["type"] == "expansion"
    loop = next(s for s in spec["template"] if "compound-plan-review-loop" in s["id"])
    assert loop["check"]["max_attempts"] == 6
    roles = {s["id"].split(".")[-1] for s in loop["children"]}
    assert {"coherence-review","feasibility-review","scope-review","architecture-review"}.issubset(roles)


def test_graph_pack_inspect_has_bounded_executable_input_sanity_gate() -> None:
    spec = load(GRAPH / "formulas/graph-long-horizon.formula.toml")
    inspect = next(s for s in spec["steps"] if s["id"] == "inspect")
    assert inspect["check"]["max_attempts"] == 2
    check = inspect["check"]["check"]
    assert check["mode"] == "exec"
    assert check["timeout"] == "2m"
    asset = (GRAPH / "formulas" / check["path"]).resolve(strict=True)
    assert asset.is_relative_to(GRAPH.resolve())
    assert asset.read_text().startswith("#!/usr/bin/env python3")
    assert "NOT_AUTHORIZED" in asset.read_text()

"""Reference-graph safety and Gas City formula packaging tests.

Runs offline; does not validate Gas City's live compiler, actual sessions, or host
state transitions. Mutations are synthetic counterexamples to the reference model.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tomllib

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
PACK = tomllib.loads((ROOT / "pack.toml").read_text())
FORMULA = tomllib.loads((ROOT / "formulas/graph-long-horizon.formula.toml").read_text())
SCHEMA = json.loads((ROOT / "schemas/semantic-graph.reference.schema.json").read_text())
EXAMPLE = json.loads((ROOT / "examples/semantic-graph.reference.json").read_text())


def validate_reference_graph(document: dict) -> None:
    """Non-authoritative but falsifiable pure structural check.

    This is NOT a Gas City graph runtime validator or Beads claim verifier.
    """
    jsonschema.Draft202012Validator(SCHEMA).validate(document)
    nodes = document["graph"]["nodes"]
    by_id = {}
    for node in nodes:
        if node["id"] in by_id:
            raise ValueError("duplicate node")
        by_id[node["id"]] = node
    for node in nodes:
        if node["id"] in node["needs"]:
            raise ValueError("self dependency")
        for predecessor in node["needs"]:
            if predecessor not in by_id:
                raise ValueError("missing predecessor")
    state = {}

    def visit(node_id: str) -> None:
        mark = state.get(node_id, 0)
        if mark == 1:
            raise ValueError("dependency cycle")
        if mark == 2:
            return
        state[node_id] = 1
        for dep in by_id[node_id]["needs"]:
            visit(dep)
        state[node_id] = 2

    for node_id in by_id:
        visit(node_id)
    reviewers = {"acceptance-review", "safety-review", "continuity-review"}
    if not reviewers.issubset(set(by_id)):
        raise ValueError("missing reviewer")
    if not reviewers.issubset(set(by_id["synthesize"]["needs"])):
        raise ValueError("incomplete review fanin")
    if len({by_id[r]["writer"] for r in reviewers}) != len(reviewers):
        raise ValueError("identical reviewer identities in reference fixture")


def test_pack_is_opt_in_and_composes_native_gascity() -> None:
    assert PACK["pack"]["schema"] == 2
    assert PACK["pack"]["name"] == "graph-engineering"
    assert PACK["imports"]["gc"]["source"] == "../gascity"
    assert not any(x in PACK for x in ("service", "named_session", "order"))
    assert FORMULA["formula"] == "graph-long-horizon"
    assert FORMULA["requires"]["formula_compiler"] == ">=2.0.0"
    assert FORMULA["target_required"] is True
    assert "contract" not in FORMULA  # avoid deprecated graph.v2 capability spelling
    assert "on_complete" not in (ROOT / "formulas/graph-long-horizon.formula.toml").read_text()


def test_native_drain_and_fanout_fanin() -> None:
    steps = FORMULA["steps"]
    by_id = {s["id"]: s for s in steps}
    assert len(steps) == len(by_id)
    assert by_id["drain"]["drain"] == {
        "context": "separate",
        "formula": "do-work",
        "member_access": "exclusive",
    }
    required = {"acceptance-review", "safety-review", "continuity-review"}
    assert all(by_id[s]["needs"] == ["drain"] for s in required)
    assert set(by_id["synthesize"]["needs"]) == required
    assert by_id["finalize"]["needs"] == ["synthesize"]
    assert not any("on_complete" in step or "provider_panel" in str(step) for step in steps)
    for step in steps:
        path = (ROOT / "formulas" / step["description_file"]).resolve()
        assert path.is_relative_to(ROOT.resolve())
        assert path.is_file(), (step["id"], path)
        assert step["metadata"]["gc.run_target"].startswith(("gc.", "{{implementation_target}}"))


def test_schema_and_example_are_reference_only() -> None:
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
    validate_reference_graph(EXAMPLE)
    assert EXAMPLE["authority"] == "REFERENCE_ONLY"
    assert EXAMPLE["evidence_class"] == "ILLUSTRATIVE"
    assert "RUNTIME_PASS" not in SCHEMA["properties"]["evidence_class"]["enum"]


@pytest.mark.parametrize(
    "mutation",
    ["duplicate", "missing", "cycle", "self", "no-reviewer", "same-writer", "missing-fanin"],
)
def test_controlled_graph_mutations_are_detected(mutation: str) -> None:
    candidate = copy.deepcopy(EXAMPLE)
    nodes = candidate["graph"]["nodes"]
    lookup = {n["id"]: n for n in nodes}
    if mutation == "duplicate":
        nodes.append(copy.deepcopy(nodes[0]))
    elif mutation == "missing":
        lookup["design"]["needs"] = ["absent"]
    elif mutation == "cycle":
        lookup["inspect"]["needs"] = ["finalize"]
    elif mutation == "self":
        lookup["inspect"]["needs"] = ["inspect"]
    elif mutation == "no-reviewer":
        nodes.remove(lookup["safety-review"])
    elif mutation == "same-writer":
        lookup["safety-review"]["writer"] = lookup["acceptance-review"]["writer"]
    elif mutation == "missing-fanin":
        lookup["synthesize"]["needs"].remove("continuity-review")
    with pytest.raises((ValueError, jsonschema.ValidationError)):
        validate_reference_graph(candidate)


@pytest.mark.parametrize("mutation", ["verified", "approved", "unrecognized"])
def test_source_generated_authority_cannot_be_declared(mutation: str) -> None:
    candidate = copy.deepcopy(EXAMPLE)
    if mutation == "verified":
        candidate["evidence_class"] = "RUNTIME_PASS"
    elif mutation == "approved":
        candidate["authority"] = "PUBLISHER"
    else:
        candidate["schema_version"] = "gc.graph-semantic-reference/overridden"
    with pytest.raises(jsonschema.ValidationError):
        validate_reference_graph(candidate)

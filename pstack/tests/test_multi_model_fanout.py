"""Real native DAG shape and negative evidence tests; no live model claim."""
from __future__ import annotations

import importlib.util
import json
import sys
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_script(filename: str):
    spec = importlib.util.spec_from_file_location(filename.removesuffix(".py"), ROOT / "scripts" / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("name,first,join", (
    ("swarm", "frame", "fanin"),
    ("arena", "trigger", "judge"),
    ("interrogate", "select", "judgment"),
))
def test_independent_model_lanes(name, first, join):
    path = ROOT / "formulas" / f"pstack-{name}-multi.formula.toml"
    formula = tomllib.loads(path.read_text(encoding="utf-8"))
    assert formula["requires"]["formula_compiler"] == ">=2.0.0"
    assert all(v["required"] for v in formula["vars"].values())
    steps = {step["id"]: step for step in formula["steps"]}
    assert len(steps) == (7 if name == "arena" else 6)
    assert not steps[first].get("needs")
    targets = []
    outputs = []
    for lane in "abc":
        step = steps[f"lane-{lane}"]
        assert step["needs"] == [first]
        meta = step["metadata"]
        assert meta["gc.run_target"] == f"pstack.panel-{lane}"
        assert meta["pstack.multi.lane_id"] == lane
        assert meta["pstack.multi.artifact_dir"] == "{{artifact_root}}/pstack/multi/" + name
        assert meta["pstack.multi.output_path"].endswith(f"lane-{lane}.json")
        targets.append(meta["gc.run_target"])
        outputs.append(meta["pstack.multi.output_path"])
    assert len(set(targets)) == len(set(outputs)) == 3
    assert set(steps["evidence-gate"]["needs"]) == {"lane-a", "lane-b", "lane-c"}
    assert steps["evidence-gate"]["check"]["check"]["path"] == "../scripts/check_multi_model_evidence.py"
    assert steps["evidence-gate"]["check"]["check"]["mode"] == "exec"
    assert steps["evidence-gate"]["metadata"]["pstack.multi.city_config"] == "{{city_config}}"
    assert steps["evidence-gate"]["metadata"]["pstack.multi.rig_name"] == "{{rig_name}}"
    assert steps[join]["needs"] == ["evidence-gate"]
    if name == "arena":
        assert steps["verify"]["needs"] == ["judge"]
    assert "gc.provider_panel" not in path.read_text()
    assert "gc.graph_operator" not in path.read_text()
    for step in steps.values():
        assert (path.parent / step["description_file"]).resolve().is_file()


def test_panel_roles_are_providerless():
    for lane in "abc":
        config = tomllib.loads((ROOT / f"agents/panel-{lane}/agent.toml").read_text())
        assert config["scope"] == "rig"
        assert config["fallback"] is True
        assert "provider" not in config
        assert "option_defaults" not in config


def receipt(lane, **override):
    value = dict(
        schema="pstack.multi-lane.v1", workflow="swarm", workflow_id="bead-1",
        lane_id=lane, run_target=f"pstack.panel-{lane}",
        provider=("claude", "codex", "gemini")["abc".index(lane)],
        model=("sonnet", "gpt-5.5", "gemini-2.5-pro")["abc".index(lane)],
        source_revision="abc1234", status="complete",
        summary="Evidence-backed finding", evidence=["file.py:12"],
        findings=[dict(id="F1", claim="Observed", evidence_refs=["file.py:12"])],
    )
    value.update(override)
    return value


def setup_receipts(root):
    folder = root / ".gc" / "runs" / "test" / "pstack" / "multi" / "swarm"
    folder.mkdir(parents=True)
    for lane in "abc":
        (folder / f"lane-{lane}.json").write_text(json.dumps(receipt(lane)))
    return folder


def checked(check, root):
    return check.validate_receipts(root, ".gc/runs/test/pstack/multi/swarm", "swarm", "bead-1", "abc1234")


def test_three_lane_gate_passes_valid_receipts(tmp_path):
    check = load_script("check_multi_model_evidence.py")
    setup_receipts(tmp_path)
    assert len(checked(check, tmp_path)) == 3


@pytest.mark.parametrize("changes", [
    {"model": "sonnet"},
    {"source_revision": "old-sha"},
    {"status": "blocked"},
    {"workflow_id": "wrong-run"},
    {"lane_id": "a"},
    {"model": "auto"},
    {"evidence": []},
    {"findings": [dict(id="F1", claim="Unsupported", evidence_refs=[])]},
])
def test_three_lane_gate_blocks_invalid_receipts(tmp_path, changes):
    check = load_script("check_multi_model_evidence.py")
    folder = setup_receipts(tmp_path)
    (folder / "lane-b.json").write_text(json.dumps(receipt("b", **changes)))
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)


def test_three_lane_gate_blocks_missing_corrupt_symlink_and_escape(tmp_path):
    check = load_script("check_multi_model_evidence.py")
    folder = setup_receipts(tmp_path)
    b = folder / "lane-b.json"
    b.unlink()
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)
    b.write_text("corrupt json")
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)
    b.unlink()
    elsewhere = tmp_path / "elsewhere.json"
    elsewhere.write_text(json.dumps(receipt("b")))
    b.symlink_to(elsewhere)
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)
    with pytest.raises(check.EvidenceError):
        check.validate_receipts(tmp_path, "../../outside", "swarm", "bead-1", "abc1234")


def city(models=("sonnet", "gpt-5.5", "gemini-2.5-pro")):
    lines = ['[[rigs]]', 'name = "app"']
    for lane, provider, model in zip("abc", ("claude", "codex", "gemini"), models):
        lines += ["[[rigs.patches]]", f'agent = "pstack.panel-{lane}"',
                  f'provider = "{provider}"',
                  f'option_defaults = {{ model = "{model}" }}']
    return "\n".join(lines) + "\n"


def test_declared_city_model_binding_preflight(tmp_path):
    check = load_script("check_multi_model_city.py")
    path = tmp_path / "city.toml"
    path.write_text(city())
    assert len(check.check_city(path, "app")) == 3
    path.write_text(city(("sonnet", "sonnet", "gemini-2.5-pro")))
    with pytest.raises(check.PanelConfigError):
        check.check_city(path, "app")
    path.write_text(city().replace('provider = "gemini"', 'provider = "unknown-runtime"'))
    with pytest.raises(check.PanelConfigError):
        check.check_city(path, "app")
    path.write_text(city().replace('model = "sonnet"', 'model = "auto"'))
    with pytest.raises(check.PanelConfigError):
        check.check_city(path, "app")


def test_original_method_formulas_are_not_replaced():
    for stem in ("swarm", "arena", "interrogate"):
        old = tomllib.loads((ROOT / "formulas" / f"pstack-{stem}.formula.toml").read_text())
        assert not any(step["id"].startswith("lane-") for step in old["steps"])


def test_receipts_must_match_declared_role_config(tmp_path):
    evidence = load_script("check_multi_model_evidence.py")
    city_check = load_script("check_multi_model_city.py")
    path = tmp_path / "city.toml"
    path.write_text(city())
    binding = city_check.check_city(path, "app")
    setup_receipts(tmp_path)
    assert len(evidence.validate_receipts(
        tmp_path, ".gc/runs/test/pstack/multi/swarm", "swarm", "bead-1", "abc1234", binding
    )) == 3
    mismatched = dict(binding)
    mismatched["pstack.panel-a"] = ("claude", "a-different-model")
    with pytest.raises(evidence.EvidenceError):
        evidence.validate_receipts(
            tmp_path, ".gc/runs/test/pstack/multi/swarm", "swarm", "bead-1", "abc1234", mismatched
        )


def test_evidence_rejects_symlinked_directory_and_oversized_receipt(tmp_path):
    check = load_script("check_multi_model_evidence.py")
    folder = setup_receipts(tmp_path)
    b = folder / "lane-b.json"
    b.write_bytes(b" " * 1_048_577)
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)
    b.write_text(json.dumps(receipt("b")))
    real = folder.parent / "swarm-real"
    folder.rename(real)
    folder.symlink_to(real, target_is_directory=True)
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)


def test_evidence_rejects_too_many_findings_and_references(tmp_path):
    check = load_script("check_multi_model_evidence.py")
    folder = setup_receipts(tmp_path)
    many = receipt("b")
    many["findings"] = many["findings"] * 201
    (folder / "lane-b.json").write_text(json.dumps(many))
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)
    many = receipt("b")
    many["evidence"] = many["evidence"] * 501
    (folder / "lane-b.json").write_text(json.dumps(many))
    with pytest.raises(check.EvidenceError):
        checked(check, tmp_path)

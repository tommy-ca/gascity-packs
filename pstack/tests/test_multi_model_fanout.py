"""Dynamic N-task PStack host-fanout contracts and negative routing checks.

Static tests only: native Gas City runtime integration is a separate proof gate.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tomllib
from pathlib import Path
from types import SimpleNamespace
import pytest

PACK = Path(__file__).resolve().parents[1]
REV = "a" * 40

def load(name):
    p = PACK / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), p)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def environment(tmp_path, count=5, role_count=2):
    roles = [(f"city.worker-{i}", ("claude", "codex", "gemini")[i % 3], f"model-{i}") for i in range(role_count)]
    lines = ['[[rigs]]', 'name = "app"']
    for target, provider, model in roles:
        lines += ["[[rigs.patches]]", f'agent = "{target}"',
                  f'provider = "{provider}"', f'option_defaults = {{ model = "{model}" }}']
    (tmp_path / "src").mkdir(exist_ok=True)
    (tmp_path / "src" / "module.py").write_text("x = 1\n")
    city = tmp_path / "city.toml"
    city.write_text("\n".join(lines) + "\n")
    policy = {"version": 1, "max_tasks": 64,
              "routes": [dict(target=r, provider=p, model=m) for r,p,m in roles]}
    plan = {"method": "swarm", "revision": REV, "artifact_root": "runs/run-001",
            "tasks": [dict(id=f"task{i}", route_target=roles[i % len(roles)][0],
                           scope_ref="src/module.py", objective=f"Inspect slice {i}")
                      for i in range(count)]}
    return plan, policy, city

@pytest.mark.parametrize("count", [2, 3, 5, 8, 64])
def test_dynamic_cardinality_without_panels(tmp_path, count):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path, count)
    result = check.validate(plan, policy, city, "app", tmp_path, "root-01")
    assert len(result["tasks"]) == count
    assert len({x["model"] for x in result["tasks"]}) == 2
    assert len({x["artifact_path"] for x in result["tasks"]}) == count

@pytest.mark.parametrize("method", ["swarm", "arena", "interrogate"])
def test_dynamic_host_formula_fans_out_from_output(method):
    body = tomllib.loads((PACK / f"formulas/pstack-{method}-multi.formula.toml").read_text())
    steps = {x["id"]: x for x in body["steps"]}
    on = steps["plan"]["on_complete"]
    assert on["for_each"] == "output.tasks"
    assert on["bond"] == "pstack-dynamic-worker"
    assert on["parallel"] is True
    assert on["vars"]["route_target"] == "{item.route_target}"
    assert len(steps) == 1
    assert "synthesize" not in steps
    # Host injects plan-fanout AFTER authored-graph validation; it is not a legal authored needs reference.
    assert not any(x.startswith("lane-") for x in steps)
    assert "gc.provider_panel" not in str(body)
    assert all(x["required"] for x in body["vars"].values())
    assert "verify" not in steps  # synthesis is a separately gated second workflow

def test_dynamic_worker_is_one_reusable_expansion():
    body = tomllib.loads((PACK / "formulas/pstack-dynamic-worker.formula.toml").read_text())
    assert body["type"] == "expansion"
    assert len(body["template"]) == 1
    item = body["template"][0]
    assert item["metadata"]["gc.run_target"] == "{route_target}"
    assert item["metadata"]["pstack.dynamic.artifact_path"] == "{artifact_path}"
    assert item["check"]["check"]["path"] == "../scripts/check_dynamic_task.py"

@pytest.mark.parametrize("mutator", [
    lambda p: p["tasks"][0].update(route_target="evil.shell"),
    lambda p: p["tasks"][0].update(id="../escape"),
    lambda p: p["tasks"][1].update(id="TASK0"),
    lambda p: p["tasks"][0].update(scope_ref="../../outside"),
    lambda p: p.update(revision="floating-main"),
    lambda p: p.update(artifact_root="../../bad"),
    lambda p: p["tasks"][0].update(objective="bad\x00instruction"),
    lambda p: p.update(tasks=p["tasks"][:1]),
])
def test_dynamic_plan_rejects_malicious_or_invalid_input(tmp_path, mutator):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    mutator(plan)
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")

def test_dynamic_plan_rejects_duplicate_or_unbound_routes(tmp_path):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    policy["routes"].append(dict(policy["routes"][0]))
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")
    policy["routes"].pop()
    text = city.read_text().replace('model = "model-0"', 'model = "mismatch"')
    city.write_text(text)
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")

def test_dynamic_plan_blocks_single_model_or_over_cap(tmp_path):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path, 5, 1)
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")
    plan, policy, city = environment(tmp_path, 8, 2)
    policy["max_tasks"] = 4
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")

def test_dynamic_plan_blocks_symlinked_scope_and_artifact_root(tmp_path):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    (tmp_path / "src" / "module.py").unlink()
    (tmp_path / "src").rmdir()
    (tmp_path / "src").symlink_to(tmp_path.parent, target_is_directory=True)
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")
    (tmp_path / "src").unlink()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "module.py").write_text("x = 1\n")
    (tmp_path / "runs").symlink_to(tmp_path.parent, target_is_directory=True)
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01")

def metadata(item):
    return {
        "pstack.dynamic.task_id": item["task_id"],
        "pstack.dynamic.route_target": item["route_target"],
        "pstack.dynamic.revision": item["revision"],
        "pstack.dynamic.workflow_id": item["workflow_id"],
        "pstack.dynamic.method": item["method"],
        "pstack.dynamic.provider": item["provider"],
        "pstack.dynamic.model": item["model"],
        "pstack.dynamic.artifact_path": item["artifact_path"],
    }

def receipt(item, **kwargs):
    fields = {"schema": "pstack.dynamic-task.v1", "status": "complete",
              "summary": "Independent evidence", "evidence": ["src/module.py:12"],
              "findings": [{"claim": "Observed source behavior"}]}
    fields.update({field: item[field] for field in
                   ("task_id","route_target","revision","workflow_id","method","provider","model")})
    fields.update(kwargs)
    return fields

def store_receipt(tmp_path, item, content=None):
    p = tmp_path / item["artifact_path"]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(receipt(item) if content is None else content))
    return p

def test_dynamic_task_receipt_validation(tmp_path):
    plan, policy, city = environment(tmp_path)
    items = load("dynamic_contract.py").validate(plan, policy, city, "app", tmp_path, "root-01")["tasks"]
    check = load("check_dynamic_task.py")
    path = store_receipt(tmp_path, items[0])
    assert check.validate(tmp_path, metadata(items[0]))["task_id"] == "task0"
    for change in ({"status":"blocked"}, {"revision":"stale"}, {"model":"fake"}, {"evidence":[]}, {"findings":[{}]}):
        path.write_text(json.dumps(receipt(items[0], **change)))
        with pytest.raises(check.TaskError):
            check.validate(tmp_path, metadata(items[0]))

def test_dynamic_task_rejects_oversized_symlink_and_wrong_path(tmp_path):
    plan, policy, city = environment(tmp_path)
    item = load("dynamic_contract.py").validate(plan, policy, city, "app", tmp_path, "root-01")["tasks"][0]
    check = load("check_dynamic_task.py")
    p = store_receipt(tmp_path, item)
    p.write_bytes(b" " * 1_048_577)
    with pytest.raises(check.TaskError):
        check.validate(tmp_path, metadata(item))
    p.unlink()
    outside = tmp_path / "other.json"
    outside.write_text(json.dumps(receipt(item)))
    p.symlink_to(outside)
    with pytest.raises(check.TaskError):
        check.validate(tmp_path, metadata(item))
    data = metadata(item)
    data["pstack.dynamic.artifact_path"] = "../../escape.json"
    with pytest.raises(check.TaskError):
        check.validate(tmp_path, data)

def test_publish_fails_on_nonpersisted_metadata(tmp_path, monkeypatch):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    output = check.validate(plan, policy, city, "app", tmp_path, "root-01")
    calls = []
    def run(args, **kwargs):
        calls.append(args)
        if args[2] == "update":
            return SimpleNamespace(returncode=0, stdout="", stderr="")
        return SimpleNamespace(returncode=0, stdout=json.dumps({"metadata":{}}), stderr="")
    monkeypatch.setattr(check.subprocess, "run", run)
    with pytest.raises(check.ContractError):
        check.publish("bead-001", output)
    assert any(call[:5] == ["gc", "bd", "update", "bead-001", "--set-metadata"] for call in calls)

def test_fixed_panel_roles_and_templates_are_not_required():
    for lane in "abc":
        assert not (PACK / f"agents/panel-{lane}").exists()
    for legacy in ("swarm", "arena", "interrogate"):
        formula = tomllib.loads((PACK / f"formulas/pstack-{legacy}.formula.toml").read_text())
        assert not any(x["id"].startswith("lane-") for x in formula["steps"])


def test_synthesis_is_separate_and_depends_on_verified_fanin():
    body = tomllib.loads((PACK / "formulas/pstack-dynamic-synthesize.formula.toml").read_text())
    steps = {x["id"]: x for x in body["steps"]}
    assert set(steps) == {"verify-fanin", "synthesize", "verify"}
    assert steps["verify-fanin"]["check"]["check"]["path"] == "../scripts/check_dynamic_fanin.py"
    assert steps["synthesize"]["needs"] == ["verify-fanin"]
    assert steps["verify"]["needs"] == ["synthesize"]


def test_fanin_requires_source_workflow_pass_and_exact_task_receipts(tmp_path):
    plan, policy, city = environment(tmp_path, 5)
    items = load("dynamic_contract.py").validate(plan, policy, city, "app", tmp_path, "root-01")["tasks"]
    checker = load("check_dynamic_fanin.py")
    worker = load("check_dynamic_task.py")
    for item in items:
        store_receipt(tmp_path, item)
        assert worker.validate(tmp_path, metadata(item))["task_id"] == item["task_id"]
    planning = {"id": "plan-bead", "metadata": {"gc.root_bead_id":"root-01",
                "gc.output_json": json.dumps({"tasks": items})}}
    root = {"id": "root-01", "status":"closed", "metadata":{"gc.outcome":"pass"}}
    assert len(checker.validate(tmp_path, root, planning, "swarm", REV, "root-01")) == 5
    root["metadata"]["gc.outcome"] = "fail"
    with pytest.raises(checker.FanInError):
        checker.validate(tmp_path, root, planning, "swarm", REV, "root-01")
    root["metadata"]["gc.outcome"] = "pass"
    (tmp_path / items[3]["artifact_path"]).unlink()
    with pytest.raises(checker.FanInError):
        checker.validate(tmp_path, root, planning, "swarm", REV, "root-01")


def test_publish_context_rejects_policy_city_root_substitution(tmp_path):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    policyfile = tmp_path / "routes.json"
    policyfile.write_text(json.dumps(policy))
    args = SimpleNamespace(
        root=str(tmp_path), city=str(city), policy=str(policyfile),
        workflow_id="root-01", rig="app"
    )
    meta = {
        "gc.root_bead_id": "root-01",
        "pstack.dynamic.method": "swarm",
        "pstack.dynamic.revision": REV,
        "pstack.dynamic.artifact_root": "runs/run-001",
        "pstack.dynamic.rig_name": "app",
        "pstack.dynamic.city_config": str(city),
        "pstack.dynamic.route_policy": str(policyfile),
        "pstack.dynamic.subject_path": "src",
    }
    check.validate_publish_context(args, meta, plan, str(tmp_path))
    for field, attr, invalid in (
        ("route_policy", "policy", str(tmp_path / "unapproved.json")),
        ("city_config", "city", str(tmp_path / "different-city.toml")),
    ):
        mutated = SimpleNamespace(**vars(args))
        setattr(mutated, attr, invalid)
        with pytest.raises(check.ContractError):
            check.validate_publish_context(mutated, meta, plan, str(tmp_path))
    with pytest.raises(check.ContractError):
        check.validate_publish_context(args, meta, plan, str(tmp_path.parent))


def test_scope_must_stay_inside_operator_authorized_subject(tmp_path):
    check = load("dynamic_contract.py")
    plan, policy, city = environment(tmp_path)
    result = check.validate(plan, policy, city, "app", tmp_path, "root-01", allowed_subject="src")
    assert len(result["tasks"]) == 5
    (tmp_path / "other.py").write_text("x = 3")
    plan["tasks"][0]["scope_ref"] = "other.py"
    with pytest.raises(check.ContractError):
        check.validate(plan, policy, city, "app", tmp_path, "root-01", allowed_subject="src")

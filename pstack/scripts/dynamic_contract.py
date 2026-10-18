#!/usr/bin/env python3
"""PStack dynamic task/route contract. Gas City owns child creation and sessions."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

METHODS = {"swarm", "arena", "interrogate"}
IDENT = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
TARGET = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,127}$")
MAX_ITEMS = 64
MAX_METADATA = 60000

class ContractError(ValueError):
    pass

def record(obj, keys, label):
    if not isinstance(obj, dict) or set(obj) != set(keys):
        raise ContractError(f"{label}: expected exactly {sorted(keys)}")
    return obj

def text_field(value, name, limit=256):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ContractError(f"{name}: empty, malformed or too long")
    return value

def secure_child(root: Path, rel: str) -> Path:
    p = Path(rel)
    if p.is_absolute() or not p.parts or any(x in {"", ".", ".."} for x in p.parts):
        raise ContractError("unsafe artifact path")
    base = root.resolve()
    curr = base
    for part in p.parts:
        curr = curr / part
        if curr.is_symlink():
            raise ContractError("symlink in artifact path")
    resolved = curr.resolve()
    if base not in resolved.parents:
        raise ContractError("artifact escaped rig")
    return resolved

def city_roles(city_path: Path, rig: str) -> dict:
    data = tomllib.loads(city_path.read_text(encoding="utf-8"))
    matches = [x for x in data.get("rigs", []) if x.get("name") == rig]
    if len(matches) != 1:
        raise ContractError(f"expected one rig named {rig!r}")
    roles = {}
    for patch in matches[0].get("patches", []):
        name = patch.get("agent")
        if name in roles:
            raise ContractError(f"duplicate city rig patch: {name}")
        if isinstance(name, str):
            roles[name] = patch
    return roles

def validate(plan: dict, policy: dict, city_path: Path, rig: str, root: Path, workflow_id: str) -> dict:
    record(plan, {"method", "revision", "artifact_root", "tasks"}, "plan")
    record(policy, {"version", "max_tasks", "routes"}, "policy")
    method = plan["method"]
    if method not in METHODS:
        raise ContractError("unknown method")
    revision = text_field(plan["revision"], "revision", 128)
    if not re.fullmatch(r"[a-fA-F0-9]{40,64}", revision):
        raise ContractError("revision must be immutable 40/64-digit hex SHA")
    runroot = text_field(plan["artifact_root"], "artifact_root", 200)
    secure_child(root, runroot)
    if policy["version"] != 1 or type(policy["max_tasks"]) is not int or not 2 <= policy["max_tasks"] <= MAX_ITEMS:
        raise ContractError("invalid policy cap")
    allowed = policy["routes"]
    if not isinstance(allowed, list) or not allowed:
        raise ContractError("missing route inventory")
    roles = city_roles(city_path, rig)
    route_map = {}
    for item in allowed:
        record(item, {"target", "provider", "model"}, "route")
        target = text_field(item["target"], "target", 128)
        if not TARGET.fullmatch(target) or target in route_map:
            raise ContractError("invalid or duplicate target")
        provider = text_field(item["provider"], "provider", 128)
        model = text_field(item["model"], "model", 128)
        configured = roles.get(target, {})
        if configured.get("provider") != provider or configured.get("option_defaults", {}).get("model") != model:
            raise ContractError(f"{target}: not explicitly bound to declared provider and model")
        if model.casefold() in {"auto", "unknown", "default"}:
            raise ContractError("model must be concrete")
        route_map[target] = (provider, model)
    tasks = plan["tasks"]
    if not isinstance(tasks, list) or not 2 <= len(tasks) <= policy["max_tasks"]:
        raise ContractError("task count outside allowed range")
    task_ids, result, models = set(), [], set()
    workflow_id = text_field(workflow_id, "workflow_id", 128)
    for task in tasks:
        record(task, {"id", "route_target", "scope_ref", "objective"}, "task")
        task_id = text_field(task["id"], "task id", 64)
        if not IDENT.fullmatch(task_id) or task_id.casefold() in task_ids:
            raise ContractError("duplicate or unsafe task id")
        task_ids.add(task_id.casefold())
        route = task["route_target"]
        if route not in route_map:
            raise ContractError("task selected a route outside allowlist")
        scope_ref = text_field(task["scope_ref"], "scope_ref", 200)
        # Only reference files relative to rig; prevent absolute, symlink and traversal.
        secure_child(root, scope_ref)
        objective = text_field(task["objective"], "objective", 500)
        if any(x in objective for x in ("\x00", "\r")):
            raise ContractError("invalid objective characters")
        provider, model = route_map[route]
        models.add(model.casefold())
        relative = f"{runroot}/pstack/dynamic/{method}/{task_id}.json"
        secure_child(root, relative)
        result.append({
            "task_id": task_id,
            "route_target": route,
            "scope_ref": scope_ref,
            "objective": objective,
            "artifact_path": relative,
            "revision": revision,
            "workflow_id": workflow_id,
            "method": method,
            "provider": provider,
            "model": model,
        })
    if len(models) < 2:
        raise ContractError("multi-model execution needs at least two distinct models")
    data = {"tasks": result}
    raw = json.dumps(data, separators=(",", ":"), ensure_ascii=True)
    if len(raw.encode("utf-8")) > MAX_METADATA:
        raise ContractError("fanout metadata exceeds 60KB")
    return data

def publish(bead_id: str, data: dict) -> None:
    raw = json.dumps(data, separators=(",", ":"), ensure_ascii=True)
    proc = subprocess.run(
        ["gc", "bd", "update", bead_id, "--set-metadata", "gc.output_json=" + raw],
        check=False, capture_output=True, text=True, timeout=30,
    )
    if proc.returncode:
        raise ContractError("gc bd update refused metadata: " + proc.stderr[:300])
    check = subprocess.run(["gc", "bd", "show", bead_id, "--json"], capture_output=True, text=True, timeout=30)
    if check.returncode:
        raise ContractError("cannot verify metadata persistence")
    current = json.loads(check.stdout)
    if isinstance(current, list):
        if len(current) != 1:
            raise ContractError("ambiguous source bead")
        current = current[0]
    if json.loads(current.get("metadata", {}).get("gc.output_json", "null")) != data:
        raise ContractError("gc.output_json did not persist exact validated plan")

def main() -> int:
    ap = argparse.ArgumentParser()
    for field in ("plan", "policy", "city", "root", "rig", "workflow-id"):
        ap.add_argument("--" + field, required=True)
    ap.add_argument("--bead-id")
    args = ap.parse_args()
    try:
        data = validate(
            json.loads(Path(args.plan).read_text(encoding="utf-8")),
            json.loads(Path(args.policy).read_text(encoding="utf-8")),
            Path(args.city), args.rig, Path(args.root), args.workflow_id,
        )
        if args.bead_id:
            publish(args.bead_id, data)
        else:
            print(json.dumps(data, indent=2))
    except (ContractError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print(f"pstack dynamic plan: BLOCKED: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail-closed post-workflow fan-in verifier, without a polling scheduler."""
from __future__ import annotations
import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

class FanInError(ValueError):
    pass

def metadata(bead):
    if isinstance(bead, list):
        if len(bead) != 1:
            raise FanInError("ambiguous Bead query")
        bead = bead[0]
    if not isinstance(bead, dict):
        raise FanInError("invalid Bead response")
    return bead

def read_bead(bead_id):
    if not bead_id:
        raise FanInError("missing Bead id")
    run = subprocess.run(["gc","bd","show",bead_id,"--json"],capture_output=True,text=True,timeout=30)
    if run.returncode:
        raise FanInError(f"cannot read Bead {bead_id}")
    return metadata(json.loads(run.stdout))

def load_worker_validator():
    path = Path(__file__).with_name("check_dynamic_task.py")
    spec = importlib.util.spec_from_file_location("pstack_dynamic_check_one", path)
    if spec is None or spec.loader is None:
        raise FanInError("worker validator unavailable")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def validate(root, workflow, planning, method, revision, expected_root):
    workflow = metadata(workflow)
    planning = metadata(planning)
    if workflow.get("id") != expected_root or workflow.get("status") != "closed":
        raise FanInError("source workflow is not fully closed")
    if workflow.get("metadata", {}).get("gc.outcome") != "pass":
        raise FanInError("source fanout did not complete successfully")
    if planning.get("metadata", {}).get("gc.root_bead_id") != expected_root:
        raise FanInError("planning Bead belongs to another source root")
    try:
        output = json.loads(planning.get("metadata", {}).get("gc.output_json", "null"))
    except ValueError as exc:
        raise FanInError(f"invalid source manifest: {exc}") from exc
    if not isinstance(output, dict) or set(output) != {"tasks"} or not isinstance(output["tasks"], list):
        raise FanInError("missing dynamic plan in source Bead")
    tasks = output["tasks"]
    if not 2 <= len(tasks) <= 64:
        raise FanInError("invalid dynamic task cardinality")
    check = load_worker_validator()
    seen, models, results = set(), set(), []
    for item in tasks:
        if not isinstance(item, dict):
            raise FanInError("invalid task descriptor")
        task_id = item.get("task_id")
        if not isinstance(task_id, str) or not task_id or task_id in seen:
            raise FanInError("duplicate or missing task ID")
        seen.add(task_id)
        if item.get("method") != method or item.get("revision") != revision or item.get("workflow_id") != expected_root:
            raise FanInError("stale/wrong source manifest")
        fields = {
            "pstack.dynamic."+key: item.get(key, "")
            for key in ("task_id","route_target","revision","workflow_id","method","provider","model")
        }
        fields["pstack.dynamic.artifact_path"] = item.get("artifact_path", "")
        try:
            result = check.validate(Path(root), fields)
        except (ValueError, OSError) as exc:
            raise FanInError(f"task {task_id}: {exc}") from exc
        models.add(item["model"].casefold())
        results.append(result)
    if len(models) < 2:
        raise FanInError("manifest does not use multiple models")
    return results

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path)
    ap.add_argument("--root-bead-json",type=Path)
    ap.add_argument("--planning-bead-json",type=Path)
    ap.add_argument("--method")
    ap.add_argument("--revision")
    ap.add_argument("--source-root-bead")
    args=ap.parse_args()
    try:
        if args.root is not None:
            if not all((args.root_bead_json,args.planning_bead_json,args.method,args.revision,args.source_root_bead)):
                raise FanInError("offline check requires all fields")
            workflow=json.loads(args.root_bead_json.read_text())
            planning=json.loads(args.planning_bead_json.read_text())
            root=args.root
            method=args.method
            revision=args.revision
            source_root=args.source_root_bead
        else:
            gate_id=os.environ.get("GC_BEAD_ID","")
            gate=read_bead(gate_id)
            m=gate.get("metadata") or {}
            source_root=m.get("pstack.dynamic.source_root_bead")
            plan_id=m.get("pstack.dynamic.planning_bead")
            method=m.get("pstack.dynamic.method")
            revision=m.get("pstack.dynamic.revision")
            root=next((os.environ[n] for n in ("GC_RIG_ROOT","GC_BEADS_SCOPE_ROOT","GC_STORE_PATH") if os.environ.get(n)),"")
            if not root:
                raise FanInError("trusted rig root missing")
            workflow=read_bead(source_root)
            planning=read_bead(plan_id)
        items=validate(root,workflow,planning,method,revision,source_root)
        print(f"dynamic fan-in: validated {len(items)} completed receipts, multiple declared models; verify live sessions separately")
    except (OSError, ValueError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f"dynamic fan-in: BLOCKED: {exc}",file=sys.stderr)
        return 1
    return 0

if __name__=="__main__":
    raise SystemExit(main())

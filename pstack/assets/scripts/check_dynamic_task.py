#!/usr/bin/env python3
"""Validate one dynamically expanded Gas City worker receipt. No agent execution."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

MAX_BYTES = 1_048_576

class TaskError(ValueError):
    pass

def required(obj: dict, key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise TaskError(f"{key}: missing non-empty string")
    return value

def validate(root: Path, meta: dict) -> dict:
    root = root.resolve()
    rel = Path(required(meta, "pstack.dynamic.artifact_path"))
    if rel.is_absolute() or ".." in rel.parts or "." in rel.parts:
        raise TaskError("unsafe task artifact path")
    current = root
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            raise TaskError("linked task evidence path")
    if root not in current.resolve().parents or not current.is_file():
        raise TaskError("missing task artifact in rig root")
    if current.stat().st_size > MAX_BYTES:
        raise TaskError("task receipt too large")
    try:
        receipt = json.loads(current.read_text(encoding="utf-8"))
    except (UnicodeError, OSError, ValueError) as exc:
        raise TaskError(f"invalid task receipt: {exc}") from exc
    if not isinstance(receipt, dict):
        raise TaskError("receipt must be object")
    for key, meta_key in (
        ("task_id", "pstack.dynamic.task_id"),
        ("route_target", "pstack.dynamic.route_target"),
        ("revision", "pstack.dynamic.revision"),
        ("workflow_id", "pstack.dynamic.workflow_id"),
        ("method", "pstack.dynamic.method"),
        ("provider", "pstack.dynamic.provider"),
        ("model", "pstack.dynamic.model"),
    ):
        if receipt.get(key) != required(meta, meta_key):
            raise TaskError(f"{key}: does not match immutable routed task")
    if receipt.get("schema") != "pstack.dynamic-task.v1" or receipt.get("status") != "complete":
        raise TaskError("receipt is incomplete, failed or has wrong schema")
    required(receipt, "summary")
    evidence = receipt.get("evidence")
    if not isinstance(evidence, list) or not evidence or len(evidence) > 500 or not all(
        isinstance(x, str) and x.strip() for x in evidence
    ):
        raise TaskError("invalid evidence array")
    findings = receipt.get("findings")
    if not isinstance(findings, list) or len(findings) > 200:
        raise TaskError("invalid findings")
    for item in findings:
        if not isinstance(item, dict) or not isinstance(item.get("claim"), str) or not item["claim"].strip():
            raise TaskError("invalid finding")
    return receipt

def runtime_meta() -> tuple[Path, dict]:
    bead = os.environ.get("GC_BEAD_ID")
    if not bead:
        raise TaskError("GC_BEAD_ID missing")
    result = subprocess.run(["gc", "bd", "show", bead, "--json"], capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise TaskError("cannot read Gas City check bead")
    value = json.loads(result.stdout)
    if isinstance(value, list):
        if len(value) != 1:
            raise TaskError("ambiguous check bead")
        value = value[0]
    root = next((os.environ[x] for x in ("GC_RIG_ROOT", "GC_BEADS_SCOPE_ROOT", "GC_STORE_PATH")
                 if os.environ.get(x)), "")
    if not root:
        raise TaskError("rig root not available")
    return Path(root), value.get("metadata") or {}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path)
    ap.add_argument("--metadata-json", type=Path)
    a = ap.parse_args()
    try:
        root, metadata = (
            (a.root, json.loads(a.metadata_json.read_text(encoding="utf-8")))
            if a.root and a.metadata_json else runtime_meta()
        )
        validate(root, metadata)
    except (OSError, ValueError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f"pstack dynamic worker: BLOCKED: {exc}", file=sys.stderr)
        return 1
    print("pstack dynamic worker: receipt valid; live model/session attestation separate")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

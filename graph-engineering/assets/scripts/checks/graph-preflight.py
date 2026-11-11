#!/usr/bin/env python3
"""Gas City graph-engineering deterministic preflight.

Reads only the canonical host step/root/convoy and rig-scoped goal paths.
Never grants operator approval, model/session identity or accepted completion.
The check script runs in Gas City's [steps.check] controller (GC_BEAD_ID).
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


class PreflightError(ValueError):
    """Non-repairable authority or structural input mismatch."""


def metadata(bead: dict) -> dict[str, str]:
    data = bead.get("metadata")
    if not isinstance(data, dict):
        raise PreflightError("missing host bead metadata")
    return data


def require_id(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or any(ch.isspace() for ch in value):
        raise PreflightError(f"missing or invalid {field}")
    return value


def read_host_bead(bead_id: str) -> dict:
    """Call host's own gc bd show; never use bd directly or a second store."""
    try:
        done = subprocess.run(
            ["gc", "bd", "show", bead_id, "--json"],
            check=True,
            capture_output=True,
            text=True,
            timeout=25,
        )
        item = json.loads(done.stdout)
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        raise PreflightError(f"host bead lookup failed: {type(exc).__name__}") from exc
    if isinstance(item, list):
        if len(item) != 1:
            raise PreflightError("bead lookup must return exactly one object")
        item = item[0]
    if not isinstance(item, dict) or item.get("id") != bead_id:
        raise PreflightError("bead lookup identity mismatch")
    return item


def normalize_scope_path(root: Path, value: str, field: str, *, must_exist: bool) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise PreflightError(f"missing {field}")
    raw = Path(value)
    if raw.is_absolute() or any(part in {".", ".."} for part in raw.parts):
        raise PreflightError(f"{field} must be a relative rig-scoped path")
    path = root / raw
    # Reject symlink components rather than relying on post-validation checks.
    current = root
    for component in raw.parts:
        current = current / component
        if current.is_symlink():
            raise PreflightError(f"{field} traverses symlink")
    resolved = path.resolve(strict=False)
    if not resolved.is_relative_to(root):
        raise PreflightError(f"{field} escapes rig root")
    if must_exist and (not resolved.is_file() or resolved.stat().st_size == 0):
        raise PreflightError(f"{field} must be a nonempty file")
    if not must_exist and resolved.exists() and not resolved.is_dir():
        raise PreflightError(f"{field} must be a directory path")
    return resolved


def validate_preflight(
    *, step: dict, workflow_root: dict, input_convoy: dict, rig: Path
) -> dict:
    """Validate host identities and path hygiene, NOT operator approval."""
    root = rig.resolve(strict=True)
    if not root.is_dir():
        raise PreflightError("rig root is not a directory")
    sm = metadata(step)
    rm = metadata(workflow_root)
    root_id = require_id(sm.get("gc.root_bead_id"), "gc.root_bead_id")
    if workflow_root.get("id") != root_id:
        raise PreflightError("workflow root identity mismatch")
    convoy_id = require_id(rm.get("gc.input_convoy_id"), "gc.input_convoy_id")
    if convoy_id != require_id(sm.get("gc.graph.expected_convoy"), "expected convoy"):
        raise PreflightError("host-injected input convoy mismatch")
    if input_convoy.get("id") != convoy_id:
        raise PreflightError("input convoy identity mismatch")
    if input_convoy.get("type", input_convoy.get("issue_type")) != "convoy":
        raise PreflightError("host target is not a convoy")
    goal = normalize_scope_path(
        root, sm.get("gc.graph.goal_path", ""), "goal_path", must_exist=True
    )
    normalize_scope_path(
        root, sm.get("gc.graph.artifact_root", ""), "artifact_root", must_exist=False
    )
    context = sm.get("gc.graph.context_path", "")
    if context:
        normalize_scope_path(root, context, "context_path", must_exist=True)
    return {
        "status": "INPUT_SANITY_OK_NOT_AUTHORIZED",
        "workflow_root_id": root_id,
        "input_convoy_id": convoy_id,
        "goal_sha256": hashlib.sha256(goal.read_bytes()).hexdigest(),
        "approval_verdict": "NOT_ESTABLISHED",
        "host_claim_and_session_provenance": "NOT_VERIFIED",
    }


def main() -> int:
    try:
        step_id = require_id(os.environ.get("GC_BEAD_ID"), "GC_BEAD_ID")
        root_env = (
            os.environ.get("GC_RIG_ROOT")
            or os.environ.get("GC_BEADS_SCOPE_ROOT")
            or os.environ.get("GC_STORE_PATH")
        )
        if not root_env:
            raise PreflightError("no canonical rig root environment supplied by host")
        step = read_host_bead(step_id)
        root_id = require_id(metadata(step).get("gc.root_bead_id"), "gc.root_bead_id")
        workflow = read_host_bead(root_id)
        convoy_id = require_id(
            metadata(workflow).get("gc.input_convoy_id"), "gc.input_convoy_id"
        )
        convoy = read_host_bead(convoy_id)
        result = validate_preflight(
            step=step,
            workflow_root=workflow,
            input_convoy=convoy,
            rig=Path(root_env),
        )
    except (PreflightError, OSError) as exc:
        print(f"graph-preflight: BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

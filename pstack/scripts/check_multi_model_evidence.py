#!/usr/bin/env python3
"""Fail-closed native three-model PStack evidence gate."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

LANES = "abc"
WORKFLOWS = {"swarm", "arena", "interrogate"}


class EvidenceError(ValueError):
    pass


def required(data: dict, key: str) -> str:
    val = data.get(key)
    if not isinstance(val, str) or not val.strip():
        raise EvidenceError(f"{key}: expected nonempty string")
    return val


def validate_receipts(
    root: Path, artifact_dir: str, workflow: str, workflow_id: str, revision: str,
) -> list[dict]:
    if workflow not in WORKFLOWS or not workflow_id or not revision:
        raise EvidenceError("invalid workflow, root bead id, or revision")
    root = root.resolve()
    rel = Path(artifact_dir)
    if rel.is_absolute():
        raise EvidenceError("artifact_dir must be rig-relative")
    folder = (root / rel).resolve()
    if folder == root or root not in folder.parents:
        raise EvidenceError("artifact directory escapes rig root")
    models: set[str] = set()
    receipts = []
    for lane in LANES:
        file = folder / f"lane-{lane}.json"
        if file.is_symlink() or not file.is_file():
            raise EvidenceError(f"{file}: missing or symlink")
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            raise EvidenceError(f"{file}: invalid JSON: {exc}") from exc
        if not isinstance(data, dict):
            raise EvidenceError(f"{file}: expected JSON object")
        for key, value in (
            ("schema", "pstack.multi-lane.v1"), ("workflow", workflow),
            ("workflow_id", workflow_id), ("lane_id", lane),
            ("run_target", f"pstack.panel-{lane}"),
            ("source_revision", revision), ("status", "complete"),
        ):
            if data.get(key) != value:
                raise EvidenceError(f"{file}: {key} != {value!r}")
        required(data, "summary")
        required(data, "provider")
        model = required(data, "model")
        if model.lower() in {"auto", "default", "unknown"} or model in models:
            raise EvidenceError(f"{file}: unverified or duplicate model identity")
        models.add(model)
        evidence = data.get("evidence")
        if not isinstance(evidence, list) or not evidence or not all(
            isinstance(s, str) and s.strip() for s in evidence
        ):
            raise EvidenceError(f"{file}: missing evidence")
        findings = data.get("findings")
        if not isinstance(findings, list):
            raise EvidenceError(f"{file}: findings must be an array")
        for finding in findings:
            if not isinstance(finding, dict):
                raise EvidenceError(f"{file}: invalid finding")
            required(finding, "id")
            required(finding, "claim")
            refs = finding.get("evidence_refs")
            if not isinstance(refs, list) or not refs or not all(
                isinstance(s, str) and s.strip() for s in refs
            ):
                raise EvidenceError(f"{file}: finding missing evidence_refs")
        receipts.append(data)
    return receipts


def gate_args() -> tuple[Path, str, str, str, str]:
    bead_id = os.environ.get("GC_BEAD_ID")
    if not bead_id:
        raise EvidenceError("GC_BEAD_ID is required")
    proc = subprocess.run(
        ["gc", "bd", "show", bead_id, "--json"],
        capture_output=True, text=True, check=False, timeout=30,
    )
    if proc.returncode:
        raise EvidenceError(f"gc bd show failed: {proc.stderr[:200]}")
    info = json.loads(proc.stdout)
    if isinstance(info, list):
        if len(info) != 1:
            raise EvidenceError("expected one gate bead")
        info = info[0]
    if not isinstance(info, dict) or not isinstance(info.get("metadata"), dict):
        raise EvidenceError("missing gate metadata")
    meta = info["metadata"]
    root = next(
        (os.environ[k] for k in ("GC_RIG_ROOT", "GC_BEADS_SCOPE_ROOT", "GC_STORE_PATH")
         if os.environ.get(k)), None,
    )
    if not root:
        raise EvidenceError("cannot locate rig root")
    return (Path(root), required(meta, "pstack.multi.artifact_dir"),
            required(meta, "pstack.multi.workflow"),
            required(meta, "gc.root_bead_id"),
            required(meta, "pstack.multi.source_revision"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path)
    parser.add_argument("--artifact-dir")
    parser.add_argument("--workflow", choices=sorted(WORKFLOWS))
    parser.add_argument("--workflow-id")
    parser.add_argument("--source-revision")
    args = parser.parse_args()
    try:
        fields = (
            (args.root, args.artifact_dir, args.workflow, args.workflow_id, args.source_revision)
            if args.root is not None else gate_args()
        )
        if any(value is None for value in fields):
            raise EvidenceError("offline mode requires every explicit argument")
        validate_receipts(*fields)
    except (EvidenceError, OSError, subprocess.TimeoutExpired, ValueError) as exc:
        print(f"multi-model-evidence: BLOCKED: {exc}", file=sys.stderr)
        return 1
    print("multi-model-evidence: valid three-lane receipts; live session provenance separately required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

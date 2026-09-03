#!/usr/bin/env python3
"""Host-sling pstack-poteto-mode then pstack-build and write cook-plus-route receipts."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.gascity_pack_inference_gate import (  # noqa: E402
    GateError,
    GateWorkspace,
    build_gate_env,
    extract_json_payload,
    parse_duration,
    parse_host_sling_root,
    parse_host_sling_routed_to,
    resolve_binary,
    run_checked,
    start_city,
    stop_city,
)

POTETO_FORMULA = "pstack-poteto-mode"
BUILD_FORMULA = "pstack-build"
DEFAULT_RIG_NAME = "fixture"
SUBJECT_PATH = Path(".gc/pstack/sling-proof-subject.md")
ROUTE_ARTIFACT_PATH = Path(".gc/pstack/sling-proof-route.json")
BUILD_ARTIFACT_ROOT = Path(".gc/pstack/sling-proof-build")
BUILD_TITLE = "pstack host sling proof"
BUILD_WORK_ITEM = "Disposable pstack-build sling proof. Do not publish."
SUBJECT_TEXT = "Classify this disposable host sling proof. Do not auto-sling.\n"
ROUTE_POLL_SECONDS = 30.0
CANONICAL_CITY_NAME = "gastown"


@dataclass(frozen=True)
class CookRouteReceipt:
    formula: str
    root_id: str
    routed_to: str


@dataclass(frozen=True)
class HostSlingProof:
    city_disposable: bool
    city: str
    poteto: CookRouteReceipt
    build: CookRouteReceipt | None = None


def canonical_cities_root() -> Path:
    return (Path.home() / ".gc" / "cities").resolve()


def city_looks_canonical(city_dir: Path, city_name: str) -> bool:
    if city_name.strip().casefold() == CANONICAL_CITY_NAME:
        return True
    try:
        city_dir.resolve().relative_to(canonical_cities_root())
    except ValueError:
        return False
    return True


def load_city_name(city_dir: Path) -> str:
    site = city_dir / ".gc" / "site.toml"
    if site.is_file():
        payload = tomllib.loads(site.read_text(encoding="utf-8"))
        name = payload.get("workspace_name")
        if isinstance(name, str) and name.strip():
            return name.strip()
    return city_dir.name


def require_disposable_roles_city(city_dir: Path) -> str:
    city_toml = city_dir / "city.toml"
    if not city_toml.is_file():
        raise GateError(f"missing city.toml: {city_toml}")
    text = city_toml.read_text(encoding="utf-8")
    if "formula_v2" not in text:
        raise GateError("city.toml lacks formula_v2")
    if "gascity/roles" not in text.replace("\\", "/"):
        raise GateError("city.toml lacks gascity/roles")
    city_name = load_city_name(city_dir)
    if city_looks_canonical(city_dir, city_name):
        raise GateError(f"refusing canonical city {city_name} at {city_dir}")
    return city_name


def require_empty_workdir(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise GateError(f"--workdir must be empty or absent: {path}")


def load_workspace(root: Path, *, rig_name: str = DEFAULT_RIG_NAME) -> GateWorkspace:
    city_dir = root / "city"
    city_name = require_disposable_roles_city(city_dir)
    gc_home = root / "gc-home"
    return GateWorkspace(
        root=root,
        city_dir=city_dir,
        rig_dir=root / rig_name,
        gc_home=gc_home,
        runtime_dir=root / "runtime",
        claude_config_dir=gc_home / ".claude",
        city_name=city_name,
        rig_name=rig_name,
    )


def proof_payload(proof: HostSlingProof) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "city_disposable": True,
        "city": proof.city,
        "poteto": asdict(proof.poteto),
    }
    if proof.build is not None:
        payload["build"] = asdict(proof.build)
    return payload


def write_receipt(path: Path, proof: HostSlingProof) -> str:
    text = json.dumps(proof_payload(proof), indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text, end="")
    return text


def write_subject(workspace: GateWorkspace) -> Path:
    path = workspace.rig_dir / SUBJECT_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(SUBJECT_TEXT, encoding="utf-8")
    return path


def run_inference_gate_setup(gc_bin: str, workdir: Path) -> None:
    run_checked(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "gascity_pack_inference_gate.py"),
            "--pack",
            "pstack",
            "--setup-only",
            "--skip-inference-env-check",
            "--keep-workdir",
            "--gc-bin",
            gc_bin,
            "--workdir",
            str(workdir),
        ],
        timeout=parse_duration("20m"),
        log_output=True,
    )


def gc_city_prefix(gc_bin: str, workspace: GateWorkspace) -> list[str]:
    return [gc_bin, "--city", str(workspace.city_dir), "--rig", workspace.rig_name]


def bead_from_show_payload(payload: Any, root_id: str) -> Mapping[str, Any]:
    if isinstance(payload, dict) and payload.get("id") == root_id:
        return payload
    if isinstance(payload, list):
        matches = [item for item in payload if isinstance(item, dict) and item.get("id") == root_id]
        if len(matches) == 1:
            return matches[0]
    raise GateError(f"unexpected gc bd show --json payload for {root_id}: {payload!r}")


def wait_for_routed_to(
    gc_bin: str,
    workspace: GateWorkspace,
    root_id: str,
    *,
    env: Mapping[str, str],
    timeout: float = ROUTE_POLL_SECONDS,
) -> str:
    deadline = time.monotonic() + timeout
    last_error: Exception | None = None
    command = [*gc_city_prefix(gc_bin, workspace), "bd", "show", root_id, "--json"]
    while time.monotonic() < deadline:
        result = subprocess.run(
            command,
            cwd=str(workspace.rig_dir),
            env=dict(env),
            text=True,
            capture_output=True,
            timeout=parse_duration("30s"),
            check=False,
        )
        output = (result.stdout or "") + (result.stderr or "")
        try:
            if result.returncode != 0:
                raise GateError(output.strip() or f"gc bd show {root_id} exited {result.returncode}")
            payload = extract_json_payload(output)
            bead = bead_from_show_payload(payload, root_id)
            return parse_host_sling_routed_to(bead)
        except GateError as exc:
            last_error = exc
            time.sleep(1)
    raise GateError(f"gc.routed_to missing for {root_id}: {last_error}")


def sling_cook_route(
    gc_bin: str,
    workspace: GateWorkspace,
    *,
    env: Mapping[str, str],
    formula: str,
    command: Sequence[str],
    input_text: str | None = None,
) -> CookRouteReceipt:
    output = run_checked(
        command,
        cwd=workspace.rig_dir,
        env=env,
        timeout=parse_duration("5m"),
        log_output=True,
        input_text=input_text,
    )
    root_id = parse_host_sling_root(output)
    routed_to = wait_for_routed_to(gc_bin, workspace, root_id, env=env)
    return CookRouteReceipt(formula=formula, root_id=root_id, routed_to=routed_to)


def poteto_sling_command(gc_bin: str, workspace: GateWorkspace) -> list[str]:
    return [
        *gc_city_prefix(gc_bin, workspace),
        "sling",
        "gc.run-operator",
        POTETO_FORMULA,
        "--formula",
        "--var",
        f"subject_path={SUBJECT_PATH.as_posix()}",
        "--var",
        f"artifact_path={ROUTE_ARTIFACT_PATH.as_posix()}",
        "--nudge",
        "--json",
    ]


def build_sling_command(gc_bin: str, workspace: GateWorkspace) -> list[str]:
    return [
        *gc_city_prefix(gc_bin, workspace),
        "sling",
        "gc.run-operator",
        "--stdin",
        "--force",
        "--on",
        BUILD_FORMULA,
        "--title",
        BUILD_TITLE,
        "--var",
        f"artifact_root={BUILD_ARTIFACT_ROOT.as_posix()}",
        "--var",
        "interaction_mode=headless",
        "--var",
        "review_mode=report",
        "--var",
        "drain_policy=separate",
        "--var",
        "push=false",
        "--var",
        "open_pr=false",
        "--var",
        "max_iterations=1",
        "--nudge",
        "--json",
    ]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gc-bin", default=os.environ.get("GC_BIN", "gc"), help="gc binary to exercise")
    parser.add_argument("--workdir", type=Path, help="empty directory for the disposable city and rig")
    parser.add_argument(
        "--receipt-path",
        type=Path,
        help="HostSlingProof JSON path (default: <workdir>/host-sling-proof.json)",
    )
    parser.add_argument("--keep-workdir", action="store_true", help="keep the generated workdir after the run")
    return parser


def run_proof(args: argparse.Namespace) -> None:
    gc_bin = resolve_binary(args.gc_bin)
    if args.workdir is not None:
        work_root = args.workdir.resolve()
        require_empty_workdir(work_root)
        cleanup = False
    else:
        work_root = Path(tempfile.mkdtemp(prefix="pstack-host-sling-proof-"))
        cleanup = not args.keep_workdir
    receipt_path = (args.receipt_path or (work_root / "host-sling-proof.json")).resolve()
    if city_looks_canonical(work_root / "city", work_root.name):
        raise GateError(f"refusing canonical city workdir {work_root}")

    workspace: GateWorkspace | None = None
    env: dict[str, str] | None = None
    started = False
    try:
        run_inference_gate_setup(gc_bin, work_root)
        workspace = load_workspace(work_root)
        env = build_gate_env(gc_bin, workspace)
        write_subject(workspace)
        start_city(gc_bin, workspace, env=env)
        started = True
        poteto = sling_cook_route(
            gc_bin,
            workspace,
            env=env,
            formula=POTETO_FORMULA,
            command=poteto_sling_command(gc_bin, workspace),
        )
        try:
            build = sling_cook_route(
                gc_bin,
                workspace,
                env=env,
                formula=BUILD_FORMULA,
                command=build_sling_command(gc_bin, workspace),
                input_text=BUILD_WORK_ITEM,
            )
        except (GateError, subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as exc:
            write_receipt(
                receipt_path,
                HostSlingProof(
                    city_disposable=True,
                    city=str(workspace.city_dir),
                    poteto=poteto,
                ),
            )
            raise GateError(f"pstack-build sling failed after poteto routed: {exc}") from exc
        write_receipt(
            receipt_path,
            HostSlingProof(
                city_disposable=True,
                city=str(workspace.city_dir),
                poteto=poteto,
                build=build,
            ),
        )
    finally:
        if started and workspace is not None and env is not None:
            stop_city(gc_bin, workspace, env=env)
        if cleanup:
            shutil.rmtree(work_root, ignore_errors=True)


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        run_proof(args)
    except (GateError, subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

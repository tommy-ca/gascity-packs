#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
import tomllib
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

PIN_COMMIT = "29c84db50f4d0d97ee548b3570094643e53973bf"
PIN_HASH = "sha256:89aee457"
PACK_NAME = "tommy-ca/pstack"


class Cmd(NamedTuple):
    name: str
    argv: tuple[str, ...]


class FilePred(NamedTuple):
    name: str
    check: Callable[[Path], str | None]
    live: bool = False


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def schemas_argv(live: Path) -> tuple[str, ...]:
    script = str(live / "pstack/scripts/validate_pstack_schemas.py")
    if importlib.util.find_spec("yaml") is None:
        return ("uv", "run", "--with", "pyyaml", "python", script)
    return (sys.executable, script)


def check_pack_name(root: Path) -> str | None:
    path = root / "pstack/pack.toml"
    if not path.is_file():
        return "pack-name: missing pstack/pack.toml"
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    name = data.get("pack", {}).get("name")
    if name != PACK_NAME:
        return f"pack-name: [pack] name is {name!r}, expected {PACK_NAME!r}"
    return None


def check_pin(root: Path) -> str | None:
    path = root / "registry.toml"
    if not path.is_file():
        return "pin: missing registry.toml"
    text = path.read_text(encoding="utf-8")
    if PIN_COMMIT not in text:
        return f"pin: missing {PIN_COMMIT}"
    if PIN_HASH not in text:
        return f"pin: missing {PIN_HASH}"
    return None


def check_omit_panel(root: Path) -> str | None:
    formulas = root / "pstack/formulas"
    if not formulas.is_dir():
        return "omit-panel: missing pstack/formulas"
    for path in sorted(formulas.glob("*.formula.toml")):
        text = path.read_text(encoding="utf-8")
        if "gc.provider_panel" in text:
            return f"omit-panel: {path.name} contains gc.provider_panel"
        if "gc.child_artifact_path_template" in text:
            return f"omit-panel: {path.name} contains gc.child_artifact_path_template"
    gascity = root / "gascity"
    if not gascity.is_dir():
        return "omit-panel: missing gascity/"
    for path in gascity.rglob("*"):
        if not path.is_file() or path.suffix == ".pyc" or "__pycache__" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "provider_panel" in text:
            rel = path.relative_to(gascity)
            return f"omit-panel: gascity/{rel} contains provider_panel"
    return None


def check_openspec_archive(root: Path) -> str | None:
    changes = root / "openspec/changes"
    if not changes.is_dir():
        return "openspec-archive: missing openspec/changes"
    names = sorted(p.name for p in changes.iterdir())
    if names != ["archive"]:
        return f"openspec-archive: expected only archive, found {names}"
    if not (changes / "archive").is_dir():
        return "openspec-archive: archive is not a directory"
    return None


def steps(live: Path) -> tuple[Cmd | FilePred, ...]:
    return (
        Cmd(
            "dest-standing",
            (sys.executable, str(live / "scripts/check_pstack_dest_standing.py")),
        ),
        Cmd("schemas", schemas_argv(live)),
        Cmd(
            "mapping-gaps",
            (
                sys.executable,
                str(live / "pstack/scripts/apply_intent_change.py"),
                "--source",
                str(live / "openspec/changes/archive/2026-09-02-pstack-mapping-gaps"),
                "--validate-only",
            ),
        ),
        FilePred("pack-name", check_pack_name),
        FilePred("pin", check_pin),
        FilePred("openspec-archive", check_openspec_archive),
        FilePred("omit-panel", check_omit_panel, True),
    )


def run_cmd(name: str, argv: tuple[str, ...], cwd: Path) -> str | None:
    if name == "mapping-gaps" and shutil.which("openspec") is None:
        return "mapping-gaps: openspec CLI missing"
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    if proc.returncode != 0:
        err = proc.stderr.strip() or proc.stdout.strip() or f"exit {proc.returncode}"
        return f"{name}: {err}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="tree root for pack.toml, registry.toml, and openspec/changes. Formula greps stay on the live repo.",
    )
    args = parser.parse_args()
    live = default_root()
    files = args.root.resolve() if args.root is not None else live
    for step in steps(live):
        if isinstance(step, Cmd):
            miss = run_cmd(step.name, step.argv, live)
        else:
            miss = step.check(live if step.live else files)
        if miss is not None:
            print(miss, file=sys.stderr, flush=True)
            return 1
        print(f"ok {step.name}", flush=True)
    print("ok delivery evidence", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

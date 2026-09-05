#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SLICES: tuple[tuple[str, str, tuple[str, ...], tuple[str, ...]], ...] = (
    (
        "remaining-units",
        "### Requirement: Remaining program units stay host sling then compiler then panel stamp",
        (
            "scripts/pstack_host_sling_proof.py",
            "is proven as cook plus route",
            "fast-forward of `feat/pstack-pack-honesty`",
            "It is not a gastownhall land",
            "Fork default tracks isolation while gastownhall does not accept PRs",
            "spawn graph does not present unscoped submit as the next click",
            "even after those sling receipts",
            "Staff land is outside this checkout",
            "a `--require-git` failure on pin `29c84db` is not a restamp trigger",
            "scripts/check_pstack_dest_standing.py",
            "scripts/check_pstack_delivery_evidence.py",
            "`pr-pstack-panel-stamp` must not start on Gherkin alone",
            "Presence of `openspec/specs/gascity-provider-panel/spec.md` MUST NOT authorize a formula stamp",
            "This leftover MUST NOT stamp panel keys",
            "gc.provider_panel",
            "gc.child_artifact_path_template",
            "`gascity/` has no `provider_panel` hit",
            "Four identities stay distinct",
            "Arena candidates stay `pstack.architect`",
            "Interrogate review stays `pstack.reviewer`",
            "Persona expansion is not N-model",
            "Delivery evidence MUST fail closed if formulas grow those keys",
            "`--root` MUST NOT relocate formula greps",
        ),
        (
            "This change MUST NOT sling",
            "without those sling receipts",
            "MUST wait on the scoped-name unit even after those sling receipts",
            "Do not send a second publish request",
            "Hosted identity is `tommy-ca/pstack` even after those sling receipts",
            "is queued",
            "pending_review",
            "MUST wait on those receipts",
            "pstack.arena-runner",
        ),
    ),
    (
        "first-pub",
        "### Requirement: First registry publication waits on host dogfood",
        ("itself a publication go",),
        (
            "MUST wait on the scoped-name unit even after",
            "already submitted",
            "pending_review",
            "Do not send a second publish request",
            "MUST follow a host city that imports the checkout path and slings",
        ),
    ),
    (
        "receipt",
        "### Requirement: Host sling receipts of pstack-poteto-mode then pstack-build are cook plus route",
        (
            "pstack-poteto-mode",
            "pstack-build",
            "gc.routed_to",
            "sling JSON",
            "full drain of `pstack-build` is not required",
            "MUST NOT treat `pstack-review` then `pstack-build` as the remaining-units sling",
            "parse_host_sling_root",
            "extract_sling_root_id",
            "failed partial",
            "gc pack registry publish",
            "--dry-run",
            "the request is not submitted",
            "gc pack registry whoami",
            "dry-run is not registry acceptance",
        ),
        (
            "This change MUST NOT sling",
            "scoped-name unit",
            "is queued",
            "pending_review",
            "Do not send a second publish request",
            "stay blocked until the proof is complete",
        ),
    ),
)


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def resolve_spec(spec: Path | None) -> Path:
    relative = Path("openspec/specs/pstack-delivery-evidence/spec.md")
    if spec is None:
        return default_root() / relative
    if spec.is_absolute():
        return spec
    return (Path.cwd() / spec).resolve()


def requirement_slice(text: str, header: str) -> str | None:
    if header not in text:
        return None
    rest = text.split(header, 1)[1]
    if "### Requirement:" in rest:
        rest = rest.split("### Requirement:", 1)[0]
    return header + rest


def check(text: str) -> str | None:
    for name, header, must, must_not in SLICES:
        block = requirement_slice(text, header)
        if block is None:
            return f"slice {name}: missing {header}"
        for needle in must:
            if needle not in block:
                return f"slice {name}: missing {needle}"
        for needle in must_not:
            if needle in block:
                return f"slice {name}: forbidden {needle}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--spec",
        type=Path,
        default=None,
        help="dest spec path. Default: openspec/specs/pstack-delivery-evidence/spec.md",
    )
    args = parser.parse_args()
    spec = resolve_spec(args.spec)
    if not spec.is_file():
        print(f"slice remaining-units: missing {spec}", file=sys.stderr)
        return 1
    miss = check(spec.read_text(encoding="utf-8"))
    if miss is not None:
        print(miss, file=sys.stderr)
        return 1
    print("ok dest standing")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fail-closed declared model binding preflight, not a live session attestation."""
from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

ROLES = tuple(f"pstack.panel-{lane}" for lane in "abc")
BUILTINS = {"claude", "codex", "gemini", "cursor", "grok", "kimi"}


class PanelConfigError(ValueError):
    pass


def check_city(path: Path, rig: str) -> dict[str, tuple[str, str]]:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    matches = [r for r in data.get("rigs", []) if r.get("name") == rig]
    if len(matches) != 1:
        raise PanelConfigError(f"missing or duplicate rig {rig!r}")
    providers = data.get("providers", {})
    patches = matches[0].get("patches", [])
    results: dict[str, tuple[str, str]] = {}
    for role in ROLES:
        options = [p for p in patches if p.get("agent") == role]
        if len(options) != 1:
            raise PanelConfigError(f"{role}: needs exactly one explicit rig patch")
        cfg = options[0]
        provider = cfg.get("provider")
        if not isinstance(provider, str) or not provider.strip():
            raise PanelConfigError(f"{role}: missing provider")
        if provider not in BUILTINS and provider not in providers:
            raise PanelConfigError(f"{role}: unknown provider catalog entry")
        model = cfg.get("option_defaults", {}).get("model") or (
            providers.get(provider, {}).get("option_defaults", {}).get("model")
        )
        if not isinstance(model, str) or not model.strip() or model.lower() in {"auto", "default", "unknown"}:
            raise PanelConfigError(f"{role}: explicit model required")
        results[role] = (provider, model)
    if len({v[1].casefold() for v in results.values()}) != 3:
        raise PanelConfigError("all three roles must declare distinct models")
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=Path, required=True)
    parser.add_argument("--rig", required=True)
    args = parser.parse_args()
    try:
        bindings = check_city(args.city, args.rig)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"multi-model-city: BLOCKED: {exc}", file=sys.stderr)
        return 1
    for role, (provider, model) in bindings.items():
        print(f"{role}: {provider}/{model}")
    print("multi-model-city: configured-model preflight passed; confirm live sessions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

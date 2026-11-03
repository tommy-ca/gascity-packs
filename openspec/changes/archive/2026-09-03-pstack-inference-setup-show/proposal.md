## Why

`write_city` already compiles every discovered pstack formula with
`gc formula show`. That city has no `formula_v2` and no gascity roles.
Sibling methodology packs compile review and build through
`scripts/gascity_pack_inference_gate.py` `--setup-only`. This session ran
that gate for pack `pstack`. It printed `setup-only gate passed for pstack`
and showed `pstack-review` and `pstack-build`. Remaining-units still names
formula sling of `pstack-poteto-mode` and `pstack-build` as unproven.

## What Changes

- ADDED `PStack setup formulas compile in the inference-gate city`.
  Do not MODIFY remaining-units. Do not MODIFY the write_city live-city
  requirement.
- The inference-gate disposable city MUST compile `pstack-review` and
  `pstack-build` with `gc formula show` during `--setup-only`.
- That city MUST import gascity roles and set `[daemon] formula_v2 = true`.
- It MUST NOT treat setup-only formula show as formula sling.
- The gate MUST still pass when operator `~/.claude.json` is unwritable if
  `CLAUDE_CONFIG_DIR` state writes. Process HOME MUST stay the operator
  home. `GIT_CONFIG_GLOBAL` MUST point at the gate workspace.
- Pack tests lock the new requirement. REQUIREMENTS names the setup-only
  command. TRACEABILITY metadata may name the setup-only shows.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`. Adds inference-gate setup-only compile of
  `pstack-review` and `pstack-build`. Show is not sling.

## Impact

`pstack/tests/test_pstack_pack.py`, `pstack/REQUIREMENTS.md`,
`pstack/TRACEABILITY.md`, `docs/pstack-program-plan.md`, and
`openspec/specs/pstack-delivery-evidence/spec.md`. This change does not
edit `scripts/gascity_pack_inference_gate.py`. Formulas stay unstamped.
`registry.toml` is not restamped. This change does not sling, cook, or
publish.

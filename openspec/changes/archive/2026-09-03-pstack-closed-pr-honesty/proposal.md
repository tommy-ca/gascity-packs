## Why

Boot recipe and REQUIREMENTS still validate
`openspec/changes/archive/2026-09-02-pstack-program-arm-list`. That archive
exits 1 under OpenSpec 1.11.0. Live remaining-units Gherkin still treats
isolation as gastownhall PR 385. That PR is closed unmerged.

## What Changes

- MODIFIED remaining-units. Isolation is on `feat/pstack-pack-honesty`.
  gastownhall PR 385 is closed unmerged. Do not reopen it.
- Host sling stays the next operator unit after isolation is in this tree.
  It is still not a GitHub PR.
- Restamp of registry `0.1.0` still waits on sling receipts. Drop "on the
  same PR" as the restamp vehicle.
- Boot recipe and REQUIREMENTS validate mapping-gaps without `--change`.
- Pack tests lock the new program sentences and the boot-recipe source.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: Remaining units name the honesty branch, not
  closed PR 385, as the isolation vehicle.

## Impact

`docs/pstack-program-plan.md`, `pstack/REQUIREMENTS.md`,
`pstack/TRACEABILITY.md`, `docs/pstack-poteto-mode-router-plan.md`,
`pstack/tests/test_pstack_pack.py`, and
`openspec/specs/pstack-delivery-evidence/spec.md`. Formulas stay unstamped.
`registry.toml` is not restamped. This change does not publish.

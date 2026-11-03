## Why

Dest freeze is pytest substring asserts. A reviewer needs a rerunnable lever.
Staff land must not fight dest.

## What Changes

- MODIFIED remaining-units. Pack tests run `scripts/check_pstack_dest_standing.py`.
  That script is a must/must-not table over dest slices remaining-units,
  first-pub, and receipt. It exits 1 on fail. It does not scan Appendix C.
  It does not restamp pin `29c84db`.
- Add scenario Dest standing check fails closed.
- Pack tests subprocess the script. REQUIREMENTS and TRACEABILITY name it.
  Program boot recipe names it.
- This leftover does not re-submit publish. It does not restamp
  gastownhall `registry.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: dest standing lever.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`scripts/check_pstack_dest_standing.py`, `pstack/tests/test_pstack_pack.py`,
`pstack/REQUIREMENTS.md`, `pstack/TRACEABILITY.md`,
`docs/pstack-program-plan.md`.

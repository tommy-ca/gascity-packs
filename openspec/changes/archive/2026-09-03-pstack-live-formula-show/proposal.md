## Why

The maintained-pack live matrix already lists formulas and agents through a
scratch city when `GC_TEST_BIN` is set. It does not compile those formulas.
A disposable city with `gc formula show` already exits 0 for every discovered
pstack formula and for pr-pipeline. Cook and sling stay unproven.

## What Changes

- MODIFIED `PStack is exercised through a disposable live city`. Copy the
  full live requirement. Keep the list and doctor scenarios.
- The live matrix MUST compile each discovered formula with `gc formula show`.
  It MUST NOT treat formula show as formula sling.
- Add one scenario that `gc formula show` exits 0 for every formula
  discovered under the imported pack's `formulas/`.
- The live test hangs on the existing `MAINTAINED_PACKS` table. It is not a
  pstack-only one-off.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: Disposable live-city coverage includes
  `gc formula show` for every discovered formula. Show is not sling.

## Impact

`tests/test_maintained_packs_live_gc.py`, `pstack/tests/test_pstack_pack.py`,
`pstack/REQUIREMENTS.md`, `pstack/TRACEABILITY.md`, and
`openspec/specs/pstack-delivery-evidence/spec.md`. Formulas stay unstamped.
`registry.toml` is not restamped. This change does not sling, cook, or
publish.

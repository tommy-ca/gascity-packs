## Why

Cheap leftover checks are still one-off Python and pytest. A reviewer needs one CLI.
Host-only city and registry work stays host-only.

## What Changes

- MODIFIED remaining-units. Pack tests run `scripts/check_pstack_delivery_evidence.py`.
  That script subprocesses dest standing, schema inventory, and mapping-gaps
  validate-only. It checks `[pack] name` is `tommy-ca/pstack`. It reads pin
  `29c84db` / `sha256:89aee457` from `registry.toml` and does not restamp.
  It fails if `openspec/changes/` is not archive-only. It does not wrap sling,
  inference-gate, or publish. It does not scan Appendix C.
- Add scenario Delivery evidence runner fails closed.
- Dest remaining-units names that script. Pack tests subprocess it.
  REQUIREMENTS, TRACEABILITY, and the program boot recipe name it.
- This leftover does not re-submit publish. It does not restamp
  gastownhall `registry.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: delivery evidence runner.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`scripts/check_pstack_delivery_evidence.py`,
`scripts/check_pstack_dest_standing.py`, `pstack/tests/test_pstack_pack.py`,
`pstack/REQUIREMENTS.md`, `pstack/TRACEABILITY.md`,
`docs/pstack-program-plan.md`.

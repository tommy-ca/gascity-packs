## Why

TRACEABILITY and remaining-units close restamp after sling. README Quick
start already says even-after and names ghost-pin CI. Operator-docs
scenario `Pack README leads with a local clone` does not require those
ANDs. `test_readme_documents_required_gas_city_roles` does not freeze
them. README can drift back to the allowing sentence while TRACEABILITY
tests stay green.

## What Changes

- MODIFIED operator-docs README scenario. Require even-after restamp and
  ghost-pin non-trigger.
- Pack tests lock those README strings.
- This change does not restamp, publish, or merge gastownhall.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: README restamp sentence is locked.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`pstack/tests/test_pstack_pack.py`. Then FF tommy `main`.

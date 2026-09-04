## Why

Interrogate of `6c004a5`. README dest names `gc pack registry publish` of
pack path `pstack/`, then says unscoped submit waits on scoped-name.
`test_readme_documents_required_gas_city_roles` does not freeze that wait.
Dropping it would not fail tests. Operator-docs Gherkin does not require it.

## What Changes

- MODIFIED operator-docs README scenario. Require unscoped-wait and
  dry-run-is-not-acceptance.
- Pack tests lock those strings.
- This change does not restamp, publish, rename `pack.toml`, or merge
  gastownhall. Scoped-name rename is a later unit.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: README unscoped-wait is locked.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`pstack/tests/test_pstack_pack.py`. Then FF tommy `main`.

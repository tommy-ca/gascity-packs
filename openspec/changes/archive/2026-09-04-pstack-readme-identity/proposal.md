## Why

Scoped-name is archived. `[pack] name` is `tommy-ca/pstack`. Hosted
publish is `pending_review`. README still says unscoped submit waits on
the scoped-name unit. Tests freeze that leftover. The wait is done.

## What Changes

- MODIFIED operator-docs README scenario. Require hosted identity
  `tommy-ca/pstack` and forbidden unscoped submit. Drop wait-on-unit.
- README and tests match.
- This change does not re-submit publish. It does not restamp
  gastownhall `registry.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: README identity after scoped-name.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`, `pstack/README.md`,
`pstack/tests/test_pstack_pack.py`.

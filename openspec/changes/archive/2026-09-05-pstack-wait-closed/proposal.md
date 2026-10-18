## Why

Scoped-name is archived. `[pack] name` is `tommy-ca/pstack`. Submit
`prq_5WDBAqIkcpy-j7ossap3TLJ5` is queued. Remaining-units, first-pub,
receipt, identity, and program still say wait on the scoped-name unit.
Tests freeze those leftovers. The wait is done.

## What Changes

- MODIFIED remaining-units. Hosted identity is `tommy-ca/pstack`. Drop
  wait-on-unit. Drop MAY-set-name. Do not send a second publish request.
- MODIFIED first-pub. First publication of `tommy-ca/pstack` is already
  submitted. Sling is not a publication go.
- MODIFIED receipt. Unscoped submit is forbidden. Drop Submit was not
  sent. Drop MUST NOT rename `pack.toml`.
- MODIFIED identity. Drop after-that-rename. Name MUST stay
  `tommy-ca/pstack`.
- Program leftover wait matches dest. Tests invert wait locks.
- This change does not re-submit publish. It does not restamp
  gastownhall `registry.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: leftover scoped-name wait closed.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/tests/test_pstack_pack.py`.

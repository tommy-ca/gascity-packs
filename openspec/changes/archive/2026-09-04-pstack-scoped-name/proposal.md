## Why

Unscoped `pstack` from `@tommy-ca` is a reserved first-party name. Dry-run
of that name is not acceptance. `--name` cannot rename at publish time.
Remaining-units already named a later scoped-name unit and forbade the
honesty tick from renaming `pack.toml`. That later unit is this change.

## What Changes

- ADDED hosted identity `tommy-ca/pstack`. Directory and formula stems
  stay `pstack`. Vendor `upstream.toml` stays Cursor `pstack`.
- MODIFIED remaining-units. This unit MAY rename `[pack] name`. Unscoped
  hosted submit stays forbidden.
- After operator go, archive, set `pstack/pack.toml` name, update tests
  and README, dry-run again, then hosted submit.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: hosted identity is `tommy-ca/pstack`.

## Impact

`pstack/pack.toml`, `pstack/tests/test_pstack_pack.py`,
`pstack/README.md`, `openspec/specs/pstack-delivery-evidence/spec.md`.
Does not restamp gastownhall `registry.toml`. Does not merge gastownhall.
Does not edit vendor.

## Why

Repeated ship requests plus whoami and dry-run do not authorize hosted
submit of unscoped `pstack` from `tommy-ca`. Community names are
`<github-owner>/<pack>`. Unscoped names are reserved. `gc` 1.4.1 dry-run
prints the request and exits 0. It does not prove the registry will
accept the name. `--name tommy-ca/pstack` cannot rename at publish time.
Remaining-units already forbids renaming `pstack/pack.toml` this tick.

Sibling packs shipped by landing on gastownhall `main` and stamping
`registry.toml`. That path is still lost. Catalog restamp is still not
the dest.

## What Changes

- MODIFIED host sling receipt requirement. Unscoped hosted submit from
  tommy waits on the scoped-name unit. Dry-run stays proven. Request is
  not submitted.
- Appendix A records the registry name contract.
- This change does not submit, restamp hashes, stamp panel keys, rename
  `pack.toml`, or merge gastownhall.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: unscoped tommy submit is deferred.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/REQUIREMENTS.md`,
`pstack/tests/test_pstack_pack.py`.

## Why

Interrogate after the tommy `main` fast-forward. Spawn graph still says
`pr-pstack-publish` via `gc pack registry publish pstack` after sling
receipts. Receipt Gherkin already defers unscoped submit. Clone of fork
`main` makes that spawn line the obvious next click. That is a lie.

Ghost pin `29c84db` is on the fork default. Fork CI `--require-git` can
fail. That failure is not a restamp trigger.

## What Changes

- MODIFIED remaining-units. Spawn graph MUST say unscoped hosted submit
  waits on the scoped-name unit. Ghost-pin CI failure MUST NOT authorize
  a catalog restamp.
- Program spawn line updated. Tests lock both.
- This change does not publish, restamp, rename `pack.toml`, or merge
  gastownhall. After archive, isolation HEAD fast-forwards tommy `main`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: spawn graph matches unscoped deferral.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/tests/test_pstack_pack.py`.
Remote tommy `main` fast-forwards isolation HEAD. `origin/main` is not
updated.

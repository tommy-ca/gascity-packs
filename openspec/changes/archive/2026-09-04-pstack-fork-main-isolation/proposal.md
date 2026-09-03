## Why

gastownhall PR 385 is closed unmerged. There are no open tommy-ca PRs.
The operator asked to merge `feat/pstack-pack-honesty` onto the fork
default branch while upstream does not accept PRs. `tommy/main` is
behind `origin/main` and is an ancestor of isolation HEAD. A
fast-forward is possible. That is fork dogfood. It is not a gastownhall
land.

## What Changes

- MODIFIED remaining-units. Remote tommy `main` MUST be a fast-forward of
  `feat/pstack-pack-honesty` while gastownhall does not accept PRs. The
  program MUST NOT merge to gastownhall. MUST NOT reopen 385.
- Program spawn names tommy `main` as the fork default.
- This change does not publish, restamp hashes, stamp panel keys, or
  rename `pack.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: fork `main` tracks isolation.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/tests/test_pstack_pack.py`.
Remote `tommy` refs/heads/main fast-forwards to isolation HEAD.
`origin/main` is not updated.

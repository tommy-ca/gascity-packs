## Context

User asked to merge the feature branch to forked main if upstream does
not accept PRs. Observed. PR 385 closed. Open tommy-ca PRs none.
`tommy/main` at `db4bd05` is an ancestor of `91b184f`. Fast-forward.
No merge commit.

Ghost pin `29c84db` remains frozen. A fresh clone of tommy `main` may
fail `validate_registry.py --require-git` for that pin. Do not restamp.

## Goals / Non-Goals

**Goals:**

- Fast-forward tommy `main` to isolation HEAD.
- Keep gastownhall `origin/main` untouched.

**Non-Goals:**

- gastownhall merge.
- Hosted unscoped submit.
- `pack.toml` rename.
- Catalog restamp.

## Decisions

Fast-forward, not a merge commit. Isolation branch name stays
`feat/pstack-pack-honesty`. Fork default is an extra pointer.

## Risks / Trade-offs

Fork `main` will contain pstack and the stranded catalog pin. Consumers
who clone tommy-ca default branch get the tree. They still cannot import
from gastownhall `main`.

## Migration Plan

Validate, archive, update program, pack tests, fast-forward push tommy
`main`. Do not push origin.

## Open Questions

None for this tick.

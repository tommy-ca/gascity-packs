## Context

Sibling packs bmad, superpowers, gstack, and compound-engineering ship by
landing on gastownhall `main` and stamping `registry.toml`. pstack cannot.
Isolation stays on tommy. Host sling is proven. Dry-run hosted publish
exited 0. `gc pack registry whoami` failed. No login.

## Goals / Non-Goals

**Goals:**

- Record dry-run as proven.
- Stop saying publish is blocked on incomplete sling proof.
- Keep submit off this tick.

**Non-Goals:**

- `gc pack registry login`.
- Submit of a publish request.
- `registry.toml` restamp.
- gastownhall merge.
- Panel stamp.

## Decisions

Do not rename `pstack/pack.toml`. Dry-run used unscoped `pstack`. Scoped
name stays a later unit.

Do not restamp `29c84db`. That pin is still a stranded catalog row.

## Risks / Trade-offs

Dry-run HEAD was `441f1a08`. Later commits on the same branch change the
commit field of a future submit. The dry-run shape is what we lock.

## Migration Plan

Validate, archive, check program publish lanes that have evidence, lock
tests, do not submit.

## Open Questions

Whether the operator logs in and submits from this branch or waits for a
gastownhall land that remaining-units still forbids.

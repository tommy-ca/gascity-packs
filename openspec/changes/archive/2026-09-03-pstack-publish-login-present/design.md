## Context

Verifier at `630efd7` saw `gc pack registry whoami` succeed as `@tommy-ca`.
An earlier session whoami failed. Login is no longer the submit block.
Remaining-units still forbids this honesty tick from submitting. The
review-gate still waits for the operator click.

## Goals / Non-Goals

**Goals:**

- Stop saying whoami failed.
- Keep submit off this tick.

**Non-Goals:**

- Live `gc pack registry publish` without the review-gate click.
- `registry.toml` restamp.
- gastownhall merge.

## Decisions

Do not submit. Credentials exist. Remaining-units and the review-gate
still say stop.

## Risks / Trade-offs

whoami can fail again if Gasworks credentials expire. The next submit
tick should re-run whoami.

## Migration Plan

Validate, archive, update docs, lock tests, do not submit.

## Open Questions

Whether submit should use unscoped `pstack` or `--name tommy-ca/pstack`.

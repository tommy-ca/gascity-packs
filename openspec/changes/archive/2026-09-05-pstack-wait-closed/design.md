## Context

Independent verify of `9093fd1` noted leftover wait copy required by
tests. Scoped-name is archived. Submit is queued. Drop the wait. Keep
forbidden unscoped submit. Invert wait presence locks to negatives.

Do not send a second publish request.

## Goals / Non-Goals

**Goals:**

- Dest and program match archived scoped-name plus queued submit.

**Non-Goals:**

- Second `gc pack registry publish`.
- Catalog restamp.
- gastownhall merge.
- Presence-lock of `pending_review`.

## Decisions

Staff land is out of this checkout. Invert wait locks. Do not freeze
`pending_review`. Replacement dest is do-not-re-submit plus
unscoped-forbidden.

## Risks / Trade-offs

A MUST NOT wait sentence would still match wait presence tests. Drop
the wait sentence instead.

## Migration Plan

Validate, archive, dest, program, tests. Do not re-submit. Do not
fast-forward tommy `main`.

## Open Questions

None.

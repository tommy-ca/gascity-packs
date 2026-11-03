## Context

Independent verify of `6e089ef` noted leftover wait copy required by
tests. The unit is done. Drop the wait. Keep forbidden-submit.

Do not submit a second publish request.

## Goals / Non-Goals

**Goals:**

- README matches archived scoped-name.

**Non-Goals:**

- Second `gc pack registry publish`.
- Catalog restamp.
- gastownhall merge.

## Decisions

Staff land is out of this checkout. Record pending_review only.

## Risks / Trade-offs

None.

## Migration Plan

Validate, archive, README, tests, push feat, FF tommy `main`.

## Open Questions

None.

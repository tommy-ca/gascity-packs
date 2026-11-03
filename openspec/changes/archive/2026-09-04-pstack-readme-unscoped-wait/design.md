## Context

Last leftover after first-publication scoped-name. README text already
waits. Tests do not. Encode that.

## Goals / Non-Goals

**Goals:**

- README unscoped-wait cannot drop without a failing test.

**Non-Goals:**

- Rename `pack.toml`.
- Unscoped submit.
- Restamp.
- gastownhall merge.

## Decisions

Do not start the scoped-name unit this tick. Remaining-units still
MUST NOT rename `pack.toml` on the honesty change.

## Risks / Trade-offs

None.

## Migration Plan

Validate, archive, tests, push feat, FF tommy `main`.

## Open Questions

None.

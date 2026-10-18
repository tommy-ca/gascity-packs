## Context

Independent leftover after wait-closed. Dest and pytest still encode
queued, already submitted, and Do not send a second publish request.
That freeze fights staff land. Dest is standing policy. Appendix C is
the event log. Tests invert second-publish locks. Do not freeze
`pending_review`.

## Goals / Non-Goals

**Goals:**

- Dest remaining-units, first-pub, and receipt are standing policy.

**Non-Goals:**

- Second `gc pack registry publish`.
- Catalog restamp.
- gastownhall merge.
- Presence-lock of `pending_review`.
- A publication state machine.

## Decisions

Staff land of `prq_5WDBAqIkcpy-j7ossap3TLJ5` stays in spawn L44 and
Appendix C. Dest does not name queued, already submitted, or second
publish. Dummy identity even-after is dropped. Restamp even-after stays.

## Risks / Trade-offs

A MUST NOT second-publish sentence still matches the old presence lock.
Drop the sentence. Invert the freeze.

## Migration Plan

Validate, archive, dest, program, tests. Do not re-submit. Do not
fast-forward tommy `main`.

## Open Questions

None.

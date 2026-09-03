## Context

Live proof on 2026-09-03. Workdir `/tmp/pstack-host-sling-proof-415185`.
Poteto `fi-06k`. Build `fi-awr`. Both routed to `fixture/gc.run-operator`.
Full drain was not waited. OpenSpec 1.11.0 forbids dropping a scenario
title, so remaining-units keeps `Host sling is the next operator unit`
and changes its THEN body.

## Goals / Non-Goals

**Goals:**

- Replace unproven sentences with proven cook-plus-route plus the proof
  script.
- Keep publish, restamp, and panel stamp off this tick.

**Non-Goals:**

- gastownhall merge.
- `registry.toml` restamp.
- Panel stamp.
- Waiting for `pstack-build` to close.

## Decisions

Record bead ids in Appendix A as session evidence. The rerunnable lever is
the script. Do not commit the `/tmp` JSON.

Keep `no separate graph-cook script` as pack-local. The host proof script
is not pack-local verification.

## Risks / Trade-offs

Bead ids die with the disposable city. Operators rerun the script.

## Migration Plan

Validate, archive, update TRACEABILITY, REQUIREMENTS, program, tests.

## Open Questions

None for this honesty tick.

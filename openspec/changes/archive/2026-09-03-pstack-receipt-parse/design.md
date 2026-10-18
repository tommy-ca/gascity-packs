## Context

Interrogate of `a905201` (one reviewer, grok-4.6) found the receipt
requirement both commands a sling and forbids one. Remaining-units already
says this change MUST NOT sling. Durable receipt Gherkin should not.

`extract_sling_root_id` falls back to JSON `id`. Formula show can pass.

## Goals / Non-Goals

**Goals:**

- Receipt requirement is the receipt shape.
- Parser rejects show and setup-only.
- Poteto-only is a failed partial.
- Restore the failed `pstack-build` cook in Appendix A.

**Non-Goals:**

- Live sling.
- Remaining-units rewrite.
- Archive task-checkbox restamp.

## Decisions

Lead judgment. Act on findings 1, 2, 4, 5, 6. Drop freeze from ADDED.
Name `parse_host_sling_root`. Keep TRACEABILITY `no separate graph-cook
script` as pack-local. Host receipts stay unproven.

Dismiss finding 7. Archives are immutable.

## Risks / Trade-offs

Parser tests use fixtures. They do not prove a live `gc sling`.

## Migration Plan

Validate, archive, add parser tests, lock spec, restore Appendix A.

## Open Questions

When the proof script runs, who records both `gc.routed_to` values in
Appendix A.

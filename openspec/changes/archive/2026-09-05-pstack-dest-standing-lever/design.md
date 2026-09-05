## Context

Standing dest closed event-state in dest Gherkin. Freeze still lives as
pytest substring asserts. A reviewer cannot rerun that freeze without the
pack test.

## Goals / Non-Goals

**Goals:**

- Dest standing is a freeze table plus a CLI a reviewer reruns.

**Non-Goals:**

- YAML framework.
- Publication state machine.
- Scan of Appendix C.
- Catalog restamp.
- Presence-lock of event-state on dest remaining-units.

## Decisions

Encode dest standing as a frozen tuple of slice records. Each record is a
name, a requirement header, must-contain strings, and must-not strings.
`scripts/check_pstack_dest_standing.py` reads dest, slices on
`### Requirement:`, and exits 1 on the first miss. Dest remaining-units
names that script. Dest Gherkin does not quote forbidden freeze strings.
Those strings live in the table and in the fail-closed pack test.

## Risks / Trade-offs

A dest scenario that quotes a forbidden freeze string fails remaining-units
must-not. Keep those tokens out of dest remaining-units.

## Migration Plan

Validate, dest, script, tests, REQUIREMENTS, TRACEABILITY, program boot,
archive. Do not re-submit. Do not restamp.

## Open Questions

None.

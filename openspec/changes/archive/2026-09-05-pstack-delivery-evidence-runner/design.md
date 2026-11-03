## Context

Dest standing is a reviewer CLI. Cheap leftover checks still sit as one-off
Python, pytest, and host commands. Pack name, pin bytes, archive-only, schema
inventory, and mapping-gaps validate-only are not one lever.

## Goals / Non-Goals

**Goals:**

- Delivery evidence is a freeze table of named steps plus a CLI a reviewer reruns.

**Non-Goals:**

- YAML framework.
- Pytest as the lever.
- Publication state machine.
- Wrap of sling, inference-gate, or publish.
- Scan of Appendix C.
- Catalog restamp.

## Decisions

Encode delivery evidence as a frozen tuple of named steps. A step is a
subprocess argv of an existing lever, or a read-only file predicate.
`scripts/check_pstack_delivery_evidence.py` walks that table, prints
`ok <name>` per pass, and exits 1 on the first miss.

`--root` relocates pack.toml, registry.toml, and `openspec/changes/` only.
Dest standing, schemas, and mapping-gaps run against the live repo from the
script parent. Dest standing is invoked without `--spec`.

The pin check reads `29c84db50f4d0d97ee548b3570094643e53973bf` and
`sha256:89aee457`. It does not write `registry.toml`.

## Risks / Trade-offs

The runner fails while a live OpenSpec change dir exists. Archive before
claiming delivery evidence is green. File `--root` is for fail-closed tests.
It does not relocate dest standing.

## Migration Plan

Validate, dest, script, dest-standing must-contain, tests, REQUIREMENTS,
TRACEABILITY, program boot, archive. Do not re-submit. Do not restamp.

## Open Questions

None.

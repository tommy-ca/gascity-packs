## Context

HEAD is `f0027d9` on `feat/pstack-pack-honesty`. Isolation ancestor is
`2f65f7b`. gastownhall PR 385 is closed unmerged.

The maintained-pack live matrix in `tests/test_maintained_packs_live_gc.py`
imports each pack in `MAINTAINED_PACKS` into a scratch city from `write_city`.
`test_pack_formulas_resolve_through_a_city` lists formulas. It does not
compile them. `gc formula show` is a compile check. It is not `gc formula
cook` and it is not formula sling.

This session prototyped `gc formula show` for all 40 pstack formulas in
5.84s. pr-pipeline's 6 formulas also showed. Remaining-units still names
host sling of `pstack-poteto-mode` then `pstack-build` as unproven.

This repository has no `adr/` tree. No in-force ADR constrains the matrix.

## Goals / Non-Goals

**Goals:**

- Live Gherkin requires `gc formula show` for every discovered formula.
- The live test uses the existing `MAINTAINED_PACKS` table, skip, and wiring.
- Pack tests lock that delivery-evidence names `gc formula show` and does
  not treat show as sling.
- REQUIREMENTS Evidence Commands name formula show next to list and agent.
- Sling stays unproven.

**Non-Goals:**

- No host sling in this change.
- No `gc formula cook`.
- No registry restamp.
- No `gc.provider_panel` stamp.
- No reopen of gastownhall PR 385.
- No publish to registry.gascity.com.
- No MODIFY of remaining-units.
- No edit of `pstack/formulas` or `pstack/schemas`.
- No pstack-only live fixture.

## Decisions

- Data shape is the set of names from `discover_formulas(pack_dir)`. For
  each name, `gc formula show <name>` in a disposable city must exit 0.
- Organizing structure is the existing parametrized `MAINTAINED_PACKS`
  table. Same skip and wiring as `test_pack_formulas_resolve_through_a_city`.
- MODIFIED live-city requirement only. Copy the full live block. Add one
  scenario. Do not MODIFY remaining-units. Do not MODIFY TRACEABILITY
  Gherkin.
- Call `run_gc` from `gc_live_city`. Fail with pack name, formula name, and
  output. Do not use `gc_output` as the only check. Show can print a body
  on success, and a failed show must name the formula.
- TRACEABILITY metadata evidence class may name formula show. Keep the
  locked import and sling sentences.

## Risks / Trade-offs

- [Risk] A reader treats a green formula show as proof of sling.
  Mitigation. The requirement says it MUST NOT treat formula show as
  formula sling. Pack tests lock that sentence. Remaining-units still
  names sling unproven.
- [Risk] A pack with many formulas makes the matrix slow.
  Mitigation. The pstack prototype was 5.84s for 40 formulas. Skip packs
  that ship no formulas, same as list.

## Migration Plan

1. Author this change under
   `openspec/changes/2026-09-03-pstack-live-formula-show/`.
2. Validate-only, then archive into this repository `openspec/`.
3. Add the live test and pack locks. Update REQUIREMENTS.
4. Run focused pack tests and the live matrix with `GC_TEST_BIN` set.

## Open Questions

- None.

## Context

HEAD is `de2883e` on `feat/pstack-pack-honesty`. Isolation ancestor is
`2f65f7b`. gastownhall PR 385 closed unmerged on 2026-09-03. julianknutsen
asked to publish at https://registry.gascity.com/publish. `pstack/` is not
on origin/main.

Boot recipe and REQUIREMENTS still run validate-only against
`openspec/changes/archive/2026-09-02-pstack-program-arm-list`. That archive
MODIFIED `PStack traceability references durable truth` without later live
scenarios. OpenSpec 1.11.0 exits 1. Pack tests already validate
mapping-gaps, which passes.

Live remaining-units still say isolation is on PR 385. Host sling and
panel omit-stamp stay true. TRACEABILITY already splits live-city import
from formula sling.

This repository has no `adr/` tree. No in-force ADR constrains the vehicle.

## Goals / Non-Goals

**Goals:**

- Remaining-units names the honesty branch as the isolation vehicle.
- gastownhall PR 385 is closed unmerged in the program and Gherkin.
- Boot recipe validate-only exits 0.
- Pack tests fail if the land vehicle returns to "on 385" or "same PR".

**Non-Goals:**

- No rebuild of `apply_intent_change.py`.
- No move of compiler Gherkin out of this repo.
- No unfreeze of `graph_operator`.
- No host sling in this change.
- No registry restamp.
- No `gc.provider_panel` stamp.
- No reopen of gastownhall PR 385.
- No publish to registry.gascity.com.
- No MODIFY of TRACEABILITY Gherkin unless every live scenario is copied.
- No rewrite of the 97-box plan skeleton.

## Decisions

- MODIFIED remaining-units only. Copy the full live requirement. Add the
  closed-PR scenario and the boot-recipe scenario on that same requirement.
  Do not MODIFY the TRACEABILITY requirement.
- Isolation vehicle is branch `feat/pstack-pack-honesty`. Keep program ids
  `pr-pstack-land-honesty` then `pr-pstack-panel-stamp`.
- Keep isolation Build box checked at `2f65f7b`. That SHA is the isolation
  commit, not HEAD. Do not chase tip SHA into the plan body.
- Lock boot recipe by parsing the `--source` path from the program plan and
  REQUIREMENTS, then running validate-only on that path. Keep the
  `change_name` unit test on dated `2026-09-02-pstack-program-arm-list`.
- TRACEABILITY Delivery boundary gets one sentence that isolation is on
  this branch and PR 385 is closed. Keep the two locked sling sentences.

## Risks / Trade-offs

- [Risk] A reader treats the checked Build box at `2f65f7b` as proof that
  gastownhall main has isolation.
  -> Mitigation. Intro, spawn graph, and Appendix A say PR 385 is closed
  unmerged. Tests lock the new spawn sentences.
- [Risk] Boot recipe Gherkin and TRACEABILITY Gherkin both grow.
  -> Mitigation. Boot recipe lives on remaining-units. TRACEABILITY stays.

## Migration Plan

1. Author this change under `openspec/changes/pstack-closed-pr-honesty/`.
2. Edit the program, REQUIREMENTS, TRACEABILITY, pointer plan, and tests.
3. Validate-only, then archive into this repository `openspec/`.
4. Run `pstack/tests/test_pstack_pack.py`.

## Open Questions

- None.

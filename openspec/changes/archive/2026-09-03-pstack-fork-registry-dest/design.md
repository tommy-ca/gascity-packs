## Context

HEAD is `59ada6f` on `feat/pstack-pack-honesty`. Isolation ancestor is
`2f65f7b`. gastownhall PR 385 closed unmerged on 2026-09-03. julianknutsen
asked to drop gastownhall `registry.toml` PRs and to publish at
registry.gascity.com. Remote `tommy` is
`https://github.com/tommy-ca/gascity-packs.git`. `pstack/` is not on
origin/main. This repository `registry.toml` cannot carry a tommy-ca source.
`validate_registry.py` `CANONICAL_REPO` stays gastownhall.

Host sling is VERIFIED-UNPROVEN. Disposable import can list formulas. No
cook or route receipts. `GC_TEST_BIN` unset. Host `gc` is 1.4.1.
Registry restamp is VERIFIED-UNPROVEN. Pin still `29c84db` /
`sha256:89aee457`. Panel stamp is VERIFIED-UNPROVEN. Formulas omit
`gc.provider_panel`. There is no `/home/tommyk/projects/gascity` tree.

This repository has no `adr/` tree. No in-force ADR constrains the dest.

## Goals / Non-Goals

**Goals:**

- Remaining-units names the tommy fork and hosted registry as dest.
- Host sling stays the next operator unit and stays unproven.
- `pr-pstack-publish` sits between sling and panel stamp.
- Pack tests fail if restamp is still the publication vehicle.
- Boot recipe validate-only still exits 0 against mapping-gaps.

**Non-Goals:**

- No rebuild of `apply_intent_change.py`.
- No change of `validate_registry.py` `CANONICAL_REPO`.
- No restamp of `registry.toml` commit or hash.
- No host sling in this change.
- No `gc pack registry publish` in this change.
- No `gc.provider_panel` stamp.
- No rename of `pstack/pack.toml`.
- No reopen of gastownhall PR 385.
- No merge to gastownhall.
- No MODIFY of TRACEABILITY Gherkin.
- No rewrite of the check-plan skeleton into a new shape.
- No switch of live lanes to `grok-4.6-fast-xhigh`.

## Decisions

- MODIFIED remaining-units only. Copy the full live requirement. Add the
  publish scenario on that same requirement. Do not MODIFY the TRACEABILITY
  requirement.
- Isolation vehicle stays branch `feat/pstack-pack-honesty`. Keep program
  ids `pr-pstack-land-honesty` then `pr-pstack-publish` then
  `pr-pstack-panel-stamp`.
- Publication vehicle is `gc pack registry publish pstack` to
  registry.gascity.com after sling receipts. Catalog restamp is not that
  vehicle.
- Keep isolation Build box checked at `2f65f7b`. That SHA is the isolation
  commit, not HEAD.
- TRACEABILITY Delivery boundary gets one dest sentence. Keep the two
  locked live-versus-sling sentences. Keep "not a slung production release".
- Lock the new spawn sentences in `test_delivery_checks_cover_pstack`.
  Drop the old restamp-as-publication assert.

## Risks / Trade-offs

- [Risk] A reader treats the gastownhall catalog pin as hosted publish.
  -> Mitigation. Plan, remaining-units, and tests say restamp of gastownhall
  `registry.toml` is not the publication vehicle.
- [Risk] A later scoped name is confused with this honesty change.
  -> Mitigation. Spec and plan say this change must not rename
  `pstack/pack.toml`.

## Migration Plan

1. Author this change under `openspec/changes/pstack-fork-registry-dest/`.
2. Edit the program, TRACEABILITY, and tests.
3. Validate-only, then archive into this repository `openspec/`.
4. Run `pstack/tests/test_pstack_pack.py`.

## Open Questions

- None.

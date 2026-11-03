## Context

HEAD is `8e0ec24` on `feat/pstack-pack-honesty`. Isolation ancestor is
`2f65f7b`. gastownhall PR 385 is closed unmerged.

`write_city` in `tests/test_maintained_packs_live_gc.py` still shows all 40
pstack formulas. That city has no `[daemon] formula_v2 = true` and no
gascity roles import. `pstack-build` cannot cook there.

`scripts/gascity_pack_inference_gate.py` already has a `PackSpec` row for
pstack. `setup_formulas` is the tuple `("pstack-review", "pstack-build")`.
`initialize_city` runs `gc formula show` on that tuple. This session ran
`--pack pstack --setup-only --skip-inference-env-check` with gc 1.4.1.
It printed `setup-only gate passed for pstack`. Workdir was
`/tmp/pstack-inference-setup-gitpin-366837`.

The parent already changed `seed_claude_project_state` so an unwritable
operator home path is skipped when `CLAUDE_CONFIG_DIR` writes. The parent
already pointed `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` at
`workspace.gc_home/gitconfig`. This change does not edit that script.

This repository has no `adr/` tree. No in-force ADR constrains the gate.

## Goals / Non-Goals

**Goals:**

- ADDED delivery-evidence for inference-gate setup-only compile of
  `pstack-review` and `pstack-build`.
- Keep the write_city live-city requirement unchanged.
- Keep remaining-units unchanged. Sling stays unproven.
- Pack tests lock the new requirement. REQUIREMENTS names the setup-only
  command. TRACEABILITY metadata may name the two setup formulas.

**Non-Goals:**

- No edit of `scripts/gascity_pack_inference_gate.py`.
- No host sling in this change.
- No `gc formula cook`.
- No registry restamp.
- No `gc.provider_panel` stamp.
- No reopen of gastownhall PR 385.
- No publish to registry.gascity.com.
- No MODIFY of remaining-units.
- No MODIFY of the write_city live-city requirement.
- No edit of `pstack/formulas` or `pstack/schemas`.

## Decisions

- Data shape is `PackSpec.setup_formulas` for pstack. The tuple is
  `("pstack-review", "pstack-build")`. Each name must compile with
  `gc formula show` during `--setup-only`.
- Organizing structure is the existing `PackSpec` table in
  `gascity_pack_inference_gate.py`. Do not add a second pstack table.
- ADDED requirement only. Do not copy or rewrite remaining-units. Do not
  copy or rewrite the write_city live-city block.
- Process HOME stays the operator home so the supervisor can start.
  Workspace `city.toml` may still set `[workspace.env]` HOME to `gc_home`.
  Those are different HOME values.
- TRACEABILITY metadata evidence class may name inference-gate setup-only
  show of `pstack-review` and `pstack-build`. Keep the locked import and
  sling sentences.

## Risks / Trade-offs

- [Risk] A reader treats a green setup-only show as proof of sling.
  Mitigation. The requirement says it MUST NOT treat setup-only formula
  show as formula sling. Pack tests lock that sentence. Remaining-units
  still names sling unproven.
- [Risk] A reader treats setup-only as a replacement for write_city show
  of all 40 formulas. Mitigation. The write_city live-city requirement
  stays. This is a second city shape.

## Migration Plan

1. Author this change under
   `openspec/changes/2026-09-03-pstack-inference-setup-show/`.
2. Validate-only, then archive into this repository `openspec/`.
3. Add pack locks. Update REQUIREMENTS, TRACEABILITY, and Appendix A.
4. Run focused pack tests and inference-gate unit tests. Do not restamp.

## Open Questions

- None.

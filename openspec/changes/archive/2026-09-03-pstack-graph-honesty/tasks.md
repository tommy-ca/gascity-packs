## 1. OpenSpec TRACEABILITY delta

- [ ] 1.1 Validate `openspec/changes/2026-09-03-pstack-graph-honesty` with `python pstack/scripts/apply_intent_change.py --source openspec/changes/2026-09-03-pstack-graph-honesty --validate-only`
- [ ] 1.2 Archive into `openspec/specs/` with `--archive` only after operator go

## 2. Pack docs and tests

- [ ] 2.1 Edit `pstack/TRACEABILITY.md` so the live-program graph names `pr-pstack-land-honesty` then `pr-pstack-publish` then `pr-pstack-panel-stamp`
- [ ] 2.2 Edit `pstack/README.md` Quick start restamp sentence so it names both sling formulas and says gastownhall restamp is not the publication vehicle
- [ ] 2.3 Edit `docs/pstack-program-plan.md` Appendix A so catalog restamp is not a remaining dest
- [ ] 2.4 Edit `pstack/tests/test_pstack_pack.py` so `test_delivery_checks_cover_pstack` fails if the TRACEABILITY requirement omits the three-id sequence
- [ ] 2.5 Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`

## 3. Freeze

- [ ] 3.1 Confirm `rg gc.provider_panel pstack/formulas` is empty
- [ ] 3.2 Confirm `registry.toml` pstack pin stays `29c84db` / `sha256:89aee457`
- [ ] 3.3 Push `feat/pstack-pack-honesty` to remote `tommy`. Do not reopen gastownhall PR 385

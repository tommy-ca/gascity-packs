## MODIFIED Requirements

### Requirement: Remaining program units stay host sling then compiler then panel stamp

Feature: pstack-delivery-evidence

Rule: Isolation on feat/pstack-pack-honesty does not authorize restamp, hosted publish, or panel stamp

The live program MUST name isolation on branch `feat/pstack-pack-honesty`.
gastownhall PR 385 is closed unmerged. It is not the land vehicle. The program
MUST NOT reopen it as the merge path. The program MUST NOT merge isolation to
gastownhall. The operator MUST maintain the tommy-ca fork as remote `tommy`.
While gastownhall does not accept PRs, remote tommy default branch `main`
MUST be a fast-forward of `feat/pstack-pack-honesty`. That is fork dogfood.
It is not a gastownhall land. Host sling of `pstack-poteto-mode` then
`pstack-build` is proven as cook plus route by
`scripts/pstack_host_sling_proof.py`. That unit MUST NOT be a GitHub PR.
Canonical-city sling is forbidden. The program MUST NOT restamp
`registry.toml` `commit` or `hash` even after those sling receipts.
A clone of tommy `main` that fails `validate_registry.py --require-git` on
unreachable pin `29c84db` MUST NOT be treated as a restamp trigger.
Hosted identity is `tommy-ca/pstack`.
Unscoped hosted submit is forbidden.
Staff land is outside this checkout. Sling receipts are
not a publication go. Hosted publication to registry.gascity.com is the
publication vehicle. Restamp of gastownhall `registry.toml` is not
the publication vehicle. `make registry-publish` is not hosted publish.
The program MUST name `pr-pstack-publish` after sling. Publish is
`gc pack registry publish` of pack path `pstack/` to registry.gascity.com.
`[pack] name` is `tommy-ca/pstack`.
Directory and formula stems stay `pstack`. Vendor `upstream.toml` MUST NOT name `tommy-ca/pstack`.
Hosted submit of unscoped `pstack` is forbidden. The live program spawn
graph MUST NOT present unscoped `gc pack registry publish pstack` as the next
click after sling receipts. The program MUST keep
ids `pr-pstack-land-honesty` and `pr-pstack-panel-stamp`.
It MUST insert `pr-pstack-publish` between sling and panel stamp.
`pstack/TRACEABILITY.md` MUST name both formulas on the restamp gate.
The program MUST say `pr-pstack-panel-stamp` must not start on Gherkin alone.
Pack tests MUST fail if any
`pstack/formulas/*.formula.toml` contains `gc.provider_panel` or
`gc.child_artifact_path_template`. Pack tests MUST fail if `gascity/` contains
`provider_panel`. Presence of `openspec/specs/gascity-provider-panel/spec.md`
MUST NOT authorize a formula stamp. The boot recipe and REQUIREMENTS MUST
validate `openspec/changes/archive/2026-09-02-pstack-mapping-gaps` without
`--change`. This leftover MUST NOT publish. This leftover MUST NOT restamp hashes.
This leftover MUST NOT stamp panel keys.
Pack tests MUST run `scripts/check_pstack_dest_standing.py`.
That script MUST encode dest standing as a must/must-not table over dest
slices remaining-units, first-pub, and receipt. It MUST exit 1 on fail.
It MUST NOT scan Appendix C. It MUST NOT restamp pin `29c84db`.
Pack tests MUST run `scripts/check_pstack_delivery_evidence.py`.
That script MUST subprocess dest standing, schema inventory, and mapping-gaps
validate-only. It MUST check `[pack] name` is `tommy-ca/pstack`.
It MUST read pin `29c84db` / `sha256:89aee457` from `registry.toml` and MUST NOT restamp.
It MUST fail if `openspec/changes/` is not archive-only.
It MUST NOT wrap sling, inference-gate, or publish.
It MUST NOT scan Appendix C.

#### Scenario: Host sling is the next operator unit

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator follows the spawn graph after isolation is on `feat/pstack-pack-honesty`
- **THEN** host sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route
- **AND** that unit is not a GitHub PR
- **AND** the proof command is `scripts/pstack_host_sling_proof.py`
- **AND** hosted identity is `tommy-ca/pstack`
- **AND** unscoped hosted submit is forbidden
- **AND** restamp of gastownhall `registry.toml` is not the publication vehicle

#### Scenario: TRACEABILITY names both sling formulas on the restamp gate

- **GIVEN** `pstack/TRACEABILITY.md`
- **WHEN** a reader follows the delivery boundary
- **THEN** it forbids restamping `commit` or `hash` even after host sling
- **AND** that sentence names `pstack-poteto-mode` and `pstack-build`
- **AND** a `--require-git` failure on pin `29c84db` is not a restamp trigger

#### Scenario: Panel stamp does not start on Gherkin alone

- **GIVEN** `docs/pstack-program-plan.md` and `openspec/specs/gascity-provider-panel/spec.md`
- **WHEN** an operator considers `pr-pstack-panel-stamp`
- **THEN** the program says the compiler is outside this packs tree
- **AND** it says `pr-pstack-panel-stamp` must not start on Gherkin alone
- **AND** pack formulas still omit `gc.provider_panel`

#### Scenario: Tests fail closed on a premature panel stamp

- **GIVEN** `pstack/tests/test_pstack_pack.py`
- **WHEN** the focused pack tests run
- **THEN** every `pstack/formulas/*.formula.toml` omits `gc.provider_panel`
- **AND** every such file omits `gc.child_artifact_path_template`
- **AND** `gascity/` has no `provider_panel` hit

#### Scenario: gastownhall PR 385 is closed unmerged

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator names the isolation land vehicle
- **THEN** the program names isolation on `feat/pstack-pack-honesty`
- **AND** it says gastownhall PR 385 is closed unmerged
- **AND** it says do not reopen that PR
- **AND** it says maintain remote tommy
- **AND** it says do not merge to gastownhall
- **AND** operator publication dest is registry.gascity.com
- **AND** this change does not publish

#### Scenario: Boot recipe validates mapping-gaps without --change

- **GIVEN** `docs/pstack-program-plan.md` and `pstack/REQUIREMENTS.md`
- **WHEN** an operator runs the boot recipe validate-only command
- **THEN** `--source` is `openspec/changes/archive/2026-09-02-pstack-mapping-gaps`
- **AND** `--change` is omitted
- **AND** OpenSpec strict validate exits 0

#### Scenario: Program names pr-pstack-publish after sling

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator follows the spawn graph after host sling receipts
- **THEN** the program names `pr-pstack-publish`
- **AND** publish is `gc pack registry publish` of pack path `pstack/`
- **AND** the dest is registry.gascity.com
- **AND** `[pack] name` is `tommy-ca/pstack`
- **AND** unscoped hosted submit is forbidden
- **AND** spawn graph does not present unscoped submit as the next click

#### Scenario: Fork default tracks isolation while gastownhall does not accept PRs

- **GIVEN** gastownhall PR 385 is closed unmerged and no open tommy-ca PRs
- **WHEN** the operator updates remote tommy default branch `main`
- **THEN** tommy `main` is a fast-forward of `feat/pstack-pack-honesty`
- **AND** that update is not a gastownhall merge
- **AND** 385 is not reopened
- **AND** a `--require-git` failure on pin `29c84db` is not a restamp trigger

#### Scenario: Dest standing check fails closed

- **GIVEN** dest remaining-units, first-pub, and receipt
- **WHEN** `python scripts/check_pstack_dest_standing.py` runs
- **THEN** it exits 0 on standing dest
- **AND** it exits 1 on a dest-slice miss or forbidden string
- **AND** pack tests subprocess that script
- **AND** Appendix C MAY still record event-state

#### Scenario: Delivery evidence runner fails closed

- **GIVEN** dest remaining-units and the cheap evidence levers
- **WHEN** `python scripts/check_pstack_delivery_evidence.py` runs
- **THEN** it exits 0 on standing dest
- **AND** it exits 1 on a wrong pack name, a restamped pin, or a live OpenSpec change dir
- **AND** pack tests subprocess that script
- **AND** it does not wrap sling, inference-gate, or publish

## MODIFIED Requirements

### Requirement: Remaining program units stay host sling then compiler then panel stamp

Feature: pstack-delivery-evidence

Rule: Isolation on feat/pstack-pack-honesty does not authorize restamp, hosted publish, or panel stamp

The live program MUST name isolation on branch `feat/pstack-pack-honesty`.
gastownhall PR 385 is closed unmerged. It is not the land vehicle. The program
MUST NOT reopen it as the merge path. The program MUST NOT merge isolation to
gastownhall. The operator MUST maintain the tommy-ca fork as remote `tommy`.
The live program MUST name host sling of
`pstack-poteto-mode` then `pstack-build` as the next operator unit after
isolation is in this tree. That unit MUST NOT be a GitHub PR. Host sling of
those formulas remains unproven. The program MUST NOT restamp
`registry.toml` `commit` or `hash` without those sling receipts.
Hosted publication to registry.gascity.com MUST wait on those receipts.
It is the publication vehicle. Restamp of gastownhall `registry.toml` is not
the publication vehicle. `make registry-publish` is not hosted publish.
The program MUST name `pr-pstack-publish` after sling. Publish is
`gc pack registry publish` of pack path `pstack/` to registry.gascity.com.
A scoped name is a later unit. This change MUST NOT rename `pstack/pack.toml`.
The program MUST keep ids `pr-pstack-land-honesty` and `pr-pstack-panel-stamp`.
It MUST insert `pr-pstack-publish` between sling and panel stamp.
`pstack/TRACEABILITY.md` MUST name both formulas on the restamp gate.
The program MUST say `pr-pstack-panel-stamp` must not start on Gherkin alone.
Pack tests MUST fail if any
`pstack/formulas/*.formula.toml` contains `gc.provider_panel` or
`gc.child_artifact_path_template`. Pack tests MUST fail if `gascity/` contains
`provider_panel`. Presence of `openspec/specs/gascity-provider-panel/spec.md`
MUST NOT authorize a formula stamp. The boot recipe and REQUIREMENTS MUST
validate `openspec/changes/archive/2026-09-02-pstack-mapping-gaps` without
`--change`. This change MUST NOT publish. This change MUST NOT sling.
This change MUST NOT restamp hashes. This change MUST NOT stamp panel keys.

#### Scenario: Host sling is the next operator unit

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator follows the spawn graph after isolation is on `feat/pstack-pack-honesty`
- **THEN** the next unit names host sling of `pstack-poteto-mode` and `pstack-build`
- **AND** that unit is not a GitHub PR
- **AND** host sling of those formulas remains unproven
- **AND** hosted publish waits on sling receipts of `pstack-poteto-mode` and `pstack-build`
- **AND** restamp of gastownhall `registry.toml` is not the publication vehicle

#### Scenario: TRACEABILITY names both sling formulas on the restamp gate

- **GIVEN** `pstack/TRACEABILITY.md`
- **WHEN** a reader follows the delivery boundary
- **THEN** it forbids restamping `commit` or `hash` without a host sling
- **AND** that sentence names `pstack-poteto-mode` and `pstack-build`

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
- **AND** this change does not rename `pstack/pack.toml`
- **AND** `pr-pstack-publish` sits between sling and `pr-pstack-panel-stamp`

# pstack-delivery-evidence Specification

## Purpose

Define CI and disposable live-city coverage for the PStack pack.

## Requirements

### Requirement: PStack delivery checks run in CI

The pack repository CI MUST run the PStack pack test suite and `gc lint pstack` alongside the existing pack checks. These checks MUST inspect the checkout being tested and MUST fail the job when PStack's pack contracts regress.

#### Scenario: PStack pack tests are part of the Python CI command

- **GIVEN** the repository CI workflow runs its Python test step
- **WHEN** the workflow checks out the repository
- **THEN** it invokes `pstack/tests/test_pstack_pack.py` with the shared pytest command
- **AND** a failing PStack test fails the CI job

#### Scenario: PStack is part of the Gas City lint loop

- **GIVEN** the repository CI workflow runs its pack lint step
- **WHEN** the workflow iterates over maintained lint targets
- **THEN** it invokes `gc lint pstack`
- **AND** a PStack lint error fails the CI job

### Requirement: PStack is exercised through a disposable live city

The maintained-pack live test matrix MUST import PStack into a scratch city with the real Gas City CLI. It MUST derive PStack's formulas and agents from its checkout, verify that each resolves through the imported city, and assert the observed doctor delta against an explicit expected set. The live test MUST retain the canary control that proves doctor findings are being surfaced. Every PStack formula MUST declare `formula_compiler >= 2.0.0` and MUST NOT retain deprecated `contract = "graph.v2"`; the expected PStack-specific doctor delta MUST be empty. The live matrix MUST compile each discovered formula with `gc formula show`. It MUST NOT treat formula show as formula sling.

#### Scenario: PStack formulas and agents resolve through Gas City

- **GIVEN** a real executable Gas City CLI is provided to the live test fixture
- **WHEN** a scratch city imports only the PStack pack under test
- **THEN** every formula discovered under `pstack/formulas/` is listed by `gc formula list`
- **AND** every agent discovered under `pstack/agents/` is listed by `gc agent list`
- **AND** no provider, publication, or canonical city state is mutated

#### Scenario: PStack doctor delta is explicit

- **GIVEN** the scratch city and equivalent baseline city are inspected by `gc doctor`
- **WHEN** the PStack delta is computed
- **THEN** the expected PStack-specific delta is empty
- **AND** the live suite records no additional PStack-specific finding
- **AND** the canary control continues to observe its intentional `formula-requirements` finding

#### Scenario: PStack formulas compile through formula show

- **GIVEN** a real executable Gas City CLI is provided to the live test fixture
- **WHEN** a scratch city imports the pack under test
- **THEN** `gc formula show` exits 0 for every formula discovered under that pack's `formulas/`
- **AND** no provider, publication, or canonical city state is mutated

### Requirement: PStack traceability references durable truth

`pstack/TRACEABILITY.md` MUST point to the durable canonical specification `openspec/specs/pstack-gascity-pack/spec.md` and MUST NOT point to a removed change directory as the current contract. Its evidence classes MUST continue to distinguish static, metadata, runtime, and unavailable claims. It MUST name `docs/pstack-program-plan.md` as the live program. That plan's Arm `git show origin/main:` list MUST name files that exist in this repository's origin/main. Focused pack tests MUST require the live Durable Gherkin AND that TRACEABILITY does not name another project as the Gherkin owner. A former-checkout token grep MUST NOT substitute for that AND. It MUST say disposable live-city import is exercised when `GC_TEST_BIN` is set. It MUST say formula sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route by `scripts/pstack_host_sling_proof.py`. Pack tests MUST lock both sentences. They MUST fail if TRACEABILITY still says that sling remains unproven. The live-program scenario MUST name `pr-pstack-land-honesty` then `pr-pstack-publish` then `pr-pstack-panel-stamp`. Pack tests MUST lock that three-id sequence in the TRACEABILITY requirement.

#### Scenario: Traceability path is stable

- **GIVEN** a fresh checkout of the pack repository
- **WHEN** a reader follows the durable PStack specification reference in `pstack/TRACEABILITY.md`
- **THEN** the reference identifies `openspec/specs/pstack-gascity-pack/spec.md`
- **AND** it does not present a historical change directory as the current contract

#### Scenario: Live program is the recursive graph

- **GIVEN** `pstack/TRACEABILITY.md` and `docs/pstack-program-plan.md`
- **WHEN** an operator follows the live program
- **THEN** TRACEABILITY names `docs/pstack-program-plan.md`
- **AND** that plan names `pr-pstack-land-honesty` then `pr-pstack-publish` then `pr-pstack-panel-stamp`

#### Scenario: Arm list is re-runnable on trunk

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator runs each `git show origin/main:` box in Arm the program
- **THEN** every path exists in this repository's origin/main
- **AND** those boxes do not require plugin `skills/` on origin/main

#### Scenario: Tests fail closed on a foreign Gherkin owner

- **GIVEN** `pstack/tests/test_pstack_pack.py` and `openspec/specs/pstack-gascity-pack/spec.md`
- **WHEN** the focused pack tests run
- **THEN** they require TRACEABILITY to name `openspec/specs/pstack-gascity-pack/spec.md`
- **AND** they require the live spec AND `it does not name another project as the Gherkin owner`
- **AND** they fail if TRACEABILITY uses `gherkin owner`

#### Scenario: TRACEABILITY splits live-city import from formula sling

- **GIVEN** `pstack/TRACEABILITY.md` and `pstack/tests/test_pstack_pack.py`
- **WHEN** a reader follows the OpenSpec payload note
- **AND** the focused pack tests run
- **THEN** TRACEABILITY says disposable live-city import is exercised when `GC_TEST_BIN` is set
- **AND** TRACEABILITY says formula sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route by `scripts/pstack_host_sling_proof.py`
- **AND** TRACEABILITY does not say that sling remains unproven
- **AND** TRACEABILITY does not say `Live city sling remains unproven`

#### Scenario: Tests lock the three program ids in TRACEABILITY Gherkin

- **GIVEN** `openspec/specs/pstack-delivery-evidence/spec.md` and `pstack/tests/test_pstack_pack.py`
- **WHEN** the focused pack tests run
- **THEN** the TRACEABILITY recursive-graph scenario names `pr-pstack-land-honesty` then `pr-pstack-publish` then `pr-pstack-panel-stamp`
- **AND** the tests fail if that three-id sequence is missing from the TRACEABILITY requirement

### Requirement: Formula requirement metadata is checked in delivery

Feature: pstack-delivery-evidence

Rule: Compiler requirements fail in the focused suite

The PStack pack test suite MUST check that every discovered PStack formula
contains the supported formula compiler requirement
`formula_compiler >= 2.0.0` and MUST NOT retain deprecated
`contract = "graph.v2"` before the live matrix is used as delivery evidence.

#### Scenario: Missing formula requirement fails the focused check

- **GIVEN** a PStack formula omits `requires.formula_compiler`
- **WHEN** the pack conformance test runs
- **THEN** it fails before accepting the delivery contract

#### Scenario: Deprecated graph contract fails the focused check

- **GIVEN** a PStack formula retains `contract = "graph.v2"`
- **WHEN** the pack conformance test runs
- **THEN** it fails before accepting the delivery contract

### Requirement: First registry publication waits on host dogfood

Feature: pstack-delivery-evidence

Rule: Catalog pin on gastownhall main is not the first live city

The pack MUST NOT treat an unmerged registry `0.1.0` pin as a gastownhall
`main` import. First publication MUST wait on the scoped-name unit even after
a host city that imports the checkout path and slings `pstack-poteto-mode`
plus `pstack-build`. Host sling of those formulas is proven and is not by
itself a publication go. Formula catalog strings MUST NOT claim Gas City
expands `gc.graph_operator`. Catalog strings MUST describe the current
sequential graphs. They MUST NOT claim this checkout cooks `gc.provider_panel`.

#### Scenario: Catalog strings do not claim executed fanout

- **GIVEN** `pstack-swarm`, `pstack-arena`, and `pstack-interrogate` catalog descriptions
- **WHEN** an operator lists formulas
- **THEN** the text says sequential frames
- **AND** the text does not claim Gas City expands `gc.graph_operator`
- **AND** the text does not claim this checkout expands `gc.provider_panel`

### Requirement: Operator docs do not advertise a slung main import

Feature: pstack-delivery-evidence

Rule: README and TRACEABILITY match the unslung catalog pin

`pstack/README.md` MUST document a local clone import as the working command.
The GitHub `gc import add` URL MAY remain as the intended form. It MUST say
that URL works only when the imported git ref contains `pstack/`. It MUST say
registry `0.1.0` is a catalog pin, not a slung production release. It MUST say
method formulas in this checkout are sequential annotated steps and MUST NOT
claim this checkout executes multi-provider fanout. It MAY describe a
`[[provider_panels]]` cook as a target that is not executed until a compiler
consumes `gc.provider_panel`. Root
`README.md` MUST say pstack is not a slung production import.
`pstack/TRACEABILITY.md` MUST forbid restamping `commit` or `hash` even after
host sling of `pstack-poteto-mode` and `pstack-build`. It MUST say a
`--require-git` failure on pin `29c84db` is not a restamp trigger.
`pstack/README.md` MUST forbid restamping even after that host sling. It MUST
say a `--require-git` failure on pin `29c84db` is not a restamp trigger.
`pstack/README.md` MUST say unscoped hosted submit from tommy waits on the scoped-name unit. It MUST say dry-run is not registry acceptance.

#### Scenario: Pack README leads with a local clone

- **GIVEN** `pstack/README.md`
- **WHEN** an operator follows Quick start step 1
- **THEN** the working import is `[imports.pstack] source = "../gascity-packs/pstack"`
- **AND** the GitHub `gc import add` URL is present
- **AND** the text says the URL works only when the imported git ref contains `pstack/`
- **AND** the text says registry `0.1.0` is not a slung production release
- **AND** the text says method formulas are not multi-provider fanout
- **AND** the text forbids restamping even after host sling of `pstack-poteto-mode` and `pstack-build`
- **AND** the text says a `--require-git` failure on pin `29c84db` is not a restamp trigger
- **AND** the text does not say without a host sling of `pstack-poteto-mode` and `pstack-build`
- **AND** the text says unscoped hosted submit from tommy waits on the scoped-name unit
- **AND** the text says dry-run is not registry acceptance

#### Scenario: README may name the unarchived panel target

- **GIVEN** `pstack/README.md` How N-model fanout will work
- **WHEN** an operator reads the target
- **THEN** the text names `[[provider_panels]]` as city configuration
- **AND** the text says the pack stamps `gc.provider_panel` only after the compiler consumes that key
- **AND** the text still says this checkout runs sequential graphs

#### Scenario: TRACEABILITY forbids restamp without a host sling

- **GIVEN** `pstack/TRACEABILITY.md`
- **WHEN** a reader follows the delivery boundary
- **THEN** it names registry `0.1.0` as the first catalog pin
- **AND** it says that pin is not a slung production release
- **AND** it forbids restamping `commit` or `hash` even after host sling of `pstack-poteto-mode` and `pstack-build`
- **AND** a `--require-git` failure on pin `29c84db` is not a restamp trigger

### Requirement: Playbook map excludes method skill stems

Feature: pstack-delivery-evidence

Rule: how, why, swarm, arena, and interrogate are sling names, not playbook stems

`pstack/mappings/playbooks.toml` MUST map Cursor playbook stems only. It MUST
NOT contain keys `how`, `why`, `swarm`, `arena`, or `interrogate`. It MUST NOT
contain a `[methods]` table until a later packing change adds one on purpose.
It MUST list corpus-only Cursor skills under `[corpus].skills`. Those skills
MUST NOT have sling formulas.

#### Scenario: Method skills stay off the playbook map

- **GIVEN** `pstack/mappings/playbooks.toml`
- **WHEN** the focused pack tests run
- **THEN** `how`, `why`, `swarm`, `arena`, and `interrogate` are absent from `[playbooks]`
- **AND** those stems are absent from `[unsupported].stems`
- **AND** the file has no `[methods]` table

#### Scenario: Corpus-only skills are named

- **GIVEN** `pstack/mappings/playbooks.toml` and `pstack/vendor/pstack/skills/`
- **WHEN** the focused pack tests run
- **THEN** `[corpus].skills` names every vendor skill directory that is not a principle, not `poteto-mode`, and not backed by a `pstack-<name>` formula
- **AND** none of those corpus skills have a sling formula

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
Hosted publication to registry.gascity.com MUST wait on the scoped-name unit even after those sling receipts.
It is the publication vehicle. Restamp of gastownhall `registry.toml` is not
the publication vehicle. `make registry-publish` is not hosted publish.
The program MUST name `pr-pstack-publish` after sling. Publish is
`gc pack registry publish` of pack path `pstack/` to registry.gascity.com.
A scoped name is a later unit. This change MUST NOT rename `pstack/pack.toml`.
Unscoped hosted submit from tommy waits on that unit. The live program spawn
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
`--change`. This change MUST NOT publish. This change MUST NOT restamp hashes.
This change MUST NOT stamp panel keys.

#### Scenario: Host sling is the next operator unit

- **GIVEN** `docs/pstack-program-plan.md`
- **WHEN** an operator follows the spawn graph after isolation is on `feat/pstack-pack-honesty`
- **THEN** host sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route
- **AND** that unit is not a GitHub PR
- **AND** the proof command is `scripts/pstack_host_sling_proof.py`
- **AND** hosted publish waits on the scoped-name unit even after sling receipts of `pstack-poteto-mode` and `pstack-build`
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
- **AND** this change does not rename `pstack/pack.toml`
- **AND** unscoped hosted submit waits on the scoped-name unit
- **AND** spawn graph does not present unscoped submit as the next click

#### Scenario: Fork default tracks isolation while gastownhall does not accept PRs

- **GIVEN** gastownhall PR 385 is closed unmerged and no open tommy-ca PRs
- **WHEN** the operator updates remote tommy default branch `main`
- **THEN** tommy `main` is a fast-forward of `feat/pstack-pack-honesty`
- **AND** that update is not a gastownhall merge
- **AND** 385 is not reopened
- **AND** a `--require-git` failure on pin `29c84db` is not a restamp trigger

### Requirement: PStack setup formulas compile in the inference-gate city

Feature: pstack-delivery-evidence

Rule: Inference-gate setup-only is compile, not sling

The inference-gate disposable city MUST compile `pstack-review` and `pstack-build` with `gc formula show` during `--setup-only`. That city MUST import gascity roles and set `[daemon] formula_v2 = true`. It MUST NOT treat setup-only formula show as formula sling. The gate MUST still pass when operator `~/.claude.json` is unwritable if `CLAUDE_CONFIG_DIR` state writes. Process HOME MUST stay the operator home so the supervisor can start. `GIT_CONFIG_GLOBAL` MUST point at the gate workspace, not `~/.gitconfig`.

#### Scenario: Setup-only shows pstack-review and pstack-build

- **GIVEN** `scripts/gascity_pack_inference_gate.py` and PackSpec `pstack`
- **WHEN** an operator runs `--pack pstack --setup-only`
- **THEN** `gc formula show` compiles `pstack-review`
- **AND** `gc formula show` compiles `pstack-build`
- **AND** the command prints that setup-only gate passed for pstack

#### Scenario: Inference-gate city uses roles and formula_v2

- **GIVEN** the pstack inference-gate disposable city
- **WHEN** `initialize_city` writes `city.toml`
- **THEN** a rig import source is `gascity/roles`
- **AND** `[daemon] formula_v2 = true`

#### Scenario: Setup-only show is not formula sling

- **GIVEN** `openspec/specs/pstack-delivery-evidence/spec.md`
- **WHEN** a reader follows this requirement
- **THEN** it MUST NOT treat setup-only formula show as formula sling

#### Scenario: Unwritable operator Claude json does not fail the gate

- **GIVEN** operator `~/.claude.json` is unwritable
- **WHEN** `seed_claude_project_state` writes `CLAUDE_CONFIG_DIR` state
- **THEN** the gate still passes

#### Scenario: Process HOME stays the operator home

- **GIVEN** `build_gate_env`
- **WHEN** the gate starts the supervisor
- **THEN** process HOME is the operator home

#### Scenario: Git config is workspace-local

- **GIVEN** `build_gate_env`
- **WHEN** the gate runs git in the workspace
- **THEN** `GIT_CONFIG_GLOBAL` points at the gate workspace gitconfig
- **AND** it does not point at `~/.gitconfig`

### Requirement: Host sling receipts of pstack-poteto-mode then pstack-build are cook plus route

Feature: pstack-delivery-evidence

Rule: Remaining-units sling is cook plus route in a disposable roles city

The operator MUST host-sling `pstack-poteto-mode` then `pstack-build`
in a disposable city that imports `gascity/roles` and sets
`[daemon] formula_v2 = true`. That city MAY be the inference-gate city
after `--setup-only`, or an equivalent city. A receipt for each formula
is the sling JSON root id plus `gc.routed_to`. `parse_host_sling_root`
MUST call `extract_sling_root_id` only after the payload has a sling root
key (`root_bead_id`, `workflow_id`, `root_id`, or `bead_id`). It MUST NOT
treat a generic JSON `id` as a sling root. It MUST reject formula show
and `--setup-only` logs. It MUST NOT call `launch_review_formula` or
`launch_build_formula` for this pair. A complete proof MUST include both
formulas with both `gc.routed_to` values. A poteto-only row MAY persist
as a failed partial. Hosted submit of unscoped `pstack` from remote
`tommy` waits on the later scoped-name unit. Registry whoami is present.
Dry-run of `gc pack registry publish` of pack path `pstack/` from this
branch is proven. That dry-run MUST NOT be treated as registry
acceptance. Catalog restamp of gastownhall `registry.toml` is not that
dest. Full drain of `pstack-build` is not required. The receipt MUST NOT
be `pstack-review` then `pstack-build`. Formula show is not a receipt.
Setup-only show is not a receipt. `pstack-poteto-mode` MUST NOT auto-sling
the classified formula. The sling unit MUST NOT be a GitHub PR. The
operator MUST NOT sling into a canonical city. Submit was not sent. This
change MUST NOT rename `pstack/pack.toml`.

#### Scenario: Cook plus route of pstack-poteto-mode then pstack-build is the sling receipt

- **GIVEN** a disposable city with `gascity/roles` and `formula_v2`
- **WHEN** the operator host-slings `pstack-poteto-mode` then `pstack-build`
- **THEN** each formula has a sling JSON root id
- **AND** each root bead has `gc.routed_to`
- **AND** the formulas are `pstack-poteto-mode` then `pstack-build`
- **AND** it MUST NOT treat `pstack-review` then `pstack-build` as the remaining-units sling
- **AND** full drain of `pstack-build` is not required
- **AND** the classified formula from `pstack.route.v1` is not auto-slung
- **AND** formula show and `--setup-only` logs are not receipts
- **AND** a poteto-only row is a failed partial, not a complete proof
- **AND** the city is not a canonical city

#### Scenario: Parse rejects show logs and generic JSON ids

- **GIVEN** `parse_host_sling_root` and `extract_sling_root_id`
- **WHEN** the input is formula-show JSON with only a generic `id`, or a `--setup-only` log
- **THEN** parse fails
- **AND** it does not return that `id` as a sling root

#### Scenario: Hosted publish dry-run is proven

- **GIVEN** a clean checkout of `feat/pstack-pack-honesty` tracking remote `tommy`
- **WHEN** an operator runs `gc pack registry publish --dry-run pstack/`
- **THEN** the command exits 0
- **AND** the request names pack `pstack` version `0.1.0`
- **AND** the registry is `https://registry.gascity.com`
- **AND** the repository is `https://github.com/tommy-ca/gascity-packs`
- **AND** the request is not submitted
- **AND** catalog restamp of gastownhall `registry.toml` is not the dest
- **AND** `gc pack registry whoami` succeeds
- **AND** unscoped hosted submit from tommy waits on the scoped-name unit
- **AND** dry-run is not registry acceptance

## Non-Goals

- Adding PStack to `registry.toml` or publishing a release.
- Claiming provider execution, remote worker execution, or canonical-city mutation from disposable live-city checks.

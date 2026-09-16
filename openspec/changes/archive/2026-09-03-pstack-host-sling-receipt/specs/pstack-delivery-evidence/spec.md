## ADDED Requirements

### Requirement: Host sling receipts of pstack-poteto-mode then pstack-build are cook plus route

Feature: pstack-delivery-evidence

Rule: Remaining-units sling is cook plus route in a disposable roles city

The operator MUST host-sling `pstack-poteto-mode` then `pstack-build`
in a disposable city that imports `gascity/roles` and sets
`[daemon] formula_v2 = true`. That city MAY be the inference-gate city
after `--setup-only`, or an equivalent city. A receipt for each formula
is the sling JSON root id plus `gc.routed_to`. Parse MUST reuse
`extract_sling_root_id`. Parse MUST reject formula show and `--setup-only`
logs. A complete proof MUST include both formulas. A poteto-only receipt
MAY persist. Full drain of `pstack-build` is not required. The receipt
MUST NOT be `pstack-review` then `pstack-build`. Formula show is not a
receipt. Setup-only show is not a receipt. `pstack-poteto-mode` MUST NOT
auto-sling the classified formula. The sling unit MUST NOT be a GitHub PR.
The operator MUST NOT sling into a canonical city. This change MUST NOT
restamp `registry.toml`, stamp `gc.provider_panel`, rename
`pstack/pack.toml`, or publish. This change MUST NOT sling.

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
- **AND** the city is not a canonical city
- **AND** this change does not sling

## MODIFIED Requirements

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

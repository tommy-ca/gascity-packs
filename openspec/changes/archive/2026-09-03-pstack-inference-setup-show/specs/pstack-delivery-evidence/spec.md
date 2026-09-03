## ADDED Requirements

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
- **AND** formula sling of `pstack-poteto-mode` and `pstack-build` remains unproven

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

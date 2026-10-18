# Native multi-model fanout on Gas City

This is a deliberately opt-in implementation of **three real, separately routed model lanes** for Swarm, Arena, and Interrogate. It does not replace the frozen sequential formulas or enable the future dynamic N-model provider-panel API.

## Host capability

Current Gas City formula v2 compiles independent sibling steps into separate durable Beads. Steps whose needs list contains only the preparation step are concurrently eligible, and a sibling with needs for all three must wait for all of them. This is the mechanism used in gastownhall/gascity docs/tutorials/05-formulas.md and gascity-packs/gascity/formulas/build-basic-review.formula.toml.

There is no working runtime consumer of gc.provider_panel or gc.child_artifact_path_template in the inspected Gas City source. This pack does not stamp those inert fields, invent a scheduler, call Cursor Task, or claim arbitrary N.

Entry points:

- pstack-swarm-multi: frame, three independent evidence slices, gate, fan-in.
- pstack-arena-multi: design trigger, three independently developed candidate shapes, gate, cross-judge, independent verification.
- pstack-interrogate-multi: select review dimensions, three independent security/quality/runtime reviewers, gate, deduplicate and judge.

Each uses the providerless pack roles pstack.panel-a, pstack.panel-b and pstack.panel-c. Only the **consuming city** can select different providers and model IDs. A formula by itself cannot prove multi-model execution.

## Configure an actual three-model city

Import the pack roles in the target rig. Then explicitly bind the three panel roles under that rig's patches. Example city.toml fragment (model availability depends on the installed harnesses and account):

~~~toml
[[rigs]]
name = "app"

[rigs.imports.pstack]
source = "/absolute/path/to/gascity-packs/pstack"

[[rigs.patches]]
agent = "pstack.panel-a"
provider = "claude"
option_defaults = { model = "sonnet" }
max_active_sessions = 1

[[rigs.patches]]
agent = "pstack.panel-b"
provider = "codex"
option_defaults = { model = "gpt-5.5" }
max_active_sessions = 1

[[rigs.patches]]
agent = "pstack.panel-c"
provider = "gemini"
option_defaults = { model = "gemini-2.5-pro" }
max_active_sessions = 1
~~~

A provider is the harness; the model is the effective option_defaults.model. Models belong in city config, not pack formulas or the session backend. No credentials are stored in PStack pack metadata.

Declared binding preflight:

~~~sh
python pstack/scripts/check_multi_model_city.py --city /path/to/city.toml --rig app
~~~

This validates the declared patch shape and three model names but **cannot attest actual model launches or catch all effective option/override changes**. Check the effective model for each live session with Gas City logs/transcripts. Fail closed rather than silently routing all lanes through one default model.

## Run

Inside a disposable Gas City city with installed pack and roles, inspect the formula graph first. The city_config argument MUST be an absolute path. The rig_name must resolve to the target rig's three explicit model patches:

~~~sh
gc formula show pstack-swarm-multi --json
gc formula cook pstack-swarm-multi --var subject_path=src/ --var artifact_root=.gc/pstack/runs/run-001 --var source_revision=COMMIT_SHA \
  --var city_config=/absolute/path/to/city.toml --var rig_name=app
~~~

Cook does not mean that models were executed. Sling and record which three worker Beads were claimed and which sessions produced receipts. Choose a **unique rig-relative** artifact root per actual workflow. Do not reuse between concurrent runs.

Each worker writes one JSON receipt to the run root under pstack/multi/swarm, arena, or interrogate, named lane-a.json, lane-b.json, lane-c.json. The versioned contract is pstack/schemas/multi-lane.v1.schema.json. It carries workflow, root Bead ID, actual lane/role, source revision, provider/model claims, findings, evidence and completion status.

A native graph barrier depends on all three worker Beads. Its exec check uses pstack/scripts/check_multi_model_evidence.py and mandates a real city.toml path + rig name. The gate compares the receipts' provider and model to the explicitly configured three role bindings, and rejects missing/corrupt/blocked receipts, duplicate model names, incorrect workflow/run/revision, missing evidence, or symlink/path escape. A passing check is evidence of **internally consistent self-reported receipts, not proof of actual independent providers**. It unblocks the synthesizer only after all three declared lanes have completed.

Offline synthetic example:

~~~sh
python pstack/scripts/check_multi_model_evidence.py \
  --root /path/to/disposable-rig \
  --artifact-dir .gc/pstack/runs/run-001/pstack/multi/swarm \
  --workflow swarm --workflow-id ACTUAL_ROOT_BEAD --source-revision COMMIT_SHA \
  --city-config /absolute/path/to/city.toml --rig-name app
~~~

## Verification and limits

Static tests: pytest -q pstack/tests/test_multi_model_fanout.py. Runtime acceptance requires receipts from **three separate live agent sessions with different effective model names**, durable claim IDs, timestamps demonstrating overlapping work where parallel execution is asserted, actual artifact bytes/hashes, correct immutable input revision, deterministic synthesis, failure/retry/cancel tests, and token/cost telemetry. Record the host and pack SHAs, redacted city configuration and effective session model IDs.

The three artifact paths are logically isolated, **not OS-enforced sandboxing**. Do not grant agents write access to each other's workspaces; enforce read-only source and permissions at the host deployment layer. A receipt can misreport its model; do not trust it without runtime provenance. Missing providers or blocked workers must block aggregation. Synthesizer must preserve dissent, evidence citations, and unresolved blockers rather than equating majority votes with truth.

The original PStack release blockers #13/#14/#18 and CI #15 remain independent. Dynamic N-model child creation belongs to Gas City host work #25, and does not authorize frozen provider-panel-stamp #6.

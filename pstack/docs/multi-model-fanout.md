# Dynamic multi-model execution quickstart

The supported opt-in formulas are pstack-swarm-multi, pstack-arena-multi and pstack-interrogate-multi. They accept a runtime-sized, operator-authorized task collection. The original sequential formulas remain separate and unchanged. No panel-a/b/c roles are required.

## Define operator-owned routes

Register/enable any required named rig agents in the consuming city. Add model bindings to those agents through explicit city rig patches. This example uses two installed agent role names, not a fixed panel; a plan may use 2, 5, 8 or more independent tasks on those models.

Example city.toml rig fragment:

~~~toml
[[rigs]]
name = "app"

[[rigs.patches]]
agent = "myorg.research-fast"
provider = "claude"
option_defaults = { model = "haiku" }

[[rigs.patches]]
agent = "myorg.review-deep"
provider = "codex"
option_defaults = { model = "gpt-5.5" }
~~~

Patching does not create the agents; these targets must already exist in the installed city/rig. Choose actual model labels available to your accounts, and confirm effective live session settings. Never put credentials in the task plan.

Operator-approved routes.json:

~~~json
{"version":1,"max_tasks":16,"routes":[{"target":"myorg.research-fast","provider":"claude","model":"haiku"},{"target":"myorg.review-deep","provider":"codex","model":"gpt-5.5"}]}
~~~

The plan.json work units come from the selected method's scope and policy, not the number of models:

~~~json
{"method":"interrogate","revision":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","artifact_root":".gc/pstack/runs/test-001","tasks":[{"id":"security","route_target":"myorg.review-deep","scope_ref":"src/","objective":"Review changed security boundaries"},{"id":"correctness","route_target":"myorg.research-fast","scope_ref":"src/","objective":"Review changed behavior"}]}
~~~

Run preflight, using the actual workflow-root bead ID:

~~~sh
python pstack/scripts/dynamic_contract.py --plan /path/to/plan.json --policy /path/to/routes.json --city /path/to/city.toml --rig app --root /path/to/disposable-rig --workflow-id ACTUAL_ROOT_BEAD
~~~

A planning bead MUST run the same command with --bead-id ACTUAL_PLANNING_BEAD before closing. This persists exact validated JSON to gc.output_json; Gas City's on_complete control will then create N per-item child formula fragments (pstack-dynamic-worker) and route them according to each item. Child output checks fail closed on invalid receipts; the FIRST workflow root finalizes only after Gas City has settled the dynamically spawned children. Do not publish an LLM-generated gc.output_json directly.

Inspect/instantiate in a disposable city:

~~~sh
gc formula show pstack-interrogate-multi --json
gc formula cook pstack-interrogate-multi --var revision=FULL_SOURCE_SHA --var artifact_root=.gc/pstack/runs/test-001 --var city_config=/path/to/city.toml --var rig_name=app --var route_policy=/path/to/routes.json --var subject_path=src/
~~~

Cook is not an execution proof. The actual live run must claim the planning bead, stamp verified source output, close it, let the host generate and route per-item child beads, run model-backed sessions, validate receipt files and complete fan-in. Record exact host revision, actual child count/targets, real model session IDs, timestamps and costs.

Implementation limitation: current Gas City on_complete is supported for structured-output dynamic children, but host guidance prefers native drain. The host does not yet expose verified member-specific heterogeneous model target vars through drain. Track #29 for a host-compatible migration; no pack scheduler or inert gc.provider_panel annotation is introduced. LIVE multi-model execution remains pending #28.


## Phase 2: synthesize only after completed fanout

Gas City's real v2 compiler does not allow an authored step to name the synthetic plan-fanout node as an explicit needs dependency. Accordingly, synthesis is a **separate formula** and is NOT automatically started by phase 1. Verify the original workflow root is closed with gc.outcome=pass; obtain its actual root Bead and its planning Bead IDs.

~~~sh
gc formula show pstack-dynamic-synthesize --json
gc formula cook pstack-dynamic-synthesize \
  --var method=interrogate --var revision=ACTUAL_FULL_SHA \
  --var artifact_root=.gc/pstack/runs/test-001 \
  --var source_root_bead=ACTUAL_FINISHED_ROOT_BEAD \
  --var planning_bead=ACTUAL_PLANNING_BEAD
~~~

Route/sling the resulting phase-2 workflow only after phase 1 passes. Its verify-fanin check validates the completed source workflow, source planning manifest, actual task count and every receipt before allowing the synthesizer to run. This gives a fail-closed, two-phase composition without a pack-specific scheduler. It still requires a disposable live host demonstration.


**Runtime claim identity:** In a model-backed agent shell, `GC_BEAD_ID` is not reliably exported. Obtain the planning Bead ID using `gc hook current --id-only` from that session; `dynamic_contract.py --bead-id` internally resolves and validates the same current claim, refusing a mismatched or absent claim. A check script executed by the host controller receives `GC_BEAD_ID` separately.


**Host asset resolution:** Both dynamic exec checks are executable files under `pstack/assets/scripts/`. Formula check declarations use `../assets/scripts/...` so Gas City's real compiler resolves a trusted absolute file path. Generic `../scripts/...` does not receive that special resolution and must not be used for controller checks.

# Native three-model PStack fanout: formal requirements and architecture

Status: **opt-in code committed, not live-verified**. The three existing sequential method formulas are preserved, and dynamic N-model host expansion remains future work.

## Source-backed architecture decision

Gas City v2 materializes sibling steps as separately claimable durable Beads. A step with needs on all siblings is a real fan-in barrier. The host already uses this pattern in gascity/formulas/build-basic-review.formula.toml. Current Gas City does not consume gc.provider_panel or gc.child_artifact_path_template. Therefore the smallest working design is three fixed sibling Beads dispatched to distinct city-configured model-backed agents, not a pack-specific scheduler or inert metadata.

## Normative requirements

- MM-001: Each multi formula SHALL have one preparation step followed by three independently ready lane Beads, an evidence barrier, and a synthesis step.
- MM-002: Workers SHALL be independently routed to pstack.panel-a, pstack.panel-b, pstack.panel-c; these pack agents SHALL remain providerless.
- MM-003: Operators SHALL supply a bounded subject, immutable source revision, unique rig-relative artifact root, absolute city configuration path and target rig name.
- MM-004: Each worker SHALL only emit its own JSON receipt; it SHALL cite source evidence, name its observed provider/model, and SHALL NOT spawn agents or edit application code.
- MM-005: The barrier SHALL depend on all three lanes and SHALL reject missing, stale, blocked, malformed, duplicate-model or city-binding-mismatched receipts.
- MM-006: Synthesis SHALL preserve dissent, unresolved blockers, provenance, and a risk assessment. A majority vote alone SHALL NOT imply verification.
- MM-007: LIVE PASS SHALL require external session and transcript evidence confirming three distinct effective models and separately claimed Beads. Worker-self-reported model identity is not sufficient.
- MM-008: Existing sequential formulas and frozen parity contracts SHALL remain unchanged. No unsupported provider panel, Cursor Task, pack scheduler, hosted submit or delayed persona expansion.
- MM-009: Cancellation, timeout, provider failure, retry exhaustion and revision drift SHALL fail closed.
- MM-010: Evidence schema changes SHALL use versioned IDs, validators and tests. Model names in code/config shall never be treated as authentication secrets.

## Components / ownership

| Component | Owner | Responsibility |
| --- | --- | --- |
| Formula compiler | Gas City | Compile DAG, runtime check, dependency barriers |
| Beads + agents | Gas City | Independent claims, routing, sessions, retries |
| PStack multi formulas | Pack | Declare fixed lanes and outputs without model names |
| City rig patches | Operator | Assign real providers, effective model names, quotas |
| JSON validator | Pack | Fail-closed receipts, revision and declared-role model matching |
| Session audit | Operator/integration test | Prove actual invoked model and temporal concurrency |
| Future dynamic panel | Gas City host | Runtime expansion for arbitrary N; not implemented |

## Code flow and data flow

~~~text
operator -> city model preflight -> gc formula cook/sling
    -> frame / trigger / select
       |------ panel-a -> lane-a.json ------|
       |------ panel-b -> lane-b.json ------| -> evidence-gate -> synthesize -> Arena verify
       |------ panel-c -> lane-c.json ------|
                          (all needs edges)
~~~

The recipe carries subject_path, source_revision, artifact_root, city_config and rig_name. Every worker reads immutable input and writes its own artifact under ARTIFACT_ROOT/pstack/multi/WORKFLOW/. The gate checks the three files against the versioned receipt model plus the city rig-patch map. Synthesis consumes gated evidence; it does not launch further models.

## Data schema

pstack.multi-lane.v1 is a JSON object with schema, workflow (swarm, arena, interrogate), workflow_id (actual root Bead), lane_id (a/b/c), run_target, provider, model, source_revision, status (complete or blocked), summary, evidence array, and findings array with id/claim/evidence_refs. Empty findings with explicit evidence can be valid. Empty evidence, incomplete/duplicate identity, symlink endpoint or an escaping directory cannot pass. Configured model comparisons alone still require correlation with actual live sessions.

## Failure model and security

- No city model binding or identical model labels: the operator preflight blocks; evidence gate also verifies configured models.
- Missing/failed/mismatched worker: barrier fails; no silent single-provider fallback.
- Source changes: verify against pinned revision; stop for drift.
- Path escapes: gate rejects, but it is not OS-level workspace isolation; operational permissions must separately prevent cross-lane or outside-tree writes.
- Multiple concurrent runs: choose unique paths and isolate/lock shared state.
- Model spoofing: worker receipts cannot attest actual session identity; live acceptance must compare Gas City effective session models and traces.
- Resource control: bounded time, token spend, retries, interruption, and cancellation are host/operator responsibilities.

## Alternatives and tradeoffs

Do not add gc.graph_operator as if it expands children, stamp gc.provider_panel without host support, or introduce an external subprocess session orchestrator. Static three-lane DAG makes a bounded feature possible now. Arbitrary N requires host architecture and tests (#25). Splitting independent read-only work follows PStack separate-before-serializing-shared-state; giving host sole scheduling ownership follows boundary-discipline; fail-closed receipts follow make-operations-idempotent.

## Thermos acceptance matrix

Security/correctness: path isolation, prompt-injection isolation, immutable revision, no secrets, no fake model identity, negative provider/receipt tests, runtime failure and recovery. Code quality: under 1000 lines per added file, no duplicate scheduler, minimal formula reuse, typed versioned contracts, simple role names, explicit evidence path.

Tier 1: Python TOML + static pytest and synthetic failure cases.
Tier 2: disposable Gas City formula show/cook and compiled Bead DAG inspection.
Tier 3: real three-model sling with overlapping session timestamps, three independent transcripts, actual model IDs and hashed files, failure/retry/cancel, resource accounting.
Tier 4: PR release gates; independent blockers #13/#14/#18/#15 still apply.

GitHub graph: #21 epic -> #22 native DAG, #23 evidence-gate -> #24 integration proof; future dynamic N #25. Separate upstream/release epic #12 is not waived.

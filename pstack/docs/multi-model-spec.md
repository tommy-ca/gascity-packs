# Dynamic PStack orchestration: formal requirements and design (v2)

Status: implemented on PR #1, with source-level CI and live runtime integration as distinct validation tiers. Preserves legacy sequential formula names. Replaces earlier fixed three-panel design.

## Semantic building blocks

| Atomic block | Data/behavior | Owner |
| --- | --- | --- |
| MethodPolicy | Swarm: independent evidence slices; Arena: alternative designs when triggered; Interrogate: relevant review dimensions | PStack policy |
| Task | Unique id, bounded scope, objective, pinned revision | Plan |
| RouteCapability | Operator-allowlisted role, declared provider and model | City / PStack validation |
| Decomposition | N work items from actual scope and budget (not a fixed model count) | Planner |
| Fanout | Host materializes one separately claimable child per item | Gas City |
| Worker | One item, one model-backed session, one evidence artifact | Gas City + reusable worker |
| EvidenceGate | Receipt validity, status, identity and provenance checks | PStack check |
| Aggregation | Wait for all children, dedupe claims, preserve dissent, report gaps | Gas City + PStack |
| Verification | Source-grounded verdict, not majority or model agreement | PStack verifier |
| FailurePolicy | Retry, cancellation, path safety, drift, spend and limits | Host + pack contract |

These semantic blocks compose all three methods without a separate database, scheduler, model SDK, process launcher, worktree manager, or fixed panel.

## Normative behavioral requirements

- MM2-001: Work count SHALL derive from task decomposition and policy, with 2..max_tasks and hard cap 64; the model roster size need not equal task count.
- MM2-002: At least two different actual model identities SHALL be selected for a multi-model run. Different tasks MAY reuse a model.
- MM2-003: Every task SHALL have a unique safe ID, pinned full source revision, bounded scope, objective, allowlisted target and unique run-relative output path.
- MM2-004: The trusted route policy SHALL match explicit city rig patches on target, provider and model. An LLM plan SHALL NOT inject commands or provider flags.
- MM2-005: The host SHALL create one durable child work unit per validated task, with separately routable target and independent output.
- MM2-006: The producer SHALL validate the entire task manifest BEFORE writing gc.output_json and closing its source bead. Failed preflight SHALL block execution.
- MM2-007: Each completed child SHALL produce a versioned bounded receipt checked by its own runtime check step. Missing, failed and stale evidence SHALL block.
- MM2-008: The aggregator SHALL enumerate the actual collection of child outcomes, preserve dissent and unresolved work, and never assume N=3 or consensus=truth.
- MM2-009: Host session logs/transcripts SHALL attest effective models independently of worker-written JSON before a LIVE PASS.
- MM2-010: The host owns retries, work claiming, session routing and cancellation. The pack SHALL not run another agent scheduler.
- MM2-011: Legacy sequential formula interfaces SHALL remain supported; the dynamic bridge SHALL disclose deprecation and current host capability limits.
- MM2-012: Migration to native drain with per-member model routing SHALL require a verified host consumer, not speculative metadata.

## Code/data flow

  Operator source SHA + unique artifact root + city config + route policy
                         |
                 Method decomposition
                         |
      validated plan.json (N tasks + route choices)
                         |
       pstack/scripts/dynamic_contract.py (policy / path / model checks)
                         |
        gc.output_json = {tasks: [normalized immutable work units]}
                         |
              Gas City on_complete runtime control
                         |
       N parallel child fragments of pstack-dynamic-worker
          |            |            |            |
        result 1      result 2     ...        result N
          |            |                         |
           child check_dynamic_task.py checks and receipts
                         |
         Gas City fanout control waits for all child sinks
                         |
                    synthesis
                         |
               Arena verification

## Data schema

Input plan: JSON object with method (swarm|arena|interrogate), revision (full 40/64 hex SHA), artifact_root (unique rig-relative), tasks[] containing id, route_target, scope_ref, objective. Operator policy: JSON version=1, max_tasks 2..64, routes[] containing target, provider, model. Runtime validated output: JSON tasks[] with fields task_id, route_target, scope_ref, objective, artifact_path, revision, workflow_id, method, provider, model. Child receipt schema: pstack.dynamic-task.v1; fields schema, task_id, route_target, revision, workflow_id, method, provider, model, status, summary, evidence[], findings[].

The safe artifact filename derives from the validated run root, method and task ID. It is not arbitrary input. Routes are chosen from an operator-reviewed capability inventory. Actual effective host model identity is NOT attested by a model's own receipt; a separate integration witness must bind session to bead and config.

## Runtime contract and chosen architecture

- Native Gas City v2 drain dynamically scatters an existing convoy into item workflows with max_units, separate work contexts, durability and retries.
- Native Gas City v2 on_complete expands output.tasks to dynamically sized child formula fragments. The bonded expansion accepts per-item route_target via item variables. The controller links sink dependencies and controls fan-in.
- Current host drain does not project a member-specific route target/model selector into per-item formula vars. Heterogeneous model routing is thus implemented with supported on_complete as an explicit temporary compatibility bridge. Host docs favor drain, and host lint may warn on this bridge. Host issue #29 specifies the migration.
- No gc.provider_panel or gc.child_artifact_path_template consumer was found. Do not invent or stamp either. The agent's session backend is not a model roster.

## Security, correctness and Thermos gates

Check plan route allowlist, city patch matching, source pin, bounded objectives, path traversal, symlinks, duplicate IDs, max children and metadata size before metadata publication. Each child check must validate single artifact identity and status. Sources/prompts remain untrusted. PStack MUST NOT treat self-reported model labels as runtime proof, grant global secret access, or assert host-level OS filesystem isolation from logical paths. Verify failed/pending/cancelled child effects, retry idempotency, recovery from partial dynamic expansion, and exact expected-vs-spawned cardinality.

SOLID/KISS/DRY/YAGNI: one atomic route/plan contract, one per-child validator, one worker expansion, three thin method entrypoints, and the existing Gas City executor. No copied session state machine or provider dispatch implementation. PStack principles applied: subtract-before-add, boundary discipline, type discipline at dynamic JSON boundaries, separate-before-serializing-shared-state, make-operations-idempotent, exhaust design space only when Arena trigger is true.

## Verification ladder and epic graph

1. Static/negative tests: cardinalities 2, 3, 5, 8, 64; role allowlist and revision/path attacks; receipt failures; formula TOML parser.
2. Real host compile/cook/sling in disposable city; inspect actual generated N child beads and actual item run targets; test host warning and output-json variable substitution.
3. Live two-or-more-model test with independently attested session identifiers, overlapping work, full receipts and timestamps, retries, cancellation, budget and source revision drift.
4. Shared release CI/CodeQL, OpenSpec compatibility and existing registry/standing/transaction issues #13/#14/#18/#15.

GitHub #21 -> #26 dynamic graph + #27 integrity contracts -> #28 runtime proof; #29 host drain migration, also tracked by #25. No LIVE PASS claim without tier 2/3 evidence.


## Executable two-phase fan-in correction

The real Gas City Go compiler rejects authored needs = ["plan-fanout"], because its on_complete control is minted only after authored-step validation. It is **incorrect** to declare a single formula with a static synth step depending on that synthetic ID; simply changing its dependency to plan would cause a race.

Current supported implementation therefore uses two independently launched formulas:
1. pstack-*-multi: one plan producer, validated output.tasks, native dynamically spawned children, and a host-owned workflow finalizer which waits for the fanout sinks.
2. pstack-dynamic-synthesize: accepts the actual completed source root and planning Bead IDs, has a check_dynamic_fanin.py gate verifying closed/pass source root and the exact dynamic receipt inventory, then runs synthesis and verification.

The operator or a higher-level Gas City coordinator starts phase 2 only after phase 1 passes; there is **no automatic phase-2 dispatch**, no polling sub-scheduler and no promise of zero-touch end-to-end automation. The existing flowchart above is a logical two-phase view rather than one atomic formula. A future host primitive may compose phases with a real reference to a minted fanout control, but it must be proved with live host tests first. Failure to enforce this boundary risks synthesizing before children finish, so the separation is intentional.


**Host asset resolution:** Both dynamic exec checks are executable files under `pstack/assets/scripts/`. Formula check declarations use `../assets/scripts/...` so Gas City's real compiler resolves a trusted absolute file path. Generic `../scripts/...` does not receive that special resolution and must not be used for controller checks.

## Engineering host ownership and optional consumer independence (2026-10-31)

**Source ownership:** This Gas City pack and the operator-selected city are the sole owners of host-specific PStack dynamic formulas, agent/route configuration, child Beads, metadata CAS, receipt schemas, runtime lifecycle and effective model-session provenance. A downstream quant or other domain overlay is **neither a dependency nor part of the acceptance test**. No host pack consumer has to install QStack/qorch; conversely QStack must not have to install Gas City.

**Atomic contracts:** (1) DecompositionPlan with N=2..64 bounded immutable-source tasks, (2) operator-validated ModelRoute, (3) native HostExpansion into separately claimable child work, (4) one versioned TaskReceipt per child, (5) explicit two-phase FanIn with root/manifest validation, (6) independent SessionAttestation for actual effective provider/model and retry/cancellation/budget. The first five have source-level implementation/tests on the exact pack PR branch; the sixth and end-to-end provider-backed proof remain unverified under issue #28.

**Owner-respecting code/data flow:** city policy -> pack validation -> planning Bead metadata CAS -> host on_complete expansion -> child claim/attempt and receipt checks -> closed/pass source root -> explicitly dispatched phase-2 fanin check -> synthesis + verification -> optional opaque immutable artifact reference for external consumers. This pack does not author or persist a domain consumer's scientific research lifecycle and does not interpret execution completion as trading readiness.

**Issue graph:** [#21](https://github.com/tommy-ca/gascity-packs/issues/21) owns this PStack/Gas City program; [#26](https://github.com/tommy-ca/gascity-packs/issues/26) owns dynamic task/route wiring, [#27](https://github.com/tommy-ca/gascity-packs/issues/27) owns security and receipt validity, [#28](https://github.com/tommy-ca/gascity-packs/issues/28) owns real runtime/independent verification, and [#29](https://github.com/tommy-ca/gascity-packs/issues/29) owns future canonical native drain/member routes. The superseded [QStack epic #2608](https://github.com/tommy-ca/qstack/issues/2608) is closed as not planned for engine-specific coupling. Do not recreate it by a vendor-aware downstream adapter.

**Review gates:** Apply Cursor PStack principles (subtract-before-add, single writer, type boundaries, idempotence), independent changed-diff Thermos correctness/security and code-quality reviews, and independently attributed Swarm/Arena/Interrogate method receipts. Existing CI compiler and mocked routing checks are not provider-backed LIVE proof. Keep existing formula migration/release blockers OPEN until real proof.

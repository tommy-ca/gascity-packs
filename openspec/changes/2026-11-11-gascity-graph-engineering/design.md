# System design — native graph-first Gas City, no second control plane

## C4: context/containers
```text
Owner intent + requirements  [authoritative scope]
     │ approved input convoy
     ▼
Gas City (existing)
 ├─ formula parser/compile (graph.v2 and >=2.0.0 capability)  ← optional graph-engineering pack
 ├─ beads/convoy store & graph controls (single state authority)
 ├─ dispatch: native drain / fanout / retry / scope and ordered dependency readiness
 ├─ agent/provider/runtime sessions via city-defined, allowlisted role targets
 └─ durable event/attempt/check references -> dashboard
                       │
                       ▼
  independent review steps (acceptance / safety / continuity)
                       │
                       ▼
  synthesize -> source-bound report (NOT a source of verified status)
                       │ (separate untrusted research notice)
                       ▼
  LLMWiki v2: HELD -> independent rights & reviewer -> existing sole CAS publisher
                      -> immutable separately issuer-pinned CompiledBundle -> read-only consumer
```
GraphCode's UI, live PTY and message/spawn actions are **not** embedded. longgraph's Markdown ledger and independent timers are **not** new runtime stores or timers here. A host order may schedule this formula if an operator configures it, never inferred from a skill.

## Three graphs, three different meanings
- Work dependency DAG: graph.v2 `needs` / child-bead prerequisites. Must reject unknown node, duplicate ID, cycles; host compiler is normative.
- Control-flow graph: `[steps.drain]`, `[steps.check]`, retry and host-minted fanout/scope/finalization. Finite retry/work budgets are host-owned, not an LLM prompt contract.
- Evidence authority graph: source hash -> actual Bead/session attempt -> test artifact -> independent review verdict -> operator accepted report -> optional separately signed wiki grant. A source's `PASS` field is data, not authority.

## Semantic atoms and ownership
| Atom | Gas City existing primitive | GraphCode / longgraph source idea | Trust / lifetime |
| --- | --- | --- | --- |
| Goal/Intent | approved source Bead, input convoy and formula vars | `GoalSpec` / North Star | human/owner-approved, versioned |
| Node/WorkUnit | `Step`, materialized child Bead | live LoopNode / executor workset | host-owned claims and state |
| DependencyEdge | `needs` graph.v2 | handoff / ledger work order | host compiler authoritative |
| ControlEdge | native drain, on_complete fanout, retry, scope check | message/spawn / supervisor signal | host-only; no generic equivalence |
| Activation | ready bead + dispatcher, optional configured orders | session cadence / host timers | actual host/city-defined |
| RuntimeRole | `gc.run_target` allowlisted city role | CLI backend / executor/supervisor | target is not a verified model identity |
| GraphState | Beads, versioned store, host graph controls | graph daemon / ledger.md | NEVER mirrored to second ledger |
| WorkClaim | host native claim and exact-store CAS | live session/one writer | worker cannot self-approve |
| Attempt/Checkpoint | native retry/check and durable event metadata | goal predicates / verified ledger rounds | check outcome != independent acceptance |
| Evidence | test output, exact SHA, session and artifact refs | supervisor audit / typed action | source bound and reproducible |
| KnowledgeNotice | QStack v2 metadata HELD candidate | compiled semantic knowledge | no publisher authority in Gas City |

## Code flow (proposed execution)
1. Operator imports pinned optional pack and rig roles; chooses a pre-approved existing convoy.
2. `gc sling` / `graphv2.PrepareInvocation` validates version requirements, reserves source target, normalizes input convoy, compiles formula via `internal/formula/compile.go`.
3. `graphv2` materializes formula steps with `needs` and runtime metadata into durable Beads. The host dispatches eligible work and owns claim/retry/cancel.
4. Pack's `drain` invokes built-in `do-work` for each approved convoy member, with separate context and exclusive work-set access. It does not mint a second task graph or take over scheduler.
5. Three review steps become ready only after drain resolution; each writes its own review artifact under operator-authorized artifact root, with source SHA and reviewer identity claims (independently verified by host where possible).
6. `synthesize` waits for all review predecessors. Prompt-level policy cannot supersede host gates; publication is absent. `finalize` reports only verifiable outcomes.
7. External LLMWiki v2 intake may later use source notice/provenance, only via independent rights/reviewer and sole publisher.

## Data flow / model
```text
ApprovedGoal + InputConvoy (host store)
  -> Formula graph.v2 compile (host control)
  -> [Bead: inspect] -> [Bead: design] -> [Bead: drain] 
                                          | native children and actual attempts
                                          v
                                  PerMember Evidence Refs
                                          |
                      +-------------------+--------------------+
                      v                   v                    v
                   acceptance          safety              continuity
                      +-------------------+--------------------+
                                          v
                                      synthesize -> final report
                                          |
                                     HELD source notice (separate)
```
`graph-engineering/schemas/semantic-graph.reference.schema.json` and the example are **non-authoritative** static crosswalks. Actual authoritative wire types remain in Gas City (`Formula`, `Step`, `graphv2.Invocation`, `Bead`, `drainManifest`). Do not store or import this model into production, create custom persistence, or trust its `writer` field.

## Failure modes and safeguards
- Unknown `formula_compiler` support -> refuse, do not silently downgrade to graph.v1.
- Unapproved/stale convoy, unknown target, out-of-rig paths, missing permissions -> block before run.
- Static `needs` cycle -> graph validation failure. Conditional control loop requires finite cap; `until` alone cannot prove bounded resources.
- Failure/cancel/retry -> host Beads and control-state receipts, no model-only success.
- Executor loses context -> restore from host store + artifacts; no warm chat as authority.
- Review lanes share one actual session or no independent evidence -> cannot claim independent Swarm PASS.
- Side effects after crash -> host idempotency/reconciliation proof needed (not granted by this pack).
- Prompt injection / forged approvals / metadata source -> inert data, never authority.
- Untrusted source-revision / licensing -> LLMWiki HELD, no automatic publishing.

## SOLID / KISS / DRY / YAGNI
Reuse one Gas City runtime and existing `do-work` child formula; keep pack as a declarative composition. No parallel Go daemon, no new graph store, no custom worker protocol, no global `ledger.md`, no model router, no new LLMWiki schema authority. Only add a host feature after exact failing native proof shows an unmet need.

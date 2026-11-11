# Reusable GasCity methodology design patterns — exact-source crosswalk

**Observed sources:** `gastownhall/gascity-packs@7f86098c04ead8cb78706ddc9524cf4cab83b028`, checked by GitHub connector, not run as live workflows. **Application:** [graph-engineering pack](../../../graph-engineering/README.md) (repository-root path: `graph-engineering/`).

## Taxonomy: decomposition to atomic semantics

| Pattern | Source implementation | Semantic leaves | How to recompose | Independent falsifier |
| --- | --- | --- | --- | --- |
| **Virtual Lifecycle Contract** | `gascity/formulas/build-base.formula.toml`; `gascity/REQUIREMENTS.md` | StageAnchor, StageSelector, ArtifactPath, Mode | For a full method use `extends=["build-base"]`; for a post-convoy job remain explicit standalone | missing/reordered base anchor |
| **Compatibility Ledger** | all four `{bmad,compound-engineering,superpowers,gstack}/REQUIREMENTS.md`; `gascity/tests/test_derived_pack_compatibility.py` | Capability, SourceClaim, RequirementID, TestRef | Per-pack ledger and source/test traceability | source formula drift invisible to ledger |
| **Plan Readiness Gate** | `bmad/formulas/bmad-build.formula.toml` | ApprovedStory, ReadinessVerdict, Precondition | Optional preflight/readiness before drain, but operator consent remains external | ready-stage omitted yet worker starts |
| **Review Expansion** | `compound-engineering/formulas/compound-plan-review.formula.toml` | ReviewLane, Evidence, Synthesis, FixPath | Disjoint reviews; separate actual sessions require host evidence | review result missing or stale; false independent identity |
| **Bounded Check Loop** | `gascity/formulas/build-basic-review.formula.toml`; `superpowers` reviews | Attempt, CheckCommand, MaxAttempts, Outcome | Prefer `[steps.check]` / `[template.check]` native gate to agent-only text | check omitted, loops exceed budget, malformed verdict accepted |
| **TDD as Dependency Graph** | `superpowers/formulas/superpowers-development.formula.toml` | TestFailureWitness, Implementation, PassingWitness, ItemReview | Optional leaf workflow for code tasks, not universal scheduler | no failing-test witness, green-on-no-test |
| **Scoped Drain** | `gascity/formulas/implement.formula.toml` | InputConvoy, DrainUnit, MemberAccess, ItemFormula | Reuse separate/exclusive `do-work` | mixed membership, duplicate claim, missing finalization |
| **Release-Readiness Gate** | `gstack/formulas/gstack-build.formula.toml`; `gstack-release-readiness` | QA, ReleaseVerdict, PublishAuthorization | Keep release after review, never infer from draft review | skip QA or publish without independent approval |
| **Read-only Delivery Gate** | `pr-pipeline/formulas/mol-pr-ship.formula.toml` | BlastRadius, Scorecard, PrePush | Expose an audit report, no push by default | report-only stage performs Git write |
| **Rig-local Ownership** | `oversight-rig/pack.toml` | RigScope, ProjectLead, EscalationEvent | Delegate review to scoped agent, no second global coordinator | cross-rig edits or fabricated escalation |
| **Explicit Pack Composition** | four derived method `pack.toml`; `gascity/roles/pack.toml` | Import, RoleBinding, VersionRequirement | Opt-in `[imports.gc]`, no hardcoded provider | implicit missing host capability |
| **Knowledge Distillation** | `compound-engineering` finalization | Finding, ReusablePrinciple, Provenance | Submit *candidate* semantic leaves to independent QStack v2 intake | self-attested confidence promoted to verified wiki |

## Recomposition architecture

**Gas City host** is the only work-control authority: parsed Formula → materialized Beads → claims and attempts → check/retry/drain controls → durable outcome. A **pack** is declarative recipe + prompts + check executables + compatibility ledger. An **agent-method** (PStack Swarm/Arena/Interrogate) is a behavior policy over runtime work nodes, not a new scheduler. An **evidence graph** records source hashes, session/Bead IDs, reproducible checks, independent reviews and issuer authorizations without replacing Beads.

Two supported composition roles must remain separate:

1. **Existing `graph-long-horizon`** (PR #33): takes an approved input convoy; performs `inspect → design → drain → 3 reviews → synthesize → finalize`. It is not the full software factory. Preflight checks host IDs and file containment but cannot grant user approval. Reviews are report-only pending independently verified evidence checks.
2. **Possible `graph-build`** (future, not implemented): only if a real requirement justifies it, extend `build-base`, preserve all base anchor IDs/order and declared `interaction_mode`, `review_mode`, `drain_policy`, producer artifacts and optional publish switch. Insert graph readiness after `decompose`, bounded graph review after implementation, and a QA/release readiness gate before publish. It must pass `GC-METH-012` as a full derived method. **YAGNI until native-run evidence is gathered.**

## Pattern constraints and antipatterns

- No provider-native opaque subagents in place of observable Gas City Beads.
- No model-reported `PASS`, or review-headings-only `Swarm/Arena/Interrogate`, as independent evidence.
- No default 17-lane review on simple graph tasks: three focused lanes are deliberate; expand only with observed failure classes.
- No automatic external side-effect on `finalize` or `synthesize`.
- No graph.v2 fixed-panel `on_complete` bridge copy or speculative per-member model routing: source owner issue #21/#29.
- No knowledge wiki writer or source-rights grant in the GasCity pack.
- No independent retries with an unbounded loop; use core retry and explicit budgets and exact-head tests.
- Prompt injection, scope escape, forged host metadata or worker-supplied session ID are untrusted data.

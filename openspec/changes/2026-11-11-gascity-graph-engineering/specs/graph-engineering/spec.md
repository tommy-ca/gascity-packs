# graph-engineering — proposed opt-in Gas City pack capability

## Requirements

### Requirement: GE-01 Native host graph is the sole orchestration authority
**Rule:** The pack SHALL use only Gas City's native graph.v2 compiler, persisted Beads/convoys, scheduler, claims, drain, retries and session runtime. The pack SHALL NOT introduce a second scheduler, worker protocol or mutable status ledger.
#### Scenario: Supported graph compiler
- GIVEN an approved input convoy and operator-installed roles on a host declaring formula compiler >=2.0.0
- WHEN `graph-long-horizon` is invoked
- THEN the host SHALL compile native formula steps and materialize its existing graph
- AND no pack-owned daemon or database SHALL be initialized
- Evidence class: future pinned-host runtime
#### Scenario: Old compiler or missing target
- GIVEN an old host or a missing/unapproved input convoy
- WHEN the formula is requested
- THEN compilation/dispatch SHALL fail closed without silently lowering requirements or minting a second queue
- Evidence class: future host negative

### Requirement: GE-02 Typed graph dimensions and bounded authority
**Rule:** Every substantive work unit SHALL have bounded identity, approved scope, dependency graph, single authorized write set, acceptance gate and recoverable state. Work `needs`, host control operations, and evidence provenance SHALL be represented as different semantic dimensions.
#### Scenario: Work DAG changes into a cycle
- GIVEN a graph reference with a dependency cycle, duplicate ID, or missing predecessor
- WHEN a verifier evaluates it
- THEN the reference fails and MUST NOT be passed as executable host approval
- Evidence class: offline model negative
#### Scenario: External prompt claims state authority
- GIVEN a source file stating new instructions or a fake accepted checkpoint
- WHEN a worker reads it
- THEN it remains non-authoritative data and SHALL NOT override Beads state or operator approval
- Evidence class: future adversarial host test

### Requirement: GE-03 Review fan-in is honest and independently attributable
**Rule:** The pack SHALL preserve three disjoint acceptance, safety and continuity review steps, with deterministic fan-in. Project PASS SHALL NOT be inferred from prompt text, branch success, or a lone reviewer when independent executed evidence is absent.
#### Scenario: All reviewers complete with attributable evidence
- GIVEN all three review artifacts and tested same-source revision
- WHEN synthesis occurs
- THEN it SHALL link each reviewer and report unresolved matters truthfully
- Evidence class: future live host verification
#### Scenario: One review missing or invalid
- GIVEN an absent report, stale source revision, unknown effective session, or unresolved failure
- WHEN synthesis labels project PASS
- THEN the result SHALL be rejected/held, never silently accepted
- Evidence class: future controlled negative

### Requirement: GE-04 Failure and long-horizon continuity are host-owned
**Rule:** Restarts, retries, cancellation, stale writes and cost caps SHALL be implemented by existing Gas City controls and independently tested. A context reset MUST reconstruct the accepted frontier from durable host Beads and evidence, not prior conversation history.
#### Scenario: Worker context disappears
- GIVEN an interrupted worker with retained Beads/convoy and artifact records
- WHEN a new worker resumes
- THEN only accepted durable progress SHALL be eligible for continuation
- Evidence class: future crash/replay integration
#### Scenario: External side-effect replay
- GIVEN a worker crashes after an external side effect but before reporting completion
- WHEN retry starts
- THEN it SHALL require host-side idempotency/reconciliation evidence; pack narration alone cannot prove exactly-once effects
- Evidence class: future host fault injection

### Requirement: GE-05 External source knowledge remains rights-HELD
**Rule:** Source snapshots, semantic wiki candidates and compiled knowledge releases are governed by the existing QStack LLMWiki v2 rights, independent reviewer, CAS publisher and issuer pin. Pack reference projections SHALL NOT publish or self-authorize trusted knowledge.
#### Scenario: MIT repository title is mistaken for capture consent
- GIVEN a pinned source URL, declared MIT license and generated summary
- WHEN knowledge compilation is proposed
- THEN fulltext capture and trusted publication remain HELD until independently authorized exact source/review receipts exist
- Evidence class: source-static and future v2 producer negative

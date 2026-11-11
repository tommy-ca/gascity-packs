# ADR — compose Gas City graph primitives, do not import a second orchestration runtime

**Status:** PROPOSED; source-static reference, not approved production architecture.

## Decision
Use an opt-in `graph-engineering` Gas City pack with one `graph-long-horizon` graph.v2 formula using existing host `needs`, drain and role targets, plus three review steps. Use modern `[requires] formula_compiler = ">=2.0.0"` instead of deprecated `contract = "graph.v2"`. Work/claims/checkpoints remain in canonical host Beads and native manifests. PStack owns method semantics, QStack LLMWiki v2 owns knowledge rights/review/publication.

## Alternatives
- Clone GraphCode daemon/PTY/session UI: rejected (new host runtime and license/portability/correctness burden).
- Adopt longgraph `ledger.md` as second Gas City scoreboard: rejected (dual state owner, DRY/consistency risk).
- Implement dynamic per-member model router in pack: rejected; live heterogeneous per-member routing belongs existing #21/#26–#29.
- Add default orders/timers, graph DB or compulsory external agent framework: YAGNI.
- Self-publish source summaries into QStack `knowledge/`: rejected; only existing independent v2 publisher can trust-release.

## Consequences
The optional pack can describe, compile and potentially run on host versions satisfying >=2.0.0; until exact-head native host execution the observed proof is static only. Review steps are *logical separation*, not proof of independent physical sessions. Future release requires source-pinned safety gates, actual GC host tests, real PStack/ Thermos reviewer receipts, and separate LLMWiki authorization.

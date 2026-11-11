# Proposal — Gas City graph engineering and long-horizon orchestration

**Owner:** [tommy-ca/gascity-packs #32](https://github.com/tommy-ca/gascity-packs/issues/32). **Status:** PROPOSED / STATIC_SOURCE. **Prerequisites:** upstream Source census, approved input convoy. **Non-goal:** add a second scheduler or implicit model-router. This work is an opt-in pack, not an upstream gascity fork.

## Intent
Decompose Gas City and GasCity Packs into semantic atoms and recompose a long-horizon workflow using *native* graph compiler, Beads, convoy/drain, roles, explicit evidence reviews and bounded host controls. Extend concepts from GraphCode (typed action edges and live session) and longgraph (durable read/write authority, supervisor and cold-resume), without treating their runtimes as equivalent.

## Read-only Probe evidence
- **STATIC_SOURCE**: host `gastownhall/gascity@6bd609f5bfb41f43f444843b1220d0cde4473446`: `internal/formula/{types,graph,compile,requirements}.go`, `internal/graphv2/invocation.go`, `internal/dispatch/{drain,fanout}.go`.
- **STATIC_SOURCE**: packs `gastownhall/gascity-packs@7f86098c04ead8cb78706ddc9524cf4cab83b028`: `gascity/{pack.toml,formulas/build-base*,formulas/do-work.formula.toml,roles/pack.toml}`.
- **METADATA**: existing fork #21/#26/#27/#28/#29/#31; QStack graph reference draft PR #3297; no verified latest live credentials.
- **UNAVAILABLE/NOT_RUN**: native `gc` compiler/linters in this session, actual Bead host runtime, independent sessions, PStack methods, both Thermos reviews, LLMWiki v2 ingestion and CAS publication.

## Scope
1. One separately importable `graph-engineering` pack using the `formula_compiler >= 2.0.0` host capability and existing `gascity` import.
2. An approved input convoy, one native separate/exclusive drain, three actual graph review steps and fan-in; no new runtime/claimed session receipts.
3. Explicit atomic semantics, source/provenance schemas for **reference only**, documentation and falsifier-first offline checks.
4. A rights-HELD LLMWiki v2 intake plan, no source-fulltext capture and no corpus or publisher mutation.

## Non-duplication
- PStack dynamic multi-model fanout already has issue owner `tommy-ca/gascity-packs#21` children #26–#28; native per-member drain routing remains host #29 and formal verifier #31. No rewrite of this work.
- PStack upstream methodology and Thermos remain external skills; this pack supplies optional engineering semantics, not new PStack execution authority.
- QStack standalone LLMWiki v2 producer owns source rights, review, CAS, release, read-only consumer. No runtime imports.

## Completion bar
Native compiler and live-session gates require actual receipts; static source claims, fixture tests, prompt review, or a green workflow with zero executed steps cannot establish LIVE. Source capture and trusted wiki release require independent rights+review and publisher proof.

# Graph Engineering — Gas City compatibility ledger

Schema: `gc.graph-engineering.requirements.v1`  
Status: **DRAFT / source-static**, scope: one narrowly opt-in, approved-convoy workflow, **not** a new Gas City core runtime and **not** a fifth full `build-base` methodology.

## Compatibility Claims

- **GC-METH-012 relationship:** BMAD, Compound Engineering, Superpowers and gstack are full `build-base` derivatives; all import `../gascity`, extend the virtual lifecycle and keep base anchors intact. `graph-long-horizon` instead starts **after an approved work convoy exists**, so it MUST NOT pretend to implement requirements, plan creation, decomposition or optional publish anchors. The proposed future `graph-build`, if ever needed, MUST extend `build-base` and satisfy GC-METH-012 like the four existing derived packs.
- **Import contract:** `graph-engineering/pack.toml` declares `schema = 2` and `[imports.gc] source="../gascity"`, without owning a runtime, service, order, named session, storage or provider.
- **Formula contract:** one cataloged `graph-long-horizon` formula with `[requires] formula_compiler=">=2.0.0"`, `target_required=true`, no deprecated compiler contract and no direct provider-native worker spawning.
- **Input boundary:** a deterministic bounded `inspect` check resolves Gas City-hosted step/root/convoy identity and paths under one rig. The result `INPUT_SANITY_OK_NOT_AUTHORIZED` is not a human approval, source-rights, model or review attestation. Missing host metadata or unsafe paths MUST fail.
- **Graph control:** work dependencies use `needs`; the existing host manages persistent Beads/convoys, claims, retries and real sessions. One `[steps.drain]` uses `context=separate`, `formula=do-work` and `member_access=exclusive`. This pack does NOT add a GraphCode daemon, longgraph ledger, on_complete bridge or synthetic host step reference.
- **Review semantics:** acceptance, safety and continuity are distinct native graph nodes which all depend on drain and all precede `synthesize`. A method title or `gc.run_target` is **not** independent session or effective model proof. Existing native `build-basic-review` and derived-pack check loops are examples of future mechanically checked acceptance; the current graph workflow remains report-only and cannot publish.
- **Artifact boundary:** all described outputs are rig-relative and source-bound. The new non-authoritative reference JSON schemas/exemplar are for audit/falsification; they are NOT Gas City runtime wire formats and cannot attest PASS.
- **Modes and limits:** the specialized `graph-long-horizon` formula provides no generalized `interaction_mode`, `review_mode` or `drain_policy` override surface. A full `graph-build` variant must inherit and honor all method metadata/mode vocabularies, selectors, base anchors and bounded check loops before advertisement. Do not invent generic model routers or indefinite `until` loops.
- **Rightful ownership:** PStack is upstream software methodology semantics; Gas City owns all host orchestration; QStack owns only standalone LLMWiki v2 rights-safe producer and immutable publication, **not** GasCity host control. Existing `tommy-ca/gascity-packs#21` owns dynamic multi-model routing; #29 owns native per-member drain-route host evolution.
- **Publication:** no push, PR, merge, registry release or trusted LLMWiki publishing path is included; source notice status HELD, unsigned reports are not authoritative.

## Source-specific design patterns learned

| Proven upstream implementation | Adopted atomic leaf | Deliberately not copied |
| --- | --- | --- |
| `gascity/formulas/build-base.formula.toml` | virtual contract, named artifacts, producer check | second base factory |
| `bmad/formulas/bmad-build.formula.toml` | readiness gate before work | vendored BMAD methodology |
| `superpowers/formulas/superpowers-development.formula.toml` | test-negative-before-positive dependency | mandatory TDD on every generic graph |
| `compound-engineering/formulas/compound-plan-review.formula.toml` | disjoint reviewer lanes, bounded synthesizer | 17-lane panel for every run |
| `gstack/formulas/gstack-build.formula.toml` | QA and release gate anchors | implicit deployment |
| `pr-pipeline/formulas/mol-pr-ship.formula.toml` | blast radius and pre-push non-authority | unwanted source publishing |
| `oversight-rig/pack.toml` | rig-local scope and deterministic escalation | second always-on mayor |
| `gascity/formulas/build-basic-review.formula.toml` | native fanout/fanin and check-loop example | fabricated verified reviewer receipt |

All upstream references are from `gastownhall/gascity-packs@7f86098c04ead8cb78706ddc9524cf4cab83b028`, inspected source-only. Implementation and full method behavior have not been executed by this ledger.

## Evidence Commands

```sh
# Offline, with pytest and jsonschema available:
python3 -m pytest graph-engineering/tests -q
# Real installed Gas City CLI and a disposable city are REQUIRED for:
gc lint graph-engineering
gc formula catalog --json
# Use a real host-approved input convoy for native compiler and Bead execution.
```

These are **commands to run**, not receipts. The `graph-engineering/tests/test_methodology_patterns.py` assertions provide a controlled compatibility crosswalk. They do not import `graph-engineering` into the four upstream derived-pack compliance cases. Document any actual result with commit SHA, runner binary version and output before closing #34/#35.

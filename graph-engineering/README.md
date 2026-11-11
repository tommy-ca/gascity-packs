# Graph Engineering — optional native Gas City pack

**Status: draft integration, source/static tests only.** This adds no scheduler, database, provider API, session wrapper, high-authority publisher or automatically approved LLMWiki content. Graph state and work claims remain Gas City Beads/convoys. Use Gas City's own `graph.v2` formula compiler. The pack's `[requires] formula_compiler = ">=2.0.0"` avoids deprecated compiler-mode declaration.

## Installation and existing runtime
In a city which already has an operator-approved rig and `gascity/roles` rig import, opt in with:

```toml
[imports.ge]
source = "/absolute/path/to/gascity-packs/graph-engineering"
```

The local-path example is for development. To use Git import, point to a reviewed pinned commit and subdirectory instead of unpinned `main`; run `gc import install` and confirm `gc formula catalog --json`.

The new formula **requires an existing, approved input convoy**. A bounded deterministic `inspect` preflight checks normalized host target identity and rig-contained goal/artifact paths. It **does not prove owner approval**; that remains an external runtime authorization and release gate. It does not create tasks or choose providers automatically. In a correctly configured rig, use Gas City's native targeted invocation:

```sh
gc sling gc.run-operator <approved-convoy-id> --on graph-long-horizon \
  --var goal_path=plans/example/approved-goal.md \
  --var artifact_root=plans/example/graph-review
```

This is an example, **not** evidence a live city was started. Its default `implementation_target` is `gc.implementation-worker`; the consuming city/rig must configure and authorize this role. No PStack, QStack, model-router or SDK is required.

## Formula shape
```text
approved convoy ─> inspect ─> design ─> native drain(separate, exclusive)
                                             ├─ acceptance-review ┐
                                             ├─ safety-review     ├─ synthesize ─> finalize
                                             └─ continuity-review ┘
```
- `[steps.drain]` is the host primitive, using the already-existing `do-work` child formula and its native bounded implementation check.
- Three reviewers are independent *steps*; separate actual provider/model/session identity is unproved until host execution evidence.
- There is no automatic publish/merge/retry cycle outside host work and check policies. A failed reviewer is not an accepted project. A source-produced report is not independent runtime proof.

## Source and semantics
Read the [OpenSpec proposal](../openspec/changes/2026-11-11-gascity-graph-engineering/proposal.md), [design](../openspec/changes/2026-11-11-gascity-graph-engineering/design.md), [reference schema](schemas/semantic-graph.reference.schema.json), [source census](../openspec/changes/2026-11-11-gascity-graph-engineering/references/source-crosswalk.md) and [feature map](../openspec/changes/2026-11-11-gascity-graph-engineering/references/feature-map.md).

The preflight is an executable safety check on the `inspect` stage, based on the existing Gas City `gc bd show` contract. Its PASS is `INPUT_SANITY_OK` only, never permission to operate or independent reviewer acceptance. Run-mode audit and exact host capability conformance are tracked in issue #34.

For shape/negative checks: `python3 -m pytest graph-engineering/tests/test_graph_engineering_pack.py -q` (requires pytest + jsonschema). For actual runtime and PStack method evidence: read `skills/verify-graph-engineering/SKILL.md`. Static fixture PASS never implies live Gas City formula compilation, session routing, independent review or authorized publication.

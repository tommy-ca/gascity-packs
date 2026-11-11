# Source-pinned Gas City / GasCity Packs crosswalk

| Item / source (pinned) | Observed semantics | Extracted atom and risk |
| --- | --- | --- |
| [GasCity types.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/formula/types.go) | Formula/Step, `needs`, typed vars, `requires` and `contract` | Node, WorkDependency, profile; `contract = graph.v2` deprecated in favor of requirement |
| [compile.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/formula/compile.go) | Resolve→control flow→advice→expansions→condition→retry/controls→recipe | compilation is native host, not pack implementation |
| [requirements.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/formula/requirements.go) | formula compiler >=2.0.0 capability declaration and fail-closed checks | explicit minimum host capability |
| [graph.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/formula/graph.go) | controls created for on_complete, scope-check and workflow-finalize; rewrites fanout prerequisites before scope | fanout convergence is host-owned; avoid synthetic step names |
| [graphv2 invocation.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/graphv2/invocation.go) | target normalization into convoy_id; legacy `issue` deprecated and `bead_id` reserved | no user-supplied reserved vars, no synthetic duplicate convoy |
| [dispatch/drain.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/dispatch/drain.go) | drainManifest, member ID, unit convoy, status, pending/expanded/completing | durable fanout and resume from host store, not file ledger |
| [dispatch/fanout.go](https://github.com/gastownhall/gascity/blob/6bd609f5bfb41f43f444843b1220d0cde4473446/internal/dispatch/fanout.go) | dynamic output items and fanout control minted into host graph | existing capability, but PStack dynamic route proof remains open #21/#28 |
| [base build](https://github.com/gastownhall/gascity-packs/blob/7f86098c04ead8cb78706ddc9524cf4cab83b028/gascity/formulas/build-base.formula.toml) | approval, drain, independent reviews, artifact checks | reuse and keep separate new pack |
| [base do-work](https://github.com/gastownhall/gascity-packs/blob/7f86098c04ead8cb78706ddc9524cf4cab83b028/gascity/formulas/do-work.formula.toml) | per-item worktree/implementation/check source shape | import and reuse, no copy of check scripts |
| [GraphCode](https://github.com/scgopi/GraphCode) | live LoopNode, handoff/message/spawn and CycleGuard | some actions not expressible in native Gas City, do not infer equivalence |
| [longgraph-skill](https://github.com/levi-qiao/longgraph-skill) | executor/supervisor, ledger STATE, directives SIGNAL, cold resume | use Beads as ledger; review artifacts as nonauthoritative signal |

## What is verified?
**STATIC_SOURCE only:** GitHub connector file reads at the pinned head SHA. No real Gas City host run, live provider session, actual GraphCode/longgraph execution, issue-close acceptance or LLMWiki source capture.

## Security/rights
Host root LICENSE observed MIT; packs root license not established by inspected top-level paths and embedded third-party terms remain separately reviewable. Licenses and pinned links do not automatically satisfy independent LLMWiki capture/grant rights. Metadata-only source notices are in `source-notices.held.json`, no raw source retained by the pack.

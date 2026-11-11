---
name: graph-engineering
description: Design or audit long-horizon Gas City graph.v2 work using approved convoys, typed dependencies, durable host state and independent reviewer lanes. Do not use for one-shot edits.
---

# Graph engineering on Gas City

Use the host's **existing** Beads, convoy, graph.v2 formulas, drain, retry, scope, session and review gates. This skill is an authoring/read-only method, not an agent-runtime, scheduler, progress database, publisher or license grant.

## Seven questions before adding an atom
1. Which objective and acceptance criteria are **approved**?
2. Which **Bead/convoy** already owns each work unit, status and dependency?
3. Which graph owns the edge: work DAG (`needs`), control graph (drain/Retry/branch), or evidence DAG (source→attempt→gate→decision)?
4. What triggers the node: host/bead readiness, user command, bounded retry, or existing order?
5. What is the unique writer and allowed write set? Never add a second `ledger.md`.
6. Which independent artifact proves completion after a fresh-context reset?
7. What would falsify the claim, and what bound prevents indefinite work?

## Recomposition
- longgraph: executor → work item/attempt in Beads; supervisor → separate review bead; ledger STATE → existing Bead store; directive SIGNAL → bounded authorized review artifact/handoff, **not** a new source of workflow status; timer → Gas City existing order/trigger only when explicitly configured.
- GraphCode: `LoopNode` → Gas City session-backed routed bead; `handoff` → native `needs`; `message` → host-authorized mail/event (not implicitly present in this pack); `spawn` → native `on_complete` or drain **only when host capability is confirmed**; `CycleGuard` → `[steps.check]` / `[steps.retry]` bounded check where supported. Live terminal/UI steering and session identity have no generic semantic guarantee.
- Gas City: formula = immutable authored recipe; compile = graph.v2; materialization = Beads/convoys; scheduler/claim = host; execution = authorized role; gate = host check + independently reproducible evidence; release = external authority.

## Operation
Use `gc formula catalog --json` to confirm the selected formula is loaded. For approved work convoys, the optional `graph-long-horizon` formula is a *demonstration* of native separate-context drain and three-lane review fan-in, not a producer of live-trust receipts by itself. Require an installed `gascity/roles` rig pack, an operator-approved goal, and an actual target convoy. Do not dispatch if any is absent. Never push/publish by default.

Use `verify-graph-engineering` for source-independent fixture tests. Use real PStack Swarm/Arena/Interrogate and Thermos only with attributable executed-session receipts; otherwise report NOT_RUN.

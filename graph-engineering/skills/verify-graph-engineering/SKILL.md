---
name: verify-graph-engineering
description: Verify the optional graph-engineering pack contracts against actual Gas City host behavior, static negative fixtures, independently attributable evidence and formalized authority boundaries.
---

# Verify graph engineering

## Offline shape/negative test (does not execute the Gas City runtime)
```bash
python3 -m pytest graph-engineering/tests/test_graph_engineering_pack.py -q
```
Record test count, exit code and exact source revision. No claim of native host compile from this command.

## Required host verification
1. Pin a real `gc` binary and commit/version, and loaded pack path. Run `gc lint graph-engineering` and `gc formula catalog --json` in a disposable city. Ensure catalog contains graph-long-horizon and no unexpected doctor findings.
2. Compile `graph-long-horizon` on the **same pinned host** with operator-authored approved input convoy; reject unknown `[requires]` capability, dangling `needs` or unresolved item formula. Do not replace with synthetic TOML-only parsing.
3. Run a disposable convoy with at least two members through native drain; verify separate bead IDs, real sessions, exclusive write scope, input-versus-root identity, retry/cancel/failure and completion gates.
4. Collect exact model/session IDs from the host; worker self-reports and static route metadata are not effective-provider attestation. Reproduce each reviewer lane's claimed test and negative witness.
5. Force a context reset and a stale/missing/duplicate artifact; demonstrate correction and fail-closed acceptance. A predicate-only loop is not a finite runtime bound without host budget/time cap.
6. Run independently recorded Swarm, Arena, Interrogate and both Thermos skills on the exact final commit. Without distinct genuine receipts record NOT_RUN. Store artifacts and source pin; do not generate fictitious success.

## Model-only / formal scenarios
- Duplicate writer, orphan/dangling dependency, directed cycle in work DAG, self-review accepted as independent, out-of-bound attempts, stale revision, missing reviewer and missing evidence must fail.
- Inspect actual `internal/formula/graph.go` fanout rewrite and `internal/dispatch/{drain,fanout}.go` for native ownership; this pack MUST NOT implement those engines.
- A runnable skill or README is not CI evidence. Source-static, offline fixture, pinned-host compiler and real-provider tests are separate evidence classes.

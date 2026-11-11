---
name: formal-verify-graph-engineering
description: Falsify small graph-state and evidence-ownership models for a Gas City graph engineering pack; record that model-only proofs do not certify the native host.
---

# Formal verification — model, not production proof

Use the existing `graph-engineering/tests/test_graph_engineering_pack.py` controlled mutants before adding a new solver, database or runtime. Model check:
1. Every `needs` edge points at an existing unique work node, and the work dependency graph is acyclic.
2. Independent review nodes remain three distinct writer identities and all must precede synthesis.
3. Untrusted reference schema cannot claim trusted `RUNTIME_PASS` or `PUBLISHER` authority.
4. Recovery correctness, atomic Bead claims and bounded cycle execution require tests on the **actual pinned Gas City Go host**; this skill only specifies those falsifiers, not formal proofs of that implementation.
5. Require one *controlled broken variant* that demonstrably fails before claiming a useful verification lever. Record mutant identity, exact source revision, witness, restored passing behavior and evidence artifact; no mutation detection implies INCONCLUSIVE.

Run offline tests with `python3 -m pytest graph-engineering/tests/test_graph_engineering_pack.py -q`. Then carry host acceptance into existing #21/#28 and this pack's #32, without duplication. Real Swarm/Arena/Interrogate and Thermos require observed independent executions, not a prose checklist.

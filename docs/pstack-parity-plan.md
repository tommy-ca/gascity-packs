# PStack Cursor parity plan

City operators get Gas City slings that match Cursor pstack methods without a second runtime. The pack stays a mapping pack. It does not stamp `gc.provider_panel` until a Gas City consumer of `gc.provider_panel` exists. PR order is how-schema, method-report, how-expand, panel-stamp.

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Each PR/task section also has a unique parenthesized identifier and a `Depends on.` list that names direct parents or `None.`. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `skills/poteto-mode/playbooks/autopilot-stack.md`. The operator lands every PR. The root stops at merge-ready.

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on her explicit go.
- [ ] On her go, write this exact text into the standing orders and persist it on disk. "docs/pstack-parity-plan.md, PR ids how-schema method-report how-expand panel-stamp, verification rule, operator lands, done when dest levers stay green and panel keys stay omitted until a Gas City consumer of gc.provider_panel exists."
- [ ] Read these from the installed plugin at program start. Re-read them at every tick.
  - [ ] `git show origin/main:skills/poteto-mode/playbooks/autopilot-stack.md`
  - [ ] `git show origin/main:skills/swarm/SKILL.md`
  - [ ] `git show origin/main:pstack/scripts/check_pstack_delivery_evidence.py`
  - [ ] `git show origin/main:skills/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:skills/how/SKILL.md`
- [ ] Arm the 30-minute audit tick with `scheduler_create` (`interval: "30m"`, `fire_immediately: true`) and `monitor` for event wakes. Never leave the cadence to memory.
- [ ] Use this tick prompt, verbatim. "Re-read the execution playbook from trunk and the persisted plan. Audit the operation against both and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then send the operator a status message, whether or not anything changed, with the queue table of PR, owner, state, and head SHA, the verdicts since the last tick, what merged, open operator gates, and blockers."
- [ ] On the operator's hold or stand-down, send every owner a zero-writes order at once.

### Spawn owners

- [ ] From this parent session, spawn one owner per PR with `spawn_subagent` (`isolation: "worktree"`). Depth is 1. Owners do not spawn.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] how-schema and method-report are independent and first. Both branch from `feat/pstack-pack-honesty`.
  - [ ] how-expand after how-schema.
  - [ ] panel-stamp after how-schema. It waits on a Gas City consumer of `gc.provider_panel` before formula keys.
- [ ] Hold the file boundaries. All PR ids touch only `pstack/`, `docs/pstack-*`, `openspec/specs/pstack-*`, `scripts/check_pstack_*`, `scripts/pstack_*`, and `tests/test_pstack_*`. They do not edit `.github/` or `gascity/`.
- [ ] Hold the review gate. how-expand and panel-stamp change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Resolve the forge once. Default to `gh`; if `command -v origin` succeeds and Origin can resolve the repository, use `origin pr` for every PR operation. Record any fallback to `gh`. Never require `gt`.
- [ ] Open the PR ready, never draft, with `origin pr create --status open --base <parent-branch>` or `gh pr create --base <parent-branch>` according to the resolved forge. A stack child targets its parent branch.
- [ ] Run `/unslop` before each commit and `/no-comments` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before babysit and again before the merge-ready report.

### Verdict and merge, for every PR

- [ ] At the merge-ready head SHA, run the swarm per `skills/swarm/SKILL.md`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. One audit lane that reads the diff and the receipts and distrusts the PR body.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner. A new head gets a fresh swarm and a fresh verdict.
- [ ] The root appends the PR to the base-branch stack. The operator lands it bottom-up.

### Boot recipe, for every live lane

Each live lane runs in its own `isolation: "worktree"` child at the PR head. Drive the real surface (running app, CLI, tests, or Grok browser tools).

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] Run dest levers from the worktree root. Wait for `ok dest standing`.
- [ ] Deliver the lane command on that CLI. Name the read-only diagnostics.
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report.

## Retarget how evidence schema (how-schema)

**Depends on.** None.

**Files.**

- [ ] Create `pstack/schemas/explanation.v1.yaml`.
- [ ] Edit `pstack/formulas/pstack-how.formula.toml`.
- [ ] Edit `openspec/specs/pstack-gascity-pack/spec.md`.
- [ ] Edit `pstack/tests/test_pstack_pack.py`.
- [ ] Edit `scripts/check_pstack_dest_standing.py` if dest remaining-units names the schema.

**Build.**

- [ ] Stamp `pstack-how` write as `pstack.explanation.v1` in `pstack/formulas/pstack-how.formula.toml`.

**You see.**

- [ ] `pstack-how` write metadata names `pstack.explanation.v1` and not `pstack.decision.v1`.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] `pstack/tests/test_pstack_pack.py` locks how schema. Run `mise exec npm:@fission-ai/openspec@1.12.0 -- uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on the configured `swarm workers` model at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run dest standing at trunk and head. If trunk lacks explanation.v1, record that and gate how formula schema plus dest standing still ok. Save `how-schema-l1.png`. Pass when dest standing prints ok dest standing.
- [ ] Lane 2. Delivery evidence at head. Save `how-schema-l2.png`. Pass when output includes ok delivery evidence.
- [ ] Lane 3. Grep how formula for decision.v1. Save `how-schema-l3.png`. Pass when grep is empty.
- [ ] Lane 4. Grep how formula for explanation.v1. Save `how-schema-l4.png`. Pass when grep hits write metadata.
- [ ] Lane 5. Omit-panel still holds. Save `how-schema-l5.png`. Pass when delivery evidence prints ok omit-panel.
- [ ] Lane 6. Pack name still tommy-ca/pstack. Save `how-schema-l6.png`. Pass when delivery evidence prints ok pack-name.
- [ ] Lane 7. Pin still 29c84db. Save `how-schema-l7.png`. Pass when delivery evidence prints ok pin.
- [ ] Lane 8. OpenSpec validate specs. Save `how-schema-l8.png`. Pass when validate --specs --strict exits 0.
- [ ] Lane 9. No gc.provider_panel in formulas. Save `how-schema-l9.png`. Pass when rg is empty.
- [ ] Lane 10. Pack tests 52 or more pass. Save `how-schema-l10.png`. Pass when pytest reports passed.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Wall time of dest standing plus delivery evidence at trunk and head.
- [ ] Probe. `/usr/bin/time -f %e python scripts/check_pstack_dest_standing.py` then delivery evidence, run at trunk and at the head, interleaved. Both sides must produce the metric.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head under 2x trunk. If the scenarios differ, fail if dest standing exceeds 5s.

**Review gate.** None.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] The root appends it to the base-branch stack and the operator lands it bottom-up.

## Fold method-report clones (method-report)

**Depends on.** None.

**Files.**

- [ ] Edit `pstack/formulas/` method-report clones.
- [ ] Edit `pstack/mappings/playbooks.toml`.
- [ ] Edit `pstack/tests/test_pstack_pack.py`.
- [ ] Keep formula count at or above 28.

**Build.**

- [ ] Delete empty aliases `pstack-perf-issue`, `pstack-refactoring`, and `pstack-shipping`. Fold remaining collect/write reports into `pstack-method-report` keyed by `pstack.playbook`.

**You see.**

- [ ] `ls pstack/formulas/*.formula.toml | wc -l` stays at or above 28 and the alias files are gone.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] `test_pstack_pack.py` formula floor. Run the pack pytest file.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on the configured `swarm workers` model at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run dest standing at trunk and head. If trunk still has aliases, record that and gate alias absence plus dest standing ok. Save `method-report-l1.png`. Pass when dest standing prints ok dest standing.
- [ ] Lane 2. Delivery evidence. Save `method-report-l2.png`. Pass when output includes ok delivery evidence.
- [ ] Lane 3. Alias pstack-shipping gone. Save `method-report-l3.png`. Pass when the file is missing.
- [ ] Lane 4. Alias pstack-perf-issue gone. Save `method-report-l4.png`. Pass when the file is missing.
- [ ] Lane 5. Formula count at or above 28. Save `method-report-l5.png`. Pass when wc -l is at least 28.
- [ ] Lane 6. playbooks.toml still maps every vendored playbook or names unsupported. Save `method-report-l6.png`. Pass when pack tests pass.
- [ ] Lane 7. Omit-panel. Save `method-report-l7.png`. Pass when ok omit-panel.
- [ ] Lane 8. Pack name. Save `method-report-l8.png`. Pass when ok pack-name.
- [ ] Lane 9. Pin. Save `method-report-l9.png`. Pass when ok pin.
- [ ] Lane 10. Pytest. Save `method-report-l10.png`. Pass when pytest reports passed.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Pack pytest wall time at trunk and head.
- [ ] Probe. pytest -q pstack/tests/test_pstack_pack.py at trunk and head, interleaved. Both sides must produce the metric.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head under 2x trunk.

**Review gate.** None.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] The root appends it to the base-branch stack and the operator lands it bottom-up.

## Expand how and why as personas (how-expand)

**Depends on.** how-schema

**Files.**

- [ ] Edit `pstack/formulas/pstack-how.formula.toml`.
- [ ] Edit `pstack/formulas/pstack-why.formula.toml`.
- [ ] Create expansion assets under `pstack/assets/workflows/`.
- [ ] Edit dest Gherkin that today locks sequential investigator collect/write.
- [ ] Edit `pstack/tests/test_pstack_pack.py`.

**Build.**

- [ ] Replace how and why two-step investigator graphs with `type = "expansion"` persona lanes on existing agents. Do not stamp `gc.provider_panel`.

**You see.**

- [ ] `pstack-how` has `type = "expansion"` and no `gc.provider_panel`.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Pack tests lock expansion without panel keys. Run pack pytest.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on the configured `swarm workers` model at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run dest standing at trunk and head. If trunk is sequential how, record that and gate expansion plus dest standing ok. Save `how-expand-l1.png`. Pass when dest standing prints ok dest standing.
- [ ] Lane 2. Delivery evidence. Save `how-expand-l2.png`. Pass when ok delivery evidence.
- [ ] Lane 3. how formula type expansion. Save `how-expand-l3.png`. Pass when type = "expansion" is in the file.
- [ ] Lane 4. No provider_panel. Save `how-expand-l4.png`. Pass when rg is empty.
- [ ] Lane 5. why expansion. Save `how-expand-l5.png`. Pass when pstack-why has type = "expansion".
- [ ] Lane 6. architect stays sequential until its own leftover. Save `how-expand-l6.png`. Pass when pstack-architect still has collect and write.
- [ ] Lane 7. Omit-panel. Save `how-expand-l7.png`. Pass when ok omit-panel.
- [ ] Lane 8. Pack name. Save `how-expand-l8.png`. Pass when ok pack-name.
- [ ] Lane 9. Pin. Save `how-expand-l9.png`. Pass when ok pin.
- [ ] Lane 10. Pytest. Save `how-expand-l10.png`. Pass when pytest reports passed.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Dest standing wall time at trunk and head.
- [ ] Probe. python scripts/check_pstack_dest_standing.py at trunk and head, interleaved. Both sides must produce the metric.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head under 2x trunk.

**Review gate.** The operator reviews before merge.

- [ ] Copy lane 3 screenshots into `/tmp/media/how-expand-review-type.png`.
- [ ] Record a 30 to 60 second video of the change on the worktree child's real surface. Save it as `/tmp/media/how-expand-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] The root appends it to the base-branch stack and the operator lands it bottom-up.

## Stamp provider panel after panel consumer (panel-stamp)

**Depends on.** how-schema

**Files.**

- [ ] Edit `pstack/formulas/pstack-arena.formula.toml`.
- [ ] Edit `pstack/formulas/pstack-interrogate.formula.toml`.
- [ ] Edit `pstack/formulas/pstack-swarm.formula.toml`.
- [ ] Edit dest remaining-units omit-panel sentences in the same wave as the stamp.
- [ ] Edit dest standing and delivery evidence omit-panel FilePred.

**Build.**

- [ ] Stamp `gc.provider_panel` and `gc.child_artifact_path_template` only after a Gas City consumer of `gc.provider_panel` exists. Delete shared `.gc/pstack/arena-candidate.md` in the same wave.

**You see.**

- [ ] Arena children write distinct paths and dest omit-panel is inverted only after a Gas City consumer of `gc.provider_panel` exists.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Pack tests lock panel keys only when dest invert lands. Run pack pytest.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on the configured `swarm workers` model at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run dest standing at trunk and head. If trunk omits panel, record that and gate consumer evidence plus dest standing. Save `panel-stamp-l1.png`. Pass when dest standing prints ok dest standing.
- [ ] Lane 2. Delivery evidence. Save `panel-stamp-l2.png`. Pass when ok delivery evidence.
- [ ] Lane 3. Gas City consumer of `gc.provider_panel` documented. Save `panel-stamp-l3.png`. Pass when the PR body names the Gas City SHA that consumes the key.
- [ ] Lane 4. Shared arena-candidate.md gone. Save `panel-stamp-l4.png`. Pass when that path is not in formulas.
- [ ] Lane 5. child_artifact_path_template present. Save `panel-stamp-l5.png`. Pass when rg hits arena formula.
- [ ] Lane 6. gascity/ still has no panel unless a Gas City consumer of `gc.provider_panel` landed there out of tree. Save `panel-stamp-l6.png`. Pass when this packs tree matches dest.
- [ ] Lane 7. Pack name. Save `panel-stamp-l7.png`. Pass when ok pack-name.
- [ ] Lane 8. Pin unchanged. Save `panel-stamp-l8.png`. Pass when ok pin.
- [ ] Lane 9. No restamp. Save `panel-stamp-l9.png`. Pass when registry pin is 29c84db.
- [ ] Lane 10. Pytest. Save `panel-stamp-l10.png`. Pass when pytest reports passed.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Dest standing wall time at trunk and head.
- [ ] Probe. python scripts/check_pstack_dest_standing.py at trunk and head, interleaved. Both sides must produce the metric.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head under 2x trunk.

**Review gate.** The operator reviews before merge.

- [ ] Copy lane 3 screenshots into `/tmp/media/panel-stamp-review-consumer.png`.
- [ ] Record a 30 to 60 second video of the change on the worktree child's real surface. Save it as `/tmp/media/panel-stamp-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] The root appends it to the base-branch stack and the operator lands it bottom-up.

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

No new prototype ran in this leftover. Prior arena on PR #1 scored sequential collapse 15, expansion fidelity 15, thinner wrap 14. Lead pick for HEAD dest is sequential mapping. how-expand is the later leftover. Panel stamp stays blocked until a Gas City consumer of `gc.provider_panel` exists. Unproven is a live Gas City cook of `gc.provider_panel`.

## Appendix B. Alternatives rejected

Full Cursor N-model in formula TOML lost. Fake N-model with extra run_targets and city patches lost. Stamp from Gherkin alone lost. Thinner wrap that deletes how/why/architect slings lost. Restamp of pin 29c84db lost. Edits to gastownhall CI lost.

## Appendix C. Risks

Identity split (pack name tommy-ca/pstack vs catalog pstack) stays dest. Check may fail validate_registry --require-git. Owner watches that job and does not restamp. Blacksmith queue cancelled PR #1 Check after 24h. Owner watches runner pickup. how-expand changes dest sequential lock. Owner waits for operator review.

## Appendix D. Links and reading list

Read `pstack/ARCHITECTURE.md`, `openspec/specs/gascity-provider-panel/spec.md`, `openspec/specs/pstack-gascity-pack/spec.md`, `docs/pstack-program-plan.md`. how-expand and panel-stamp get `skills/how/SKILL.md` and `skills/interrogate/SKILL.md`. Trail is local `.audit/pstack-parity.tsv` per `skills/show-me-your-work/SKILL.md`. Issue https://github.com/tommy-ca/gascity-packs/issues/10 is why-schema honesty after how-schema. It is not a fifth program PR.

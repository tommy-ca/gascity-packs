# PStack program plan

A city operator needs pstack as a sequential Gas City factory today and N-model arena later without pack Task spawn. Isolation is on branch `feat/pstack-pack-honesty`. It is not landed on gastownhall main. gastownhall PR 385 is closed unmerged. Do not reopen it. Maintain remote tommy. Host sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route. Hosted publish waits on sling receipts of `pstack-poteto-mode` and `pstack-build`. Operator publication dest is https://registry.gascity.com. Restamp of gastownhall registry.toml is not the publication vehicle. This change does not publish, restamp hashes, or stamp panel keys. The live graph is this file.

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The execution playbook is `skills/poteto-mode/playbooks/orchestrate.md`. That playbook is the standing fork plus registry program. The operator maintains the tommy fork and publishes. Owners do not merge to gastownhall. The operator lands nothing on origin.

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on her explicit go.
- [ ] On her go, persist the plan path on disk with this exact text. "docs/pstack-program-plan.md. PR ids pr-pstack-land-honesty then pr-pstack-publish then pr-pstack-panel-stamp. Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. The operator publishes via gc pack registry publish after sling. Isolation is already on feat/pstack-pack-honesty. Done when host sling receipts exist, hosted publish is queued or shown, and formulas still omit gc.provider_panel until the compiler consumer exists."
- [ ] Read these from trunk at program start. Re-read them at every tick.
  - [ ] `git show origin/main:.github/workflows/ci.yml`
  - [ ] `git show origin/main:registry.toml`
  - [ ] `git show origin/main:README.md`
  - [ ] `git show origin/main:gascity/pack.toml`
  - [ ] `git show origin/main:bmad/pack.toml`
  - [ ] `git show origin/main:gascity/REQUIREMENTS.md`
  - [ ] `git show origin/main:validate_registry.py`
- [ ] Arm the 30-minute audit tick with `scheduler_create` (`interval: "30m"`, `fire_immediately: true`) and `monitor` for event wakes. Never leave the cadence to memory.
- [ ] Use this tick prompt, verbatim. "Re-read docs/pstack-program-plan.md. The execution playbook is the host plugin skills/poteto-mode/playbooks/orchestrate.md, not a path on this origin/main. Audit the operation against both and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then send the operator a status message, whether or not anything changed, with the queue table of PR, owner, state, and head SHA, the verdicts since the last tick, what merged, open operator gates, and blockers."
- [ ] On the operator's hold or stand-down, send every owner a zero-writes order at once.

### Spawn owners

- [ ] From this parent session, spawn one owner per PR with `spawn_subagent` (`isolation: "worktree"`). Depth is 1. Owners do not spawn.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] `pr-pstack-land-honesty` first. Branch `feat/pstack-pack-honesty`. gastownhall PR 385 is closed unmerged. Do not reopen it.
  - [ ] `pr-pstack-graph-honesty` after isolation is on `feat/pstack-pack-honesty`. Docs and OpenSpec only. Parallel with host sling.
  - [ ] Maintain remote tommy. Push isolation to remote `tommy` (`tommy-ca/gascity-packs`). Not origin. Not reopen 385.
  - [x] While gastownhall does not accept PRs, tommy `main` is a fast-forward of `feat/pstack-pack-honesty`. Not a gastownhall merge.
  - [x] Host sling of `pstack-poteto-mode` and `pstack-build` after isolation is on `feat/pstack-pack-honesty`. Not a GitHub PR.
  - [x] Host sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route.
  - [ ] Do not restamp registry.toml commit or hash even after sling receipts. Ghost-pin CI is not a restamp trigger.
  - [x] Hosted publish waits on sling receipts of `pstack-poteto-mode` and `pstack-build`.
  - [ ] Restamp of gastownhall registry.toml is not the publication vehicle.
  - [ ] After receipts, `pr-pstack-publish` waits on the scoped-name unit. Unscoped submit is not the next click.
  - [ ] Gas City compiler consumer for `gc.provider_panel`. Outside this packs formula tree.
  - [ ] `pr-pstack-panel-stamp` after that consumer exists.
- [ ] Hold the file boundaries. `pr-pstack-land-honesty` must not touch `pstack/formulas`, `pstack/schemas`, or `registry.toml`. `pr-pstack-graph-honesty` touches TRACEABILITY Gherkin, `pstack/TRACEABILITY.md`, `pstack/README.md`, pack tests, and Appendix A. It must not touch `pstack/formulas`, `pstack/schemas`, or `registry.toml`. `pr-pstack-publish` must not rename `pstack/pack.toml` in this honesty change. `pr-pstack-panel-stamp` touches formulas, schemas, and tests.
- [ ] Hold the review gate. `pr-pstack-land-honesty` changes no interaction. It is not review-gated. `pr-pstack-graph-honesty` changes no interaction. It is not review-gated. `pr-pstack-publish` talks to the hosted registry. It is review-gated. `pr-pstack-panel-stamp` changes sling behavior. It is review-gated.

### PR mechanics, for every PR

- [ ] Open the PR ready, never draft, with `gh pr create` and `draft: false`, or with Graphite `gt` for a stack.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Run `/unslop` before each commit and `/no-comments` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before babysit and again before the merge-ready report.

### Verdict and merge, for every PR

- [ ] At the merge-ready head SHA, run the swarm per `skills/swarm/SKILL.md`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. One audit lane that reads the diff and the receipts and distrusts the PR body.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner. A new head gets a fresh swarm and a fresh verdict.
- [ ] Root does not merge to gastownhall. The operator lands nothing on origin. Owners do not merge.

### Boot recipe, for every live lane

Each live lane runs in its own `isolation: "worktree"` child at the PR head. Drive the real surface (running app, CLI, tests, or Grok browser tools).

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] Use the repo CLI. `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`. `python pstack/scripts/apply_intent_change.py --source openspec/changes/archive/2026-09-02-pstack-mapping-gaps --validate-only`.
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report.

## Land isolation and OpenSpec (`pr-pstack-land-honesty`)

**Depends on.** None.

**Files.**

- [ ] Edit `pstack/DESIGN.md`.
- [ ] Edit `pstack/ARCHITECTURE.md`.
- [ ] Edit `pstack/REQUIREMENTS.md`.
- [ ] Edit `pstack/TRACEABILITY.md`.
- [ ] Edit `pstack/README.md`.
- [ ] Edit `pstack/scripts/apply_intent_change.py`.
- [ ] Edit `pstack/tests/test_pstack_pack.py`.
- [ ] Keep `openspec/specs/` as durable Gherkin.
- [ ] Create `docs/pstack-program-plan.md`.
- [ ] Point `docs/pstack-production-readiness-plan.md` at this file.
- [ ] Point `docs/pstack-provider-panel-plan.md` at this file.
- [ ] Point `docs/pstack-gascity-pack-apply-plan.md` at this file.
- [ ] Point `docs/pstack-poteto-mode-router-plan.md` at this file.
- [ ] Keep `openspec/` in the land commit.

**Build.**

- [x] Commit isolation, filled panel Purpose, `openspec/` including archived `pstack-gherkin-restamp`, and this plan on `feat/pstack-pack-honesty` at `2f65f7b`. Do not stamp `gc.provider_panel`. Do not restamp `registry.toml` in this box.

**You see.**

- [ ] `rg gc.provider_panel pstack/formulas` prints nothing. `pytest -q pstack/tests/test_pstack_pack.py` prints `50 passed`. `openspec/specs/gascity-provider-panel/spec.md` has no TBD.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] `pstack/tests/test_pstack_pack.py` locks spec files and isolation. Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `grok-4.6` at the PR head, per the boot recipe.

- [ ] Lane 1. Read DESIGN Provider panel fanout. Save `design-panel.png`. Pass when the section names `[[provider_panels]]` and forbids stamping before a consumer.
- [ ] Lane 2. Grep formulas for `gc.provider_panel`. Save `no-stamp.png`. Pass when the grep is empty.
- [ ] Lane 3. Run pack tests. Save `pytest.png`. Pass when the log shows 50 passed.
- [ ] Lane 4. Read `openspec/specs/gascity-provider-panel/spec.md`. Save `panel-purpose.png`. Pass when Purpose is not TBD.
- [ ] Lane 5. Grep TRACEABILITY for another project checkout. Save `no-foreign-openspec.png`. Pass when the grep is empty.
- [ ] Lane 6. Confirm this plan has no gitignored payload path. Save `plan-clean.png`. Pass when no gitignored OpenSpec payload path appears.
- [ ] Lane 7. Confirm old plan files point here. Save `pointers.png`. Pass when each old H1 file names `docs/pstack-program-plan.md`.
- [ ] Lane 8. Read `openspec/specs/pstack-gascity-pack/spec.md` vendor rule. Save `gherkin-owner.png`. Pass when durable Gherkin is this repository `openspec/`.
- [ ] Lane 9. Confirm `pstack-arena.formula.toml` catalog is sequential. Save `arena-catalog.png`. Pass when the catalog line names sequential steps.
- [ ] Lane 10. Confirm `gascity/` has zero `graph_operator` hits. Save `no-consumer.png`. Pass when that grep is empty.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Wall time of `pstack/tests/test_pstack_pack.py`.
- [ ] Probe. `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py` at trunk then at the head, interleaved.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head fails if it is more than twice the trunk seconds.

**Review gate.** None. `pr-pstack-land-honesty` is not review-gated.

**Merge.**

- [ ] Isolation is already on `feat/pstack-pack-honesty`.
- [ ] Do not merge to gastownhall.
- [ ] Do not reopen gastownhall PR 385.
- [ ] Maintain remote tommy.

## Align TRACEABILITY recursive graph (`pr-pstack-graph-honesty`)

**Depends on.** Isolation on `feat/pstack-pack-honesty`.

**Files.**

- [x] Create `openspec/changes/archive/2026-09-03-pstack-graph-honesty/proposal.md`.
- [x] Create `openspec/changes/archive/2026-09-03-pstack-graph-honesty/specs/pstack-delivery-evidence/spec.md`.
- [x] Create `openspec/changes/archive/2026-09-03-pstack-graph-honesty/design.md`.
- [x] Create `openspec/changes/archive/2026-09-03-pstack-graph-honesty/adr.md`.
- [x] Create `openspec/changes/archive/2026-09-03-pstack-graph-honesty/tasks.md`.
- [x] Edit `pstack/TRACEABILITY.md`.
- [x] Edit `pstack/README.md`.
- [x] Edit `pstack/tests/test_pstack_pack.py`.
- [x] Edit `docs/pstack-program-plan.md` Appendix A.

**Build.**

- [x] Author intent-driven artifacts under `openspec/changes/2026-09-03-pstack-graph-honesty/`. Archived on operator go.

**You see.**

- [x] The TRACEABILITY recursive-graph scenario names `pr-pstack-land-honesty` then `pr-pstack-publish` then `pr-pstack-panel-stamp`.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [x] Pack tests lock the three-id sequence in the TRACEABILITY requirement. Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `grok-4.6` at the PR head, per the boot recipe.

- [ ] Lane 1. Validate the new change. Save `graph-honesty-validate.png`. Pass when `python pstack/scripts/apply_intent_change.py --source openspec/changes/2026-09-03-pstack-graph-honesty --validate-only` prints `Change 'pstack-graph-honesty' is valid`.
- [ ] Lane 2. Confirm mapping-gaps still validates. Save `mapping-gaps.png`. Pass when mapping-gaps validate-only exits 0.
- [ ] Lane 3. Read the recursive-graph scenario. Save `three-ids.png`. Pass when the delta names publish between land-honesty and panel-stamp.
- [ ] Lane 4. Grep formulas for `gc.provider_panel`. Save `no-panel-honesty.png`. Pass when the grep is empty.
- [ ] Lane 5. Confirm `registry.toml` pin is unchanged. Save `pin-unchanged.png`. Pass when commit is `29c84db` and hash is `sha256:89aee457`.
- [ ] Lane 6. Confirm gastownhall PR 385 stays closed. Save `no-385-honesty.png`. Pass when that PR is not reopened.
- [ ] Lane 7. Confirm pack name is still `pstack`. Save `pack-name-honesty.png`. Pass when `pstack/pack.toml` `[pack] name` is `pstack`.
- [ ] Lane 8. Confirm remaining-units still names hosted dest. Save `hosted-dest-honesty.png`. Pass when remaining-units still names `gc pack registry publish`.
- [ ] Lane 9. Confirm host `check-plan.mjs` is still the live checker. Save `host-checker.png`. Pass when host plugin `check-plan.mjs` prints `0 problems`.
- [ ] Lane 10. Confirm the change is archived. Save `archived.png`. Pass when `openspec/changes/archive/2026-09-03-pstack-graph-honesty/` exists and no live `openspec/changes/2026-09-03-pstack-graph-honesty/` dir remains.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Wall time of `pstack/tests/test_pstack_pack.py`.
- [ ] Probe. `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py` at trunk then at the head, interleaved.
- [ ] Baseline. Record the trunk seconds first.
- [ ] Rule. Head fails if it is more than twice the trunk seconds.

**Review gate.** None. `pr-pstack-graph-honesty` is not review-gated.

**Merge.**

- [ ] Isolation stays on `feat/pstack-pack-honesty`.
- [ ] Do not merge to gastownhall.
- [ ] Do not reopen gastownhall PR 385.
- [ ] Maintain remote tommy.

## Publish pstack to hosted Registry (`pr-pstack-publish`)

**Depends on.** Host sling receipts of `pstack-poteto-mode` and `pstack-build`.

**Files.**

- [ ] Later scoped-name unit may edit `pstack/pack.toml` and pack tests.
- [ ] This honesty change must not rename `pstack/pack.toml`.

**Build.**

- [ ] Do not run `gc pack registry publish` in this honesty change.

**You see.**

- [x] `gc pack registry publish --dry-run` exited 0 against pack path `pstack/`. Submit was not sent.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Pack tests lock `pr-pstack-publish` and refuse restamp as the publication vehicle. Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `grok-4.6` at the PR head, per the boot recipe.

- [x] Lane 1. Confirm host sling receipts of both formulas. Save `sling-receipts.png`. Pass when cook and route receipts exist for `pstack-poteto-mode` and `pstack-build`.
- [x] Lane 2. Confirm isolation is on remote `tommy`. Save `tommy-push.png`. Pass when `tommy/feat/pstack-pack-honesty` contains isolation.
- [x] Lane 3. Dry-run hosted publish. Save `publish-dry-run.png`. Pass when `gc pack registry publish --dry-run` exits 0 against pack path `pstack/`.
- [x] Lane 4. Confirm pack name is still `pstack`. Save `pack-name.png`. Pass when `pstack/pack.toml` `[pack] name` is `pstack`.
- [x] Lane 5. Confirm `registry.toml` pin is unchanged in this honesty change. Save `no-restamp.png`. Pass when `commit` and `hash` match the parent blob.
- [x] Lane 6. Confirm gastownhall PR 385 stays closed. Save `no-385.png`. Pass when that PR is not reopened.
- [x] Lane 7. Grep formulas for `gc.provider_panel`. Save `no-panel.png`. Pass when the grep is empty.
- [x] Lane 8. Confirm `validate_registry.py` still names gastownhall. Save `canonical-repo.png`. Pass when `CANONICAL_REPO` is unchanged.
- [x] Lane 9. Confirm dest is registry.gascity.com. Save `hosted-dest.png`. Pass when publish targets registry.gascity.com.
- [x] Lane 10. Confirm registry login and pushed HEAD. Save `registry-login.png`. Pass when the operator is logged in and HEAD is on remote `tommy`.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Wall time of `gc pack registry publish --dry-run` for pack path `pstack/`.
- [ ] Probe. Run that dry-run at the head after sling receipts exist.
- [ ] Baseline. Record the dry-run seconds first.
- [ ] Rule. Head fails if dry-run is more than twice the recorded seconds without an accepted cost note.

**Review gate.** The operator reviews before publish. Publish is an interaction with the registry.

- [ ] Copy lane 3 screenshots into `<media path>/pr-pstack-publish-review-dry-run.png`.
- [ ] Record a 30 to 60 second video of the dry-run on the worktree child's real surface. Save it as `<media path>/pr-pstack-publish-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Operator publishes after the scoped-name unit. Unscoped `gc pack registry publish pstack` is not this honesty tick.
- [ ] Do not merge to gastownhall.
- [ ] Do not restamp gastownhall `registry.toml` as the publication vehicle.

## Stamp panel keys after the consumer (`pr-pstack-panel-stamp`)

**Depends on.** `pr-pstack-publish`. Gas City compiler consumer for `gc.provider_panel`.

**Files.**

- [ ] Edit `pstack/formulas/pstack-arena.formula.toml`.
- [ ] Edit `pstack/formulas/pstack-interrogate.formula.toml`.
- [ ] Edit `pstack/schemas/arena-candidate.v1.yaml` or add per-child path bindings.
- [ ] Edit `pstack/tests/test_pstack_pack.py`.

**Build.**

- [ ] Stamp `gc.provider_panel` and `{child_id}` paths only after Gas City documents a compiler consumer. Delete the shared `.gc/pstack/arena-candidate.md` binding in the same wave.

**You see.**

- [ ] `gc sling ... --on pstack-arena` in a city with a three-member panel writes three candidate files under `.gc/pstack/arena/`.

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Replace graph_operator freeze tests for arena and interrogate with panel-stamp tests. Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `grok-4.6` at the PR head, per the boot recipe.

- [ ] Lane 1. City with a three-member `pstack-arena` panel. Save `arena-n3.png`. Pass when three candidate files exist.
- [ ] Lane 2. City with no panel. Save `arena-fallback.png`. Pass when the sling stays one candidate bead.
- [ ] Lane 3. City with the session provider in members. Save `session-reject.png`. Pass when cook fails closed.
- [ ] Lane 4. Interrogate with two members. Save `interrogate-n2.png`. Pass when two review files exist and judgment has a path gate.
- [ ] Lane 5. Confirm no apply-findings child on interrogate. Save `no-apply.png`. Pass when the cooked graph has no apply node.
- [ ] Lane 6. Confirm pack TOML has no provider id strings. Save `no-provider-ids.png`. Pass when grep of formulas for `cursor-grok` is empty.
- [ ] Lane 7. Confirm isolated paths. Save `isolated.png`. Pass when two children do not share `arena-candidate.md`.
- [ ] Lane 8. Judge after candidates. Save `judge-order.png`. Pass when synthesis `needs` the child ids.
- [ ] Lane 9. Disposable city import lists `pstack-arena`. Save `formula-list.png`. Pass when `gc formula list` names it.
- [ ] Lane 10. Dual corpus. Save `skill-vs-asset.png`. Pass when formula `description_file` still wins over `pstack/skills/arena/SKILL.md`.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. Cook time for `pstack-arena` with four panel members versus sequential fallback.
- [ ] Probe. `gc formula show pstack-arena` at trunk then at the head.
- [ ] Baseline. Record the sequential cook time first.
- [ ] Rule. Head fails if four-member cook is more than ten times sequential cook without an accepted cost note in DESIGN.md.

**Review gate.** The operator reviews before merge.

- [ ] Copy lane 1 screenshots into `<media path>/pr-pstack-panel-stamp-review-arena-n3.png`.
- [ ] Record a 30 to 60 second video of the sling on the worktree child's real surface. Save it as `<media path>/pr-pstack-panel-stamp-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Do not merge to gastownhall.
- [ ] Stamp only after the compiler consumer exists.
- [ ] Formulas stay unstamped until that consumer exists.

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

Isolation lives on `feat/pstack-pack-honesty`. Fork default tommy `main` fast-forwards that branch while gastownhall does not accept PRs. gastownhall PR 385 is closed unmerged. Inference-gate `--setup-only` printed `setup-only gate passed for pstack`. After `bd init`, `gc formula cook pstack-build --attach de-a5l` failed with unknown formulas v2 target `gc.run-operator` in a city that lacked roles. `scripts/pstack_host_sling_proof.py` then cooked and routed both formulas in a disposable roles city. Poteto root `fi-06k`. Build root `fi-awr`. Both `gc.routed_to` values were `fixture/gc.run-operator`. Full drain was not waited. Host sling of `pstack-poteto-mode` and `pstack-build` is proven as cook plus route. `gc pack registry publish --dry-run pstack/` exited 0. Registry `https://registry.gascity.com`. Repository `https://github.com/tommy-ca/gascity-packs`. Pack `pstack` `0.1.0`. Submit was not sent. `gc pack registry whoami` succeeds as `@tommy-ca`. Dry-run is not registry acceptance. Unscoped hosted submit from tommy waits on the scoped-name unit. Sibling packs ship by landing on gastownhall `main` and stamping `registry.toml`. pstack cannot. Pack-release-compatibility would fetch gastownhall `tree/main/pstack` at pin `29c84db`, which is not on `origin/main`. Pin still `29c84db` / `sha256:89aee457`. Do not restamp it. Restamp of gastownhall registry.toml is not the publication vehicle. Panel stamp remains verified-unproven. Formulas omit `gc.provider_panel`. Dest is remote tommy plus registry.gascity.com.

## Appendix B. Alternatives rejected

Merge isolation to gastownhall. Lost.

Catalog restamp of gastownhall `registry.toml` as the publication vehicle. Lost.

A third GitHub PR for restamp. Already lost.

A new remaining-units delta just to write sling again. Lost. Remaining-units already names sling, publish, compiler, and panel stamp.

Treat inference-gate `pstack-review` then `pstack-build` launch as remaining-units sling. Lost. Arena base is cook plus route of `pstack-poteto-mode` then `pstack-build`.

Rewrite the live checker to pack-vendor `grok-4.6-fast-xhigh`. Lost. Host plugin `check-plan.mjs` is the live checker.

## Appendix C. Risks

`origin/main` still lacks `pstack/`. Arm boxes read files that exist on trunk today. Watch pstack landing in `pr-pstack-land-honesty`.

Gas City compiler is outside this packs tree. `pr-pstack-panel-stamp` must not start on Gherkin alone.

Dual corpus. `pstack/skills/arena/SKILL.md` still documents Cursor Task. Host plugin `check-plan.mjs` is the live checker. Pack vendor `check-plan.mjs` is a second corpus. Watch that in stamp lane 10.

Scoped name is a later unit. `pstack/pack.toml` stays unscoped `pstack` in this honesty change.

Hosted publish of unscoped `pstack` from tommy waits on the scoped-name unit. Registry whoami is present. Dry-run is not acceptance. HEAD is on remote `tommy`.

Orchestrate ceremony can drown host sling. Sling is not a GitHub PR. Do not spawn worktree owners to sling.

The catalog pin on this branch still points at gastownhall `tree/main/pstack`. That path is absent on `origin/main`. Do not treat the pin as a gastownhall main import.

## Appendix D. Links and reading list

`pstack/DESIGN.md` Provider panel fanout. `openspec/specs/gascity-provider-panel/spec.md`. `openspec/specs/pstack-gascity-pack/spec.md`. `openspec/specs/pstack-delivery-evidence/spec.md`. `openspec/changes/archive/2026-09-03-pstack-graph-honesty/`. `openspec/changes/archive/2026-09-03-pstack-host-sling-receipt/`. `pstack/scripts/apply_intent_change.py`. `validate_registry.py` foreign-source message names registry.gascity.com/publish and refuses a tommy-ca catalog source. Hosted publish is `gc pack registry publish`. Use `skills/how/SKILL.md` and `skills/interrogate/SKILL.md` on `pr-pstack-panel-stamp`. Use `skills/how/SKILL.md` on `pr-pstack-graph-honesty`.

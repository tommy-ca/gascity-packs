## Context

Isolation is on `feat/pstack-pack-honesty` at ancestor `2f65f7b`. HEAD is
`f0027d9`. Dest lock `2026-09-03-pstack-fork-registry-dest` already named
`pr-pstack-publish` in remaining-units. It refused to MODIFY TRACEABILITY
Gherkin. The recursive-graph scenario still omits publish.

## Goals / Non-Goals

**Goals:**

- Make TRACEABILITY Gherkin name the same three program ids remaining-units
  already names.
- Lock that sequence in pack tests.
- Align README restamp prose and program Appendix A with hosted publish.

**Non-Goals:**

- Host sling of `pstack-poteto-mode` or `pstack-build`.
- Hosted publish.
- Restamp of `registry.toml` commit or hash.
- Stamp of `gc.provider_panel`.
- Rename of `pstack/pack.toml`.
- Split remaining-units out of `pstack-delivery-evidence`.
- Change `CANONICAL_REPO`.
- Reopen gastownhall PR 385.

## Decisions

Copy the full live TRACEABILITY requirement. OpenSpec 1.11.0 treats
MODIFIED as a full-block replace. Omitting later scenarios fails
validate.

Do not MODIFY remaining-units. That requirement already names publish.
Growing it again is a process changelog, not a product spec.

Do not restamp `registry.toml`. The catalog pin stays `29c84db` /
`sha256:89aee457`. Hosted dest is `gc pack registry publish`.

Keep the host plugin `check-plan.mjs` as the live checker. Do not rewrite
lanes to pack-vendor `grok-4.6-fast-xhigh`.

Keep execution playbook `playbooks/orchestrate.md` as the named standing
fork program. Host sling is still not a GitHub PR. Owners do not sling
from a worktree child.

## Risks / Trade-offs

A fourth program id `pr-pstack-graph-honesty` is a docs and spec unit on
the same branch. Tests already require the three remaining-units ids.
They do not forbid a fourth.

Disposable live-city import with `GC_TEST_BIN` set passed this session.
That is not formula sling.

## Migration Plan

Author the change under `openspec/changes/2026-09-03-pstack-graph-honesty/`.
Validate with `python pstack/scripts/apply_intent_change.py --source
openspec/changes/2026-09-03-pstack-graph-honesty --validate-only`.
On operator go, apply and `--archive` into `openspec/specs/`. Then edit
TRACEABILITY, README, tests, and Appendix A on `feat/pstack-pack-honesty`.
Push remote `tommy`. Do not open a gastownhall PR.

## Open Questions

Whether the operator slings `pstack-poteto-mode` then `pstack-build` in
the same tick as this honesty unit. Sling remains unproven until cook and
route receipts exist.

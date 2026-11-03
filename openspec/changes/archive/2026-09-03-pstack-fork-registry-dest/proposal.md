## Why

Remaining-units still treats gastownhall `registry.toml` restamp as the
publication step after host sling. julian said drop gastownhall
registry.toml PRs. The operator dest is the tommy-ca fork plus
`gc pack registry publish` to registry.gascity.com. Isolation is already
on `feat/pstack-pack-honesty`. gastownhall PR 385 is closed unmerged.

## What Changes

- MODIFIED remaining-units. Isolation stays on `feat/pstack-pack-honesty`.
  Maintain remote `tommy`. Do not merge to gastownhall. Do not reopen 385.
- Host sling of `pstack-poteto-mode` then `pstack-build` stays the next
  operator unit. It remains unproven. It is still not a GitHub PR.
- Hosted publish waits on those sling receipts. Name `pr-pstack-publish`.
  Publish is `gc pack registry publish` of pack path `pstack/`.
- Do not restamp `registry.toml` commit or hash without sling receipts.
  Restamp of gastownhall `registry.toml` is not the publication vehicle.
- Keep `pr-pstack-land-honesty` and `pr-pstack-panel-stamp`. Insert
  `pr-pstack-publish` between sling and panel stamp.
- This change does not publish, sling, restamp hashes, stamp panel keys,
  or rename `pstack/pack.toml`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: Remaining units name the tommy fork and
  hosted registry as dest. They stop treating catalog restamp as publish.

## Impact

`docs/pstack-program-plan.md`, `pstack/TRACEABILITY.md`,
`pstack/tests/test_pstack_pack.py`, and
`openspec/specs/pstack-delivery-evidence/spec.md`. Formulas stay unstamped.
`registry.toml` is not restamped. This change does not publish.

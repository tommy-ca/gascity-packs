## Why

Interrogate of `347fc24` leftovers. Remaining-units still says hosted
publication MUST wait on sling receipts. Sling is proven. That sentence
reads as a go. Spawn intro and persist still say publish after sling.
README tests do not fail if the old without-a-host-sling allowance is
added back.

## What Changes

- MODIFIED remaining-units. Hosted publication waits on the scoped-name
  unit even after sling receipts.
- MODIFIED operator-docs README scenario. Negative lock on the old
  restamp allowance.
- Program intro, persist, Depends on, and spawn wait line match.
- This change does not restamp, publish, or merge gastownhall.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: hosted publish waits on scoped-name.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/tests/test_pstack_pack.py`.
Then FF tommy `main`.

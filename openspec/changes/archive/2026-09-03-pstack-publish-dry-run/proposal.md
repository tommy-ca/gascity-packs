## Why

Sibling methodology packs publish by landing on gastownhall `main` and
stamping this repo `registry.toml`. pstack is not on `origin/main`. Host
sling cook plus route is proven. The next unit is hosted
`gc pack registry publish` of `pstack/`.

`gc pack registry publish --dry-run pstack/` exited 0 from this branch.
Repository `https://github.com/tommy-ca/gascity-packs`. Commit `441f1a08`.
Ref `feat/pstack-pack-honesty`. Pack `pstack` `0.1.0`. Registry
`https://registry.gascity.com`. Submit was not sent. `gc pack registry
whoami` still fails without login.

Receipt Gherkin still says remaining-units and publish stay blocked until
the sling proof is complete. That proof is complete. Submit still waits
on login. Catalog restamp is still not the dest.

## What Changes

- MODIFIED host sling receipt requirement. Drop the stale publish-blocked
  sentence. Name dry-run proven. Submit waits on registry login.
- Program publish lanes that have evidence get checked. Actual submit
  stays unchecked.
- This change does not submit a publish request. It does not restamp
  `registry.toml`. It does not stamp panel keys.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: dry-run hosted publish is proven. Submit
  waits on login.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/REQUIREMENTS.md`,
`pstack/tests/test_pstack_pack.py`. Formulas and `registry.toml` unchanged.

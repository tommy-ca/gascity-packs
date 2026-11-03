## Why

Host sling is proven. TRACEABILITY still says do not restamp without a
host sling of `pstack-poteto-mode` and `pstack-build`. That sentence now
allows restamp. Remaining-units already says a `--require-git` miss on
`29c84db` is not a restamp trigger. TRACEABILITY and README do not.
Tests freeze the weaker sentence.

## What Changes

- MODIFIED operator-docs and remaining-units restamp scenarios. Keep
  scenario title `TRACEABILITY forbids restamp without a host sling`.
  Body forbids restamp even after proven sling. Ghost-pin CI is not a
  trigger.
- TRACEABILITY.md and README match.
- Tests lock the closed gate and fail if the old "without a host sling"
  allowance remains as the only rule.
- This change does not restamp `registry.toml`. It does not publish.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: restamp gate stays closed after sling.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`pstack/TRACEABILITY.md`, `pstack/README.md`,
`pstack/tests/test_pstack_pack.py`. After archive, isolation HEAD
fast-forwards tommy `main`. `origin/main` is not updated.

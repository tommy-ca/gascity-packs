## Why

Independent verify of the dry-run found `gc pack registry whoami` now
succeeds as `@tommy-ca`. Appendix A and REQUIREMENTS still say whoami
failed. Receipt Gherkin still says submit waits on login. That is stale.
Submit still waits on the operator review-gate. This change does not
submit.

## What Changes

- MODIFIED host sling receipt requirement. Submit waits on the review-gate.
  Registry whoami is present. Dry-run stays proven. Request is not submitted.
- Lane 10 of `pr-pstack-publish` is checked. Merge submit stays unchecked.
- This change does not restamp `registry.toml`. It does not stamp panel keys.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: submit waits on review-gate, not missing login.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`docs/pstack-program-plan.md`, `pstack/REQUIREMENTS.md`,
`pstack/README.md`, `pstack/tests/test_pstack_pack.py`.

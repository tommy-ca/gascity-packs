## Why

Interrogate of `a905201` found the ADDED receipt requirement unsatisfiable.
The operator MUST host-sling. The same block says this change MUST NOT sling.
Remaining-units already carries that freeze. Durable receipt Gherkin must
describe the receipt, not the honesty tick.

`extract_sling_root_id` also accepts a generic `id`, so formula-show JSON
can look like a sling root. Parse must reject that.

## What Changes

- MODIFIED `Host sling receipts of pstack-poteto-mode then pstack-build are
  cook plus route`. Drop tick freeze from the product requirement. Name
  `parse_host_sling_root`. Poteto-only is a failed partial. Remaining-units
  stays blocked until both roots and both `gc.routed_to` exist.
- TRACEABILITY metadata still has no pack-local graph-cook script. It names
  cook-plus-route receipts as unproven host evidence.
- Appendix A restores the failed `pstack-build` cook.
- This change does not sling.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `pstack-delivery-evidence`: receipt requirement is the receipt shape, not
  the honesty freeze.

## Impact

`openspec/specs/pstack-delivery-evidence/spec.md`,
`scripts/gascity_pack_inference_gate.py`,
`tests/test_gascity_pack_inference_gate.py`,
`pstack/tests/test_pstack_pack.py`, `pstack/TRACEABILITY.md`,
`docs/pstack-program-plan.md`. This change does not sling.

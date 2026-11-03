## Context

Arena base is Shape B. Cross-judge scored B 12 and A 8. Remaining-units
already names `pstack-poteto-mode` then `pstack-build`. Shape A wanted
`pstack-review` then `pstack-build`. That is the setup-only compile pair.

Grafts from A. Parse rejects setup-only and formula show. Reuse
`extract_sling_root_id`. Keep a poteto-only row if build sling fails.

## Goals / Non-Goals

**Goals:**

- Name cook plus route as the host-sling receipt.
- Drop one duplicated unproven sentence.
- Keep remaining-units unproven until live receipts exist.

**Non-Goals:**

- Live sling in this change.
- Remaining-units formula rename.
- Full drain of `pstack-build`.
- `write_city` cook.
- Canonical city sling.

## Decisions

ADDED only for the receipt. MODIFY setup-only only to drop the extra
unproven AND. Do not MODIFY remaining-units this tick.

The proof script is a later unit. This change is the contract.

## Risks / Trade-offs

A later live sling may still fail `gc.routed_to` timing. The 30s poll is
the same budget as the gate root wait.

## Migration Plan

Validate, archive, lock pack tests. Do not sling.

## Open Questions

Whether the next tick writes `scripts/pstack_host_sling_proof.py` on this
branch or waits for an operator city with a live `gc.run-operator` session.

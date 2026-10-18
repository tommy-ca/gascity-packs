## Context

Last consumer-facing step is hosted publish. Registry community names are
`<github-owner>/<pack>`. Path stays `pstack/`. Name comes from pack.toml.

Honesty isolation MUST NOT have been the rename. This unit is the rename.

## Goals / Non-Goals

**Goals:**

- `[pack] name = "tommy-ca/pstack"`.
- Hosted dry-run then submit of that identity.

**Non-Goals:**

- gastownhall land.
- Catalog restamp of `29c84db`.
- Vendor pin `tommy-ca/pstack`.
- Panel stamp.
- Formula stem rename.

## Decisions

Do not archive until operator go. This checkout authors the change only.

Keep `test_pack_does_not_ship` vendor `tommy-ca/pstack` forbid on
`upstream.toml`. That is corpus identity, not registry identity.

## Risks / Trade-offs

Registry staff still land community packs. Submit may queue pending.

`gc` 1.4.1 may still print unscoped pack path. Name field is what staff
see.

## Migration Plan

1. Operator go.
2. Archive this change.
3. Set pack.toml name.
4. Flip tests that assert `name == "pstack"` for `[pack]`.
5. README dest says hosted identity is `tommy-ca/pstack`.
6. `gc pack registry publish --dry-run pstack/`.
7. `gc pack registry publish pstack/` after review-gate.

## Open Questions

Whether staff require a different owner slug than `tommy-ca`.

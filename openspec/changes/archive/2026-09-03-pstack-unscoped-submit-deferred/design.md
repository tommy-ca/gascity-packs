## Context

Interrogate of submit-now. Unscoped `pstack` from `@tommy-ca` is a
community publish of a reserved first-party name. `gc` 1.4.1 has no
`--allow-unscoped-name`. Dry-run does not prove acceptance.
`--name tommy-ca/pstack` cannot rename at publish time.

Sibling nightly and inference on this branch already include pstack
smoke and review+build. Those run from the local tree. They do not
prove gastownhall `main`. `pack-release-compatibility` would fetch
`tree/main/pstack` at pin `29c84db`, which is not on `origin/main`.

## Goals / Non-Goals

**Goals:**

- Freeze unscoped tommy submit until the scoped-name unit.
- Keep dry-run as request-shape evidence only.

**Non-Goals:**

- Rename `pstack/pack.toml`.
- Live submit.
- `registry.toml` restamp.
- `METHODOLOGY_FLOW_CONTRACTS` for pstack.
- gastownhall merge.

## Decisions

Do not submit. Repeated ship text does not override remaining-units
rename freeze.

## Risks / Trade-offs

Operators who submit anyway can create an unapprovable pending row.

## Migration Plan

Validate, archive, lock tests, do not publish.

## Open Questions

Whether the scoped-name unit is `tommy-ca/pstack` on the hosted registry
or a gastownhall land that claims unscoped `pstack`.

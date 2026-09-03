## Context

After tommy `main` fast-forward, spawn graph still invited unscoped
submit. Receipt Gherkin already forbids it. Ghost pin CI can fail on a
fresh clone. Restamp is still forbidden.

## Goals / Non-Goals

**Goals:**

- Spawn graph matches unscoped deferral.
- Ghost-pin CI failure is not a restamp trigger.

**Non-Goals:**

- Live submit.
- `registry.toml` restamp.
- gastownhall merge.
- Isolation renamed onto tommy `main`.

## Decisions

Keep isolation named on `feat/pstack-pack-honesty`. tommy `main` stays
an extra pointer. Next isolation commit lands on feat then fast-forwards
tommy `main`.

## Risks / Trade-offs

Fork CI may stay red until gastownhall has `pstack/` or a later unit
drops the ghost pin without calling it publish.

## Migration Plan

Validate, archive, update spawn line, pack tests, push feat, fast-forward
tommy `main`. Do not push origin.

## Open Questions

None for this tick.

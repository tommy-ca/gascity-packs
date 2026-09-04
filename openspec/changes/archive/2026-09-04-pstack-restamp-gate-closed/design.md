## Context

Interrogate of leftover honesty after `2160c50`. TRACEABILITY restamp
gate opened because sling is proven. Do not close it by restamping.

OpenSpec 1.11.0 forbids dropping the scenario title. Keep the title.
Change the AND body.

## Goals / Non-Goals

**Goals:**

- Restamp stays forbidden after proven sling.
- Ghost-pin CI is not a restamp trigger.

**Non-Goals:**

- `registry.toml` restamp.
- Unscoped submit.
- gastownhall merge.

## Decisions

Keep formula names in the TRACEABILITY sentence. Keep the old scenario
title. Tests require "is not a restamp trigger" and fail if the old
allowance is the only rule.

## Risks / Trade-offs

Fork CI may stay red. That is accepted.

## Migration Plan

Validate, archive, update TRACEABILITY and README, pack tests, push feat,
fast-forward tommy `main`.

## Open Questions

None for this tick.

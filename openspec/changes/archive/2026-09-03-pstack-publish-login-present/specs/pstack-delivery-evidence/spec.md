## MODIFIED Requirements

### Requirement: Host sling receipts of pstack-poteto-mode then pstack-build are cook plus route

Feature: pstack-delivery-evidence

Rule: Remaining-units sling is cook plus route in a disposable roles city

The operator MUST host-sling `pstack-poteto-mode` then `pstack-build`
in a disposable city that imports `gascity/roles` and sets
`[daemon] formula_v2 = true`. That city MAY be the inference-gate city
after `--setup-only`, or an equivalent city. A receipt for each formula
is the sling JSON root id plus `gc.routed_to`. `parse_host_sling_root`
MUST call `extract_sling_root_id` only after the payload has a sling root
key (`root_bead_id`, `workflow_id`, `root_id`, or `bead_id`). It MUST NOT
treat a generic JSON `id` as a sling root. It MUST reject formula show
and `--setup-only` logs. It MUST NOT call `launch_review_formula` or
`launch_build_formula` for this pair. A complete proof MUST include both
formulas with both `gc.routed_to` values. A poteto-only row MAY persist
as a failed partial. Hosted submit of `gc pack registry publish` waits on
the operator review-gate after dry-run. Registry whoami is present.
Catalog restamp of gastownhall `registry.toml` is not that dest. Full
drain of `pstack-build` is not required. The receipt MUST NOT be
`pstack-review` then `pstack-build`. Formula show is not a receipt.
Setup-only show is not a receipt. `pstack-poteto-mode` MUST NOT auto-sling
the classified formula. The sling unit MUST NOT be a GitHub PR. The
operator MUST NOT sling into a canonical city. Dry-run of
`gc pack registry publish` of pack path `pstack/` from this branch is
proven. Submit was not sent.

#### Scenario: Cook plus route of pstack-poteto-mode then pstack-build is the sling receipt

- **GIVEN** a disposable city with `gascity/roles` and `formula_v2`
- **WHEN** the operator host-slings `pstack-poteto-mode` then `pstack-build`
- **THEN** each formula has a sling JSON root id
- **AND** each root bead has `gc.routed_to`
- **AND** the formulas are `pstack-poteto-mode` then `pstack-build`
- **AND** it MUST NOT treat `pstack-review` then `pstack-build` as the remaining-units sling
- **AND** full drain of `pstack-build` is not required
- **AND** the classified formula from `pstack.route.v1` is not auto-slung
- **AND** formula show and `--setup-only` logs are not receipts
- **AND** a poteto-only row is a failed partial, not a complete proof
- **AND** the city is not a canonical city

#### Scenario: Parse rejects show logs and generic JSON ids

- **GIVEN** `parse_host_sling_root` and `extract_sling_root_id`
- **WHEN** the input is formula-show JSON with only a generic `id`, or a `--setup-only` log
- **THEN** parse fails
- **AND** it does not return that `id` as a sling root

#### Scenario: Hosted publish dry-run is proven

- **GIVEN** a clean checkout of `feat/pstack-pack-honesty` tracking remote `tommy`
- **WHEN** an operator runs `gc pack registry publish --dry-run pstack/`
- **THEN** the command exits 0
- **AND** the request names pack `pstack` version `0.1.0`
- **AND** the registry is `https://registry.gascity.com`
- **AND** the repository is `https://github.com/tommy-ca/gascity-packs`
- **AND** the request is not submitted
- **AND** catalog restamp of gastownhall `registry.toml` is not the dest
- **AND** `gc pack registry whoami` succeeds
- **AND** submit waits on the operator review-gate

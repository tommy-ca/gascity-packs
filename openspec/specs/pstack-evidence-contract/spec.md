# pstack-evidence-contract Specification

## Purpose

Define canonical principle-enforcement declarations and fail-closed evidence validation for the PStack pack.

## Requirements

### Requirement: Required artifact declarations fail closed

The pack schema validator MUST treat an explicitly present
`required_fields` schema declaration as a non-empty list of non-empty field
paths. `pstack/scripts/validate_pstack_schemas.py` owns that list-shape check
through `require_string_list`. The shared build-artifact validator MUST NOT
own `required_fields`. The shared validator MUST fail closed for empty
strings on keys listed in `required_front_matter`.
`gascity/assets/scripts/validate_build_artifact.py` owns that non-empty
string check. The shared validator MUST retain the execution-metadata guard
for forbidden owner, persona, or role leaves in `required_front_matter`.
Namespaced domain fields that appear only in `required_fields` remain
domain data and are not subject to that execution-metadata blacklist.
Decision domain keys MUST stay in `required_fields` and MUST NOT be added
to `required_front_matter`.

#### Scenario: Empty required-field schema declarations are rejected

- **GIVEN** a custom schema that explicitly declares `required_fields: []`, a non-list value, or a list containing a blank/non-string field path
- **WHEN** the schema is loaded by `pstack/scripts/validate_pstack_schemas.py`
- **THEN** validation fails with a schema-definition error that `required_fields` must be a non-empty list of non-empty strings

#### Scenario: Empty required_front_matter values are rejected

- **GIVEN** a valid `pstack.explanation.v1` schema whose `overview` key is listed in `required_front_matter`
- **WHEN** an artifact supplies `overview` as whitespace
- **THEN** the shared build-artifact validator fails with a front-matter non-empty error

#### Scenario: Empty required_fields values that are not front matter stay accepted

- **GIVEN** a valid `pstack.decision.v1` schema whose `subtraction` key is listed only in `required_fields`
- **WHEN** an artifact supplies empty `subtraction`
- **THEN** the shared build-artifact validator accepts the artifact
- **AND** the pack schema validator still requires `subtraction` in the `required_fields` list

#### Scenario: Domain owner fields remain valid

- **GIVEN** a namespaced PStack schema that requires the domain field `owner` only in `required_fields`
- **WHEN** the artifact supplies a non-empty owner value
- **THEN** the shared validator accepts the field
- **AND** the execution-metadata blacklist still rejects a forbidden `required_front_matter` leaf such as `producer.role`

### Requirement: Decision artifacts record explicit subtraction outcomes

The PStack decision artifact contract MUST allow a trivial subtraction assessment
to use `status: no_removal_opportunity`. The pack schema MUST still declare
`subtraction` and `rationale` in `required_fields`. Those keys MUST NOT move
into `required_front_matter`. The shared validator MUST NOT fail closed on
empty `subtraction` this turn.

#### Scenario: No-removal decision validates

- **GIVEN** a valid `pstack.decision.v1` artifact whose subtraction found no removable complexity
- **WHEN** the shared validator checks the artifact
- **THEN** `status: no_removal_opportunity` is accepted
- **AND** empty `subtraction` does not fail as a `required_front_matter` non-empty string

#### Scenario: Empty subtraction stays a pack-schema list entry

- **GIVEN** a `pstack.decision.v1` artifact with the no-removal status and empty `subtraction`
- **WHEN** the shared validator checks the artifact
- **THEN** validation succeeds
- **AND** `pstack/schemas/decision.v1.yaml` still lists `subtraction` under `required_fields`

### Requirement: Validator portability is preserved

The shared artifact validator MUST remain executable by the repository's bare
`python3` gate without introducing a newer-only standard-library import for
existing behavior. Ordered required sections MUST retain their current success
and failure semantics on the supported Python runtime.

#### Scenario: Section order keeps its existing behavior

- **GIVEN** required sections appear in declaration order
- **WHEN** the validator checks their order
- **THEN** validation succeeds
- **AND** a reordered section produces the existing order diagnostic

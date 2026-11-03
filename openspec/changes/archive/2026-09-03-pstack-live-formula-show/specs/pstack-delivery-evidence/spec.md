## MODIFIED Requirements

### Requirement: PStack is exercised through a disposable live city

The maintained-pack live test matrix MUST import PStack into a scratch city with the real Gas City CLI. It MUST derive PStack's formulas and agents from its checkout, verify that each resolves through the imported city, and assert the observed doctor delta against an explicit expected set. The live test MUST retain the canary control that proves doctor findings are being surfaced. Every PStack formula MUST declare `formula_compiler >= 2.0.0` and MUST NOT retain deprecated `contract = "graph.v2"`; the expected PStack-specific doctor delta MUST be empty. The live matrix MUST compile each discovered formula with `gc formula show`. It MUST NOT treat formula show as formula sling.

#### Scenario: PStack formulas and agents resolve through Gas City

- **GIVEN** a real executable Gas City CLI is provided to the live test fixture
- **WHEN** a scratch city imports only the PStack pack under test
- **THEN** every formula discovered under `pstack/formulas/` is listed by `gc formula list`
- **AND** every agent discovered under `pstack/agents/` is listed by `gc agent list`
- **AND** no provider, publication, or canonical city state is mutated

#### Scenario: PStack doctor delta is explicit

- **GIVEN** the scratch city and equivalent baseline city are inspected by `gc doctor`
- **WHEN** the PStack delta is computed
- **THEN** the expected PStack-specific delta is empty
- **AND** the live suite records no additional PStack-specific finding
- **AND** the canary control continues to observe its intentional `formula-requirements` finding

#### Scenario: PStack formulas compile through formula show

- **GIVEN** a real executable Gas City CLI is provided to the live test fixture
- **WHEN** a scratch city imports the pack under test
- **THEN** `gc formula show` exits 0 for every formula discovered under that pack's `formulas/`
- **AND** no provider, publication, or canonical city state is mutated

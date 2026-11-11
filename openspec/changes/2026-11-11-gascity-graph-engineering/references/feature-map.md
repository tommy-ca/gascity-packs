# Feature-map and falsifier-first verification (NOT_RUN unless indicated)

| ID | Requirement | Positive | Negative / mutant | Evidence |
| --- | --- | --- | --- | --- |
| GE-F01 | GE-01 | pack import resolves and formula cataloged | missing import | not run |
| GE-F02 | GE-01 | host compiler >=2.0.0 accepts `requires` | obsolete host / missing capability | not run |
| GE-F03 | GE-01 | approved input convoy → native Bead graph | no/unauthorized convoy | not run |
| GE-F04 | GE-02 | valid reference graph DAG | duplicate node ID | offline test authored; not run |
| GE-F05 | GE-02 | all predecessors exist | unknown predecessor | offline test authored; not run |
| GE-F06 | GE-02 | acyclic dependency graph | injected cycle/self-edge | offline test authored; not run |
| GE-F07 | GE-02 | approved scope and role | untrusted absolute path/model command | not run |
| GE-F08 | GE-03 | 3 reviewer Beads fan-in | remove one reviewer/edge | offline test authored; not run |
| GE-F09 | GE-03 | independent session receipts | one model self-reports 3 reviewers | not run |
| GE-F10 | GE-03 | review artifacts exact SHA | forged/stale PASS/evidence | not run |
| GE-F11 | GE-04 | N member drain and recovery | stale claimed write + retry | not run |
| GE-F12 | GE-04 | fresh-context replay | missing durable frontier | not run |
| GE-F13 | GE-04 | safe crash after external effect | duplicate effect on retry | not run |
| GE-F14 | GE-05 | source notice remains HELD | generated grant/verdict promoted | offline test authored; not run |
| GE-F15 | GE-05 | no producer/QStack import without optional adapter | graph pack publishes wiki | not run |
| GE-F16 | Existing #21 | N=2/3/5/8 real child Beads | mere synthetic task metadata | live NOT_RUN |
| GE-F17 | PStack | real Swarm/Arena/Interrogate receipts | panel headings only | not run |
| GE-F18 | Thermos | executed code-quality and review skills | self-attested review | not run |

Offline tests are Python reference-model checks; even when they pass, they are **not** real host compiler or provider runtime evidence. Native GC `lint`, `formula catalog`, `gc sling`, Bead/session logs and exact-head CI evidence are separate. A host runtime test requires explicit bounded budget, disposable city and authorized credentials; report BLOCKED otherwise.

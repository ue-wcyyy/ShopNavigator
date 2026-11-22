# Feature backlog

Prioritised, living list. Every item needs **acceptance criteria** and, once it starts, a dated
issue or PR link. Keep completed items at the bottom so the history stays auditable.

Priority: `P0` blocks the milestone · `P1` needed for `v1.0` acceptance · `P2` nice to have.

| ID | Priority | Feature | Acceptance criteria | Milestone | Issue / PR | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SN-001 | P0 | Simulated store: catalog + search + product pages | A seeded catalog subset loads offline; `search`/`open_product` return observation objects; prices and options come from simulator state only | v0.1 | TODO | TODO | todo |
| SN-002 | P0 | Constraint checklist model | A goal string yields budget, mandatory properties and soft preferences as a structured, user-visible checklist | v0.1 | TODO | TODO | todo |
| SN-003 | P0 | Reactive baseline agent | Baseline completes a scripted task set and logs success rate, violations and action count | v0.1 | TODO | TODO | todo |
| SN-004 | P0 | Constraint-aware navigation loop | Agent searches, opens, compares and selects using observed page data; hard step/time caps enforced; bounded replanning on errors | v0.2 | TODO | TODO | todo |
| SN-005 | P0 | Integrated UI | Goal entry → checklist → status → comparison → cart review, with validation and recoverable errors | v0.2 | TODO | TODO | todo |
| SN-006 | P0 | Run tracing and replay | Every run saves tool calls, costs, invalid actions and the final constraint check; a saved run can be replayed | v0.2 | TODO | TODO | todo |
| SN-007 | P1 | Evaluation harness (40 tasks) | 40 varied tasks run reproducibly; results exported with metrics defined in `docs/evaluation-plan.md` | v1.0 | TODO | TODO | todo |
| SN-008 | P1 | Hard-case suite (15) | Unavailable products, misleading descriptions, changing options — expected outcomes documented | v1.0 | TODO | TODO | todo |
| SN-009 | P1 | Baseline comparison report | Reactive vs constraint-aware compared on success, violations, unnecessary actions, cost | v1.0 | TODO | TODO | todo |
| SN-010 | P1 | Usability review | ≥3 non-team participants, think-aloud protocol, defects logged, at least one change or a justified no-change | v1.0 | TODO | TODO | todo |
| SN-011 | P2 | CSV / report export | Saved runs export to CSV plus a human-readable summary | v1.0 | TODO | TODO | todo |
| SN-012 | P2 | Ambiguity clarification | Ambiguous goals trigger a targeted question instead of a guess; recorded in the trace | v1.0 | TODO | TODO | todo |

## Done

| ID | Completed | Commit / PR | Note |
| --- | --- | --- | --- |
| — | — | — | — |

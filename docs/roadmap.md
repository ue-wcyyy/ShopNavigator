# Roadmap

Next-version ideas, kept separate from the graded scope so the `v1.0` boundary stays clear.

## Near term (during the course)

| Version | Item | Why |
| --- | --- | --- |
| `v0.1` | Environment pilot + reactive baseline | Proves feasibility before building the agent |
| `v0.1` | Tiny catalog snapshot with seeds | Reproducibility for every later number |
| `v0.2` | Constraint-aware navigation + UI | The actual product |
| `v0.2` | Trace/replay | Makes failures reviewable and grading auditable |
| `v1.0` | 40-task evaluation + 15 hard cases | Evidence, not demos |
| `v1.0` | Usability review + fixes | Catches what tests miss |

## Later (after the course, if continued)

- Multi-store comparison and price-history views over snapshots.
- Richer action space (filters, sorting, pagination) with the same whitelist discipline.
- Learned action policy distilled from successful traces (cheaper per task).
- Human-in-the-loop checklist editing with diff history.
- Packaging as a reusable simulator for agent benchmarking.

## Explicitly not planned

- Real checkout, payments or account handling.
- Scraping live commercial sites.
- Training large models from scratch.

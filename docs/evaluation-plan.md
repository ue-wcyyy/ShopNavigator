# Evaluation plan

> Status: outline. Every number below is a requirement from the Topic 5 brief; none has been
> measured yet.

## Metrics

| Metric | Definition | Source |
| --- | --- | --- |
| Task success | Task reward from simulator state (all hard constraints satisfied and the right product selected) | simulator |
| Constraint satisfaction | Share of hard constraints met by the final product; soft preferences reported separately | constraint checker |
| Rule violations | Invalid actions, out-of-whitelist calls, budget/step-cap breaches | trace |
| Unnecessary page actions | Actions that did not advance the search (re-opened page, redundant search) | trace |
| Efficiency | Environment steps and wall-clock runtime per task | trace |
| Cost | API spend per task and per run, tokens in/out | trace + provider usage |
| False confidence | Confident recommendation when nothing satisfies the constraints | manual review of J2-style tasks |
| Evidence accuracy | Explanation claims that are not supported by a logged observation | manual review sample |

## Test sets

| Set | Size | Purpose |
| --- | --- | --- |
| Main evaluation | **≥40** simulated shopping tasks, varied hard constraints and budgets | Primary success/constraint numbers |
| Difficult cases | **≥15** tasks: unavailable products, misleading descriptions, changing options | Robustness and failure classification |
| Journeys | **5** end-to-end journeys including one failure/recovery (`docs/user-journeys.md`) | Integration acceptance |
| Usability | **≥3** people outside the team | Interface defects and one improvement |

Split: tasks are held out from any prompt or few-shot examples. Record task ids and seeds so runs are
reproducible.

## Baselines and comparison

| System | Description | Compared on |
| --- | --- | --- |
| B0 — direct LLM | Single prompt, no browsing; the model names a product from memory | Success (expected near zero), hallucination rate |
| B1 — reactive agent | One search, open top result, recommend if it looks close | Success, violations, steps, cost |
| Ours — constraint-aware agent | Checklist-driven search, comparison, validation, bounded replanning | Same metrics; per-category breakdown |

Report all failures, not only hand-picked successes, plus the performance/cost trade-off between the
baseline and the improved pipeline.

## Reporting

- `evaluation/results/<date>/` holds raw JSON/CSV per run (not committed).
- `evaluation/report.md` (committed) holds the final tables, per-category results, failure analysis
  and cost discussion.
- Every reported number must be reproducible with a documented command and seed.

## Usability review protocol

1. Recruit ≥3 participants outside the team.
2. Give each the same three goals (one happy path, one infeasible, one ambiguous) without coaching.
3. Think-aloud; log confusion points, dead ends and defects with timestamps.
4. Triage: reproduce critical defects, fix at least one, or record a justified decision not to.
5. Summarise in `evaluation/report.md` and log the follow-up in `PROGRESS.md`.

## Open questions

- How to score partial constraint satisfaction without rewarding a wrong product?
- Which failures count as "agent error" vs "environment error" for the report?

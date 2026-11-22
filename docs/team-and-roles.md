# Team and responsibilities

Three members, all able to explain the entire system. Update this file when ownership changes, and
keep `PROGRESS.md` consistent with it.

## Members

| Member | GitHub | Primary area | Secondary area | Weekly commitment |
| --- | --- | --- | --- | --- |
| TODO (A) | @TODO | | | TODO |
| TODO (B) | @TODO | | | TODO |
| TODO (C) | @TODO | | | TODO |

## Work packages

| Package | Description | Owner | Backup |
| --- | --- | --- | --- |
| Simulator & catalog | Store state, actions, observations, seeds, snapshots | TODO | TODO |
| Constraint model | Goal parsing, checklist, product validation | TODO | TODO |
| Agent | Planner, policy, tool layer, bounded replanning | TODO | TODO |
| UI | Goal entry, checklist, status, comparison, cart review, replay | TODO | TODO |
| Tracing & evaluation | Trace format, metrics, batch runner, report tables | TODO | TODO |
| Docs & demo | Proposal, README, report, presentation, demo script | TODO | TODO |

## Collaboration rules

- One feature per branch, small commits with a message that says *why*.
- Every PR links its backlog item (`SN-0xx`) and updates `PROGRESS.md` when it changes the plan.
- Review: at least one other member reads each PR; the author merges.
- Never commit secrets or restricted data — check `git status` before pushing.
- Weekly sync: update `PROGRESS.md` first, then decide next week's backlog items.

## Presentation readiness

Every member should be able to answer questions on: architecture and data flow, why the simulator is
the source of truth, the evaluation design and its limitations, and what each failure case taught us.

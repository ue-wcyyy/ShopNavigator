# Architecture

> Status: outline. Replace the sketch with the final diagram once the `v0.1` pilot is done
> (`assets/diagrams/architecture.(png|svg)`).

## Layers

| Layer | Module | Responsibility |
| --- | --- | --- |
| Simulator | `src/shopnavigator/simulator/` | Owns catalog, prices, option availability and page state. Returns an observation for every action; rejects anything outside the whitelist. |
| Constraint model | `src/shopnavigator/constraints/` | Turns the goal into a structured checklist (budget / hard / soft) and scores any product against it. Pure functions, no LLM. |
| Agent | `src/shopnavigator/agent/` | Planner proposes the next action from the observations so far; policy decides search vs open vs select vs stop; tools wrap the action space and validate arguments. |
| UI | `src/shopnavigator/ui/` | Goal entry, checklist editor, live status, comparison table, cart review, run history/replay. |
| Trace / evaluation | `src/shopnavigator/tracing.py`, `evaluation/` | Records every step, action, cost and failure; batch-runs task sets and computes metrics. |

## Data flow

```text
 user goal
    │
    ▼
constraint parser ──► checklist (editable by user)
    │
    ▼
   planner ◄──────────── observation (page content, options, prices)
    │  action                    ▲
    ▼                           │
 action validator ──► simulator ┘
    │                    │
    │                    └─► state check (cart, final validation)
    ▼
  trace ──► UI (status, comparison, explanation) ──► saved run ──► replay
                              │
                              └─► evaluation runner ──► metrics / report
```

## Key design decisions

1. **Simulator is the only source of truth.** LLM output is a proposal, never evidence. Final
   success is computed from simulator state.
2. **Deterministic constraint checking.** Budget, required attributes and soft preferences are
   evaluated in code so the same product always gets the same verdict.
3. **Bounded autonomy.** Step, time and spend caps plus loop detection; infeasible goals end with a
   specific blocking constraint instead of a guess.
4. **Everything is replayable.** Each run stores the initial seed, actions, observations digest and
   costs so a reviewer can reproduce it.

## Open questions

- Text action space vs browser-driven (Playwright) navigation? — decide in the `v0.1` pilot.
- Streamlit vs FastAPI + small frontend? — decide before `v0.2`.
- How much of the reason text comes from the model vs a template filled from the checklist?

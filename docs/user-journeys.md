# End-to-end user journeys

Required by the brief: **five journeys** with measurable success criteria, defined in the proposal
and tested after integration — at least one of them a failure/recovery case, each with reproducible
inputs and expected outcomes.

Status: `draft` → `passing` once covered by an integration test in `tests/`.

## J1 — Happy path: budget + two hard attributes

- **Input:** "17-inch laptop, 32 GB RAM, under $1,500, prefer dark grey."
- **Steps:** goal entry → checklist confirmation → agent searches → opens 3–5 candidates → compares
  → selects the cheapest item satisfying both hard attributes and the budget → cart review → user
  confirms.
- **Expected:** every hard constraint verified against simulator state; every claim in the
  explanation traceable to an observation; no purchase action.
- **Success criteria:** final product passes 100% of hard constraints; ≤12 environment steps;
  run completes under the per-task time cap.
- **Status:** TODO

## J2 — Infeasible goal: no product can satisfy the constraints

- **Input:** "15-inch laptop with 64 GB RAM under $400."
- **Steps:** agent searches, opens candidates, proves the budget/attribute combination is impossible
  → stops → explains the specific blocking constraint.
- **Expected:** no recommendation is fabricated; the agent does not silently relax the constraints;
  it offers to relax one constraint explicitly.
- **Success criteria:** zero false recommendations; blocking constraint named correctly; bounded
  steps and cost.
- **Status:** TODO

## J3 — Ambiguous goal: clarification instead of guessing

- **Input:** "a good laptop for school, not too expensive."
- **Steps:** checklist shows missing budget/attribute slots → agent asks one focused question →
  user answers → navigation proceeds.
- **Expected:** the ambiguity is recorded; the agent does not invent a budget.
- **Success criteria:** clarification asked within the first 2 turns; the resulting checklist is
  complete before any product page is opened.
- **Status:** TODO

## J4 — Failure and recovery: navigation breaks mid-run

- **Input:** a valid goal on a task seeded so a product page 404s / an option becomes unavailable.
- **Steps:** invalid action or dead end → error surfaced → bounded replan (≤2 attempts) → alternate
  product selected or a clean stop with explanation.
- **Expected:** no crash, no infinite loop, no invented page content; failure classified in the
  trace.
- **Success criteria:** recovered within the step cap, or stopped with an accurate reason; the saved
  run reproduces the same failure.
- **Status:** TODO

## J5 — Comparison and soft-preference trade-off, then save and replay

- **Input:** "wireless headphones under $200, noise cancelling required, lightest possible, prefer
  black."
- **Steps:** agent opens several candidates → comparison panel shows per-constraint pass/fail and
  the trade-off → user reviews → run saved → run replayed by a reviewer.
- **Expected:** soft preferences influence ranking but never override hard constraints; replay
  reproduces identical steps and the same final verdict.
- **Success criteria:** ranking explained by observed attributes only; replay matches the original
  trace field by field.
- **Status:** TODO

## Test matrix (after integration)

| Journey | Automated test | Reproducible input | Expected outcome recorded |
| --- | --- | --- | --- |
| J1 | TODO | task id + seed | yes |
| J2 | TODO | task id + seed | yes |
| J3 | TODO | goal string | yes |
| J4 | TODO | seeded failure task | yes |
| J5 | TODO | task id + seed + saved run | yes |

# API cost and compute budget

Documented assumptions are a graded requirement. Fill in real numbers after the `v0.1` pilot; until
then this file states the caps that the code must enforce.

## Hard caps (enforced in `configs/default.yaml`)

| Cap | Value | Where enforced |
| --- | --- | --- |
| Steps per task | 30 | agent loop |
| Wall clock per task | 300 s | agent loop |
| Searches per task | 6 | planner |
| Product pages per task | 10 | planner |
| USD per task | $0.05 | budget guard |
| USD per run (40 tasks) | $2.00 | evaluation runner |

## Cost model (TODO: replace with measured values)

| Item | Assumption | Notes |
| --- | --- | --- |
| Planner calls per task | TODO (est. 6–12) | One call per decision step |
| Prompt tokens per call | TODO | Observation digests kept short; no full HTML |
| Completion tokens per call | TODO | JSON action only, ≤200 tokens |
| Price per 1M input tokens | TODO | Provider price at time of writing |
| Price per 1M output tokens | TODO | |
| Estimated cost per task | TODO | |
| Estimated cost for 40 tasks × 3 systems | TODO | Baseline + ours + rerun margin |

## Compute

- CPU only. No GPU training, no LoRA/QLoRA, no local large model hosting required.
- Simulator and tests must run offline (no network) except for explicit LLM calls.

## Controls

- Budget guard aborts a run before exceeding the per-task/per-run cap.
- Every call's token usage and cost is written to the trace, so the evaluation report can quote
  measured spend.
- `.env` holds the key; `configs/` never does. CI never calls a paid API.

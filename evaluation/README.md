# Evaluation

Task set, runner outputs and the final report.

| Path | Committed? | Purpose |
| --- | --- | --- |
| `tasks/` | No (`.gitkeep` only) | Held-out evaluation tasks with seeds and expected outcomes |
| `results/` | No (`.gitkeep` only) | Raw per-run JSON/CSV, traces, cost logs |
| `report.md` | **Yes** — TODO | Final tables, per-category results, failure analysis, cost discussion |

## How to run (target)

```bash
python -m shopnavigator.evaluation.runner --config configs/default.yaml --split eval \
    --systems reactive,constraint_aware --out evaluation/results/$(date +%F)
```

## Requirements checklist

- [ ] ≥40 tasks with varied hard constraints and budgets
- [ ] ≥15 difficult cases (unavailable product, misleading description, changing options)
- [ ] Baseline vs improved pipeline on the same tasks, all failures reported
- [ ] Cost and runtime per system
- [ ] 5 end-to-end journeys, including failure/recovery
- [ ] Usability review with ≥3 external participants

Details: [../docs/evaluation-plan.md](../docs/evaluation-plan.md).

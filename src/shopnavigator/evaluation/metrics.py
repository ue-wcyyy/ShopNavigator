"""Evaluation metrics.

Definitions live in ``docs/evaluation-plan.md``; keep this module the single implementation so the
report and the tests agree.

TODO(v1.0): task success, constraint satisfaction, rule violations, unnecessary page actions,
steps, runtime, cost, false-confidence flags.
"""

from __future__ import annotations


def summarize(runs: list[dict[str, object]]) -> dict[str, float]:
    """Aggregate per-run traces into the metrics reported in ``evaluation/report.md``."""
    raise NotImplementedError("metrics land in v1.0 — see BACKLOG.md SN-007")

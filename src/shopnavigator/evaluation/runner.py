"""Batch evaluation runner.

TODO(v1.0): load a task split, run each system (direct LLM, reactive baseline, ours) with the same
seeds, write raw results under ``evaluation/results/<date>/``, then emit the report tables.
Enforce the per-task and per-run USD caps from ``configs/default.yaml``.
"""

from __future__ import annotations


def main(argv: list[str] | None = None) -> int:
    """Entry point for ``python -m shopnavigator.evaluation.runner``."""
    raise NotImplementedError("runner lands in v1.0 — see BACKLOG.md SN-007")

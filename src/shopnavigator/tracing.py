"""Structured run traces.

One run = one task attempt. A trace must be enough to replay the run and to classify failures
(navigation error vs constraint error vs planner error).

TODO(v0.2): append-only JSONL writer, secret redaction, token/cost accounting, replay loader.
"""

from __future__ import annotations


def record_step(*args: object, **kwargs: object) -> None:
    """Append one step (action, observation digest, rationale, cost) to the current trace."""
    raise NotImplementedError("trace writer lands in v0.2 — see BACKLOG.md SN-006")

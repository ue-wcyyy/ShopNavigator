"""Planner: decide the next action from observations so far.

TODO(v0.2): build a short observation digest, ask the policy for the next action, validate it,
and stop when the goal is satisfied or provably infeasible. Enforce search/page/step caps and
bounded replanning (max 2 attempts) before giving up.
"""

from __future__ import annotations


def plan_next(*args: object, **kwargs: object) -> object:
    """Return the next action for the current state, or a stop decision with a reason."""
    raise NotImplementedError("planner lands in v0.2 — see BACKLOG.md SN-004")

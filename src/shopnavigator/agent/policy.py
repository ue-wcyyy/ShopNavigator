"""Policies: how aggressively the agent explores and how it ranks candidates.

Two policies are required for the comparison in ``docs/evaluation-plan.md``:

* ``reactive``         — one search, open the first result, recommend it.
* ``constraint_aware`` — checklist-driven search, comparison and explicit validation.

TODO(v0.1/v0.2): implement both behind one interface so the evaluation runner can swap them.
"""

from __future__ import annotations


class ReactivePolicy:
    """Baseline: shallow search, no full constraint validation."""

    name = "reactive"

    def next_action(self, state: object) -> object:
        raise NotImplementedError("baseline lands in v0.1 — see BACKLOG.md SN-003")


class ConstraintAwarePolicy:
    """Improved pipeline: verify hard constraints, rank by soft preferences."""

    name = "constraint_aware"

    def next_action(self, state: object) -> object:
        raise NotImplementedError("policy lands in v0.2 — see BACKLOG.md SN-004")

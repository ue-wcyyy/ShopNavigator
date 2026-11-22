"""Goal parsing: natural-language instruction → structured constraint checklist.

TODO(v0.1): extract budget, mandatory attributes and soft preferences. Never invent a missing
budget: ambiguous goals must produce an explicit clarification request instead (journey J3).
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Checklist:
    """Structured, user-visible constraints extracted from a shopping goal."""

    budget: float | None = None
    required: dict[str, str] = field(default_factory=dict)
    preferred: dict[str, str] = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)


def parse_goal(goal: str) -> Checklist:
    """Parse ``goal`` into a checklist; list unresolved fields in ``missing``."""
    raise NotImplementedError("goal parsing lands in v0.1 — see BACKLOG.md SN-002")

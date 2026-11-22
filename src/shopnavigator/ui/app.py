"""UI screens (Streamlit target).

Layout TODO(v0.2):
  * goal entry with validation and example goals
  * editable constraint checklist (budget / hard / soft)
  * live agent status: current step, last action, remaining budget
  * comparison panel: per-constraint pass/fail for each candidate
  * cart review and explicit confirmation (no real purchase)
  * run history: load a saved run and replay it step by step
"""

from __future__ import annotations


def render() -> None:
    """Render the application shell."""
    raise NotImplementedError("UI lands in v0.2 — see BACKLOG.md SN-005")

"""Deterministic constraint checking.

Pure functions: same product + same checklist ⇒ same verdict. No LLM here, ever — this is what makes
"success" auditable.

TODO(v0.1): evaluate budget, required attributes and option combinations; return per-constraint
pass/fail plus the blocking constraints, and keep soft preferences as a separate ranking signal.
"""

from __future__ import annotations


def check(product: object, checklist: object) -> dict[str, bool]:
    """Return a per-constraint pass/fail map for ``product`` against ``checklist``."""
    raise NotImplementedError("constraint checker lands in v0.1 — see BACKLOG.md SN-002")

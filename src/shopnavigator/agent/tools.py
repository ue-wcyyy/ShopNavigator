"""Tool layer exposed to the model: a narrow, validated wrapper over the action space.

Design rule: the model never touches the simulator directly. Every tool call is validated,
logged with its cost, and returns a compact observation — never raw HTML.

TODO(v0.2): define the JSON schemas, reject unknown arguments, cap observation length.
"""

from __future__ import annotations


def tool_schemas() -> list[dict[str, object]]:
    """Return provider-ready tool schemas for the allowed actions."""
    raise NotImplementedError("tool layer lands in v0.2 — see BACKLOG.md SN-004")

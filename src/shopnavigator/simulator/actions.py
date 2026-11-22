"""Action space definitions and validation.

TODO(v0.1): define the closed set of actions with their argument schemas, validate every proposed
action against the whitelist, and return a typed error instead of executing anything unexpected.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    """A single environment action, e.g. ``search(query="...")``."""

    name: str
    args: dict[str, str]


ALLOWED_ACTIONS: tuple[str, ...] = (
    "search",
    "open_product",
    "select_option",
    "add_to_cart",
    "back",
)


def validate(action: Action) -> None:
    """Raise ``ValueError`` if ``action`` is not permitted or its arguments are malformed."""
    raise NotImplementedError("action validation lands in v0.1 — see BACKLOG.md SN-001")

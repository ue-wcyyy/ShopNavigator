"""Simulated store: the only environment the agent may act on.

The store owns prices, option availability and page state, and returns an explicit observation for
every accepted action. Success is decided here, never by the agent's own text.

TODO(v0.1):
  * search(query) -> ranked product cards
  * open_product(id) -> page observation (attributes, price, options)
  * select_option(product_id, name, value) -> updated observation
  * add_to_cart(product_id) / review_cart()
  * reject and log any action outside ``navigation_whitelist``
  * deterministic state from a seed so runs replay identically
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Store:
    """Deterministic simulated storefront."""

    seed: int = 42
    cart: list[str] = field(default_factory=list)

    def reset(self) -> None:
        """Return to the initial state for ``seed``."""
        raise NotImplementedError("simulator lands in v0.1 — see BACKLOG.md SN-001")

"""Catalog representation.

TODO(v0.1): load the prepared catalog, expose lookup by id and simple attribute filters. The
catalog is data, not state — availability lives in the store.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """One simulated product."""

    id: str
    title: str
    price: float
    attributes: Mapping[str, str]
    options: Mapping[str, tuple[str, ...]]


def load_catalog(path: str) -> list[Product]:
    """Load products from a prepared catalog file."""
    raise NotImplementedError("catalog loading lands in v0.1 — see BACKLOG.md SN-001")

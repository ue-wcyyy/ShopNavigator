"""Configuration loading: committed YAML + local ``.env`` overrides.

TODO(v0.1): load ``configs/default.yaml``, apply ``SHOPNAV_*`` environment overrides, validate
with pydantic models, and fail loudly on a missing/invalid cap so no run can start unbounded.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Validated runtime settings (placeholder shape — refine with the real config)."""

    max_steps: int = 30
    timeout_seconds: int = 300
    max_usd_per_task: float = 0.05


def load_settings(path: str = "configs/default.yaml") -> Settings:
    """Load and validate settings from ``path`` plus environment overrides."""
    raise NotImplementedError("config loading lands in v0.1 — see BACKLOG.md SN-001")

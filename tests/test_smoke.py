"""Smoke test: proves the test harness and CI wiring run before real tests exist."""

from __future__ import annotations

import shopnavigator


def test_package_is_importable() -> None:
    assert shopnavigator.__version__


def test_src_layout_is_on_the_path() -> None:
    from shopnavigator.simulator import store

    assert store.Store(seed=1).seed == 1

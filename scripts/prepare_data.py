"""Prepare the local catalog and task files.

TODO(v0.1): download or copy the chosen WebShop subset into ``data/raw/``, normalise products into
``data/processed/catalog.json``, and freeze ``data/tasks/tasks.json`` with seeds so every reported
number can be reproduced. Never write credentials or restricted data into the repository.
"""

from __future__ import annotations


def main() -> int:
    """Run data preparation end to end."""
    raise NotImplementedError("data preparation lands in v0.1 — see BACKLOG.md SN-001")


if __name__ == "__main__":
    raise SystemExit(main())

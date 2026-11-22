"""Run a single shopping task from the command line (demo/debug helper).

Target usage::

    python scripts/run_demo.py --goal "15-inch laptop, 16 GB RAM, under $900" --seed 42

TODO(v0.2): wire to the agent loop and print the step-by-step trace plus the final constraint check.
"""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run one ShopNavigator task.")
    parser.add_argument("--goal", required=True, help="natural-language shopping goal")
    parser.add_argument("--seed", type=int, default=42, help="task seed for reproducibility")
    parser.parse_args(argv)
    raise NotImplementedError("demo CLI lands in v0.2 — see BACKLOG.md SN-004")


if __name__ == "__main__":
    raise SystemExit(main())

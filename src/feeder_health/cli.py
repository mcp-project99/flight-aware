"""Command-line entry point for the local feeder health checker."""

from __future__ import annotations

import argparse
import json

from .checks import run_checks


DEFAULT_SERVICES = ("piaware", "dump1090-fa")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run privacy-first local health checks for an ADS-B feeder."
    )
    parser.add_argument(
        "--service",
        action="append",
        dest="services",
        help="Service to inspect; repeat for more than one. Defaults to PiAware services.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = run_checks(args.services or DEFAULT_SERVICES)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

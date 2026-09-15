#!/usr/bin/env python3
"""Regenerate the progress table and badge in README.md from stars.json.

The table lives between the two marker comments in README.md, so everything
written by hand around it survives regeneration.

    python tools/make_readme.py            # rewrite README.md in place
    python tools/make_readme.py --check     # exit 1 if README.md is stale (for CI)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STARS = ROOT / "stars.json"
README = ROOT / "README.md"

BEGIN = "<!-- progress:begin -->"
END = "<!-- progress:end -->"

BADGE = (
    "![Advent of Code](https://img.shields.io/badge/Advent%20of%20Code-{total}%20%E2%98%85"
    "-ffff66?style=flat-square&logo=adventofcode&logoColor=ffff66&labelColor=0f0f23)"
)


def load_years() -> tuple[list[dict], int]:
    data = json.loads(STARS.read_text(encoding="utf-8"))
    years = sorted(data["years"], key=lambda y: y["year"], reverse=True)
    for entry in years:
        if entry["stars"] > entry["available"]:
            raise ValueError(
                f"{entry['year']}: stars ({entry['stars']}) exceeds "
                f"available ({entry['available']})"
            )
    return years, sum(y["stars"] for y in years)


def render(years: list[dict], total: int) -> str:
    lines = [
        BADGE.format(total=total),
        "",
        "| Year | Stars | Completion | |",
        "| :--- | ----: | ---------: | :--- |",
    ]
    for entry in years:
        stars, available = entry["stars"], entry["available"]
        pct = 100.0 * stars / available if available else 0.0
        filled = round(pct / 10)
        bar = "█" * filled + "░" * (10 - filled)
        link = f"https://adventofcode.com/{entry['year']}"
        lines.append(
            f"| [{entry['year']}]({link}) | {stars} / {available} | {pct:.0f}% | `{bar}` |"
        )
    lines += ["", f"**Total: {total} ★**"]
    return "\n".join(lines)


def splice(readme: str, block: str) -> str:
    if BEGIN not in readme or END not in readme:
        raise SystemExit(
            f"README.md is missing the {BEGIN} / {END} markers; add them and rerun."
        )
    head = readme.split(BEGIN)[0]
    tail = readme.split(END)[1]
    return f"{head}{BEGIN}\n{block}\n{END}{tail}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit 1 if README.md is out of date",
    )
    args = parser.parse_args()

    years, total = load_years()
    current = README.read_text(encoding="utf-8")
    updated = splice(current, render(years, total))

    if args.check:
        if updated != current:
            print("README.md is out of date; run: python tools/make_readme.py")
            return 1
        print("README.md is up to date.")
        return 0

    if updated == current:
        print("README.md already up to date.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"README.md updated ({total} stars across {len(years)} events).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

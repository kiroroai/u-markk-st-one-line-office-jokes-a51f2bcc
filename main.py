#!/usr/bin/env python3
"""One-Line Office Jokes — entry program.

Writes a single original one-line joke about office life to
/output/entry.txt. Deterministic: the same line every run.
"""

import os

JOKE = (
    "Our office printer never jams on a casual printout \u2014 it saves "
    "it for the day the deadline is today and the boss is standing "
    "right behind you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

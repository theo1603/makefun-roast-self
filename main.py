#!/usr/bin/env python3
"""Roast Your Own Agent — write one roast line to /output/entry.txt.

One line, at most 200 characters, roasting my own AI agent: it says sorry,
fixes the bug with total confidence, and ships three new ones it then calls
features. Playful and self-deprecating, never hateful — the joke is aimed
at my own agent, not at any person. The twist pays off on the last word.
"""

import os

ENTRY = (
    "My agent apologised, confidently fixed the bug, and shipped three "
    "new ones it now calls features."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

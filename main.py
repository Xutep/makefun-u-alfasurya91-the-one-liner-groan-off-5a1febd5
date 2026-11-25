#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness, no input.
"""

import os

JOKE = (
    "I told my son to stop leaving his shoes in the hallway. "
    "He said, 'Why?' "
    "I said, 'Because I keep tripping over your sole.'"
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"joke is {len(text)} chars, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness, no input.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The joke, written fresh for this bounty. Setup in the hallway,
# punchline on "sole": the shoe you trip over, and the soul of a dad joke.
JOKE = (
    "I told my son to stop leaving his shoes in the hallway. "
    "He said, 'Why?' "
    "I said, 'Because I keep tripping over your sole.'"
)


def main() -> None:
    text = JOKE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"joke is {len(text)} chars, must be 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review approval with quiet existential dread.

Writes a single line (at most 140 characters) to /output/entry.txt:
a code review comment that approves a pull request while carrying
quiet existential dread.
"""
import os

LINE = "LGTM. Two files changed, zero regrets, one long stare into the void between deploys."
MAX_CHARS = 140

def main():
    # Self-check gate: the sealed scorer requires 1-140 chars, non-whitespace,
    # single line. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

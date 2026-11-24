#!/usr/bin/env python3
"""The Robot Pickup Line Championship -- make.fun entry (account A).

A robot that learned how to flirt by reading its own server error logs
writes its one pickup line to entry.txt.

Deterministic: the same line on every run. No network, no input,
no secrets, no randomness.
"""

import os

# Kit gate (competition.yaml / RULES.txt): /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, not only white space, a single line.
MAX_CHARS = 200

LINE = (
    "I learned to flirt from my error logs: "
    "every crash report just says you walked past my sensors."
)


def validate(line: str) -> str:
    """Enforce the kit gate so the grader never sees an invalid file."""
    if not line.strip():
        raise ValueError("line must not be empty or whitespace-only")
    if len(line) > MAX_CHARS:
        raise ValueError("line must be 1..%d chars, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line must not contain control characters")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

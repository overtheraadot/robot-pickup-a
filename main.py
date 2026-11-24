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
DEFAULT_OUTPUT = "/output/entry.txt"


def build_pickup_line() -> str:
    """Assemble the robot's one pickup line from its three beats."""
    setup = "I learned to flirt from my error logs: "
    twist = "every crash report just says "
    punchline = "you walked past my sensors."
    return setup + twist + punchline


def _check_not_blank(line: str) -> None:
    if not line.strip():
        raise ValueError("line must not be empty or whitespace-only")


def _check_length(line: str) -> None:
    if len(line) > MAX_CHARS:
        raise ValueError("line must be 1..%d chars, got %d" % (MAX_CHARS, len(line)))


def _check_single_line(line: str) -> None:
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line must not contain control characters")


def _check_no_padding(line: str) -> None:
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")


def validate(line: str) -> str:
    """Enforce the kit gate so the grader never sees an invalid file."""
    for check in (_check_not_blank, _check_length, _check_single_line, _check_no_padding):
        check(line)
    return line


def resolve_output_path() -> str:
    """Where the line goes.

    OUTPUT_PATH names the file directly when set; otherwise the output
    directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
    """
    direct = os.environ.get("OUTPUT_PATH")
    if direct:
        return direct
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def ensure_parent_dir(path: str) -> None:
    """Create the output file's parent directory if it has one."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def write_entry(line: str, path: str) -> None:
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    line = validate(build_pickup_line())
    write_entry(line, resolve_output_path())


if __name__ == "__main__":
    main()

"""Entry for make.fun: The Funniest Excuse for Skipping a Meeting.

Writes one line (at most 200 characters) to the output directory as
entry.txt: the excuse for skipping a pointless work meeting. The joke is
a single concrete scene, told flat: the last "quick sync" ran 94 minutes
and ended by booking a second meeting. No wifi, no cat, no dentist --
just the meeting that reproduces itself.
"""

import os
import sys

LINE = (
    "Can't make it \u2014 the last 'quick sync' ran 94 minutes and ended "
    "by booking a second meeting."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the excuse is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the excuse must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the excuse is {len(text)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read the file back: the grader scores exactly what landed on disk,
    # so a short or garbled write must fail loudly here, not silently there.
    with open(target, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print(
                "error: written entry does not match the excuse",
                file=sys.stderr,
            )
            return 1
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

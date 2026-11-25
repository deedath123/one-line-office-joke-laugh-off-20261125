#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes the single-line office joke to /output/entry.txt.
Standard library only; no network, no files, no fonts.
"""

import os

ENTRY = (
    "Finance rejected my $4 pen \u2014 it needed a manager's signature "
    "\u2014 so we spent $214 of salaries in a meeting to approve it, "
    "and Dave signed it with Finance's own pen."
)


def _check_entry(text: str) -> None:
    """Validation guard: entry must be a single non-blank line, 1-200 chars."""
    assert isinstance(text, str) and text.strip(), "entry must be non-blank"
    assert "\n" not in text and "\r" not in text, "entry must be single-line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"


def main() -> None:
    _check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

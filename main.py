"""The Funniest Out-of-Office -- make.fun bounty entry.

Writes a single-line out-of-office auto-reply (TEXT) verbatim to
$OUTPUT_DIR/entry.txt (default /output). Stdlib-only, deterministic,
no network, no randomness, no external input.
"""

import os
import unicodedata
from pathlib import Path

TEXT = "I'm out of the office and my inbox has unionised: it refuses to answer until I return, and frankly, it's winning."

MAX_CHARS = 140


def main() -> int:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Returns 0 on success. Raises ValueError (and writes nothing) when
    TEXT fails the gate: 1-140 characters, not whitespace-only, a single
    line, no leading/trailing whitespace, no control characters, ASCII.
    """
    text = TEXT  # read the global live, at call time (tests patch it)

    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"TEXT must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("TEXT must not be whitespace-only")
    if text != text.strip():
        raise ValueError("TEXT must not start or end with whitespace")
    if any(unicodedata.category(ch) == "Cc" or ch == "\x7f" for ch in text):
        raise ValueError("TEXT must not contain control characters")
    if not text.isascii():
        raise ValueError("TEXT must be pure ASCII")

    # Empty OUTPUT_DIR counts as unset (PLAN contract): fall back to /output.
    # os.environ.get("OUTPUT_DIR", "/output") alone would return "" and
    # Path("") resolves to ".", writing entry.txt into the working directory.
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

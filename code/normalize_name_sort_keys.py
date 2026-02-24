#!/usr/bin/env python3
"""Add ASCII sort keys to non-ASCII name index tags.

Rewrites:
  \\ixnq{Gärdenfors, Peter}
to:
  \\ixnq{Gardenfors, Peter@Gärdenfors, Peter}

This preserves printed form while forcing stable alphabetization.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path


IXNQ_RE = re.compile(r"\\ixnq\{([^{}]+)\}")

# Characters not reliably decomposed by NFKD.
EXTRA_MAP = str.maketrans(
    {
        "ß": "ss",
        "ẞ": "SS",
        "Ł": "L",
        "ł": "l",
        "Ø": "O",
        "ø": "o",
        "Đ": "D",
        "đ": "d",
        "Æ": "AE",
        "æ": "ae",
        "Œ": "OE",
        "œ": "oe",
        "Þ": "Th",
        "þ": "th",
        "Ð": "D",
        "ð": "d",
    }
)


def ascii_sort_key(text: str) -> str:
    t = text.translate(EXTRA_MAP)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    # Drop any remaining non-ASCII codepoints to avoid makeindex surprises.
    t = "".join(ch for ch in t if ord(ch) < 128)
    # Normalize spaces around punctuation.
    t = re.sub(r"\s+", " ", t).strip()
    return t


def rewrite_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        body = m.group(1).strip()
        if "@" in body:
            return m.group(0)
        if all(ord(ch) < 128 for ch in body):
            return m.group(0)
        key = ascii_sort_key(body)
        if not key or key == body:
            return m.group(0)
        count += 1
        return f"\\ixnq{{{key}@{body}}}"

    out = IXNQ_RE.sub(repl, text)
    return out, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapters-dir",
        default="chapters",
        help="Directory containing chapter .tex files (default: chapters)",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes in place (default: dry run)",
    )
    args = parser.parse_args()

    files = sorted(Path(args.chapters_dir).glob("*.tex"))
    touched = 0
    total = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        out, n = rewrite_text(text)
        if n == 0:
            continue
        touched += 1
        total += n
        if args.write:
            path.write_text(out, encoding="utf-8")
        verb = "updated" if args.write else "would update"
        print(f"{path}: {verb}, sort_keys_added={n}")

    print(
        f"Done. files_{'updated' if args.write else 'would_update'}={touched}, "
        f"sort_keys_added={total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

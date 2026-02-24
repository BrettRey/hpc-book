#!/usr/bin/env python3
"""Normalize redundant reverse see/seealso cross-references.

Rule:
- If `A|see{B}` exists, remove `B|seealso{A}` for the same index command.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


XREF_RE = re.compile(
    r"\\(?P<cmd>ix[a-z]+)\{(?P<src>[^|{}]+)\|(?P<kind>see|seealso)\{(?P<tgt>[^{}]+)\}\}"
)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def normalize_crossrefs(path: Path, write: bool) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    matches: list[tuple[int, str, str, str, str]] = []
    for i, line in enumerate(lines):
        m = XREF_RE.search(line)
        if not m:
            continue
        matches.append(
            (
                i,
                m.group("cmd"),
                m.group("kind"),
                m.group("src").strip(),
                m.group("tgt").strip(),
            )
        )

    see_pairs: set[tuple[str, str, str]] = set()
    for _, cmd, kind, src, tgt in matches:
        if kind != "see":
            continue
        see_pairs.add((cmd, norm(src), norm(tgt)))

    drop_indexes: set[int] = set()
    for i, cmd, kind, src, tgt in matches:
        if kind != "seealso":
            continue
        if (cmd, norm(tgt), norm(src)) in see_pairs:
            drop_indexes.add(i)

    if write and drop_indexes:
        new_lines = [line for i, line in enumerate(lines) if i not in drop_indexes]
        path.write_text("".join(new_lines), encoding="utf-8")

    return len(matches), len(drop_indexes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        help="Cross-reference .tex files to normalize",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write normalized files in place (default: dry run)",
    )
    args = parser.parse_args()

    total_matches = 0
    total_dropped = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        matches, dropped = normalize_crossrefs(path, write=args.write)
        total_matches += matches
        total_dropped += dropped
        action = "updated" if args.write else "would update"
        print(f"{path}: {action}, xrefs={matches}, removed={dropped}")

    print(f"Done. xrefs={total_matches}, removed={total_dropped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

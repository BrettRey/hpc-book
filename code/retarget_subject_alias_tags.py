#!/usr/bin/env python3
"""Retarget subject index tags from alias heads to canonical see-targets.

Reads subject alias mappings from frontmatter/index-crossrefs.tex lines of the form:
  \\ixsq{alias|see{canonical}}

Then rewrites chapter tags so aliases no longer accumulate independent page lists.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SEE_RE = re.compile(r"\\ixsq\{(?P<alias>[^|{}]+)\|see\{(?P<target>[^{}]+)\}\}")


def load_alias_map(crossrefs_path: Path) -> dict[str, str]:
    text = crossrefs_path.read_text(encoding="utf-8")
    mapping: dict[str, str] = {}
    for m in SEE_RE.finditer(text):
        alias = m.group("alias").strip()
        target = m.group("target").strip()
        if alias and target and alias != target:
            mapping[alias] = target
    return mapping


def replace_subject_aliases(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    total = 0
    out = text

    # Longest aliases first to avoid accidental partial overlap.
    for alias, target in sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True):
        patterns = (
            (rf"\\ixsq\{{{re.escape(alias)}\}}", rf"\\ixsq{{{target}}}"),
            (rf"\\ixs\{{{re.escape(alias)}\}}", rf"\\ixs{{{target}}}"),
            (
                rf"\\index\[subject\]\{{{re.escape(alias)}\}}",
                rf"\\index[subject]{{{target}}}",
            ),
        )
        for pat, repl in patterns:
            out, n = re.subn(pat, repl, out)
            total += n
    return out, total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--crossrefs",
        default="frontmatter/index-crossrefs.tex",
        help="Path to subject cross-reference scaffold",
    )
    parser.add_argument(
        "--chapters-dir",
        default="chapters",
        help="Directory containing chapter .tex files",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes in place (default: dry run)",
    )
    args = parser.parse_args()

    crossrefs_path = Path(args.crossrefs)
    chapters_dir = Path(args.chapters_dir)
    mapping = load_alias_map(crossrefs_path)

    if not mapping:
        print("No subject alias mappings found.")
        return 0

    print(f"Loaded {len(mapping)} alias mapping(s) from {crossrefs_path}")
    for alias, target in sorted(mapping.items()):
        print(f"  {alias} -> {target}")

    files = sorted(chapters_dir.glob("*.tex"))
    total_files = 0
    total_replacements = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        out, n = replace_subject_aliases(text, mapping)
        if n == 0:
            continue
        total_files += 1
        total_replacements += n
        if args.write:
            path.write_text(out, encoding="utf-8")
        verb = "updated" if args.write else "would update"
        print(f"{path}: {verb}, replacements={n}")

    print(
        f"Done. files_{'updated' if args.write else 'would_update'}={total_files}, "
        f"replacements={total_replacements}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

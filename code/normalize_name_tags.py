#!/usr/bin/env python3
"""Normalize duplicate name-index tags to a canonical form.

Detects near-duplicate names by (family name, first given token), then rewrites
`\ixn{...}` / `\ixnq{...}` / `\index[names]{...}` tags in chapter files to use
one canonical spelling per cluster.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


ITEM_RE = re.compile(r"\s*\\item\s+(.+?)(?:,\s+\d|,\s+\\see|,\s+\\seealso|$)")


def parse_names_ind(path: Path) -> list[str]:
    entries: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ITEM_RE.match(line)
        if m:
            entries.append(m.group(1).strip())
    return entries


def name_key(name: str) -> tuple[str, str]:
    s = name.replace(".", "").strip()
    if "," in s:
        family, given = [part.strip() for part in s.split(",", 1)]
    else:
        parts = s.split()
        family = parts[0] if parts else s
        given = " ".join(parts[1:]) if len(parts) > 1 else ""
    first_given = given.split()[0].lower() if given.split() else ""
    return family.lower(), first_given


def score_name(name: str) -> tuple[int, int, int]:
    # Prefer richer forms: longer alnum payload and explicit initials with periods.
    alnum_len = len(re.sub(r"[^A-Za-z0-9]", "", name))
    has_period = 1 if "." in name else 0
    token_count = len(name.replace(",", " ").split())
    return alnum_len, has_period, token_count


def build_alias_map(entries: list[str]) -> dict[str, str]:
    clusters: dict[tuple[str, str], set[str]] = defaultdict(set)
    for entry in entries:
        clusters[name_key(entry)].add(entry)

    mapping: dict[str, str] = {}
    for _, names in sorted(clusters.items()):
        if len(names) < 2:
            continue
        ordered = sorted(names, key=lambda n: score_name(n), reverse=True)
        canonical = ordered[0]
        for alias in ordered[1:]:
            mapping[alias] = canonical
    return mapping


def replace_name_tags(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    out = text
    total = 0
    for alias, canonical in sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True):
        patterns = (
            (rf"\\ixnq\{{{re.escape(alias)}\}}", rf"\\ixnq{{{canonical}}}"),
            (rf"\\ixn\{{{re.escape(alias)}\}}", rf"\\ixn{{{canonical}}}"),
            (rf"\\index\[names\]\{{{re.escape(alias)}\}}", rf"\\index[names]{{{canonical}}}"),
        )
        for pat, repl in patterns:
            out, n = re.subn(pat, repl, out)
            total += n
    return out, total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--names-ind",
        default="build/names.ind",
        help="Path to generated names.ind file used to detect duplicates",
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

    names = parse_names_ind(Path(args.names_ind))
    mapping = build_alias_map(names)
    if not mapping:
        print("No duplicate name clusters found.")
        return 0

    print(f"Duplicate mappings: {len(mapping)}")
    for alias, canonical in sorted(mapping.items()):
        print(f"  {alias} -> {canonical}")

    files = sorted(Path(args.chapters_dir).glob("*.tex"))
    total_files = 0
    total_replacements = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        out, n = replace_name_tags(text, mapping)
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

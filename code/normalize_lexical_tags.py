#!/usr/bin/env python3
"""Normalize lexical index sort keys to canonical lemma forms.

This rewrites the first argument of lexical-tag macros:
- \\ixlq{...}
- \\ixlqs{sort}{display}
- \\ixlgq{sort}{display}{language}
- \\ixlgqs{sort}{display}{language}{gloss}

Display forms are left unchanged; only sort/canonical keys are normalized.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


CANONICAL = {
    "adjectives": "adjective",
    "balls": "ball",
    "books": "book",
    "cats": "cat",
    "dogs": "dog",
    "eaten": "eat",
    "eating": "eat",
    "emojis": "emoji",
    "furnitures": "furniture",
    "nouns": "noun",
    "phonemes": "phoneme",
    "problems": "problem",
    "students": "student",
    "wugs": "wug",
}


IXLQ_RE = re.compile(r"\\ixlq\{([^{}]+)\}")
IXLQS_RE = re.compile(r"\\ixlqs\{([^{}]+)\}\{([^{}]+)\}")
IXLGQ_RE = re.compile(r"\\ixlgq\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}")
IXLGQS_RE = re.compile(r"\\ixlgqs\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}")


def normalize_key(key: str) -> str | None:
    return CANONICAL.get(key.lower())


def rewrite_text(text: str, stats: Counter[str]) -> str:
    def repl_ixlq(m: re.Match[str]) -> str:
        key = m.group(1)
        norm = normalize_key(key)
        if not norm:
            return m.group(0)
        stats[f"{key}->{norm}"] += 1
        return f"\\ixlq{{{norm}}}"

    def repl_ixlqs(m: re.Match[str]) -> str:
        key, display = m.group(1), m.group(2)
        norm = normalize_key(key)
        if not norm:
            return m.group(0)
        stats[f"{key}->{norm}"] += 1
        return f"\\ixlqs{{{norm}}}{{{display}}}"

    def repl_ixlgq(m: re.Match[str]) -> str:
        key, display, lang = m.group(1), m.group(2), m.group(3)
        norm = normalize_key(key)
        if not norm:
            return m.group(0)
        stats[f"{key}->{norm}"] += 1
        return f"\\ixlgq{{{norm}}}{{{display}}}{{{lang}}}"

    def repl_ixlgqs(m: re.Match[str]) -> str:
        key, display, lang, gloss = m.group(1), m.group(2), m.group(3), m.group(4)
        norm = normalize_key(key)
        if not norm:
            return m.group(0)
        stats[f"{key}->{norm}"] += 1
        return f"\\ixlgqs{{{norm}}}{{{display}}}{{{lang}}}{{{gloss}}}"

    text = IXLGQS_RE.sub(repl_ixlgqs, text)
    text = IXLGQ_RE.sub(repl_ixlgq, text)
    text = IXLQS_RE.sub(repl_ixlqs, text)
    text = IXLQ_RE.sub(repl_ixlq, text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapters-dir",
        default="chapters",
        help="Directory containing chapter .tex files (default: chapters)",
    )
    args = parser.parse_args()

    chapters_dir = Path(args.chapters_dir)
    files = sorted(chapters_dir.glob("*.tex"))

    stats: Counter[str] = Counter()
    touched = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        out = rewrite_text(text, stats)
        if out != text:
            path.write_text(out, encoding="utf-8")
            touched += 1
            print(path)

    print(f"files_touched={touched}")
    for key, count in sorted(stats.items()):
        print(f"{key}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Tag language names across all chapter .tex files.

Inserts quiet language index tags (\\ixgq{...}) after matched language names
and language-variety names throughout chapters.

The matcher uses a curated, book-specific lexicon plus basic guards to avoid
common false positives (e.g., ``French fries`` and author-surname contexts like
``French (2021)``).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Map surface forms in the text to canonical index entries.
# Longest forms are matched first.
LANGUAGE_INDEX_MAP = {
    # English and varieties
    "Historical American English": "English!Historical American",
    "Contemporary American English": "English!Contemporary American",
    "Early Modern English": "English!Early Modern",
    "Middle English": "English!Middle",
    "Old English": "English!Old",
    "Modern English": "English!Modern",
    "African American English": "English!African American (AAVE)",
    "Standard English": "English!Standard",
    "Canadian English": "English!Canadian",
    "American English": "English!American",
    "Internet English": "English!Internet",
    "AAVE": "English!African American (AAVE)",
    "AAE": "English!African American (AAVE)",
    "English": "English",

    # Sign languages / named sign systems
    "Al-Sayyid Bedouin Sign Language": "Al-Sayyid Bedouin Sign Language (ABSL)",
    "Nicaraguan Sign Language": "Nicaraguan Sign Language (NSL)",
    "Israeli Sign Language": "Israeli Sign Language",
    "Japanese Sign Language": "Japanese Sign Language",
    "Kata Kolok": "Kata Kolok",
    "ABSL": "Al-Sayyid Bedouin Sign Language (ABSL)",
    "NSL": "Nicaraguan Sign Language (NSL)",
    "BSL": "British Sign Language (BSL)",
    "ISN": "Nicaraguan Sign Language (NSL)",

    # Spoken languages
    "Mandarin Chinese": "Chinese!Mandarin",
    "Proto-Indo-European": "Proto-Indo-European",
    "Old Norse": "Old Norse",
    "French": "French",
    "German": "German",
    "Polish": "Polish",
    "Japanese": "Japanese",
    "Spanish": "Spanish",
    "Russian": "Russian",
    "Dutch": "Dutch",
    "Greek": "Greek",
    "Italian": "Italian",
    "Latin": "Latin",
    "Bulgarian": "Bulgarian",
    "Turkish": "Turkish",
    "Tibetan": "Tibetan",
    "Arabic": "Arabic",
    "Swahili": "Swahili",
    "Shilluk": "Shilluk",
    "Tagalog": "Tagalog",
    "Indonesian": "Indonesian",
    "Navajo": "Navajo",
    "Mohawk": "Mohawk",
    "Quechua": "Quechua",
    "Halkomelem": "Halkomelem",
    "Dyirbal": "Dyirbal",
    "Zulu": "Zulu",
    "Mandarin": "Chinese!Mandarin",
    "PIE": "Proto-Indo-European",

    # Families/areal groupings discussed as language groupings
    "Amazonian languages": "Amazonian languages",
    "Scandinavian": "Scandinavian languages",
    "Algonquian": "Algonquian languages",
    "Slavic": "Slavic languages",
    "Bantu": "Bantu languages",
}

# Skip matches inside existing indexing commands.
IGNORE_SPAN_RE = re.compile(
    r"\\(?:ixs|ixn|ixl|ixg|ixsq|ixnq|ixlq|ixgq)\{[^{}]*\}|"
    r"\\index\[[^\[\]{}]+\]\{[^{}]*\}"
)

FOLLOWING_LANG_TAG_RE = re.compile(r"\s*\\ixgq\{[^{}]+\}")


def compile_language_regex() -> re.Pattern[str]:
    terms = sorted(LANGUAGE_INDEX_MAP, key=len, reverse=True)
    alts = "|".join(re.escape(term) for term in terms)
    # Do not match command names (preceded by backslash) or inside longer words.
    return re.compile(r"(?<![\\A-Za-z])(?P<lemma>" + alts + r")(?P<poss>'s)?(?![A-Za-z])")


LANGUAGE_RE = compile_language_regex()


def build_ignore_spans(text: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in IGNORE_SPAN_RE.finditer(text)]


def in_ignore_span(pos: int, spans: list[tuple[int, int]]) -> bool:
    for start, end in spans:
        if start <= pos < end:
            return True
        if start > pos:
            return False
    return False


def looks_like_author_citation(text: str, end: int) -> bool:
    # e.g. "French (2021)" likely surname use, not language mention.
    return bool(re.match(r"\s*\((?:19|20)\d{2}[a-z]?\)", text[end:]))


def false_positive_context(lemma: str, text: str, start: int, end: int) -> bool:
    if lemma == "French":
        if re.match(r"\s+fries\b", text[end:]):
            return True
    if looks_like_author_citation(text, end):
        return True
    # Suppress all-caps acronym matches inside longer all-caps strings.
    if lemma.isupper():
        left = text[start - 1] if start > 0 else ""
        right = text[end] if end < len(text) else ""
        if left.isupper() or right.isupper():
            return True
    return False


def tag_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    spans = build_ignore_spans(text)
    insertions: list[tuple[int, str]] = []

    for m in LANGUAGE_RE.finditer(text):
        start = m.start()
        end = m.end()
        lemma = m.group("lemma")
        if in_ignore_span(start, spans):
            continue
        if false_positive_context(lemma, text, start, end):
            continue
        if FOLLOWING_LANG_TAG_RE.match(text, end):
            continue
        canonical = LANGUAGE_INDEX_MAP[lemma]
        insertions.append((end, f"\\ixgq{{{canonical}}}"))

    if not insertions:
        return 0

    insertions.sort(key=lambda x: x[0], reverse=True)
    out = text
    for pos, payload in insertions:
        out = out[:pos] + payload + out[pos:]
    path.write_text(out, encoding="utf-8")
    return len(insertions)


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

    total = 0
    touched = 0
    for path in files:
        n = tag_file(path)
        if n:
            touched += 1
            total += n
            print(f"{path}: +{n} languages")

    print(f"Done. files_touched={touched}, language_inserted={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

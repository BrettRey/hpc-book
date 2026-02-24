#!/usr/bin/env python3
"""Tag names and lexical items across all chapter .tex files.

Name tags:
- Insert \\ixnq{Family, Given} before \\textcite / \\citet / \\citeauthor
  commands based on citation keys resolved via references.bib files.

Lexical tags:
- Insert \\ixlq{term} after \\mention{term} when term looks like a simple
  lexical item and no immediate lexical tag already follows.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

import bibtexparser


CITE_CMDS = (
    "textcite",
    "citet",
    "citeauthor",
    "citep",
    "parencite",
    "autocite",
    "citealt",
    "cite",
)

CITE_RE = re.compile(
    r"\\(?P<cmd>" + "|".join(CITE_CMDS) + r")\*?(?:\[[^\]]*\]){0,2}\{(?P<keys>[^}]*)\}"
)
MENTION_RE = re.compile(r"\\mention\{(?P<body>[^{}]*)\}")
ADJACENT_NAME_TAGS_RE = re.compile(r"(?:\\ixnq\{([^{}]+)\}\s*)+$")
FOLLOWING_LEX_TAG_RE = re.compile(r"\s*\\ixlq\{[^{}]+\}")

# Keep this conservative to avoid indexing full phrases/sentences.
LEX_SIMPLE_RE = re.compile(r"^[A-Za-z][A-Za-z'-]*$")
LEX_AFFIX_RE = re.compile(r"^-[A-Za-z]+$")
LEX_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "for",
    "from",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "were",
    "with",
}


def clean_latex_text(text: str) -> str:
    # Strip braces used for BibTeX capitalization control and collapse spaces.
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_author_name(raw: str) -> str | None:
    name = clean_latex_text(raw)
    if not name:
        return None
    if name.lower() == "others":
        return None
    if "," in name:
        parts = [p.strip() for p in name.split(",") if p.strip()]
        if not parts:
            return None
        family = parts[0]
        given = " ".join(parts[1:]).strip()
    else:
        bits = name.split()
        if not bits:
            return None
        if len(bits) == 1:
            family = bits[0]
            given = ""
        else:
            family = bits[-1]
            given = " ".join(bits[:-1])
    if not family:
        return None
    return f"{family}, {given}".strip(", ")


def parse_authors_field(author_field: str) -> list[str]:
    if not author_field:
        return []
    parts = re.split(r"\s+and\s+", author_field)
    authors: list[str] = []
    for part in parts:
        parsed = parse_author_name(part)
        if parsed:
            authors.append(parsed)
    return authors


def load_citation_author_map(bib_paths: Iterable[Path]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for path in bib_paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            db = bibtexparser.load(handle)
        for entry in db.entries:
            key = str(entry.get("ID", "")).strip()
            if not key:
                continue
            authors = parse_authors_field(str(entry.get("author", "")).strip())
            if authors:
                mapping[key] = authors
    return mapping


def normalize_lexical_term(text: str) -> str | None:
    value = clean_latex_text(text)
    if not value:
        return None
    if "\\" in value:
        return None
    if LEX_AFFIX_RE.fullmatch(value):
        return value
    if not LEX_SIMPLE_RE.fullmatch(value):
        return None
    if value.lower() in LEX_STOPWORDS:
        return None
    # Sentence-initial capitalization often appears in mentions.
    if value[:1].isupper() and value[1:].islower():
        return value.lower()
    return value


def extract_adjacent_name_tags(prefix: str) -> set[str]:
    tags: set[str] = set()
    # Collect only trailing adjacent ixnq tags.
    m = ADJACENT_NAME_TAGS_RE.search(prefix)
    if not m:
        return tags
    block = m.group(0)
    for tag in re.findall(r"\\ixnq\{([^{}]+)\}", block):
        tags.add(tag.strip())
    return tags


def tag_file(path: Path, author_map: dict[str, list[str]]) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    name_insertions: list[tuple[int, str]] = []
    lex_insertions: list[tuple[int, str]] = []

    # Name tags before in-text citation commands.
    for m in CITE_RE.finditer(text):
        start = m.start()
        keys_raw = m.group("keys")
        keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
        wanted: list[str] = []
        for key in keys:
            for author in author_map.get(key, []):
                if author not in wanted:
                    wanted.append(author)
        if not wanted:
            continue
        prefix = text[max(0, start - 400) : start]
        existing = extract_adjacent_name_tags(prefix)
        missing = [a for a in wanted if a not in existing]
        if not missing:
            continue
        tags = "".join(f"\\ixnq{{{author}}}" for author in missing)
        name_insertions.append((start, tags))

    # Lexical tags after mention commands (simple lexical items only).
    for m in MENTION_RE.finditer(text):
        end = m.end()
        body = m.group("body")
        term = normalize_lexical_term(body)
        if not term:
            continue
        if FOLLOWING_LEX_TAG_RE.match(text, end):
            continue
        lex_insertions.append((end, f"\\ixlq{{{term}}}"))

    if not name_insertions and not lex_insertions:
        return 0, 0

    insertions = name_insertions + lex_insertions
    insertions.sort(key=lambda x: x[0], reverse=True)
    out = text
    for pos, payload in insertions:
        out = out[:pos] + payload + out[pos:]
    path.write_text(out, encoding="utf-8")
    return len(name_insertions), len(lex_insertions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapters-dir",
        default="chapters",
        help="Directory containing chapter .tex files (default: chapters)",
    )
    parser.add_argument(
        "--bib",
        nargs="*",
        default=["references.bib", "references-local.bib"],
        help="Bib files used to resolve citation keys",
    )
    args = parser.parse_args()

    root = Path(".")
    chapters_dir = root / args.chapters_dir
    bib_paths = [root / b for b in args.bib]
    author_map = load_citation_author_map(bib_paths)

    files = sorted(chapters_dir.glob("*.tex"))
    total_name = 0
    total_lex = 0
    touched = 0
    for path in files:
        n, l = tag_file(path, author_map)
        if n or l:
            touched += 1
            total_name += n
            total_lex += l
            print(f"{path}: +{n} names, +{l} lexical")
    print(
        f"Done. files_touched={touched}, names_inserted={total_name}, lexical_inserted={total_lex}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

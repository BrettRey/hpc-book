#!/usr/bin/env python3
"""Tag names and lexical items across all chapter .tex files.

Name tags:
- Insert \\ixnq{Family, Given} before in-text citation commands using
  citation keys resolved via references.bib files.

Lexical tags:
- Insert \\ixlq{term} after \\mention{term} for simple lexical mentions.
- For complex \\mention{...} examples, infer topical terms from local context
  and add one or two \\ixlq{term} tags when confidence is high enough.
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
FOLLOWING_LEX_TAG_RE = re.compile(
    r"\s*(?:\\ixlq\{[^{}]+\}|\\ixlqs\{[^{}]+\}\{[^{}]+\}|"
    r"\\ixlgq\{[^{}]+\}\{[^{}]+\}\{[^{}]+\}|"
    r"\\ixlgqs\{[^{}]+\}\{[^{}]+\}\{[^{}]+\}\{[^{}]+\})"
)

# Keep this conservative to avoid indexing full phrases/sentences.
LEX_SIMPLE_RE = re.compile(r"^[A-Za-z][A-Za-z'-]*$")
LEX_AFFIX_RE = re.compile(r"^-[A-Za-z]+$")
LEX_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")
LEX_STOPWORDS = {
    "about",
    "after",
    "all",
    "also",
    "a",
    "an",
    "any",
    "and",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "but",
    "by",
    "can",
    "could",
    "did",
    "do",
    "does",
    "done",
    "for",
    "from",
    "get",
    "go",
    "goes",
    "going",
    "had",
    "has",
    "have",
    "he",
    "her",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "are",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "itself",
    "just",
    "left",
    "let",
    "like",
    "made",
    "make",
    "many",
    "me",
    "might",
    "more",
    "most",
    "my",
    "myself",
    "no",
    "not",
    "now",
    "in",
    "of",
    "on",
    "one",
    "only",
    "or",
    "other",
    "our",
    "ours",
    "ourselves",
    "out",
    "quite",
    "really",
    "say",
    "says",
    "see",
    "she",
    "should",
    "so",
    "some",
    "such",
    "than",
    "that",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "too",
    "up",
    "very",
    "was",
    "we",
    "well",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "why",
    "with",
    "would",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
}
LEX_CONTEXT_CUES = (
    "word",
    "words",
    "term",
    "terms",
    "label",
    "labels",
    "example",
    "examples",
    "expression",
    "expressions",
    "form",
    "forms",
    "item",
    "items",
    "called",
    "means",
    "meaning",
)
LEX_NP_HEAD_RE = re.compile(
    r"\b(?:the|a|an|this|that|these|those|my|your|his|her|our|their)\s+"
    r"(?:[A-Za-z][A-Za-z'-]*\s+){0,3}([A-Za-z][A-Za-z'-]*)\b",
    flags=re.IGNORECASE,
)
LEX_CONTEXT_WINDOW = 240
LEX_COMPLEX_MIN_SCORE = 4
LEX_COMPLEX_MAX_TERMS = 1


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


def extract_existing_lexical_terms(text: str) -> set[str]:
    terms: set[str] = set()
    for m in re.finditer(r"\\ixlq\{([^{}]+)\}", text):
        terms.add(m.group(1).strip().lower())
    for m in re.finditer(r"\\ixlqs\{([^{}]+)\}\{[^{}]+\}", text):
        terms.add(m.group(1).strip().lower())
    for m in re.finditer(r"\\ixlgq\{([^{}]+)\}\{[^{}]+\}\{[^{}]+\}", text):
        terms.add(m.group(1).strip().lower())
    for m in re.finditer(
        r"\\ixlgqs\{([^{}]+)\}\{[^{}]+\}\{[^{}]+\}\{[^{}]+\}", text
    ):
        terms.add(m.group(1).strip().lower())
    return terms


def singular_fallback(word: str) -> str:
    if len(word) <= 3:
        return word
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith("es") and len(word) > 4:
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def tokenise_for_scoring(text: str) -> list[str]:
    return [t.lower() for t in LEX_TOKEN_RE.findall(clean_latex_text(text))]


def infer_complex_mention_terms(
    body: str, prefix: str, suffix: str, known_terms: set[str]
) -> list[str]:
    # Skip command-heavy mentions; these are usually not lexical exemplars.
    if "\\" in body:
        return []
    cleaned = clean_latex_text(body)
    raw_tokens = LEX_TOKEN_RE.findall(cleaned)
    if not raw_tokens:
        return []

    candidates: list[str] = []
    seen: set[str] = set()
    for tok in raw_tokens:
        cand = tok.lower()
        if cand in seen:
            continue
        if cand in LEX_STOPWORDS:
            continue
        if len(cand) < 2:
            continue
        seen.add(cand)
        candidates.append(cand)
    if not candidates:
        return []

    head_candidates: set[str] = set()
    for m in LEX_NP_HEAD_RE.finditer(cleaned):
        head = m.group(1).lower()
        if head not in LEX_STOPWORDS:
            head_candidates.add(head)

    context_text = f"{prefix} {suffix}"
    context_tokens = tokenise_for_scoring(context_text)
    context_counts: dict[str, int] = {}
    for tok in context_tokens:
        context_counts[tok] = context_counts.get(tok, 0) + 1
    near_context = clean_latex_text(prefix[-160:]).lower()
    cue_bonus = any(cue in near_context for cue in LEX_CONTEXT_CUES)

    scored: list[tuple[int, int, str]] = []
    for i, cand in enumerate(candidates):
        # Keep only terms that are already lexicalized, clear NP heads,
        # or recurrent in the surrounding discussion.
        if (
            cand not in known_terms
            and cand not in head_candidates
            and context_counts.get(cand, 0) < 2
        ):
            continue
        score = 0
        if cand in head_candidates:
            score += 2
        if cand in known_terms:
            score += 2
        score += min(2, context_counts.get(cand, 0)) * 2
        singular = singular_fallback(cand)
        if singular != cand:
            score += min(1, context_counts.get(singular, 0))
        if cue_bonus and (context_counts.get(cand, 0) > 0):
            score += 1
        scored.append((score, -i, cand))

    scored.sort(reverse=True)
    picked: list[str] = []
    for score, _, cand in scored:
        if score < LEX_COMPLEX_MIN_SCORE:
            continue
        if cand not in picked:
            picked.append(cand)
        if len(picked) >= LEX_COMPLEX_MAX_TERMS:
            break

    # Fallback: for NP-like examples, index the head noun if it is context-backed.
    if not picked and head_candidates:
        # Determiner-headed lexical examples are common in this manuscript;
        # prefer these when context confirms the head word.
        for head in head_candidates:
            if context_counts.get(head, 0) > 0 or head in known_terms:
                picked.append(head)
                break

    return picked


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


def tag_file(
    path: Path, author_map: dict[str, list[str]], known_terms: set[str]
) -> tuple[int, int]:
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

    # Lexical tags after mention commands.
    for m in MENTION_RE.finditer(text):
        end = m.end()
        body = m.group("body")
        if FOLLOWING_LEX_TAG_RE.match(text, end):
            continue
        term = normalize_lexical_term(body)
        if term:
            lex_insertions.append((end, f"\\ixlq{{{term}}}"))
            continue

        prefix = text[max(0, m.start() - LEX_CONTEXT_WINDOW) : m.start()]
        suffix = text[end : end + LEX_CONTEXT_WINDOW]
        inferred = infer_complex_mention_terms(body, prefix, suffix, known_terms)
        if not inferred:
            continue
        tags = "".join(f"\\ixlq{{{term}}}" for term in inferred)
        lex_insertions.append((end, tags))

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
    known_terms: set[str] = set()
    for path in files:
        known_terms |= extract_existing_lexical_terms(path.read_text(encoding="utf-8"))

    total_name = 0
    total_lex = 0
    touched = 0
    for path in files:
        n, l = tag_file(path, author_map, known_terms)
        if n or l:
            touched += 1
            total_name += n
            total_lex += l
            print(f"{path}: +{n} names, +{l} lexical")
            # Make newly inserted terms available to later files in the run.
            known_terms |= extract_existing_lexical_terms(path.read_text(encoding="utf-8"))
    print(
        f"Done. files_touched={touched}, names_inserted={total_name}, lexical_inserted={total_lex}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

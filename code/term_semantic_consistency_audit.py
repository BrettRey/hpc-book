#!/usr/bin/env python3
"""Audit semantic consistency of glossary-backed term usage.

This audit only considers \term{...} usages that map to glossary terms. It does
NOT flag missing glossary entries. It flags potential semantic drift/outlier uses
based on context similarity to:
1) the glossary definition for the term, and
2) the term's own usage cluster across the book.

Outputs:
- Markdown report with flagged occurrences in context.
- Decisions CSV compatible with review_term_audit.py.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_DIR.parent

TERM_PATTERN = re.compile(r"\\term\{([^{}]+)\}")
ENTRY_START_PATTERN = re.compile(r"^\\newglossaryentry\{([^}]+)\}\{")

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "into",
    "is",
    "it",
    "its",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "was",
    "were",
    "with",
    "we",
    "you",
    "our",
    "not",
}


@dataclass(frozen=True)
class GlossaryTerm:
    key: str
    canonical: str
    aliases: Tuple[str, ...]
    definition: str
    definition_vector: Counter


@dataclass
class Occurrence:
    canonical: str
    observed: str
    file_path: str
    line: int
    context: str
    vector: Counter
    sim_definition: float = 0.0
    sim_cluster: float = 0.0
    score: float = 0.0


@dataclass
class FlaggedIssue:
    issue_id: str
    canonical: str
    observed: str
    file_path: str
    line: int
    context: str
    sim_definition: float
    sim_cluster: float
    score: float
    definition: str


def normalize_space(text: str) -> str:
    return " ".join(text.split())


def normalize_term(text: str) -> str:
    s = normalize_space(text).lower()
    s = s.replace("–", "-").replace("—", "-")
    s = s.replace("-", " ")
    s = s.replace("/", " ")
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return normalize_space(s)


def singularize(norm_term: str) -> List[str]:
    variants: List[str] = [norm_term]
    if norm_term.endswith("ies") and len(norm_term) > 4:
        variants.append(norm_term[:-3] + "y")
    if norm_term.endswith("es") and len(norm_term) > 4:
        variants.append(norm_term[:-2])
    if norm_term.endswith("s") and not norm_term.endswith("ss") and len(norm_term) > 3:
        variants.append(norm_term[:-1])
    return list(dict.fromkeys(v for v in variants if v))


def extract_braced_value(block_text: str, field_name: str) -> str:
    marker = f"{field_name}={{"
    start = block_text.find(marker)
    if start == -1:
        return ""
    i = start + len(marker)
    depth = 1
    out: List[str] = []
    while i < len(block_text):
        ch = block_text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                break
        out.append(ch)
        i += 1
    return "".join(out).strip()


def strip_latex_commands(text: str) -> str:
    s = text
    # Remove comments
    s = re.sub(r"(?<!\\)%.*", " ", s)
    # Drop common citation/index commands entirely.
    s = re.sub(r"\\(?:cite|citet|citep|textcite|parencite|ixs|ixn|ixl|ixsubj)\*?(?:\[[^\]]*\])?\{[^{}]*\}", " ", s)
    # Remove command names but keep potential argument text.
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", s)
    # Remove braces/backslashes and leftover TeX syntax markers.
    s = s.replace("{", " ").replace("}", " ").replace("\\", " ")
    s = s.replace("~", " ")
    s = s.replace("$", " ")
    return normalize_space(s)


def tokenize(text: str) -> List[str]:
    cleaned = strip_latex_commands(text).lower()
    cleaned = re.sub(r"[^a-z0-9 ]+", " ", cleaned)
    tokens = [t for t in cleaned.split() if len(t) > 1 and t not in STOPWORDS]
    return tokens


def vectorize(tokens: Iterable[str]) -> Counter:
    return Counter(tokens)


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    dot = 0.0
    for key, val in a.items():
        dot += val * b.get(key, 0)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def parse_glossary(glossary_path: Path) -> List[GlossaryTerm]:
    lines = glossary_path.read_text(encoding="utf-8").splitlines()
    entries: List[GlossaryTerm] = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = ENTRY_START_PATTERN.match(line)
        if not m:
            i += 1
            continue

        key = m.group(1)
        block_lines = [lines[i]]
        i += 1
        while i < len(lines):
            block_lines.append(lines[i])
            if lines[i].strip() == "}":
                break
            i += 1

        block_text = "\n".join(block_lines)
        name = normalize_space(extract_braced_value(block_text, "name"))
        text = normalize_space(extract_braced_value(block_text, "text"))
        desc = normalize_space(extract_braced_value(block_text, "description"))

        canonical = text or name
        if not canonical:
            i += 1
            continue

        aliases = tuple(dict.fromkeys([v for v in (canonical, name, text) if v]))
        definition = strip_latex_commands(desc)
        def_vec = vectorize(tokenize(definition))

        entries.append(
            GlossaryTerm(
                key=key,
                canonical=canonical,
                aliases=aliases,
                definition=definition,
                definition_vector=def_vec,
            )
        )
        i += 1

    return entries


def build_alias_maps(entries: Sequence[GlossaryTerm]) -> Tuple[Dict[str, str], Dict[str, List[str]]]:
    exact: Dict[str, str] = {}
    norm: Dict[str, List[str]] = defaultdict(list)

    for entry in entries:
        for alias in entry.aliases:
            if alias not in exact:
                exact[alias] = entry.canonical
            n = normalize_term(alias)
            if n and entry.canonical not in norm[n]:
                norm[n].append(entry.canonical)

    norm = {k: sorted(v) for k, v in norm.items()}
    return exact, norm


def resolve_term(observed: str, exact: Dict[str, str], norm: Dict[str, List[str]]) -> str:
    obs = normalize_space(observed)
    if obs in exact:
        return exact[obs]

    for n in singularize(normalize_term(obs)):
        cands = norm.get(n, [])
        if len(cands) == 1:
            return cands[0]
    return ""


def resolve_project_relative(path_str: str) -> Path:
    p = Path(path_str).expanduser()
    if p.is_absolute():
        return p.resolve()
    return (PROJECT_ROOT / p).resolve()


def expand_inputs(patterns: Sequence[str], excludes: Sequence[str]) -> List[Path]:
    exclude_set = set()
    for ex in excludes:
        ex_path = Path(ex).expanduser()
        if not ex_path.is_absolute():
            ex_path = PROJECT_ROOT / ex_path
        exclude_set.add(ex_path.resolve())

    found: List[Path] = []
    for pat in patterns:
        pat_path = Path(pat).expanduser()
        if not pat_path.is_absolute():
            pat = str(PROJECT_ROOT / pat_path)
        else:
            pat = str(pat_path)

        for p in glob.glob(pat, recursive=True):
            path = Path(p).resolve()
            if path.is_file() and path not in exclude_set:
                found.append(path)

    return sorted(set(found), key=lambda p: str(p))


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def make_context(text: str, start: int, end: int, observed: str, window: int = 240) -> str:
    left = max(0, start - window)
    right = min(len(text), end + window)
    snippet = normalize_space(text[left:right].replace("\n", " "))
    if observed in snippet:
        snippet = snippet.replace(observed, f"[[{observed}]]", 1)
    if left > 0:
        snippet = "... " + snippet
    if right < len(text):
        snippet = snippet + " ..."
    return snippet


def collect_occurrences(
    files: Sequence[Path],
    exact: Dict[str, str],
    norm: Dict[str, List[str]],
) -> Dict[str, List[Occurrence]]:
    grouped: Dict[str, List[Occurrence]] = defaultdict(list)

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(PROJECT_ROOT)) if path.is_relative_to(PROJECT_ROOT) else str(path)
        for m in TERM_PATTERN.finditer(text):
            observed = normalize_space(m.group(1))
            canonical = resolve_term(observed, exact, norm)
            if not canonical:
                continue
            context = make_context(text, m.start(), m.end(), observed)
            tokens = tokenize(context)
            vec = vectorize(tokens)
            occ = Occurrence(
                canonical=canonical,
                observed=observed,
                file_path=rel,
                line=line_number(text, m.start()),
                context=context,
                vector=vec,
            )
            grouped[canonical].append(occ)

    return grouped


def robust_threshold(values: List[float]) -> float:
    if not values:
        return 0.0
    med = statistics.median(values)
    if len(values) < 3:
        return med - 0.12
    abs_dev = [abs(v - med) for v in values]
    mad = statistics.median(abs_dev)
    return med - max(0.10, 1.5 * mad)


def flag_outliers(
    occurrences_by_term: Dict[str, List[Occurrence]],
    glossary_by_canonical: Dict[str, GlossaryTerm],
    *,
    min_occurrences: int,
    max_flags_per_term: int,
) -> List[FlaggedIssue]:
    flagged: List[FlaggedIssue] = []
    issue_num = 1

    for canonical in sorted(occurrences_by_term):
        occs = occurrences_by_term[canonical]
        if len(occs) < min_occurrences:
            continue

        gloss = glossary_by_canonical.get(canonical)
        if gloss is None:
            continue

        # Compute definition similarity.
        for occ in occs:
            occ.sim_definition = cosine(occ.vector, gloss.definition_vector)

        # Compute cluster similarity using all other occurrences as centroid.
        for idx, occ in enumerate(occs):
            centroid = Counter()
            for j, other in enumerate(occs):
                if j == idx:
                    continue
                centroid.update(other.vector)
            occ.sim_cluster = cosine(occ.vector, centroid)
            occ.score = 0.7 * occ.sim_cluster + 0.3 * occ.sim_definition

        scores = [o.score for o in occs]
        threshold = robust_threshold(scores)

        candidates = [o for o in occs if o.score < threshold]
        # Absolute floor: ignore tiny differences near the center.
        med = statistics.median(scores)
        candidates = [o for o in candidates if (med - o.score) >= 0.05]

        # Extra signal: very low alignment to both glossary and cluster.
        for o in occs:
            if o.sim_definition < 0.03 and o.sim_cluster < 0.16 and o not in candidates:
                candidates.append(o)

        candidates = sorted(candidates, key=lambda o: (o.score, o.sim_definition, o.sim_cluster))
        if max_flags_per_term > 0:
            candidates = candidates[:max_flags_per_term]

        for occ in candidates:
            issue_id = f"S{issue_num:04d}"
            issue_num += 1
            flagged.append(
                FlaggedIssue(
                    issue_id=issue_id,
                    canonical=canonical,
                    observed=occ.observed,
                    file_path=occ.file_path,
                    line=occ.line,
                    context=occ.context,
                    sim_definition=occ.sim_definition,
                    sim_cluster=occ.sim_cluster,
                    score=occ.score,
                    definition=gloss.definition,
                )
            )

    return flagged


def write_decisions_csv(path: Path, issues: Sequence[FlaggedIssue]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "issue_id",
                "issue_type",
                "file",
                "line",
                "observed_form",
                "canonical_term",
                "suggested_replacement",
                "alternatives",
                "default_action",
                "decision",
                "custom_replacement",
                "scope",
                "notes",
                "context",
            ],
        )
        writer.writeheader()
        for issue in issues:
            writer.writerow(
                {
                    "issue_id": issue.issue_id,
                    "issue_type": "semantic_drift_suspect",
                    "file": issue.file_path,
                    "line": issue.line,
                    "observed_form": issue.observed,
                    "canonical_term": issue.canonical,
                    "suggested_replacement": "",
                    "alternatives": "",
                    "default_action": "keep",
                    "decision": "pending",
                    "custom_replacement": "",
                    "scope": "this_occurrence",
                    "notes": f"score={issue.score:.3f}; sim_def={issue.sim_definition:.3f}; sim_cluster={issue.sim_cluster:.3f}; glossary={issue.definition}",
                    "context": issue.context,
                }
            )


def render_markdown(
    *,
    glossary_path: Path,
    files: Sequence[Path],
    mapped_occurrences: int,
    terms_with_occurrences: int,
    issues: Sequence[FlaggedIssue],
    decisions_csv: Path,
    min_occurrences: int,
    max_flags_per_term: int,
) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    g_disp = str(glossary_path.relative_to(PROJECT_ROOT))
    d_disp = str(decisions_csv.relative_to(PROJECT_ROOT))

    lines: List[str] = []
    lines.append(f"# Semantic Term Consistency Audit ({now})")
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- Glossary source: `{g_disp}`")
    lines.append(f"- TeX files scanned: {len(files)}")
    lines.append(f"- Glossary-backed term occurrences analyzed: {mapped_occurrences}")
    lines.append(f"- Distinct glossary terms observed: {terms_with_occurrences}")
    lines.append(f"- Minimum occurrences per term for outlier detection: {min_occurrences}")
    lines.append(f"- Max flags per term: {max_flags_per_term}")
    lines.append(f"- Flagged semantic-drift suspects: {len(issues)}")
    lines.append(f"- Decisions CSV: `{d_disp}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("- This report only audits terms that already map to glossary entries.")
    lines.append("- Flags are outlier candidates, not automatic errors.")
    lines.append("- Use the walkthrough to mark each as `keep` or propose revision.")
    lines.append("")

    if not issues:
        lines.append("## Findings")
        lines.append("No semantic outlier uses were detected under current thresholds.")
        return "\n".join(lines)

    lines.append("## Findings")
    lines.append("")
    for issue in issues:
        lines.append(f"### {issue.issue_id} - `{issue.canonical}`")
        lines.append(f"- Location: `{issue.file_path}:{issue.line}`")
        lines.append(f"- Observed form: `{issue.observed}`")
        lines.append(f"- Similarity to glossary definition: `{issue.sim_definition:.3f}`")
        lines.append(f"- Similarity to this term's usage cluster: `{issue.sim_cluster:.3f}`")
        lines.append(f"- Combined outlier score: `{issue.score:.3f}`")
        lines.append(f"- Glossary definition excerpt: {issue.definition}")
        lines.append(f"- Context: {issue.context}")
        lines.append(
            f"- Review in decisions CSV row `{issue.issue_id}` (recommended default: `keep` unless clearly inconsistent)."
        )
        lines.append("")

    return "\n".join(lines)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit semantic consistency for glossary-backed term usage."
    )
    parser.add_argument("--glossary", default="glossary.tex")
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Glob pattern(s) for TeX files. Defaults to chapters/frontmatter/hpc-book.tex",
    )
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument(
        "--min-occurrences",
        type=int,
        default=3,
        help="Minimum occurrences per term to run outlier detection (default: 3).",
    )
    parser.add_argument(
        "--max-flags-per-term",
        type=int,
        default=2,
        help="Max flagged outliers per term (default: 2).",
    )
    parser.add_argument(
        "--output-md",
        default="reports/term-semantic-audit.md",
    )
    parser.add_argument(
        "--output-csv",
        default="reports/term-semantic-audit-decisions.csv",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any suspect issues are flagged.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)

    glossary_path = resolve_project_relative(args.glossary)
    if not glossary_path.exists():
        print(f"ERROR: glossary not found: {glossary_path}")
        return 2

    includes = args.include or ["chapters/*.tex", "frontmatter/*.tex", "hpc-book.tex"]
    excludes = list(args.exclude)
    excludes.append(str(glossary_path))

    files = expand_inputs(includes, excludes)
    if not files:
        print("ERROR: no TeX files found to scan")
        return 2

    glossary_terms = parse_glossary(glossary_path)
    if not glossary_terms:
        print("ERROR: no glossary terms parsed")
        return 2

    exact_map, norm_map = build_alias_maps(glossary_terms)
    glossary_by_canonical = {g.canonical: g for g in glossary_terms}

    grouped = collect_occurrences(files, exact_map, norm_map)
    mapped_occurrences = sum(len(v) for v in grouped.values())

    issues = flag_outliers(
        grouped,
        glossary_by_canonical,
        min_occurrences=max(2, args.min_occurrences),
        max_flags_per_term=max(0, args.max_flags_per_term),
    )

    output_md = resolve_project_relative(args.output_md)
    output_csv = resolve_project_relative(args.output_csv)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    report = render_markdown(
        glossary_path=glossary_path,
        files=files,
        mapped_occurrences=mapped_occurrences,
        terms_with_occurrences=len(grouped),
        issues=issues,
        decisions_csv=output_csv,
        min_occurrences=max(2, args.min_occurrences),
        max_flags_per_term=max(0, args.max_flags_per_term),
    )
    output_md.write_text(report, encoding="utf-8")
    write_decisions_csv(output_csv, issues)

    print(f"Wrote markdown report: {output_md}")
    print(f"Wrote decisions CSV: {output_csv}")
    print(f"Scanned files: {len(files)}")
    print(f"Glossary terms: {len(glossary_terms)}")
    print(f"Glossary-backed occurrences analyzed: {mapped_occurrences}")
    print(f"Flagged semantic-drift suspects: {len(issues)}")

    if args.strict and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Audit full-book \term{} usage against glossary canonical terms.

Outputs:
- Markdown review report with context snippets.
- CSV decisions file with per-issue keep/replace/custom controls.

This script is intentionally conservative: it audits explicit \term{...} usages
and compares them to glossary name/text forms.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import glob
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


TERM_PATTERN = re.compile(r"\\term\{([^{}]+)\}")
ENTRY_START_PATTERN = re.compile(r"^\\newglossaryentry\{([^}]+)\}\{")
NAME_PATTERN = re.compile(r"\bname=\{([^{}]+)\}")
TEXT_PATTERN = re.compile(r"\btext=\{([^{}]+)\}")
SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_DIR.parent


@dataclass(frozen=True)
class GlossaryEntry:
    key: str
    name: str
    text: str
    canonical: str
    aliases: Tuple[str, ...]


@dataclass
class Issue:
    issue_id: str
    issue_type: str
    file_path: str
    line: int
    observed_form: str
    canonical_term: str
    suggested_replacement: str
    alternatives: List[str]
    default_action: str
    context: str


def singularize(norm_term: str) -> List[str]:
    variants: List[str] = [norm_term]
    if norm_term.endswith("ies") and len(norm_term) > 4:
        variants.append(norm_term[:-3] + "y")
    if norm_term.endswith("es") and len(norm_term) > 4:
        variants.append(norm_term[:-2])
    if norm_term.endswith("s") and not norm_term.endswith("ss") and len(norm_term) > 3:
        variants.append(norm_term[:-1])
    return list(dict.fromkeys(v for v in variants if v))


def token_jaccard(a: str, b: str) -> float:
    a_tokens = set(a.split())
    b_tokens = set(b.split())
    if not a_tokens or not b_tokens:
        return 0.0
    return len(a_tokens & b_tokens) / len(a_tokens | b_tokens)


def close_suggestions(observed_norm: str, candidates: Sequence[str], max_n: int = 3) -> List[str]:
    scored: List[Tuple[float, float, str]] = []
    for cand in candidates:
        ratio = difflib.SequenceMatcher(None, observed_norm, cand).ratio()
        jac = token_jaccard(observed_norm, cand)
        # Conservative thresholding to avoid noisy false suggestions.
        if ratio >= 0.88 or (ratio >= 0.8 and jac >= 0.6):
            scored.append((ratio, jac, cand))
    scored.sort(reverse=True)
    return [cand for _, _, cand in scored[:max_n]]


def normalize_space(text: str) -> str:
    return " ".join(text.split())


def normalize_term(text: str) -> str:
    s = normalize_space(text)
    s = s.lower()
    s = s.replace("–", "-").replace("—", "-")
    s = s.replace("-", " ")
    s = s.replace("/", " ")
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return normalize_space(s)


def differs_only_by_case(a: str, b: str) -> bool:
    a_norm = normalize_space(a)
    b_norm = normalize_space(b)
    return a_norm.casefold() == b_norm.casefold() and a_norm != b_norm


def parse_glossary_entries(glossary_path: Path) -> List[GlossaryEntry]:
    lines = glossary_path.read_text(encoding="utf-8").splitlines()
    entries: List[GlossaryEntry] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        match = ENTRY_START_PATTERN.match(line.strip())
        if not match:
            i += 1
            continue

        key = match.group(1).strip()
        block_lines = [line]
        i += 1
        while i < len(lines):
            block_lines.append(lines[i])
            if lines[i].strip() == "}":
                break
            i += 1

        block_text = "\n".join(block_lines)
        name_match = NAME_PATTERN.search(block_text)
        text_match = TEXT_PATTERN.search(block_text)
        name = normalize_space(name_match.group(1)) if name_match else ""
        text = normalize_space(text_match.group(1)) if text_match else ""

        # Use text as preferred display/canonical form when available.
        canonical = text or name
        if canonical:
            aliases = tuple(dict.fromkeys([canonical, name, text]))
            entries.append(
                GlossaryEntry(
                    key=key,
                    name=name,
                    text=text,
                    canonical=canonical,
                    aliases=aliases,
                )
            )
        i += 1

    return entries


def expand_input_files(patterns: Sequence[str], excludes: Sequence[str]) -> List[Path]:
    found: List[Path] = []
    exclude_paths = set()
    for ex in excludes:
        ex_path = Path(ex).expanduser()
        if not ex_path.is_absolute():
            ex_path = PROJECT_ROOT / ex_path
        exclude_paths.add(ex_path.resolve())
    for pattern in patterns:
        pattern_path = Path(pattern).expanduser()
        if not pattern_path.is_absolute():
            pattern = str(PROJECT_ROOT / pattern_path)
        else:
            pattern = str(pattern_path)

        for path_str in glob.glob(pattern, recursive=True):
            path = Path(path_str)
            if not path.is_file():
                continue
            if path.resolve() in exclude_paths:
                continue
            found.append(path.resolve())

    unique_sorted = sorted(set(found), key=lambda p: str(p))
    return unique_sorted


def get_line_number(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def make_context(text: str, start: int, end: int, observed_form: str, window: int = 220) -> str:
    left = max(0, start - window)
    right = min(len(text), end + window)
    snippet = text[left:right]
    snippet = snippet.replace("\n", " ")
    snippet = normalize_space(snippet)

    marker = f"[[{observed_form}]]"
    if observed_form in snippet:
        snippet = snippet.replace(observed_form, marker, 1)

    if left > 0:
        snippet = "... " + snippet
    if right < len(text):
        snippet = snippet + " ..."

    return snippet


def build_glossary_maps(
    entries: Sequence[GlossaryEntry],
) -> Tuple[
    Dict[str, str],
    Dict[str, List[str]],
    Dict[str, List[str]],
    List[str],
]:
    # Exact alias -> canonical
    exact_alias_map: Dict[str, str] = {}
    ambiguous_exact: Dict[str, List[str]] = defaultdict(list)

    # Normalized alias -> canonical(s)
    normalized_map: Dict[str, List[str]] = defaultdict(list)

    canonical_terms: List[str] = []

    for entry in entries:
        canonical_terms.append(entry.canonical)
        for alias in entry.aliases:
            if not alias:
                continue
            if alias in exact_alias_map and exact_alias_map[alias] != entry.canonical:
                ambiguous_exact[alias] = sorted(
                    {exact_alias_map[alias], entry.canonical}
                )
            else:
                exact_alias_map[alias] = entry.canonical

            norm = normalize_term(alias)
            if not norm:
                continue
            if entry.canonical not in normalized_map[norm]:
                normalized_map[norm].append(entry.canonical)

    normalized_map = {k: sorted(v) for k, v in normalized_map.items()}
    ambiguous_exact = {k: sorted(v) for k, v in ambiguous_exact.items()}

    return exact_alias_map, ambiguous_exact, normalized_map, sorted(set(canonical_terms))


def classify_term_usage(
    observed_form: str,
    exact_alias_map: Dict[str, str],
    ambiguous_exact: Dict[str, List[str]],
    normalized_map: Dict[str, List[str]],
    canonical_terms: Sequence[str],
    *,
    flag_case_variants: bool,
) -> Tuple[str, str, str, List[str], str]:
    """Return (issue_type, canonical, suggested, alternatives, default_action).

    Returns issue_type == "" if no issue.
    """
    observed = normalize_space(observed_form)

    if observed in ambiguous_exact:
        alternatives = ambiguous_exact[observed]
        canonical = alternatives[0]
        return (
            "ambiguous_exact_alias",
            canonical,
            canonical,
            alternatives,
            "keep",
        )

    if observed in exact_alias_map:
        canonical = exact_alias_map[observed]
        if observed == canonical:
            return ("", "", "", [], "")
        if differs_only_by_case(observed, canonical) and not flag_case_variants:
            return ("", "", "", [], "")
        if differs_only_by_case(observed, canonical) and flag_case_variants:
            return (
                "case_variant",
                canonical,
                canonical,
                [],
                "replace_with_canonical",
            )
        return (
            "alias_used",
            canonical,
            canonical,
            [],
            "replace_with_canonical",
        )

    observed_norm = normalize_term(observed)
    norm_candidates = singularize(observed_norm)

    for observed_variant in norm_candidates:
        if observed_variant not in normalized_map:
            continue
        candidates = normalized_map[observed_variant]
        if len(candidates) == 1:
            canonical = candidates[0]
            if observed != canonical:
                if differs_only_by_case(observed, canonical) and not flag_case_variants:
                    return ("", "", "", [], "")
                if differs_only_by_case(observed, canonical) and flag_case_variants:
                    return (
                        "case_variant",
                        canonical,
                        canonical,
                        [],
                        "replace_with_canonical",
                    )
                return (
                    "normalized_variant",
                    canonical,
                    canonical,
                    [],
                    "replace_with_canonical",
                )
            return ("", "", "", [], "")

        canonical = candidates[0]
        return (
            "ambiguous_normalized_match",
            canonical,
            canonical,
            candidates,
            "keep",
        )

    canonical_norm_map = {normalize_term(t): t for t in canonical_terms}
    suggestion_norms = close_suggestions(observed_norm, list(canonical_norm_map.keys()))
    suggestions = [canonical_norm_map[s] for s in suggestion_norms]

    if suggestions:
        canonical = suggestions[0]
        return (
            "unknown_term_with_suggestion",
            canonical,
            canonical,
            suggestions,
            "replace_with_canonical",
        )

    return ("unknown_term", "", "", [], "keep")


def collect_issues(
    input_files: Sequence[Path],
    exact_alias_map: Dict[str, str],
    ambiguous_exact: Dict[str, List[str]],
    normalized_map: Dict[str, List[str]],
    canonical_terms: Sequence[str],
    *,
    flag_case_variants: bool,
) -> List[Issue]:
    issues: List[Issue] = []
    issue_index = 1

    for path in input_files:
        text = path.read_text(encoding="utf-8")
        try:
            rel_path = str(path.relative_to(Path.cwd()))
        except ValueError:
            rel_path = str(path)
        for match in TERM_PATTERN.finditer(text):
            observed = normalize_space(match.group(1))
            issue_type, canonical, suggested, alternatives, default_action = classify_term_usage(
                observed,
                exact_alias_map,
                ambiguous_exact,
                normalized_map,
                canonical_terms,
                flag_case_variants=flag_case_variants,
            )
            if not issue_type:
                continue

            issue_id = f"T{issue_index:04d}"
            issue_index += 1
            line = get_line_number(text, match.start())
            context = make_context(text, match.start(), match.end(), observed)

            issues.append(
                Issue(
                    issue_id=issue_id,
                    issue_type=issue_type,
                    file_path=rel_path,
                    line=line,
                    observed_form=observed,
                    canonical_term=canonical,
                    suggested_replacement=suggested,
                    alternatives=alternatives,
                    default_action=default_action,
                    context=context,
                )
            )

    return issues


def write_decisions_csv(path: Path, issues: Sequence[Issue]) -> None:
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
                "decision",  # keep | replace_with_canonical | replace_custom
                "custom_replacement",
                "scope",  # this_occurrence | all_same_observed_form
                "notes",
                "context",
            ],
        )
        writer.writeheader()
        for issue in issues:
            writer.writerow(
                {
                    "issue_id": issue.issue_id,
                    "issue_type": issue.issue_type,
                    "file": issue.file_path,
                    "line": issue.line,
                    "observed_form": issue.observed_form,
                    "canonical_term": issue.canonical_term,
                    "suggested_replacement": issue.suggested_replacement,
                    "alternatives": " | ".join(issue.alternatives),
                    "default_action": issue.default_action,
                    "decision": "pending",
                    "custom_replacement": "",
                    "scope": "this_occurrence",
                    "notes": "",
                    "context": issue.context,
                }
            )


def render_markdown(
    *,
    glossary_path: Path,
    input_files: Sequence[Path],
    entries: Sequence[GlossaryEntry],
    issues: Sequence[Issue],
    decisions_csv_path: Path,
) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    counts = Counter(issue.issue_type for issue in issues)
    try:
        glossary_display = str(glossary_path.relative_to(Path.cwd()))
    except ValueError:
        glossary_display = str(glossary_path)
    try:
        decisions_display = str(decisions_csv_path.relative_to(Path.cwd()))
    except ValueError:
        decisions_display = str(decisions_csv_path)

    lines: List[str] = []
    lines.append(f"# Term Consistency Audit ({now})")
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- Glossary source: `{glossary_display}`")
    lines.append(f"- Glossary entries parsed: {len(entries)}")
    lines.append(f"- TeX files scanned: {len(input_files)}")
    lines.append(f"- Issues found: {len(issues)}")
    lines.append(f"- Decisions file: `{decisions_display}`")
    lines.append("")
    lines.append("## Decision Options")
    lines.append("- `keep`: accept the observed form as-is.")
    lines.append("- `replace_with_canonical`: replace with the glossary canonical term.")
    lines.append("- `replace_custom`: provide your own replacement in `custom_replacement`.")
    lines.append("- `scope`: choose `this_occurrence` or `all_same_observed_form`.")
    lines.append("")

    lines.append("## Issue Counts")
    if not counts:
        lines.append("- None")
    else:
        for issue_type in sorted(counts):
            lines.append(f"- `{issue_type}`: {counts[issue_type]}")
    lines.append("")

    if not issues:
        lines.append("## Findings")
        lines.append("No term consistency issues detected for explicit `\\term{...}` usages.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Findings")
    lines.append("")

    for issue in issues:
        lines.append(f"### {issue.issue_id} - {issue.issue_type}")
        lines.append(f"- Location: `{issue.file_path}:{issue.line}`")
        lines.append(f"- Observed: `{issue.observed_form}`")
        if issue.canonical_term:
            lines.append(f"- Canonical: `{issue.canonical_term}`")
        if issue.suggested_replacement:
            lines.append(f"- Suggested replacement: `{issue.suggested_replacement}`")
        if issue.alternatives:
            alternatives = ", ".join(f"`{a}`" for a in issue.alternatives)
            lines.append(f"- Alternatives: {alternatives}")
        lines.append(f"- Default action: `{issue.default_action}`")
        lines.append(f"- Context: {issue.context}")
        lines.append(
            f"- Review in decisions CSV row `{issue.issue_id}`: `keep` | `replace_with_canonical` | `replace_custom`"
        )
        lines.append("")

    return "\n".join(lines)


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit full-book term consistency against glossary canonical forms."
    )
    parser.add_argument(
        "--glossary",
        default="glossary.tex",
        help="Path to glossary.tex (default: glossary.tex).",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help=(
            "Glob pattern(s) for TeX files to scan. Repeatable. "
            "Defaults to chapters/*.tex, frontmatter/*.tex, hpc-book.tex."
        ),
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Optional file paths to exclude from scan. Repeatable.",
    )
    parser.add_argument(
        "--output-md",
        default="reports/term-audit.md",
        help="Markdown report output path.",
    )
    parser.add_argument(
        "--output-csv",
        default="reports/term-audit-decisions.csv",
        help="Decision queue CSV output path.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any issues are found.",
    )
    parser.add_argument(
        "--flag-case-variants",
        action="store_true",
        help="Include case-only variants (e.g., sentence-initial capitalization) as issues.",
    )
    return parser.parse_args(argv)


def resolve_project_relative(path_str: str) -> Path:
    p = Path(path_str).expanduser()
    if p.is_absolute():
        return p.resolve()
    return (PROJECT_ROOT / p).resolve()


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)

    glossary_path = resolve_project_relative(args.glossary)
    if not glossary_path.exists():
        print(f"ERROR: glossary file not found: {glossary_path}", file=sys.stderr)
        return 2

    includes = args.include or ["chapters/*.tex", "frontmatter/*.tex", "hpc-book.tex"]
    excludes = list(args.exclude)
    excludes.append(str(glossary_path))

    input_files = expand_input_files(includes, excludes)
    if not input_files:
        print("ERROR: no input files found for scan", file=sys.stderr)
        return 2

    entries = parse_glossary_entries(glossary_path)
    if not entries:
        print("ERROR: no glossary entries parsed", file=sys.stderr)
        return 2

    exact_alias_map, ambiguous_exact, normalized_map, canonical_terms = build_glossary_maps(entries)

    issues = collect_issues(
        input_files,
        exact_alias_map,
        ambiguous_exact,
        normalized_map,
        canonical_terms,
        flag_case_variants=args.flag_case_variants,
    )

    output_md = resolve_project_relative(args.output_md)
    output_csv = resolve_project_relative(args.output_csv)

    md = render_markdown(
        glossary_path=glossary_path,
        input_files=input_files,
        entries=entries,
        issues=issues,
        decisions_csv_path=output_csv,
    )

    write_markdown(output_md, md)
    write_decisions_csv(output_csv, issues)

    print(f"Wrote markdown report: {output_md}")
    print(f"Wrote decisions CSV: {output_csv}")
    print(f"Scanned files: {len(input_files)}")
    print(f"Glossary entries: {len(entries)}")
    print(f"Issues: {len(issues)}")

    if args.strict and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Audit full BibTeX data quality (not limited to cited keys).

Checks:
- key collisions (exact duplicate key, case-colliding keys)
- likely duplicate records (shared DOI, shared title+author+year signature)
- required-field gaps by entry type
- malformed year/doi/url values
- placeholder/stub markers
- field-shape consistency (journal vs journaltitle, year vs date, address vs location)

Outputs markdown by default, JSON with --json.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Sequence, Tuple
from urllib.parse import urlparse

try:  # Optional dependency
    import bibtexparser  # type: ignore
except Exception:  # pragma: no cover - fallback parser handles absence
    bibtexparser = None


YEAR_PATTERN = re.compile(r"^\d{4}[a-z]?$")
PLACEHOLDER_PATTERN = re.compile(r"\b(todo|tbd|fixme|stub|xxx|placeholder)\b", re.IGNORECASE)
FORTHCOMING_PATTERN = re.compile(r"\b(forthcoming|in press|to appear)\b", re.IGNORECASE)
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)

SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}


REQUIRED_FIELDS: Dict[str, Sequence[str]] = {
    "article": ("title", "journal", "year"),
    "book": ("title", "publisher", "year"),
    "inbook": ("title", "booktitle", "year"),
    "incollection": ("title", "booktitle", "year"),
    "inproceedings": ("title", "booktitle", "year"),
    "mastersthesis": ("title", "school", "year"),
    "phdthesis": ("title", "school", "year"),
    "techreport": ("title", "institution", "year"),
    "thesis": ("title", "school", "year"),
    "misc": ("title", "year"),
    "online": ("title", "year"),
    "unpublished": ("title", "year"),
    "software": ("title", "year"),
}


def _strip_braces(text: str) -> str:
    return text.replace("{", "").replace("}", "").strip()


def _strip_bib_comments(text: str) -> str:
    cleaned_lines: List[str] = []
    for line in text.splitlines():
        cur: List[str] = []
        prev = ""
        for ch in line:
            if ch == "%" and prev != "\\":
                break
            cur.append(ch)
            prev = ch
        cleaned_lines.append("".join(cur))
    return "\n".join(cleaned_lines)


def _find_matching(text: str, open_pos: int, open_ch: str, close_ch: str) -> int:
    depth = 1
    i = open_pos + 1
    in_quote = False
    while i < len(text):
        ch = text[i]
        prev = text[i - 1] if i > 0 else ""
        if ch == '"' and prev != "\\":
            in_quote = not in_quote
        elif not in_quote:
            if ch == open_ch:
                depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1


def _split_top_level(value: str, sep: str = ",") -> List[str]:
    parts: List[str] = []
    depth_brace = 0
    depth_paren = 0
    in_quote = False
    cur: List[str] = []
    prev = ""
    for ch in value:
        if ch == '"' and prev != "\\":
            in_quote = not in_quote
        elif not in_quote:
            if ch == "{":
                depth_brace += 1
            elif ch == "}":
                depth_brace = max(0, depth_brace - 1)
            elif ch == "(":
                depth_paren += 1
            elif ch == ")":
                depth_paren = max(0, depth_paren - 1)

        if ch == sep and not in_quote and depth_brace == 0 and depth_paren == 0:
            token = "".join(cur).strip()
            if token:
                parts.append(token)
            cur = []
        else:
            cur.append(ch)
        prev = ch

    tail = "".join(cur).strip()
    if tail:
        parts.append(tail)
    return parts


def parse_bib_text(text: str) -> List[dict]:
    text = _strip_bib_comments(text)
    entries: List[dict] = []
    i = 0
    while i < len(text):
        at = text.find("@", i)
        if at == -1:
            break

        m = re.match(r"@([A-Za-z][A-Za-z0-9_-]*)\s*([({])", text[at:])
        if not m:
            i = at + 1
            continue

        entry_type = m.group(1).lower()
        open_ch = m.group(2)
        close_ch = "}" if open_ch == "{" else ")"
        open_pos = at + m.end() - 1
        close_pos = _find_matching(text, open_pos, open_ch, close_ch)
        if close_pos == -1:
            break

        # Skip declarations that are not standard entries.
        if entry_type in {"comment", "preamble", "string"}:
            i = close_pos + 1
            continue

        raw_inside = text[open_pos + 1 : close_pos].strip()
        parts = _split_top_level(raw_inside, ",")
        if not parts:
            i = close_pos + 1
            continue

        key = parts[0].strip()
        if not key:
            i = close_pos + 1
            continue

        entry = {"ENTRYTYPE": entry_type, "ID": key}
        for field in parts[1:]:
            if "=" not in field:
                continue
            name, val = field.split("=", 1)
            field_name = name.strip().lower()
            field_value = val.strip().rstrip(",").strip()
            entry[field_name] = field_value

        entries.append(entry)
        i = close_pos + 1

    return entries


def parse_bib_file(path: Path) -> List[dict]:
    if bibtexparser is not None:
        with path.open("r", encoding="utf-8") as fh:
            db = bibtexparser.load(fh)
        return list(db.entries)
    return parse_bib_text(path.read_text(encoding="utf-8"))


def _entry_value(entry: dict, *fields: str) -> str:
    for field in fields:
        val = _strip_braces(str(entry.get(field, "")))
        if val:
            return val
    return ""


def _entry_year(entry: dict) -> str:
    year = _entry_value(entry, "year")
    if year:
        return year
    date_val = _entry_value(entry, "date")
    if not date_val:
        return ""
    match = re.search(r"\d{4}[a-z]?", date_val)
    return match.group(0) if match else ""


def _normalize_doi(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    return text


def _normalize_title(raw: str) -> str:
    text = _strip_braces(raw).lower()
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _first_author_surname(raw_author: str) -> str:
    if not raw_author:
        return ""
    first = raw_author.split(" and ")[0].strip()
    first = _strip_braces(first)
    if "," in first:
        return first.split(",", 1)[0].strip().lower()
    parts = first.split()
    if not parts:
        return ""
    return parts[-1].lower()


def _is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _new_issue(
    severity: str,
    code: str,
    message: str,
    suggestion: str,
    key: str = "",
    source: str = "",
    field: str = "",
) -> dict:
    return {
        "severity": severity,
        "code": code,
        "key": key,
        "source": source,
        "field": field,
        "message": message,
        "suggestion": suggestion,
    }


def load_records(bib_paths: Iterable[Path]) -> Tuple[List[dict], List[str], List[dict]]:
    records: List[dict] = []
    load_errors: List[str] = []
    issues: List[dict] = []

    for bib_path in bib_paths:
        if not bib_path.exists():
            load_errors.append(f"Missing bib file: {bib_path}")
            continue
        try:
            entries = parse_bib_file(bib_path)
        except Exception as exc:  # pragma: no cover - defensive
            load_errors.append(f"Failed to parse {bib_path}: {exc}")
            continue

        for idx, entry in enumerate(entries, 1):
            key = str(entry.get("ID", "")).strip()
            if not key:
                issues.append(
                    _new_issue(
                        "error",
                        "missing_key",
                        f"Entry #{idx} in {bib_path} has no key (ID).",
                        "Add a unique BibTeX key immediately after @type{...}.",
                        source=str(bib_path),
                    )
                )
                continue

            item = dict(entry)
            item["_source"] = str(bib_path)
            item["_index"] = idx
            records.append(item)

    return records, load_errors, issues


def audit_records(records: Sequence[dict], bib_sources: Sequence[Path], report_date: str) -> dict:
    issues: List[dict] = []

    key_occurrences: DefaultDict[str, List[dict]] = defaultdict(list)
    key_by_lower: DefaultDict[str, set] = defaultdict(set)
    doi_occurrences: DefaultDict[str, List[dict]] = defaultdict(list)
    sig_occurrences: DefaultDict[str, List[dict]] = defaultdict(list)

    style_counts = {
        "journal_only": 0,
        "journaltitle_only": 0,
        "both_journal_fields": 0,
        "year_only": 0,
        "date_only": 0,
        "both_year_date": 0,
        "address_only": 0,
        "location_only": 0,
        "both_address_location": 0,
    }

    for entry in records:
        key = str(entry.get("ID", "")).strip()
        source = str(entry.get("_source", ""))
        entry_type = str(entry.get("ENTRYTYPE", "")).lower().strip()

        key_occurrences[key].append(entry)
        key_by_lower[key.lower()].add(key)

        journal = _entry_value(entry, "journal")
        journaltitle = _entry_value(entry, "journaltitle")
        if journal and journaltitle:
            style_counts["both_journal_fields"] += 1
        elif journal:
            style_counts["journal_only"] += 1
        elif journaltitle:
            style_counts["journaltitle_only"] += 1

        year = _entry_value(entry, "year")
        date = _entry_value(entry, "date")
        if year and date:
            style_counts["both_year_date"] += 1
        elif year:
            style_counts["year_only"] += 1
        elif date:
            style_counts["date_only"] += 1

        address = _entry_value(entry, "address")
        location = _entry_value(entry, "location")
        if address and location:
            style_counts["both_address_location"] += 1
        elif address:
            style_counts["address_only"] += 1
        elif location:
            style_counts["location_only"] += 1

        required = REQUIRED_FIELDS.get(entry_type, ("title", "year"))
        for field in required:
            if field == "journal":
                if not _entry_value(entry, "journal", "journaltitle"):
                    issues.append(
                        _new_issue(
                            "warning",
                            "missing_required_field",
                            "Required field `journal` is missing.",
                            "Add `journal={...}` (or standardize to `journaltitle`, then normalize style).",
                            key=key,
                            source=source,
                            field="journal",
                        )
                    )
                continue
            if field == "year":
                if not _entry_year(entry):
                    issues.append(
                        _new_issue(
                            "warning",
                            "missing_required_field",
                            "Required field `year` is missing (and no parseable `date`).",
                            "Add `year={YYYY}`. If status is pending, keep year numeric and move status to `note`.",
                            key=key,
                            source=source,
                            field="year",
                        )
                    )
                continue
            if not _entry_value(entry, field):
                issues.append(
                    _new_issue(
                        "warning",
                        "missing_required_field",
                        f"Required field `{field}` is missing.",
                        f"Add `{field}={{...}}`.",
                        key=key,
                        source=source,
                        field=field,
                    )
                )

        if entry_type not in {"collection", "proceedings"}:
            if not _entry_value(entry, "author") and not _entry_value(entry, "editor"):
                issues.append(
                    _new_issue(
                        "warning",
                        "missing_author_editor",
                        "Entry has neither `author` nor `editor`.",
                        "Add `author={...}` or `editor={...}`.",
                        key=key,
                        source=source,
                    )
                )

        year_raw = _entry_value(entry, "year")
        if year_raw:
            if FORTHCOMING_PATTERN.search(year_raw):
                issues.append(
                    _new_issue(
                        "warning",
                        "placeholder_year",
                        f"Year uses placeholder value `{year_raw}`.",
                        "Use numeric `year={YYYY}` and move publication status to `note={Forthcoming}`.",
                        key=key,
                        source=source,
                        field="year",
                    )
                )
            elif not YEAR_PATTERN.match(year_raw):
                issues.append(
                    _new_issue(
                        "warning",
                        "invalid_year_format",
                        f"Year has non-standard format `{year_raw}`.",
                        "Use `year={YYYY}` (or `YYYYa`, `YYYYb`) and put extra text in `note`.",
                        key=key,
                        source=source,
                        field="year",
                    )
                )

        if year_raw and date:
            match = re.search(r"\d{4}[a-z]?", date)
            date_year = match.group(0) if match else ""
            if date_year and date_year != year_raw:
                issues.append(
                    _new_issue(
                        "warning",
                        "year_date_conflict",
                        f"`year` ({year_raw}) and `date` ({date}) disagree.",
                        "Keep one authoritative year value or make `date` and `year` consistent.",
                        key=key,
                        source=source,
                        field="year/date",
                    )
                )

        doi_raw = _entry_value(entry, "doi")
        if doi_raw:
            doi_norm = _normalize_doi(doi_raw)
            if DOI_PATTERN.match(doi_norm):
                doi_occurrences[doi_norm.lower()].append(entry)
            else:
                issues.append(
                    _new_issue(
                        "warning",
                        "malformed_doi",
                        f"DOI appears malformed: `{doi_raw}`.",
                        "Use bare DOI format: `10.xxxx/xxxxx` (no spaces).",
                        key=key,
                        source=source,
                        field="doi",
                    )
                )

        url_raw = _entry_value(entry, "url")
        if url_raw and not _is_valid_url(url_raw):
            issues.append(
                _new_issue(
                    "warning",
                    "malformed_url",
                    f"URL appears malformed: `{url_raw}`.",
                    "Use a full http(s) URL with a host, e.g. `https://example.org/...`.",
                    key=key,
                    source=source,
                    field="url",
                )
            )

        for field in ("title", "note"):
            val = _entry_value(entry, field)
            if val and PLACEHOLDER_PATTERN.search(val):
                issues.append(
                    _new_issue(
                        "warning",
                        "placeholder_marker",
                        f"Field `{field}` contains placeholder text.",
                        "Replace placeholder text with final metadata or remove the field.",
                        key=key,
                        source=source,
                        field=field,
                    )
                )

        sig_title = _normalize_title(_entry_value(entry, "title"))
        sig_author = _first_author_surname(_entry_value(entry, "author"))
        sig_year = _entry_year(entry)
        if sig_title and sig_author and sig_year:
            sig = f"{sig_title}|{sig_author}|{sig_year}"
            sig_occurrences[sig].append(entry)

    # Exact duplicate keys.
    for key, hits in sorted(key_occurrences.items()):
        if len(hits) > 1:
            srcs = ", ".join(f"{h['_source']}#{h['_index']}" for h in hits)
            issues.append(
                _new_issue(
                    "error",
                    "duplicate_key",
                    f"Key `{key}` appears {len(hits)} times ({srcs}).",
                    "Keep one canonical entry for this key and merge metadata.",
                    key=key,
                )
            )

    # Case-collision keys.
    for lower_key, keys in sorted(key_by_lower.items()):
        if len(keys) > 1:
            sorted_keys = sorted(keys)
            issues.append(
                _new_issue(
                    "warning",
                    "case_collision_key",
                    f"Case-colliding keys share lowercase form `{lower_key}`: {', '.join(sorted_keys)}.",
                    "Choose one canonical key casing and update citations/references accordingly.",
                )
            )

    # Duplicate DOI records.
    for doi_norm, hits in sorted(doi_occurrences.items()):
        keys = sorted({str(h.get("ID", "")) for h in hits})
        if len(keys) > 1:
            issues.append(
                _new_issue(
                    "warning",
                    "duplicate_doi_record",
                    f"DOI `{doi_norm}` is shared by multiple keys: {', '.join(keys)}.",
                    "Merge duplicate records under one key and update citation usage.",
                    key=";".join(keys),
                    field="doi",
                )
            )

    # Duplicate signature records.
    for sig, hits in sorted(sig_occurrences.items()):
        keys = sorted({str(h.get("ID", "")) for h in hits})
        if len(keys) > 1:
            issues.append(
                _new_issue(
                    "info",
                    "possible_duplicate_record",
                    f"Same title+first-author+year signature appears under multiple keys: {', '.join(keys)}.",
                    "Manually inspect and merge if records are the same work.",
                    key=";".join(keys),
                )
            )

    # Style consistency signals.
    if style_counts["journal_only"] > 0 and style_counts["journaltitle_only"] > 0:
        issues.append(
            _new_issue(
                "info",
                "mixed_journal_field_style",
                (
                    f"Mixed use of `journal` ({style_counts['journal_only']}) and "
                    f"`journaltitle` ({style_counts['journaltitle_only']})."
                ),
                "Choose one field style for articles and normalize across the bibliography.",
            )
        )
    if style_counts["year_only"] > 0 and style_counts["date_only"] > 0:
        issues.append(
            _new_issue(
                "info",
                "mixed_year_date_style",
                (
                    f"Mixed use of `year` ({style_counts['year_only']}) and "
                    f"`date` ({style_counts['date_only']})."
                ),
                "Normalize to house style (typically keep `year`, optionally also `date` when needed).",
            )
        )
    if style_counts["address_only"] > 0 and style_counts["location_only"] > 0:
        issues.append(
            _new_issue(
                "info",
                "mixed_address_location_style",
                (
                    f"Mixed use of `address` ({style_counts['address_only']}) and "
                    f"`location` ({style_counts['location_only']})."
                ),
                "Choose one location field style and normalize.",
            )
        )

    # Load errors are first-class issues.
    load_error_issues: List[dict] = []
    # Added during report creation if needed.

    by_severity: Dict[str, int] = defaultdict(int)
    by_code: Dict[str, int] = defaultdict(int)
    for issue in issues:
        by_severity[issue["severity"]] += 1
        by_code[issue["code"]] += 1

    issues_sorted = sorted(
        issues,
        key=lambda x: (
            SEVERITY_ORDER.get(x["severity"], 99),
            x["code"],
            x.get("key", ""),
            x.get("source", ""),
        ),
    )

    report = {
        "date": report_date,
        "bib_sources": [str(p) for p in bib_sources],
        "bib_source_count": len(bib_sources),
        "entry_count": len(records),
        "unique_key_count": len(key_occurrences),
        "style_counts": style_counts,
        "issue_counts": {
            "total": len(issues_sorted),
            "error": by_severity.get("error", 0),
            "warning": by_severity.get("warning", 0),
            "info": by_severity.get("info", 0),
        },
        "issues_by_code": dict(sorted(by_code.items())),
        "issues": issues_sorted,
        "load_error_issues": load_error_issues,
    }
    return report


def as_markdown(report: dict) -> str:
    lines: List[str] = []
    lines.append(f"# Full Bib Audit ({report['date']})")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Bib sources loaded: {report['bib_source_count']}")
    lines.append(f"- Total entries: {report['entry_count']}")
    lines.append(f"- Unique keys: {report['unique_key_count']}")
    lines.append(f"- Total issues: {report['issue_counts']['total']}")
    lines.append(f"- Errors: {report['issue_counts']['error']}")
    lines.append(f"- Warnings: {report['issue_counts']['warning']}")
    lines.append(f"- Info: {report['issue_counts']['info']}")
    lines.append("")

    lines.append("## Bib Sources")
    for src in report["bib_sources"]:
        lines.append(f"- `{src}`")
    lines.append("")

    lines.append("## Field Style Snapshot")
    style = report["style_counts"]
    lines.append(
        "- Journal fields: "
        f"`journal`={style['journal_only']}, "
        f"`journaltitle`={style['journaltitle_only']}, "
        f"both={style['both_journal_fields']}"
    )
    lines.append(
        "- Time fields: "
        f"`year`={style['year_only']}, "
        f"`date`={style['date_only']}, "
        f"both={style['both_year_date']}"
    )
    lines.append(
        "- Place fields: "
        f"`address`={style['address_only']}, "
        f"`location`={style['location_only']}, "
        f"both={style['both_address_location']}"
    )
    lines.append("")

    lines.append("## Issues By Code")
    if not report["issues_by_code"]:
        lines.append("- None")
    else:
        for code, count in report["issues_by_code"].items():
            lines.append(f"- `{code}`: {count}")
    lines.append("")

    lines.append("## Issue Details")
    if not report["issues"]:
        lines.append("- None")
    else:
        grouped: DefaultDict[str, List[dict]] = defaultdict(list)
        for issue in report["issues"]:
            grouped[issue["code"]].append(issue)

        for code in sorted(grouped):
            lines.append(f"### `{code}` ({len(grouped[code])})")
            for issue in grouped[code][:20]:
                loc = ""
                if issue.get("key"):
                    loc += f" key=`{issue['key']}`"
                if issue.get("source"):
                    loc += f" source=`{issue['source']}`"
                if issue.get("field"):
                    loc += f" field=`{issue['field']}`"
                lines.append(
                    f"- [{issue['severity']}] {issue['message']}{loc}"
                )
                lines.append(f"  Suggestion: {issue['suggestion']}")
            if len(grouped[code]) > 20:
                lines.append(f"- ... {len(grouped[code]) - 20} more")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit full bibliography data quality for one or more BibTeX files."
    )
    parser.add_argument(
        "--bib",
        action="append",
        default=[],
        help="Bib source file (repeatable). Default: references.bib",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Optional output file path. Format defaults to markdown unless --json is set.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON to stdout/output instead of markdown.",
    )
    parser.add_argument(
        "--date",
        default="",
        help="Optional report date override in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any error-level issues are found.",
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Exit non-zero if any warning-level issues are found.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)

    bib_args = args.bib if args.bib else ["references.bib"]
    bib_sources = [Path(p).expanduser().resolve() for p in bib_args]
    report_date = args.date or dt.date.today().isoformat()

    records, load_errors, load_issues = load_records(bib_sources)
    report = audit_records(records, bib_sources, report_date)

    # Promote load errors into error issues for output/strict handling.
    for err in load_errors:
        report["issues"].append(
            _new_issue(
                "error",
                "load_error",
                err,
                "Fix path/parse issues, then re-run audit.",
            )
        )
    report["issues"].extend(load_issues)
    if load_errors or load_issues:
        report["issues"] = sorted(
            report["issues"],
            key=lambda x: (
                SEVERITY_ORDER.get(x["severity"], 99),
                x["code"],
                x.get("key", ""),
                x.get("source", ""),
            ),
        )
        by_severity: Dict[str, int] = defaultdict(int)
        by_code: Dict[str, int] = defaultdict(int)
        for issue in report["issues"]:
            by_severity[issue["severity"]] += 1
            by_code[issue["code"]] += 1
        report["issue_counts"] = {
            "total": len(report["issues"]),
            "error": by_severity.get("error", 0),
            "warning": by_severity.get("warning", 0),
            "info": by_severity.get("info", 0),
        }
        report["issues_by_code"] = dict(sorted(by_code.items()))

    payload = json.dumps(report, indent=2, sort_keys=True) if args.json else as_markdown(report)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload, encoding="utf-8")
    else:
        print(payload)

    if args.strict and report["issue_counts"]["error"] > 0:
        return 1
    if args.strict_warnings and report["issue_counts"]["warning"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

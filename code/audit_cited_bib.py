#!/usr/bin/env python3
"""Audit bibliography quality for keys actually cited in the compiled book.

Reads citekeys and bib data sources from a .bcf file, then audits only cited
entries across the loaded BibTeX files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

try:  # Optional dependency
    import bibtexparser  # type: ignore
except Exception:  # pragma: no cover - fallback parser handles absence
    bibtexparser = None


YEAR_PATTERN = re.compile(r"^\d{4}[a-z]?$")

# Minimal required-field checks, conservative by design.
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
    "unpublished": ("title", "year"),
    "online": ("title", "year"),
    "misc": ("title", "year"),
    "software": ("title", "year"),
}


def _local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def parse_bcf(bcf_path: Path) -> Tuple[List[str], List[str]]:
    """Return (unique_citekeys, bib_datasources) from a BCF file."""
    tree = ET.parse(bcf_path)
    root = tree.getroot()

    citekeys: List[str] = []
    datasources: List[str] = []
    seen_keys = set()
    seen_sources = set()

    for elem in root.iter():
        tag = _local_name(elem.tag)
        text = (elem.text or "").strip()
        if not text:
            continue
        if tag == "citekey":
            if text != "*" and text not in seen_keys:
                seen_keys.add(text)
                citekeys.append(text)
        elif tag == "datasource":
            if text not in seen_sources:
                seen_sources.add(text)
                datasources.append(text)

    return citekeys, datasources


def load_bib_entries(bib_paths: Iterable[Path]) -> Tuple[Dict[str, dict], Dict[str, List[Path]], List[str]]:
    """Load BibTeX entries from paths; return (entries, key_to_paths, load_errors)."""
    entries: Dict[str, dict] = {}
    key_to_paths: Dict[str, List[Path]] = defaultdict(list)
    load_errors: List[str] = []

    for bib_path in bib_paths:
        if not bib_path.exists():
            load_errors.append(f"Missing bib file: {bib_path}")
            continue

        try:
            parsed_entries = parse_bib_file(bib_path)
        except Exception as exc:  # pragma: no cover - defensive
            load_errors.append(f"Failed to parse {bib_path}: {exc}")
            continue

        for entry in parsed_entries:
            key = entry.get("ID")
            if not key:
                continue
            key_to_paths[key].append(bib_path)
            if key not in entries:
                entries[key] = entry

    return entries, key_to_paths, load_errors


def parse_bib_file(path: Path) -> List[dict]:
    """Parse a bib file into a list of dict entries.

    Uses bibtexparser when available, otherwise a lightweight built-in parser.
    """
    if bibtexparser is not None:
        with path.open("r", encoding="utf-8") as fh:
            db = bibtexparser.load(fh)
        return list(db.entries)

    text = path.read_text(encoding="utf-8")
    return parse_bib_text(text)


def _find_matching(text: str, open_pos: int, open_ch: str, close_ch: str) -> int:
    """Find matching close char position for a BibTeX entry block."""
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

        # Skip non-entry declarations.
        if entry_type in {"comment", "preamble", "string"}:
            i = close_pos + 1
            continue

        raw_inside = text[open_pos + 1 : close_pos].strip()
        parts = _split_top_level(raw_inside, ",")
        if not parts:
            i = close_pos + 1
            continue

        key = parts[0].strip()
        if not key or key.startswith("%"):
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
    if match:
        return match.group(0)
    return ""


def audit_entry_fields(key: str, entry: dict) -> List[str]:
    """Return quality warnings for a cited entry."""
    warnings: List[str] = []
    entry_type = (entry.get("ENTRYTYPE") or "").lower().strip()

    required = REQUIRED_FIELDS.get(entry_type, ("title", "year"))
    for field in required:
        if field == "journal":
            if not _entry_value(entry, "journal", "journaltitle"):
                warnings.append("missing `journal`")
            continue
        if field == "year":
            if not _entry_year(entry):
                warnings.append("missing `year`")
            continue
        if not _entry_value(entry, field):
            warnings.append(f"missing `{field}`")

    # Most scholarly entries should have either author or editor.
    if not _entry_value(entry, "author") and not _entry_value(entry, "editor"):
        warnings.append("missing both `author` and `editor`")

    year = _entry_value(entry, "year")
    if year and not YEAR_PATTERN.match(year):
        warnings.append(f"non-standard `year` value `{year}`")

    return warnings


def make_case_suggestions(missing_keys: Sequence[str], known_keys: Iterable[str]) -> Dict[str, List[str]]:
    lower_map: Dict[str, List[str]] = defaultdict(list)
    for key in known_keys:
        lower_map[key.lower()].append(key)

    suggestions: Dict[str, List[str]] = {}
    for key in missing_keys:
        near = lower_map.get(key.lower(), [])
        if near:
            suggestions[key] = near
    return suggestions


def _split_ids(raw_ids: str) -> List[str]:
    """Split BibLaTeX `ids` into individual alias keys."""
    cleaned = _strip_braces(raw_ids).strip()
    if not cleaned:
        return []
    return [part.strip() for part in cleaned.split(",") if part.strip()]


def build_alias_map(entries: Dict[str, dict]) -> Dict[str, str]:
    """Map alias key -> canonical key from BibLaTeX `ids` fields."""
    alias_to_key: Dict[str, str] = {}
    for key, entry in entries.items():
        raw_ids = str(entry.get("ids", "")).strip()
        if not raw_ids:
            continue
        for alias in _split_ids(raw_ids):
            if alias == key:
                continue
            # Real entry keys always take precedence over aliases.
            if alias in entries:
                continue
            alias_to_key.setdefault(alias, key)
    return alias_to_key


def as_markdown(report: dict) -> str:
    lines: List[str] = []
    lines.append(f"# Cited Bib Audit ({report['date']})")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Cited keys: {report['cited_key_count']}")
    lines.append(f"- Bib sources loaded: {report['bib_source_count']}")
    lines.append(f"- Resolved cited keys: {report['resolved_key_count']}")
    lines.append(f"- Alias-resolved cited keys: {report.get('alias_resolved_key_count', 0)}")
    lines.append(f"- Missing cited keys: {report['missing_key_count']}")
    lines.append(f"- Cited entries with field warnings: {report['entries_with_warnings_count']}")
    lines.append(f"- Duplicate keys in loaded bib sources: {report['duplicate_key_count']}")
    lines.append("")

    lines.append("## Bib Sources")
    for src in report["bib_sources"]:
        lines.append(f"- `{src}`")
    lines.append("")

    if report["load_errors"]:
        lines.append("## Load Errors")
        for err in report["load_errors"]:
            lines.append(f"- {err}")
        lines.append("")

    lines.append("## Missing Cited Keys")
    if not report["missing_keys"]:
        lines.append("- None")
    else:
        for key in report["missing_keys"]:
            lines.append(f"- `{key}`")
            suggestions = report["missing_key_case_suggestions"].get(key, [])
            if suggestions:
                lines.append(f"  - case-similar keys: {', '.join(f'`{s}`' for s in suggestions)}")
    lines.append("")

    lines.append("## Alias Resolutions")
    if not report.get("alias_resolutions"):
        lines.append("- None")
    else:
        for alias, canonical in sorted(report["alias_resolutions"].items()):
            lines.append(f"- `{alias}` -> `{canonical}`")
    lines.append("")

    lines.append("## Duplicate Keys In Loaded Sources")
    if not report["duplicate_keys"]:
        lines.append("- None")
    else:
        for key, info in sorted(report["duplicate_keys"].items()):
            count = info["count"]
            files = info["files"]
            joined = ", ".join(f"`{p}`" for p in files)
            lines.append(f"- `{key}`: {count} occurrences ({joined})")
    lines.append("")

    lines.append("## Cited Entry Field Warnings")
    if not report["entry_warnings"]:
        lines.append("- None")
    else:
        for key, warnings in sorted(report["entry_warnings"].items()):
            joined = "; ".join(warnings)
            lines.append(f"- `{key}`: {joined}")
    lines.append("")

    return "\n".join(lines)


def build_report(
    bcf_path: Path,
    bib_sources: Sequence[Path],
    report_date: str,
) -> dict:
    cited_keys, _ = parse_bcf(bcf_path)
    entries, key_to_paths, load_errors = load_bib_entries(bib_sources)
    alias_to_key = build_alias_map(entries)

    resolved_map: Dict[str, str] = {}
    missing_keys: List[str] = []
    for key in cited_keys:
        if key in entries:
            resolved_map[key] = key
            continue
        alias_target = alias_to_key.get(key)
        if alias_target:
            resolved_map[key] = alias_target
            continue
        missing_keys.append(key)

    resolved_keys = list(resolved_map.keys())
    alias_resolutions = {
        citekey: canonical for citekey, canonical in resolved_map.items() if citekey != canonical
    }

    case_suggestions = make_case_suggestions(
        sorted(missing_keys),
        list(entries.keys()) + list(alias_to_key.keys()),
    )

    duplicate_keys = {}
    for key, paths in key_to_paths.items():
        if len(paths) > 1:
            unique_files = sorted({str(p) for p in paths})
            duplicate_keys[key] = {"count": len(paths), "files": unique_files}

    entry_warnings: Dict[str, List[str]] = {}
    for cited_key, canonical_key in resolved_map.items():
        warnings = audit_entry_fields(cited_key, entries[canonical_key])
        if warnings:
            entry_warnings[cited_key] = warnings

    report = {
        "date": report_date,
        "bcf_path": str(bcf_path),
        "bib_sources": [str(p) for p in bib_sources],
        "bib_source_count": len(bib_sources),
        "cited_key_count": len(cited_keys),
        "resolved_key_count": len(resolved_keys),
        "alias_resolved_key_count": len(alias_resolutions),
        "alias_resolutions": dict(sorted(alias_resolutions.items())),
        "missing_key_count": len(missing_keys),
        "missing_keys": sorted(missing_keys),
        "missing_key_case_suggestions": case_suggestions,
        "duplicate_key_count": len(duplicate_keys),
        "duplicate_keys": duplicate_keys,
        "entries_with_warnings_count": len(entry_warnings),
        "entry_warnings": entry_warnings,
        "load_errors": load_errors,
    }
    return report


def resolve_bib_sources(bcf_path: Path, cli_bib_sources: Sequence[str]) -> List[Path]:
    if cli_bib_sources:
        return [Path(p).expanduser().resolve() for p in cli_bib_sources]

    _, source_names = parse_bcf(bcf_path)
    project_root = bcf_path.parent.parent.resolve()
    sources: List[Path] = []
    for name in source_names:
        source_path = (project_root / name).resolve()
        sources.append(source_path)
    return sources


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit BibTeX entries for keys cited in a compiled .bcf file."
    )
    parser.add_argument(
        "--bcf",
        default="build/hpc-book.bcf",
        help="Path to BCF file (default: build/hpc-book.bcf).",
    )
    parser.add_argument(
        "--bib",
        action="append",
        default=[],
        help="Bib source file (repeatable). If omitted, use data sources from the BCF.",
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
        "--strict",
        action="store_true",
        help="Exit non-zero if missing cited keys or load errors are found.",
    )
    parser.add_argument(
        "--date",
        default="",
        help="Optional report date override in YYYY-MM-DD format.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    bcf_path = Path(args.bcf).expanduser().resolve()
    if not bcf_path.exists():
        print(f"BCF file not found: {bcf_path}", file=sys.stderr)
        return 2

    bib_sources = resolve_bib_sources(bcf_path, args.bib)
    report_date = args.date or dt.date.today().isoformat()
    report = build_report(bcf_path, bib_sources, report_date)

    payload = json.dumps(report, indent=2, sort_keys=True) if args.json else as_markdown(report)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    if args.strict and (report["missing_key_count"] > 0 or report["load_errors"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

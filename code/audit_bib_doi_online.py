#!/usr/bin/env python3
"""Online DOI quality audit for full bibliography.

This script audits every entry in a BibTeX file and reports:
- malformed DOI strings
- DOI resolution failures via Crossref
- DOI metadata mismatches (title/author/year)
- missing DOI with high-confidence DOI candidates

Outputs:
- JSON report with per-entry results
- Markdown summary
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
YEAR_PATTERN = re.compile(r"^(\d{4})")


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
        m = YEAR_PATTERN.search(year)
        return m.group(1) if m else year
    date_val = _entry_value(entry, "date")
    if not date_val:
        return ""
    m = re.search(r"\d{4}", date_val)
    return m.group(0) if m else ""


def _normalize_doi(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    return text


def _normalize_title(raw: str) -> str:
    text = html.unescape(_strip_braces(raw)).lower()
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"\b(i|b|sup|sub)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\b\d+\b$", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _normalize_person_token(token: str) -> str:
    token = token.strip().lower()
    token = re.sub(r"\\[\"'`^~=.Hcukvbdtr]\{?([a-zA-Z])\}?", r"\1", token)
    token = re.sub(r"\\[a-zA-Z]{1,2}\{?([a-zA-Z])\}?", r"\1", token)
    token = re.sub(r"\\.", "", token)
    token = token.replace("{", "").replace("}", "")
    token = token.replace("’", "'").replace("`", "'")
    token = token.replace("ı", "i").replace("ł", "l").replace("ø", "o")
    token = token.replace("ß", "ss").replace("đ", "d").replace("æ", "ae").replace("œ", "oe")
    token = unicodedata.normalize("NFKD", token)
    token = "".join(ch for ch in token if not unicodedata.combining(ch))
    token = re.sub(r"[^a-z0-9]+", "", token)
    return token


def _first_author_surname(raw_author: str) -> str:
    if not raw_author:
        return ""
    first = raw_author.split(" and ")[0].strip()
    first = _strip_braces(first)
    if "," in first:
        return _normalize_person_token(first.split(",", 1)[0].strip())
    parts = first.split()
    return _normalize_person_token(parts[-1]) if parts else ""


def _crossref_first_author_surname(message: dict) -> str:
    authors = message.get("author") or []
    if not authors:
        return ""
    first = authors[0]
    family_raw = str(first.get("family", "")).strip()
    given_raw = str(first.get("given", "")).strip()
    if family_raw and not given_raw and " " in family_raw and "," not in family_raw:
        family_raw = family_raw.split()[-1]
    family = _normalize_person_token(family_raw)
    if family:
        return family
    name = str(first.get("name", "")).strip().lower()
    if not name:
        return ""
    parts = name.split()
    return _normalize_person_token(parts[-1]) if parts else ""


def _crossref_title(message: dict) -> str:
    titles = message.get("title") or []
    if titles and isinstance(titles, list):
        return str(titles[0]).strip()
    return ""


def _crossref_year(message: dict) -> str:
    for field in ("published-print", "published-online", "issued", "created"):
        block = message.get(field) or {}
        date_parts = block.get("date-parts") or []
        if date_parts and isinstance(date_parts, list) and date_parts[0]:
            year = str(date_parts[0][0])
            if year.isdigit() and len(year) == 4:
                return year
    return ""


def _title_similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def _title_match(a: str, b: str) -> Tuple[bool, float]:
    na = _normalize_title(a)
    nb = _normalize_title(b)
    if not na or not nb:
        return False, 0.0
    if na == nb:
        return True, 1.0
    if na in nb or nb in na:
        return True, 0.96
    a_tokens = set(na.split())
    b_tokens = set(nb.split())
    if a_tokens and b_tokens:
        overlap = len(a_tokens & b_tokens) / float(max(len(a_tokens), len(b_tokens)))
        if overlap >= 0.8:
            return True, max(overlap, 0.9)
    score = _title_similarity(na, nb)
    return score >= 0.8, score


def _year_match(bib_year: str, cr_year: str) -> bool:
    if not bib_year or not cr_year:
        return False
    try:
        by = int(re.search(r"\d{4}", bib_year).group(0))  # type: ignore[union-attr]
        cy = int(re.search(r"\d{4}", cr_year).group(0))  # type: ignore[union-attr]
    except Exception:
        return False
    return by == cy or abs(by - cy) <= 1


def _author_match(bib_author: str, cr_author: str) -> Optional[bool]:
    if not bib_author or not cr_author:
        return None
    b = bib_author.strip().lower()
    c = cr_author.strip().lower()
    if b == c:
        return True
    if b in c or c in b:
        return True
    if c.endswith(b) or b.endswith(c):
        return True
    return False


def _safe_get_json(url: str, headers: Dict[str, str], timeout: float, retries: int = 3) -> Tuple[Optional[dict], Optional[str]]:
    backoff = 1.0
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.load(resp)
            return payload, None
        except Exception as exc:
            err = str(exc)
            if attempt == retries:
                return None, err
            time.sleep(backoff)
            backoff *= 2.0
    return None, "unknown_error"


def fetch_crossref_work(doi: str, headers: Dict[str, str], timeout: float) -> Tuple[Optional[dict], Optional[str]]:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    payload, err = _safe_get_json(url, headers=headers, timeout=timeout)
    if err:
        return None, err
    msg = payload.get("message") if isinstance(payload, dict) else None
    if not isinstance(msg, dict):
        return None, "invalid_crossref_payload"
    return msg, None


def fetch_doi_csl(doi: str, timeout: float, user_agent: str) -> Tuple[Optional[dict], Optional[str]]:
    url = f"https://doi.org/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "application/vnd.citationstyles.csl+json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.load(resp)
        if not isinstance(payload, dict):
            return None, "invalid_doi_csl_payload"
        return payload, None
    except Exception as exc:
        return None, str(exc)


def csl_to_message(csl: dict) -> dict:
    title = str(csl.get("title", "")).strip()
    authors = []
    for person in csl.get("author") or []:
        if not isinstance(person, dict):
            continue
        family = str(person.get("family", "")).strip()
        given = str(person.get("given", "")).strip()
        name = str(person.get("literal", "")).strip()
        item = {}
        if family:
            item["family"] = family
        if given:
            item["given"] = given
        if name:
            item["name"] = name
        if item:
            authors.append(item)

    issued = csl.get("issued") if isinstance(csl.get("issued"), dict) else {}
    if not issued:
        year_text = str(csl.get("issued", "")).strip()
        year_match = re.search(r"\d{4}", year_text)
        if year_match:
            issued = {"date-parts": [[int(year_match.group(0))]]}
    message = {
        "title": [title] if title else [],
        "author": authors,
        "issued": issued,
    }
    return message


def search_crossref_candidate(
    title: str,
    author_surname: str,
    year: str,
    rows: int,
    headers: Dict[str, str],
    timeout: float,
) -> Tuple[Optional[dict], Optional[str]]:
    q_parts = [title.strip()]
    if author_surname:
        q_parts.append(author_surname)
    if year:
        q_parts.append(year)
    query = " ".join(part for part in q_parts if part)
    if not query:
        return None, "insufficient_query"

    params = {
        "query.bibliographic": query,
        "rows": str(rows),
        "select": "DOI,title,author,issued,published-print,published-online,score",
    }
    url = f"https://api.crossref.org/works?{urllib.parse.urlencode(params)}"
    payload, err = _safe_get_json(url, headers=headers, timeout=timeout)
    if err:
        return None, err
    message = payload.get("message") if isinstance(payload, dict) else {}
    items = message.get("items") if isinstance(message, dict) else []
    if not items:
        return None, "no_results"

    best: Optional[dict] = None
    best_rank = -1.0
    bib_author = author_surname.lower().strip()
    for item in items:
        cr_title = _crossref_title(item)
        cr_author = _crossref_first_author_surname(item)
        cr_year = _crossref_year(item)
        title_ok, title_score = _title_match(title, cr_title)
        author_state = _author_match(bib_author, cr_author)
        author_ok = bool(author_state is True)
        year_ok = _year_match(year, cr_year)
        crossref_score = float(item.get("score", 0.0))

        rank = (
            100.0 * (1.0 if title_ok else 0.0)
            + 30.0 * title_score
            + 35.0 * (1.0 if author_ok else 0.0)
            + 20.0 * (1.0 if year_ok else 0.0)
            + min(crossref_score, 100.0) * 0.15
        )
        candidate = {
            "doi": str(item.get("DOI", "")).strip(),
            "crossref_score": crossref_score,
            "title_score": round(title_score, 4),
            "title_match": title_ok,
            "author_match": author_ok,
            "year_match": year_ok,
            "crossref_title": cr_title,
            "crossref_author": cr_author,
            "crossref_year": cr_year,
            "rank": round(rank, 4),
        }
        if rank > best_rank:
            best_rank = rank
            best = candidate

    if not best or not best.get("doi"):
        return None, "no_viable_candidate"
    return best, None


def _candidate_confidence(candidate: dict) -> str:
    title_ok = bool(candidate.get("title_match"))
    author_ok = bool(candidate.get("author_match"))
    year_ok = bool(candidate.get("year_match"))
    title_score = float(candidate.get("title_score", 0.0))
    if title_ok and author_ok and (year_ok or not candidate.get("crossref_year")):
        return "high"
    if title_ok and (author_ok or year_ok):
        return "medium"
    if title_ok and title_score >= 0.95:
        return "medium"
    if title_score >= 0.9 and (author_ok or year_ok):
        return "medium"
    return "low"


def audit_entries(
    entries: List[dict],
    lookups_for_missing: bool,
    rows: int,
    headers: Dict[str, str],
    timeout: float,
    user_agent: str,
    sleep_seconds: float,
) -> dict:
    work_cache: Dict[str, Tuple[Optional[dict], Optional[str], str]] = {}
    results: List[dict] = []

    for idx, entry in enumerate(entries, 1):
        key = str(entry.get("ID", "")).strip()
        entry_type = str(entry.get("ENTRYTYPE", "")).lower().strip()
        title = _entry_value(entry, "title")
        author = _entry_value(entry, "author")
        first_author = _first_author_surname(author)
        year = _entry_year(entry)
        doi_raw = _entry_value(entry, "doi")
        doi_norm = _normalize_doi(doi_raw) if doi_raw else ""

        row = {
            "index": idx,
            "key": key,
            "entrytype": entry_type,
            "title": title,
            "first_author_surname": first_author,
            "year": year,
            "doi_raw": doi_raw,
            "doi_normalized": doi_norm,
            "status": "",
            "severity": "",
            "notes": [],
            "crossref_title": "",
            "crossref_author": "",
            "crossref_year": "",
            "title_similarity": None,
            "year_match": None,
            "author_match": None,
            "suggested_doi": "",
            "suggestion_confidence": "",
            "metadata_source": "",
        }

        if doi_raw:
            if not DOI_PATTERN.match(doi_norm):
                row["status"] = "doi_malformed"
                row["severity"] = "warning"
                row["notes"].append("DOI is present but fails basic DOI format validation.")
                results.append(row)
                continue

            if doi_norm.lower() not in work_cache:
                cr_msg, cr_err = fetch_crossref_work(doi_norm, headers, timeout)
                if cr_msg:
                    work_cache[doi_norm.lower()] = (cr_msg, None, "crossref")
                else:
                    csl_payload, csl_err = fetch_doi_csl(doi_norm, timeout, user_agent)
                    if csl_payload:
                        work_cache[doi_norm.lower()] = (csl_to_message(csl_payload), None, "doi.org")
                    else:
                        work_cache[doi_norm.lower()] = (None, cr_err or csl_err or "unknown", "none")
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
            cr_msg, cr_err, meta_source = work_cache[doi_norm.lower()]
            row["metadata_source"] = meta_source
            if cr_err or not cr_msg:
                row["status"] = "doi_unresolved"
                row["severity"] = "warning"
                row["notes"].append(f"DOI did not resolve cleanly via Crossref/doi.org: {cr_err or 'unknown'}")
                results.append(row)
                continue

            cr_title = _crossref_title(cr_msg)
            cr_author = _crossref_first_author_surname(cr_msg)
            cr_year = _crossref_year(cr_msg)
            title_ok, title_score = _title_match(title, cr_title)
            author_ok = (first_author == cr_author) if first_author and cr_author else None
            year_ok = _year_match(year, cr_year) if year and cr_year else None

            row["crossref_title"] = cr_title
            row["crossref_author"] = cr_author
            row["crossref_year"] = cr_year
            row["title_similarity"] = round(title_score, 4)
            row["author_match"] = _author_match(first_author, cr_author)
            row["year_match"] = year_ok

            mismatch_notes: List[str] = []
            major_mismatch = False
            if not title_ok:
                mismatch_notes.append("Title does not match DOI metadata.")
                major_mismatch = True
            if row["author_match"] is False:
                mismatch_notes.append("First-author surname does not match DOI metadata.")
            if year_ok is False:
                mismatch_notes.append("Year differs from DOI metadata (allowing +/-1 year).")

            if mismatch_notes and major_mismatch:
                row["status"] = "doi_metadata_mismatch"
                row["severity"] = "warning"
                row["notes"].extend(mismatch_notes)
            elif mismatch_notes and row["author_match"] is False and year_ok is False:
                row["status"] = "doi_metadata_mismatch"
                row["severity"] = "warning"
                row["notes"].extend(mismatch_notes)
            elif mismatch_notes and row["author_match"] is False:
                row["status"] = "doi_ok_author_variant"
                row["severity"] = "info"
                row["notes"].extend(mismatch_notes)
            elif mismatch_notes and year_ok is False:
                row["status"] = "doi_ok_year_variant"
                row["severity"] = "info"
                row["notes"].extend(mismatch_notes)
            else:
                row["status"] = "doi_ok"
                row["severity"] = "ok"
                row["notes"].append("DOI resolved and metadata is consistent.")
            results.append(row)
            continue

        if not lookups_for_missing:
            row["status"] = "missing_doi"
            row["severity"] = "info"
            row["notes"].append("DOI is missing.")
            results.append(row)
            continue

        candidate, cand_err = search_crossref_candidate(
            title=title,
            author_surname=first_author,
            year=year,
            rows=rows,
            headers=headers,
            timeout=timeout,
        )
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)

        if not candidate:
            row["status"] = "missing_doi_no_match"
            row["severity"] = "info"
            row["notes"].append(f"No DOI candidate found ({cand_err}).")
            results.append(row)
            continue

        confidence = _candidate_confidence(candidate)
        row["suggested_doi"] = candidate.get("doi", "")
        row["suggestion_confidence"] = confidence
        row["crossref_title"] = candidate.get("crossref_title", "")
        row["crossref_author"] = candidate.get("crossref_author", "")
        row["crossref_year"] = candidate.get("crossref_year", "")
        row["title_similarity"] = candidate.get("title_score")
        row["author_match"] = candidate.get("author_match")
        row["year_match"] = candidate.get("year_match")

        if confidence == "high":
            row["status"] = "missing_doi_candidate_high"
            row["severity"] = "warning"
            row["notes"].append("High-confidence DOI candidate found.")
        elif confidence == "medium":
            row["status"] = "missing_doi_candidate_medium"
            row["severity"] = "info"
            row["notes"].append("Medium-confidence DOI candidate found; manual confirmation needed.")
        else:
            row["status"] = "missing_doi_candidate_low"
            row["severity"] = "info"
            row["notes"].append("Low-confidence DOI candidate found; likely needs manual lookup.")
        results.append(row)

    status_counts = Counter(item["status"] for item in results)
    severity_counts = Counter(item["severity"] for item in results)
    return {
        "entry_count": len(entries),
        "status_counts": dict(sorted(status_counts.items())),
        "severity_counts": dict(sorted(severity_counts.items())),
        "results": results,
    }


def make_markdown(report: dict, report_date: str, bib_path: Path) -> str:
    lines: List[str] = []
    lines.append(f"# DOI Audit Report ({report_date})")
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- Bib source: `{bib_path}`")
    lines.append(f"- Total entries audited: {report['entry_count']}")
    lines.append("")
    lines.append("## Status Counts")
    for status, count in report["status_counts"].items():
        lines.append(f"- `{status}`: {count}")
    lines.append("")
    lines.append("## Severity Counts")
    for sev, count in report["severity_counts"].items():
        lines.append(f"- `{sev}`: {count}")
    lines.append("")
    lines.append("## Key Findings")

    mismatch = [r for r in report["results"] if r["status"] == "doi_metadata_mismatch"]
    unresolved = [r for r in report["results"] if r["status"] == "doi_unresolved"]
    malformed = [r for r in report["results"] if r["status"] == "doi_malformed"]
    missing_high = [r for r in report["results"] if r["status"] == "missing_doi_candidate_high"]

    lines.append(f"- DOI metadata mismatches: {len(mismatch)}")
    lines.append(f"- DOI unresolved: {len(unresolved)}")
    lines.append(f"- DOI malformed: {len(malformed)}")
    lines.append(f"- Missing DOI with high-confidence candidate: {len(missing_high)}")
    lines.append("")

    def _emit_table(title: str, rows: List[dict], limit: int = 40) -> None:
        lines.append(f"## {title}")
        if not rows:
            lines.append("- None")
            lines.append("")
            return
        lines.append("| Key | Status | DOI | Suggested DOI | Notes |")
        lines.append("|---|---|---|---|---|")
        for item in rows[:limit]:
            notes = "; ".join(item.get("notes") or [])
            lines.append(
                f"| `{item['key']}` | `{item['status']}` | `{item.get('doi_normalized','')}` | "
                f"`{item.get('suggested_doi','')}` | {notes} |"
            )
        if len(rows) > limit:
            lines.append(f"| ... | ... | ... | ... | {len(rows)-limit} more rows not shown |")
        lines.append("")

    _emit_table("DOI Metadata Mismatches", mismatch)
    _emit_table("DOI Unresolved", unresolved)
    _emit_table("DOI Malformed", malformed)
    _emit_table("Missing DOI (High Confidence Candidates)", missing_high)
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit bibliography DOI quality using Crossref.")
    parser.add_argument("--bib", default="references.bib", help="BibTeX file path.")
    parser.add_argument("--output-json", default="", help="Output JSON report path.")
    parser.add_argument("--output-md", default="", help="Output markdown report path.")
    parser.add_argument(
        "--email",
        default="noreply@example.com",
        help="Contact email for polite API User-Agent.",
    )
    parser.add_argument("--timeout", type=float, default=25.0, help="HTTP timeout seconds.")
    parser.add_argument("--rows", type=int, default=5, help="Crossref rows for DOI candidate search.")
    parser.add_argument("--sleep", type=float, default=0.05, help="Sleep between requests in seconds.")
    parser.add_argument(
        "--skip-missing-lookups",
        action="store_true",
        help="Skip Crossref DOI discovery for entries without DOI.",
    )
    parser.add_argument("--date", default="", help="Optional report date (YYYY-MM-DD).")
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    bib_path = Path(args.bib).expanduser().resolve()
    if not bib_path.exists():
        print(f"Missing bib file: {bib_path}", file=sys.stderr)
        return 2

    report_date = args.date or dt.date.today().isoformat()
    entries = parse_bib_file(bib_path)
    ua = f"HPC-bib-audit/1.0 (mailto:{args.email})"
    headers = {
        "User-Agent": ua,
        "Accept": "application/json",
    }

    report = audit_entries(
        entries=entries,
        lookups_for_missing=not args.skip_missing_lookups,
        rows=max(1, args.rows),
        headers=headers,
        timeout=max(5.0, args.timeout),
        user_agent=ua,
        sleep_seconds=max(0.0, args.sleep),
    )
    report["date"] = report_date
    report["bib_source"] = str(bib_path)

    if args.output_json:
        out_json = Path(args.output_json).expanduser().resolve()
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    else:
        print(json.dumps(report, indent=2, sort_keys=True))

    if args.output_md:
        out_md = Path(args.output_md).expanduser().resolve()
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text(make_markdown(report, report_date, bib_path), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Interactive walkthrough for term-audit decisions.

Reads `reports/term-audit-decisions.csv` and lets you review issues one-by-one
without editing CSV manually.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Sequence


LEGACY_CSV = "reports/term-audit-decisions.csv"
SEMANTIC_CSV = "reports/term-semantic-audit-decisions.csv"
SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_DIR.parent


def default_csv_path() -> str:
    semantic = (PROJECT_ROOT / SEMANTIC_CSV).resolve()
    if semantic.exists():
        return SEMANTIC_CSV
    return LEGACY_CSV


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    default_csv = default_csv_path()
    parser = argparse.ArgumentParser(
        description="Interactive reviewer for term consistency audit decisions."
    )
    parser.add_argument(
        "--csv",
        default=default_csv,
        help=f"Path to decisions CSV (default: {default_csv}).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Review all rows, not only pending rows.",
    )
    parser.add_argument(
        "--start-at",
        default="",
        help="Issue ID to start at (e.g., T0042).",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI colors in output.",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print decision summary and exit.",
    )
    return parser.parse_args(argv)


def resolve_project_relative(path_str: str) -> Path:
    p = Path(path_str).expanduser()
    if p.is_absolute():
        return p.resolve()

    cwd_candidate = (Path.cwd() / p).resolve()
    root_candidate = (PROJECT_ROOT / p).resolve()
    if cwd_candidate.exists():
        return cwd_candidate
    return root_candidate


def use_color(disabled: bool) -> bool:
    return (not disabled) and sys.stdout.isatty()


def ansi(text: str, code: str, enabled: bool) -> str:
    if not enabled:
        return text
    return f"\033[{code}m{text}\033[0m"


def style_term(text: str, enabled: bool) -> str:
    return ansi(f"<<< {text} >>>", "1;97;41", enabled)


def style_header(text: str, enabled: bool) -> str:
    return ansi(text, "1;36", enabled)


def style_hint(text: str, enabled: bool) -> str:
    return ansi(text, "2", enabled)


def style_context_highlight(text: str, enabled: bool) -> str:
    return ansi(text, "1;30;43", enabled)


def load_rows(csv_path: Path) -> tuple[List[Dict[str, str]], List[str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    return rows, fieldnames


def save_rows(csv_path: Path, fieldnames: List[str], rows: List[Dict[str, str]]) -> None:
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def backup_csv(csv_path: Path) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = csv_path.with_suffix(csv_path.suffix + f".{stamp}.bak")
    backup.write_text(csv_path.read_text(encoding="utf-8"), encoding="utf-8")
    return backup


def decision_counts(rows: List[Dict[str, str]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for row in rows:
        key = (row.get("decision") or "").strip() or "(empty)"
        counts[key] = counts.get(key, 0) + 1
    return counts


def matching_indexes(rows: List[Dict[str, str]], observed_form: str, include_decided: bool) -> List[int]:
    out: List[int] = []
    for i, row in enumerate(rows):
        if row.get("observed_form", "") != observed_form:
            continue
        if include_decided:
            out.append(i)
        else:
            if row.get("decision", "").strip() == "pending":
                out.append(i)
    return out


def highlight_context(context: str, observed: str, color_enabled: bool) -> str:
    text = context
    marker_open = "[["
    marker_close = "]]"
    while marker_open in text and marker_close in text:
        start = text.find(marker_open)
        if start == -1:
            break
        end = text.find(marker_close, start + len(marker_open))
        if end == -1:
            break
        term = text[start + len(marker_open) : end]
        repl = style_context_highlight(term, color_enabled)
        text = text[:start] + repl + text[end + len(marker_close) :]

    if marker_open not in text and marker_close not in text and observed:
        token = observed
        if token in text:
            text = text.replace(token, style_context_highlight(token, color_enabled), 1)
    return text


def row_location(row: Dict[str, str]) -> str:
    file_path = row.get("file", "")
    line = row.get("line", "")
    if file_path and line:
        return f"{file_path}:{line}"
    return file_path or "(unknown location)"


def print_summary(rows: List[Dict[str, str]]) -> None:
    counts = decision_counts(rows)
    total = len(rows)
    print(f"Total rows: {total}")
    for key in sorted(counts):
        print(f"- {key}: {counts[key]}")


def prompt_action(color_enabled: bool) -> str:
    print(style_hint("Action: [k]eep  [r]eplace canonical  [c]ustom  [p]ending/skip  [b]ack  [q]uit  [?]help", color_enabled))
    return input("> ").strip().lower()


def prompt_scope(color_enabled: bool) -> str:
    print(style_hint("Scope: [t]his occurrence or [a]ll same observed form?", color_enabled))
    while True:
        answer = input("scope> ").strip().lower()
        if answer in {"t", "a"}:
            return "this_occurrence" if answer == "t" else "all_same_observed_form"
        print("Please enter 't' or 'a'.")


def apply_decision(
    rows: List[Dict[str, str]],
    idx: int,
    decision: str,
    custom_replacement: str,
    scope: str,
    include_decided_for_all: bool,
) -> List[int]:
    row = rows[idx]
    targets: List[int]
    if scope == "all_same_observed_form":
        targets = matching_indexes(rows, row.get("observed_form", ""), include_decided_for_all)
    else:
        targets = [idx]

    for t in targets:
        rows[t]["decision"] = decision
        rows[t]["custom_replacement"] = custom_replacement
        rows[t]["scope"] = scope

    return targets


def interactive_review(csv_path: Path, rows: List[Dict[str, str]], fieldnames: List[str], args: argparse.Namespace) -> int:
    color_enabled = use_color(args.no_color)

    queue = list(range(len(rows)))
    if not args.all:
        queue = [i for i in queue if rows[i].get("decision", "").strip() == "pending"]

    if not queue:
        print("No rows to review for current filter.")
        return 0

    start_pos = 0
    if args.start_at:
        for pos, idx in enumerate(queue):
            if rows[idx].get("issue_id", "") == args.start_at:
                start_pos = pos
                break

    backup_path = backup_csv(csv_path)
    print(f"Backup created: {backup_path}")

    pos = start_pos
    try:
        while pos < len(queue):
            idx = queue[pos]
            row = rows[idx]

            if not args.all and row.get("decision", "").strip() != "pending":
                pos += 1
                continue

            width = min(100, shutil.get_terminal_size((100, 30)).columns)
            print("\n" + "=" * width)
            print(style_header(f"Issue {pos + 1}/{len(queue)}   {row.get('issue_id', '')}   {row.get('issue_type', '')}", color_enabled))
            print("-" * width)

            observed = row.get("observed_form", "")
            canonical = row.get("canonical_term", "")
            suggested = row.get("suggested_replacement", "")
            alternatives = row.get("alternatives", "")
            current_decision = row.get("decision", "") or "pending"
            notes = row.get("notes", "")

            print(f"Location: {row_location(row)}")
            print(f"Term At Issue: {style_term(observed, color_enabled)}")
            if canonical:
                print(f"Canonical: {canonical}")
            if suggested:
                print(f"Suggested replacement: {suggested}")
            if alternatives:
                print(f"Alternatives: {alternatives}")
            print(f"Current decision: {current_decision}")
            if notes:
                print(f"Notes: {notes}")
            print()

            context = highlight_context(row.get("context", ""), observed, color_enabled)
            print("Context:")
            print(context)
            print()

            action = prompt_action(color_enabled)

            if action == "?":
                print("k = keep")
                print("r = replace_with_canonical")
                print("c = replace_custom")
                print("p = leave pending and move on")
                print("b = go back one issue")
                print("q = save and quit")
                continue
            if action == "q":
                save_rows(csv_path, fieldnames, rows)
                print("Saved. Exiting.")
                return 0
            if action == "b":
                pos = max(0, pos - 1)
                continue
            if action == "p" or action == "":
                pos += 1
                continue

            if action == "k":
                decision = "keep"
                custom = ""
            elif action == "r":
                decision = "replace_with_canonical"
                custom = ""
            elif action == "c":
                custom = input("Custom replacement> ").strip()
                if not custom:
                    print("Custom replacement cannot be empty.")
                    continue
                decision = "replace_custom"
            else:
                print("Unknown action. Enter ?, k, r, c, p, b, or q.")
                continue

            scope = prompt_scope(color_enabled)
            targets = apply_decision(
                rows,
                idx,
                decision,
                custom,
                scope,
                include_decided_for_all=args.all,
            )
            save_rows(csv_path, fieldnames, rows)

            print(
                f"Saved decision '{decision}' for {len(targets)} row(s)."
            )
            pos += 1

    except KeyboardInterrupt:
        save_rows(csv_path, fieldnames, rows)
        print("\nInterrupted. Progress saved.")
        return 130

    save_rows(csv_path, fieldnames, rows)
    print("Review queue complete. All changes saved.")
    return 0


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    csv_path = resolve_project_relative(args.csv)

    if not csv_path.exists():
        print(f"ERROR: decisions CSV not found: {csv_path}", file=sys.stderr)
        return 2

    rows, fieldnames = load_rows(csv_path)
    required = {
        "issue_id",
        "issue_type",
        "file",
        "line",
        "observed_form",
        "canonical_term",
        "suggested_replacement",
        "alternatives",
        "decision",
        "custom_replacement",
        "scope",
        "context",
    }
    missing = sorted(required - set(fieldnames))
    if missing:
        print(f"ERROR: CSV is missing required columns: {', '.join(missing)}", file=sys.stderr)
        return 2

    if args.summary:
        print_summary(rows)
        return 0

    return interactive_review(csv_path, rows, fieldnames, args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

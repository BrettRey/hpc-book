#!/usr/bin/env python3
"""Apply strict name/lexical judgment safely to LaTeX files.

For dropped name tags, remove the tag command.
For dropped lexical tags:
- \\ixl{...} is replaced by visible term text (to avoid deleting prose tokens).
- \\ixlq{...} is removed (quiet marker used next to explicit surface text).
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def normalize_term(content: str) -> str:
    text = (content or "").strip()
    if text.endswith("|(") or text.endswith("|)"):
        text = text[:-2]
    if "@" in text:
        text = text.split("@", 1)[1]
    if "|" in text:
        text = text.split("|", 1)[0]
    if "!" in text:
        text = text.split("!")[-1]
    return text.strip()


def replacement_for(item: dict[str, Any]) -> str:
    item_type = str(item.get("type", "")).strip().lower()
    cmd = str(item.get("cmd", "")).strip().lower()
    if item_type != "language":
        return ""
    if cmd == "ixl":
        term = normalize_term(str(item.get("term", "")))
        return f"\\textit{{{term}}}"
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, help="Strict judgment report JSON")
    args = parser.parse_args()

    report_path = Path(args.report)
    report = json.loads(report_path.read_text(encoding="utf-8"))
    items = report.get("items", [])
    decisions = report.get("decisions", [])

    item_by_id = {
        int(item["id"]): item
        for item in items
        if isinstance(item, dict) and "id" in item
    }

    dropped_items: list[dict[str, Any]] = []
    for decision in decisions:
        if not isinstance(decision, dict) or "id" not in decision:
            continue
        if decision.get("keep") is not False:
            continue
        item = item_by_id.get(int(decision["id"]))
        if item:
            dropped_items.append(item)

    by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in dropped_items:
        by_file[item["file"]].append(item)

    replaced = 0
    failed = 0
    by_cmd = Counter()
    by_type = Counter()

    for file_path, entries in by_file.items():
        path = Path(file_path)
        if not path.exists():
            failed += len(entries)
            continue
        content = path.read_text(encoding="utf-8")

        spans = []
        fallback = []
        for entry in entries:
            start = entry.get("start")
            end = entry.get("end")
            tag = entry.get("tag", "")
            if (
                isinstance(start, int)
                and isinstance(end, int)
                and 0 <= start < end <= len(content)
                and content[start:end] == tag
            ):
                spans.append((start, end, entry))
            else:
                fallback.append(entry)

        spans.sort(key=lambda t: t[0], reverse=True)
        for start, end, entry in spans:
            replacement = replacement_for(entry)
            content = content[:start] + replacement + content[end:]
            replaced += 1
            by_cmd[str(entry.get("cmd", ""))] += 1
            by_type[str(entry.get("type", ""))] += 1

        if fallback:
            lines = content.splitlines(keepends=True)
            for entry in fallback:
                tag = entry.get("tag", "")
                if not tag:
                    failed += 1
                    continue
                replacement = replacement_for(entry)
                line_no = entry.get("line")
                done = False
                if isinstance(line_no, int) and 1 <= line_no <= len(lines):
                    idx = line_no - 1
                    if tag in lines[idx]:
                        lines[idx] = lines[idx].replace(tag, replacement, 1)
                        done = True
                if not done and tag in content:
                    content = content.replace(tag, replacement, 1)
                    done = True
                if done:
                    replaced += 1
                    by_cmd[str(entry.get("cmd", ""))] += 1
                    by_type[str(entry.get("type", ""))] += 1
                else:
                    failed += 1
            content = "".join(lines)

        path.write_text(content, encoding="utf-8")

    print(f"Applied replacements: {replaced}")
    print(f"Failed replacements: {failed}")
    print(f"By type: {dict(by_type)}")
    print(f"By cmd: {dict(by_cmd)}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

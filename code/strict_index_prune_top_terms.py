#!/usr/bin/env python3
"""Strict second-pass prune for high-frequency index terms.

Reads an existing book-indexer judgment report, filters to kept occurrences of
the top-N most frequent terms, and asks an LLM to re-judge those occurrences
under stricter indexing criteria.

Output format matches book_indexer.llm_judge apply-judgment expectations.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from collections import Counter
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


def run_llm_command(
    llm_bridge: Path,
    system: str,
    user: str,
    model: str = "",
) -> dict[str, Any]:
    payload = {
        "system": system,
        "user": user,
        "model": model,
        "response_keys": ["decisions", "notes"],
    }
    result = subprocess.run(
        ["python", str(llm_bridge)],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"LLM bridge failed ({result.returncode}): "
            f"{(result.stderr or '').strip() or (result.stdout or '').strip()}"
        )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"LLM bridge returned invalid JSON: {exc}") from exc


def build_prompt(batch: list[dict[str, Any]]) -> tuple[str, str]:
    system = (
        "You are an expert back-of-book indexer doing a strict second-pass prune. "
        "Keep an index tag only if the passage substantively discusses the tagged "
        "concept (definition, contrast, claim, mechanism explanation, method, or "
        "extended argument). "
        "Drop if it is a passing mention, rhetorical repetition, list filler, "
        "heading echo, or incidental usage. "
        "When uncertain, drop. Return strict JSON only."
    )
    items = []
    for item in batch:
        items.append(
            {
                "id": item["id"],
                "term": item["normalized_term"],
                "file": Path(item["file"]).name,
                "line": item.get("line"),
                "context": item.get("context", ""),
            }
        )
    user = (
        "Return JSON with schema:\n"
        "{\n"
        '  "decisions": [\n'
        '    {"id": <int>, "keep": <bool>, "reason": <string>}\n'
        "  ],\n"
        '  "notes": [<string>]\n'
        "}\n"
        "You must return one decision for every id.\n"
        f"Items:\n{json.dumps(items, ensure_ascii=True)}\n"
    )
    return system, user


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-report", required=True, help="Existing judgment JSON")
    parser.add_argument("--output-report", required=True, help="Strict judgment JSON output")
    parser.add_argument(
        "--llm-bridge",
        default="/Users/brettreynolds/Documents/LLM-CLI-projects/tools/book-indexer/scripts/gemini_llm.py",
        help="Path to LLM bridge script",
    )
    parser.add_argument("--top-n", type=int, default=20, help="Top N kept terms")
    parser.add_argument("--chunk-size", type=int, default=80, help="Batch size")
    parser.add_argument("--model", default="", help="Optional model string for bridge")
    parser.add_argument("--resume", action="store_true", help="Resume from existing output")
    parser.add_argument("--max-retries", type=int, default=3, help="Retries per failed batch")
    args = parser.parse_args()

    source_path = Path(args.source_report)
    out_path = Path(args.output_report)
    llm_bridge = Path(args.llm_bridge)

    source = json.loads(source_path.read_text(encoding="utf-8"))
    items: list[dict[str, Any]] = source.get("items", [])
    decisions = {
        int(d["id"]): d
        for d in source.get("decisions", [])
        if isinstance(d, dict) and "id" in d
    }

    kept_items: list[dict[str, Any]] = []
    for item in items:
        item_id = int(item.get("id"))
        if decisions.get(item_id, {}).get("keep") is not True:
            continue
        term = normalize_term(item.get("term", ""))
        if not term:
            continue
        new_item = dict(item)
        new_item["normalized_term"] = term
        kept_items.append(new_item)

    term_counts = Counter(item["normalized_term"] for item in kept_items)
    top_terms = [term for term, _ in term_counts.most_common(args.top_n)]
    target_items = [item for item in kept_items if item["normalized_term"] in top_terms]

    strict_decisions: dict[int, dict[str, Any]] = {}
    notes: list[str] = []
    if args.resume and out_path.exists():
        existing = json.loads(out_path.read_text(encoding="utf-8"))
        for d in existing.get("decisions", []):
            if isinstance(d, dict) and "id" in d:
                strict_decisions[int(d["id"])] = d
        existing_notes = existing.get("notes", [])
        if isinstance(existing_notes, list):
            notes.extend(str(x) for x in existing_notes)

    pending = [it for it in target_items if int(it["id"]) not in strict_decisions]
    total = len(target_items)
    print(f"Top terms: {top_terms}")
    print(f"Target occurrences: {total}")
    print(f"Already decided: {len(strict_decisions)}")
    print(f"Pending: {len(pending)}")

    if not pending:
        print("No pending items.")
    else:
        batches = [
            pending[i : i + args.chunk_size]
            for i in range(0, len(pending), args.chunk_size)
        ]
        for i, batch in enumerate(batches, start=1):
            print(f"Batch {i}/{len(batches)} ({len(batch)} items)...", flush=True)
            system, user = build_prompt(batch)
            result: dict[str, Any] | None = None
            last_error = ""
            for attempt in range(1, args.max_retries + 1):
                try:
                    result = run_llm_command(llm_bridge, system, user, model=args.model)
                    break
                except RuntimeError as exc:
                    last_error = str(exc)
                    print(
                        f"  Warning: batch {i} attempt {attempt}/{args.max_retries} failed: {last_error}",
                        flush=True,
                    )
                    time.sleep(2)
            if result is None:
                notes.append(
                    f"batch_{i}_fallback_keep_after_failures: {last_error[:500]}"
                )
                for item in batch:
                    item_id = int(item["id"])
                    strict_decisions[item_id] = {
                        "id": item_id,
                        "keep": True,
                        "reason": "fallback_keep_batch_failure",
                    }
                snapshot = {
                    "items": target_items,
                    "decisions": [strict_decisions[int(it["id"])] for it in target_items if int(it["id"]) in strict_decisions],
                    "notes": notes,
                    "meta": {
                        "top_n": args.top_n,
                        "top_terms": top_terms,
                        "source_report": str(source_path),
                        "strict_mode": True,
                    },
                }
                out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
                print(f"Checkpoint: {out_path}", flush=True)
                continue
            batch_decisions = result.get("decisions", [])
            seen: set[int] = set()
            if isinstance(batch_decisions, list):
                for dec in batch_decisions:
                    if not isinstance(dec, dict) or "id" not in dec:
                        continue
                    try:
                        dec_id = int(dec["id"])
                    except (TypeError, ValueError):
                        continue
                    strict_decisions[dec_id] = {
                        "id": dec_id,
                        "keep": bool(dec.get("keep", False)),
                        "reason": str(dec.get("reason", ""))[:400],
                    }
                    seen.add(dec_id)
            for item in batch:
                item_id = int(item["id"])
                if item_id not in seen and item_id not in strict_decisions:
                    strict_decisions[item_id] = {
                        "id": item_id,
                        "keep": True,
                        "reason": "fallback_keep_missing_decision",
                    }
            batch_notes = result.get("notes", [])
            if isinstance(batch_notes, list):
                notes.extend(str(x) for x in batch_notes)

            snapshot = {
                "items": target_items,
                "decisions": [strict_decisions[int(it["id"])] for it in target_items if int(it["id"]) in strict_decisions],
                "notes": notes,
                "meta": {
                    "top_n": args.top_n,
                    "top_terms": top_terms,
                    "source_report": str(source_path),
                    "strict_mode": True,
                },
            }
            out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
            print(f"Checkpoint: {out_path}", flush=True)

    final_report = {
        "items": target_items,
        "decisions": [strict_decisions[int(it["id"])] for it in target_items if int(it["id"]) in strict_decisions],
        "notes": notes,
        "meta": {
            "top_n": args.top_n,
            "top_terms": top_terms,
            "source_report": str(source_path),
            "strict_mode": True,
        },
    }
    out_path.write_text(json.dumps(final_report, indent=2), encoding="utf-8")

    drop_count = sum(1 for d in final_report["decisions"] if d.get("keep") is False)
    keep_count = sum(1 for d in final_report["decisions"] if d.get("keep") is True)
    print(f"Final report: {out_path}")
    print(f"Strict keep: {keep_count}")
    print(f"Strict drop: {drop_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

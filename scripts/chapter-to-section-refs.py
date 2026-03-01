#!/usr/bin/env python3
"""Convert chapter-level cross-references to section-level where appropriate."""

import re
from pathlib import Path

# Each entry: (file, old_string, new_string, description)
CHANGES = [
    # === Two-Diagnostic Test references (4 instances) → sec:8:diagnostics ===
    ("chapter09.tex",
     r"Chapter~\ref{ch:failure-modes} introduced the Two-Diagnostic Test",
     r"§\ref{sec:8:diagnostics} introduced the Two-Diagnostic Test",
     "TDT reference"),
    ("chapter10.tex",
     r"Chapter~\ref{ch:failure-modes} introduced the Two-Diagnostic Test",
     r"§\ref{sec:8:diagnostics} introduced the Two-Diagnostic Test",
     "TDT reference"),
    ("chapter12.tex",
     r"Chapter~\ref{ch:failure-modes} introduced the Two-Diagnostic Test",
     r"§\ref{sec:8:diagnostics} introduced the Two-Diagnostic Test",
     "TDT reference"),
    ("chapter14.tex",
     r"Chapter~\ref{ch:failure-modes} introduced the Two-Diagnostic Test",
     r"§\ref{sec:8:diagnostics} introduced the Two-Diagnostic Test",
     "TDT reference"),

    # === Lexical semantics / grain argument → sec:8:lexical-semantics ===
    ("chapter09.tex",
     r"Chapter~\ref{ch:failure-modes} argued that lexical semantics alone",
     r"§\ref{sec:8:lexical-semantics} argued that lexical semantics alone",
     "lexical semantics argument"),
    ("chapter09.tex",
     r"the payoff from Chapter~\ref{ch:failure-modes} arrives",
     r"the payoff from §\ref{sec:8:lexical-semantics} arrives",
     "lexical semantics payoff"),

    # === Fat-class references → sec:8:fat ===
    ("chapter11.tex",
     r"This is Chapter~\ref{ch:failure-modes}'s fat-class",
     r"This is the fat-class",
     "fat-class signature (part 1 — remove Chapter ref)"),
    # Add section ref after "signature" — handled separately below

    ("chapter15.tex",
     r"fat class\ixsq{fat class} (Chapter~\ref{ch:failure-modes})",
     r"fat class\ixsq{fat class} (§\ref{sec:8:fat})",
     "fat class parenthetical"),

    # === Thin-class reference → sec:8:thin ===
    ("chapter11.tex",
     r"(Chapter~\ref{ch:failure-modes}). As a comparative concept",
     r"(§\ref{sec:8:thin}). As a comparative concept",
     "thin kinds reference"),

    # === Tolerance dynamics → sec:5:formal-solution ===
    ("chapter09.tex",
     r"Chapter~\ref{ch:dynamic-discreteness} offered a framework for this",
     r"§\ref{sec:5:formal-solution} offered a framework for this",
     "tolerance dynamics"),

    # === Basin dynamics → sec:5:geometry-to-mechanism ===
    ("chapter15.tex",
     r"basin dynamics of Chapter~\ref{ch:dynamic-discreteness}",
     r"basin dynamics of §\ref{sec:5:geometry-to-mechanism}",
     "basin dynamics"),

    # === Triadic architecture → sec:13:mediation ===
    ("chapter14.tex",
     r"triadic architecture of Chapter~\ref{ch:the-category-zipper}",
     r"triadic architecture of §\ref{sec:13:mediation}",
     "triadic/mediation architecture"),

    # === Bidirectional inference coupling → sec:9:coupling ===
    ("chapter12.tex",
     r"(Chapter~\ref{ch:countability}) and identifiability to deitality",
     r"(§\ref{sec:9:coupling}) and identifiability to deitality",
     "bidirectional inference coupling"),

    # === Countability two-categories split → sec:9:two-categories ===
    ("chapter10.tex",
     r"Chapter~\ref{ch:countability} distinguished the",
     r"§\ref{sec:9:two-categories} distinguished the",
     "individuation/count split"),

    # === Would-be / projectibility → sec:7:what-projection-is ===
    ("chapter10.tex",
     r"Chapter~\ref{ch:projectibility} argued that projectibility",
     r"§\ref{sec:7:what-projection-is} argued that projectibility",
     "would-be generation"),
    ("chapter15.tex",
     r"the terms of Chapter~\ref{ch:projectibility}, the indexical field",
     r"the terms of §\ref{sec:7:what-projection-is}, the indexical field",
     "would-be space"),

    # === Field-relative projectibility → sec:7:field-relative ===
    ("chapter15.tex",
     r"field-relative projectibility\ixsq{field-relative projectibility} (Chapter~\ref{ch:projectibility})",
     r"field-relative projectibility\ixsq{field-relative projectibility} (§\ref{sec:7:field-relative})",
     "field-relative projectibility"),

    # === Proper noun/proper name → sec:7:proper-nouns-names ===
    ("chapter12.tex",
     r"(Chapter~\ref{ch:definiteness-and-deitality}).",
     r"(§\ref{sec:7:proper-nouns-names}).",
     "proper noun/name distinction"),

    # === Mixed-bin diagnostic → sec:15:mixed-bin ===
    ("chapter17.tex",
     r"Chapter~\ref{ch:social-stabilization} established (conditioned models",
     r"§\ref{sec:15:mixed-bin} established (conditioned models",
     "mixed-bin diagnostic"),

    # === Hub-node coupling → sec:13:map ===
    ("chapter17.tex",
     r"(Chapter~\ref{ch:the-category-zipper}) but doesn't ask",
     r"(§\ref{sec:13:map}) but doesn't ask",
     "stabilizer-weighting map"),

    # === Definiteness/deitality budding → sec:10:coupling ===
    ("chapter17.tex",
     r"case from Chapter~\ref{ch:definiteness-and-deitality} provides",
     r"case from §\ref{sec:10:coupling} provides",
     "definiteness budding case"),

    # === Data case study → sec:9:data ===
    ("chapter17.tex",
     r"\\mention{data}\\ixlq{data} from Chapter~\\ref{ch:countability}",
     r"\\mention{data}\\ixlq{data} from §\\ref{sec:9:data}",
     "data case study"),

    # === Personhood hierarchy → sec:12:hierarchy ===
    ("chapter17.tex",
     r"Chapter~\ref{ch:proform-gender} established",
     r"§\ref{sec:12:hierarchy} established",
     "personhood hierarchy"),

    # === Chain coherence → sec:12:chain-coherence ===
    ("chapter17.tex",
     r"Chapter~\ref{ch:proform-gender} showed that once",
     r"§\ref{sec:12:chain-coherence} showed that once",
     "chain coherence"),
]

def main():
    chapters_dir = Path(__file__).parent.parent / 'chapters'
    count = 0
    errors = []

    for filename, old, new, desc in CHANGES:
        filepath = chapters_dir / filename
        if not filepath.exists():
            errors.append(f"  FILE NOT FOUND: {filename}")
            continue

        text = filepath.read_text()

        # Handle the special regex entry for "data" case
        if old.startswith("\\\\mention"):
            import re as re2
            if re2.search(old, text):
                text = re2.sub(old, new, text, count=1)
                filepath.write_text(text)
                count += 1
                print(f"  [{filename}] {desc}")
            else:
                errors.append(f"  NOT FOUND in {filename}: {desc}")
            continue

        if old in text:
            # Verify it appears exactly once
            occurrences = text.count(old)
            if occurrences > 1:
                errors.append(f"  MULTIPLE ({occurrences}) in {filename}: {desc}")
                continue
            text = text.replace(old, new, 1)
            filepath.write_text(text)
            count += 1
            print(f"  [{filename}] {desc}")
        else:
            errors.append(f"  NOT FOUND in {filename}: {desc}")

    # Handle the ch11 fat-class signature separately (needs two-part edit)
    # After first replacement, "This is the fat-class\ixsq{class} signature"
    # needs "(§\ref{sec:8:fat})" appended
    ch11 = chapters_dir / "chapter11.tex"
    text = ch11.read_text()
    old_fat = r"This is the fat-class\ixsq{class} signature. No shared"
    new_fat = r"This is the fat-class\ixsq{class} signature (§\ref{sec:8:fat}). No shared"
    if old_fat in text:
        text = text.replace(old_fat, new_fat, 1)
        ch11.write_text(text)
        count += 1
        print(f"  [chapter11.tex] fat-class signature (part 2 — add section ref)")
    else:
        errors.append(f"  NOT FOUND in chapter11.tex: fat-class part 2")

    print(f"\nTotal changes: {count}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(e)


if __name__ == '__main__':
    main()

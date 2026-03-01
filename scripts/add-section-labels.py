#!/usr/bin/env python3
"""Add missing \label{} to sections/subsections that lack them."""

import re
import sys
from pathlib import Path

# Map of (chapter_num, section_title) -> label slug
# Only sections/subsections that are missing labels
LABELS = {
    # Chapter 1
    (1, "Essentialism beyond formalism"): "essentialism-beyond-formalism",
    (1, "Feature bundles: essentialism in disguise"): "feature-bundles",
    (1, "Prototypes in the grammar"): "prototypes-in-grammar",
    (1, "But there's a cost"): "cost",
    (1, "An analogy"): "analogy",
    (1, "The deeper issue"): "deeper-issue",

    # Chapter 6
    (6, "The quotative cluster"): "quotative-cluster",
    (6, "Quotative stabilizers"): "quotative-stabilizers",
    (6, "What if a mechanism were absent?"): "mechanism-absent",
    (6, "Cross-linguistic convergence"): "cross-linguistic-convergence",
    (6, "How deep do mechanisms go?"): "how-deep",
    (6, "The filler-gap mechanism"): "filler-gap-mechanism",
    (6, "Independent relative \\mentionhead{whose}: a gap that isn't"): "independent-whose",
    (6, "Filler-gap stabilizers"): "filler-gap-stabilizers",

    # Chapter 8
    (8, "Why both are needed"): "why-both",
    (8, "The grain question"): "grain-question",
    (8, "The nonce word test"): "nonce-word-test",
    (8, "Case study: Preposition copying and pruning"): "preposition-copying",
    (8, "Case study: The \\term{Adverb}"): "adverb",
    (8, "The projectibility failure"): "projectibility-failure",
    (8, "Return to Huddleston"): "return-huddleston",
    (8, "Case study: The Left Branch Gap"): "left-branch",
    (8, "Case study: The \\term{non-finite clause}"): "non-finite",
    (8, "Both diagnostics fail"): "both-fail",
    (8, "Why lexical semantics feels slippery"): "lexical-semantics",
    (8, "What to do when you diagnose failure"): "diagnose-failure",
    (8, "For typology"): "for-typology",
    (8, "For theory"): "for-theory",
    (8, "For methodology"): "for-methodology",
    (8, "Looking forward"): "looking-forward",
    (8, "Hard coupling"): "hard-coupling",
    (8, "Loose coupling"): "loose-coupling",
    (8, "Composite coupling"): "composite-coupling",
    (8, "The continuum"): "continuum",

    # Chapter 9
    (9, "What maintains the cluster"): "maintains-cluster",
    (9, "The problem: Object-mass nouns"): "object-mass",
    (9, "Why the coupling produces an HPC"): "coupling-hpc",
    (9, "Multi-timescale maintenance"): "multi-timescale",
    (9, "The chunking story"): "chunking",
    (9, "Locks with different tolerances"): "locks",
    (9, "From locks to basins"): "locks-to-basins",
    (9, "The implicational pattern"): "implicational",
    (9, "Why are they stable?"): "why-stable",
    (9, "The unstable case: \\mentionhead{folks}"): "folks",
    (9, "How the cluster self-completes: \\mentionhead{pea}"): "pea",
    (9, "The unstable hybrids: Data"): "data",
    (9, "Projectibility"): "projectibility",
    (9, "Homeostasis"): "homeostasis",
    (9, "The verdict"): "verdict",
    (9, "Perturbation 1: The collective basin (Welsh)"): "welsh",
    (9, "Perturbation 2: Weakened structural reinforcement"): "weakened-reinforcement",
    (9, "Perturbation 3: Reweighted semantics (Yudja)"): "yudja",
    (9, "The value of variation"): "value-variation",

    # Chapter 10
    (10, "Existential \\mentionhead{there}"): "existential-there",
    (10, "Partitive \\mentionhead{of}"): "partitive-of",
    (10, "Identificational hosting"): "identificational",
    (10, "Convergence"): "convergence",
    (10, "Weak definites"): "weak-definites",
    (10, "Generic definites"): "generic-definites",
    (10, "Proper names"): "proper-names",
    (10, "Indefinite \\mentionhead{this}"): "indefinite-this",
    (10, "Projectibility"): "projectibility",
    (10, "Homeostasis"): "homeostasis",
    (10, "Falsifiable predictions"): "predictions",

    # Chapter 13
    (13, "The null case"): "null-case",

    # Chapter 14
    (14, "Entrenchment in action"): "entrenchment",
    (14, "Three registers"): "three-registers",
    (14, "Feels ungrammatical, is grammatical"): "feels-ungrammatical",
    (14, "Feels grammatical, is ungrammatical"): "feels-grammatical",
    (14, "Value at every grain"): "value-every-grain",
    (14, "Grammaticality as a species of appropriateness"): "appropriateness",
    (14, "Satiation"): "satiation",
    (14, "Individual differences"): "individual-differences",
    (14, "Processing difficulty and beyond"): "processing-difficulty",
}


def get_chapter_num(filepath):
    """Extract chapter number from filename."""
    m = re.search(r'chapter(\d+)', filepath.name)
    return int(m.group(1)) if m else None


def process_file(filepath, chapter_num):
    """Add missing labels to a chapter file."""
    lines = filepath.read_text().splitlines(keepends=True)
    new_lines = []
    count = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Check if this is a \section or \subsection line
        m = re.match(r'\\(?:sub)?section\{(.+)\}\s*$', line.rstrip())
        if m:
            title = m.group(1)
            key = (chapter_num, title)

            if key in LABELS:
                # Check that next lines don't already have a \label
                has_label = False
                j = i + 1
                while j < len(lines) and j <= i + 3:
                    next_line = lines[j].strip()
                    if next_line.startswith('\\label{'):
                        has_label = True
                        break
                    if next_line and not next_line.startswith('\\ix') and not next_line.startswith('%'):
                        break
                    j += 1

                if not has_label:
                    slug = LABELS[key]
                    label_line = f'\\label{{sec:{chapter_num}:{slug}}}\n'
                    # Skip past any \ix lines that follow
                    while i + 1 < len(lines) and lines[i + 1].strip().startswith('\\ix'):
                        i += 1
                        new_lines.append(lines[i])
                    new_lines.append(label_line)
                    count += 1
                    print(f"  Added \\label{{sec:{chapter_num}:{slug}}} after: {title}")

        i += 1

    if count > 0:
        filepath.write_text(''.join(new_lines))
    return count


def main():
    chapters_dir = Path(__file__).parent.parent / 'chapters'
    total = 0

    for ch_num in [1, 6, 8, 9, 10, 13, 14]:
        filepath = chapters_dir / f'chapter{ch_num:02d}.tex'
        if not filepath.exists():
            print(f"WARNING: {filepath} not found")
            continue
        print(f"\nProcessing {filepath.name}:")
        count = process_file(filepath, ch_num)
        total += count
        if count == 0:
            print("  No changes needed")

    print(f"\nTotal labels added: {total}")


if __name__ == '__main__':
    main()

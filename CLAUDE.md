# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX academic book project: "Words That Won't Hold Still: How Linguistic Categories Work" (working title also: "Language Without Essences"). The core thesis is that many core linguistic categories (with grammar as the main focus) are Homeostatic Property Cluster (HPC) kinds rather than essentialist or nominalist constructs.

## Build Commands

```bash
# Full compile (requires XeLaTeX and Biber)
xelatex hpc-book.tex && biber hpc-book && xelatex hpc-book.tex && xelatex hpc-book.tex

# Single pass for quick checks
xelatex hpc-book.tex

# Validate bibliography
python code/validate_bib.py
```

The project uses XeLaTeX (not pdfLaTeX) because of fontspec and the Charis SIL font.

**Compilation workflow:** Most chapters in `hpc-book.tex` are commented out for faster compilation. Uncomment the chapter(s) you're working on.

**Build artifacts:** The `.latexmkrc` routes output to `build/`. Use `latexmk -xelatex hpc-book.tex` for the recommended workflow. Snapshots are saved to `snapshots/` with date stamps.

## Repository Structure

- `hpc-book.tex` - Main document; chapters are commented out for faster compilation
- `chapters/` - Individual chapter files (chapter01.tex through chapter15.tex)
- `.house-style/preamble.tex` - All LaTeX packages and custom macros
- `.house-style/style-guide.md` - Writing conventions (MUST READ before editing prose)
- `references.bib` - Bibliography (BibTeX format, Biber backend)
- `notes/` - Planning documents and chapter development notes
- `literature/` - Symlink to centralized `../../literature/` (shared across all projects)
- `code/` - Utility scripts (e.g., `validate_bib.py`, `countability_abm.py`)

## Modeling Guidelines

**ABMs in this book are didactic mechanism sketches, not evidence.**

When building agent-based models or simulations for the book:

1. **Explicit epistemic status**: State clearly in docstrings that the model is an "intuition pump" that makes mechanisms visible, NOT a calibrated simulation or empirical support for the theory.

2. **No outcome-assumptive nudges**: Don't manually force outcomes (e.g., `individuation *= 0.97` to make drift happen). Let dynamics emerge from the mechanisms.

3. **Stress tests required**: Add mechanism ablation experiments that show the predicted pattern *breaks* when key mechanisms are removed. This proves results aren't tautological. Examples:
   - Disable entrenchment → pattern changes
   - Remove functional anchors → stability degrades
   - Freeze learning → system becomes static

4. **Multi-timescale fidelity**: If claiming multi-timescale maintenance, actually implement generational turnover, not just interaction + incremental learning.

### Reference Implementation

`code/countability_abm.py` (~1300 lines) is the reference implementation for Chapter 9:
- Five experiments: baseline hierarchy, data drift, functional anchoring, prescriptivism, folks instability
- Mechanism ablation stress tests (proves results aren't tautological)
- Visualizations generated to `figures/`

### Key Planning Documents

- `notes/CHAPTER_OUTLINE.md` - Authoritative chapter structure and key points
- `notes/chapterNN-master.md` - Master notes consolidating chapter material (pattern established with Ch 7, 8, 13)
- `notes/chapterNN-grist.md` - Raw conceptual material for chapters
- `notes/ch11/ch11-implementation-plan.md` - Approved implementation plan for Ch 11
- `notes/field-relative-projectibility.md` - Core theoretical principle (projectibility is field-relative)
- `notes/*-analysis.md` - Literature analysis files
- `notes/board-*-*.md` - Advisory board feedback simulations
- `PROJECT_LOG.md` — Session history with meta-reflection on what works
- `synopsis.md` - Book synopsis (~880 words)

## House Style Conventions

### LaTeX Macros (defined in `.house-style/preamble.tex`)

```latex
\term{text}         % Technical terms when introduced (small caps)
\mention{text}      % Linguistic mentions (italics) - words as examples
\enquote{text}      % Quotations (locale-aware quotes)
\abbr{text}         % Gloss abbreviations (small caps)
\crossmark          % Cross-linguistic subscript marker (†)
\ungram{*sentence}  % Ungrammatical
\marg{?sentence}    % Marginal
\odd{#sentence}     % Semantically odd
\eg \ie \etc        % Standard abbreviations with spacing
```

**Important distinction:** `\term{}` = small caps for introducing key concepts; `\mention{}` = italics for citing linguistic forms.

### Numbered Examples

Uses `langsci-gb4e` package. No `exe` environment:

```latex
\ea\label{ex:label}
\textit{Example sentence.}
\z
```

### Syntax Safety (Critical)

- **`gb4e` examples with judgments:** When using `\ex` with an optional argument (like `[*]` or `[?]`), you **MUST** enclose the example content in braces `{...}`. Failure to do this causes `TeX capacity exceeded` errors by creating recursion loops in the `.aux` file via `hyperref`.
    - **CORRECT:** `\ex[*]{\gll ... \\ ... \\ \glt ...}`
    - **WRONG:** `\ex[*] \gll ... \\ ... \\ \glt ...`
- **Bibliography hygiene:**
    - Keys are case-sensitive in Biber/LaTeX interaction. Ensure `references.bib` case matches citations exactly.
    - Year fields must be integers (`2024`), not ranges (`2008--2024`) or strings (`forthcoming`). Put extra info in `note={...}`.

### Citations

Uses `biblatex` with APA style and `natbib=true`:
- `\citep{key}` - parenthetical: (Author Year)
- `\textcite{key}` - textual: Author (Year)
- `\citep[page]{key}` - with page number

### Writing Style

- Use Oxford spelling (-ize not -ise)
- Contractions are preferred ("don't" not "do not")
- Avoid em-dashes; use en-dashes with spaces for parentheticals
- Prefer simple coordinators (and, but) over academic adverbs (moreover, nevertheless)
- Keep paragraphs under 100 words on average

### Grammatical Framework (CGEL-style)

- Distinguish lexical categories from syntactic functions
- Determinative = category; Determiner = function
- Reject Abney's DP hypothesis: "the dog" is an NP with a DP in determiner function

## Book Structure

Four parts, 15 chapters:
1. **Part I: The Problem** (Ch 1-3) - Essentialism's failures, nominalism's limits
2. **Part II: The Fix** (Ch 4-8) - HPC kinds, discreteness, projectibility, homeostasis, failure modes
3. **Part III: Categories Reconsidered** (Ch 9-13) - Countability, definiteness, lexical categories, gender, the stack
4. **Part IV: Implications** (Ch 14-15) - Grammaticality, methodological consequences

### Current Chapter Status (Jan 2026)
- **Ch 1-3**: Drafted and revised (Part I: The Problem)
- **Ch 4**: Drafted and revised (HPC introduction)
- **Ch 5**: Drafted and revised (discreteness problem)
- **Ch 6**: Drafted and revised (projectibility)
- **Ch 7**: Drafted and revised (The Stabilisers)
- **Ch 8**: Drafted and revised (Failure Modes)
- **Ch 9**: Drafted and revised (Countability) - ABM complete
- **Ch 10**: Drafted and revised (Definiteness)
- **Ch 11**: §11.1–§11.5 drafted; §11.6–§11.8 remaining (Lexical Categories)
- **Ch 12**: Drafted and revised (Pro-form Gender)
- **Ch 13**: Restructuring decided — synthesis chapter; coupling coda goes in Ch 8 (see `notes/ch13-restructuring-analysis.md`)
- **Ch 14**: Outlined (Grammaticality itself)
- **Ch 15**: Outlined (Methodological consequences)

## Chapter Development Workflow

The project uses a master-notes pattern for chapter development:

1. **Grist file** (`notes/chapterNN-grist.md`) - Raw conceptual material, quotes, ideas
2. **Master file** (`notes/chapterNN-master.md`) - Consolidated structure with sections A-N covering:
   - What the chapter must do (forward/backward references)
   - Key concepts and frameworks
   - Evidence to include
   - Structural recommendations
   - Open questions
3. **LaTeX file** (`chapters/chapterNN.tex`) - Final prose

When working on a chapter, check the master notes first to understand the planned structure and accumulated material.

## Intellectual Engagement (Not Just Implementation)

This book develops original theoretical content, not just documentation. When the author introduces ideas:

### Resist Implementation Mode
- Don't immediately jump to creating notes or editing files
- Engage with the *substance* of the ideas first
- Ask probing questions before transcribing

### Go Deeper
- When you find a connection, ask if there are more
- The field-relative projectibility insight (Dec 2025) was developed by repeatedly pushing deeper — each layer revealed new connections
- If going deeper still yields insights, keep going

### Watch for Hidden Architecture
- Slogans and formulas can import assumptions (see the Tabarok/HPC slogan discussion)
- Ask: what am I smuggling in with this framing?
- Keep distinct: (a) metaphysics, (b) epistemology, (c) pragmatics

### The Three-Way Discipline
For HPC claims, don't collapse:
- **Metaphysics** — what keeps tokens similar (mechanisms)
- **Epistemology** — what lets us infer (projectibility)
- **Pragmatics** — what classification is for (field-relative purposes)

### Field-Relative Projectibility (Core Principle)
Projectibility is indexed to analytical purpose. Different subfields (semantics, syntax, phonology) may have different right-sized categories for overlapping extensions. "Definiteness" (semantic) ≠ "deitality" (structural). See `notes/field-relative-projectibility.md`.

### The HPC Slogan
> **"A category is a profile, stabilised by mechanisms, projectible for a purpose."**

### Anti-Essentialist Discipline
When describing categories, do NOT use single-property gatekeeping tests for membership. No "X is a pronoun because it resists determiners" or "X isn't a category because it doesn't project phrases." These are essentialist moves — defining by necessary conditions. Instead, describe clusters of properties that co-occur because mechanisms hold them together. Items at the edges share some properties but not others. That's HPC, not failure.

## Key Concepts

- **HPC (Homeostatic Property Cluster) kinds**: Categories defined by property clusters maintained by causal mechanisms
- **Mechanisms**: Acquisition, entrenchment, interactive alignment, iterated transmission
- **Projectibility**: Why categories support inductive generalizations
- **Failure modes**: Thin clustering, fat clustering, negative diagnosis

### Terminology (load-bearing distinctions)
- **Category** = genuine HPC (passes the projectibility + homeostasis tests). Use for nouns, verbs, adjectives-in-English, the IRE family.
- **Class** = any grouping, may or may not be a category. Use for adverbs, traditional "pronoun."
- **Do NOT use "kind"** — the book uses "category" throughout.
- **Fat/thin/negative** diagnose CLASSES, not categories. A fat class is not a category. A thin class may be a category in some languages but not others (adjective).
- **IRE words** = interrogative, relative, exclamative. The cross-linguistic functional family. Distinct from *wh*-words (English phonology, includes *how* which lacks *wh*-) and *question words* (too narrow — relative *who* isn't interrogative).
- **Coupling** (Ch 8 coda, Ch 13 synthesis): hard-coupled (phonemes) → loose-coupled (grammatical categories) → re-unified (constructions).

## Session Layout (Startup & Shutdown)
    
**Startup:**
1. Read `PROJECT_STATUS.md`
2. Read `PROJECT_LOG.md` (for recent context and patterns)
3. Check `notes/CHAPTER_OUTLINE.md`

**Shutdown:**
1. Update `PROJECT_LOG.md` with:
   - **Session summary**: What was achieved
   - **Decisions Made**: What should persist
   - **Context Learned**: Patterns/preferences discovered
2. Commit and push

## Chapter Completion Polish

As each chapter nears completion, do a final pass for:

### Humour
Look for opportunities to add a little wit—not jokes, but moments of self-awareness, unexpected phrasing, or dry observation that reward close reading. Examples:
- "which is more than most PhD students manage" (Ch 4, line 95)
- "Good luck." after noting entrenchment (Ch 4, line 108)

### Structural Rhetorical Figures
Add figures that do architectural work, not ornament:
- **Tricolon** — groupings of three for rhythm
- **Chiasmus** — A-B-B-A reversal for emphasis
- **Anaphora** — repeated opening phrase across sentences
- **Antithesis** — balanced contrast (X, not Y)
- **Antimetabole** — "categories are real because they are maintained"

### Extended Palette (less "speechy," suited to analytic prose)

**Repetition placement:**
- **Symploce** — same start + same end: "When maintained, it supports induction; when not maintained, it stops."
- **Mesodiplosis** — repetition in the middle: "The cluster, in practice, drifts; the diagnostic, in practice, misfires."
- **Conduplicatio** — carry a key term forward: "The issue is projectibility. Projectibility is what mechanisms buy you."
- **Epanalepsis** — frame a unit with the same word: "Not essences, but mechanisms—mechanisms."

**Linkage and inevitability (causal chains):**
- **Anadiplosis** — end → start: "Stability produces predictability; predictability licences induction."
- **Gradatio** — anadiplosis as a ladder: "Acquisition yields convergence; convergence yields alignment; alignment yields discreteness."

**Mapping and bookkeeping:**
- **Epanodos** — AB, then BA: "Mechanisms stabilise clusters; clusters licence inductions."
- **Epimetabole** — repeated ending: "It looks like a definition, but it behaves like a mechanism; it sounds like a boundary, but it behaves like a mechanism."

**Compression:**
- **Gapping/ellipsis** — parallel clauses with deletion: "Some diagnostics track membership; others, merely tradition."
- **Zeugma** — one governor, two complements: "The account explains the data and the temptation to essentialise."

**Repair and live thinking:**
- **Epanorthosis** — self-correction: "That looks like an exception—no, it's a different maintenance regime."
- **Anacoluthon** — intentional syntactic derailment (use sparingly): "If categories were just conveniences—well, conveniences don't usually survive this kind of pressure."

Keep these **subtle and functional**. The goal is prose that rewards re-reading without signalling cleverness.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX academic book project: "Words That Won't Hold Still: How Grammatical Categories Work" (working title also: "Language Without Essences"). The core thesis is that grammatical categories are Homeostatic Property Cluster (HPC) kinds rather than essentialist or nominalist constructs.

## Build Commands

```bash
# Full compile (requires XeLaTeX and Biber)
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex

# Single pass for quick checks
xelatex main.tex

# Validate bibliography
python validate_bib.py
```

The project uses XeLaTeX (not pdfLaTeX) because of fontspec and the Charis SIL font.

**Compilation workflow:** Most chapters in `main.tex` are commented out for faster compilation. Uncomment the chapter(s) you're working on. Currently only `chapter06.tex` is active.

## Repository Structure

- `main.tex` - Main document; chapters are commented out for faster compilation
- `chapters/` - Individual chapter files (chapter01.tex through chapter14.tex)
- `.house-style/preamble.tex` - All LaTeX packages and custom macros
- `.house-style/style-guide.md` - Writing conventions (MUST READ before editing prose)
- `references.bib` - Bibliography (BibTeX format, Biber backend)
- `notes/` - Planning documents and chapter development notes
- `literature/` - Topic-specific literature review notes

### Key Planning Documents

- `notes/CHAPTER_OUTLINE.md` - Authoritative chapter structure and key points
- `notes/chapter07-master.md` - Master notes consolidating all Ch 7 material (pattern for other chapters)
- `notes/chapter07-grist.md` - Raw conceptual material for Ch 7
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

Four parts, 14 chapters:
1. **Part I: The Problem** (Ch 1-3) - Essentialism's failures, nominalism's limits
2. **Part II: The Fix** (Ch 4-8) - HPC kinds, discreteness, projectibility, homeostasis, failure modes
3. **Part III: Categories Reconsidered** (Ch 9-12) - Countability, definiteness, word classes, constructions
4. **Part IV: Implications** (Ch 13-14) - Grammaticality, methodological consequences

### Current Chapter Status (Dec 2025)
- **Ch 1-3**: Drafted and revised (Part I: The Problem)
- **Ch 4**: Drafted and revised (HPC introduction) - Millikan + Craver quotes added
- **Ch 5**: Drafted and revised (discreteness problem) - Kirby quote added
- **Ch 6**: Drafted and revised (projectibility) - Favier citation refined
- **Ch 7**: Drafted and revised (The Stabilisers) - quotatives case study complete
- **Ch 8**: Drafted (Failure Modes) - thin/fat/negative taxonomy, Miller citation refined
- **Ch 9-14**: Outlined only

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

## Key Concepts

- **HPC (Homeostatic Property Cluster) kinds**: Categories defined by property clusters maintained by causal mechanisms
- **Mechanisms**: Acquisition, entrenchment, interactive alignment, iterated transmission
- **Projectibility**: Why categories support inductive generalizations
- **Failure modes**: Thin clustering, fat clustering, negative diagnosis

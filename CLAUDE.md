# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX academic book project: "Words That Won't Hold Still: How Grammatical Categories Work" (working title also: "Language Without Essences"). The core thesis is that grammatical categories are Homeostatic Property Cluster (HPC) kinds rather than essentialist or nominalist constructs.

## Build Commands

```bash
# Compile the book (requires XeLaTeX and Biber)
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex

# Single pass for quick checks
xelatex main.tex

# Validate bibliography
python validate_bib.py
```

The project uses XeLaTeX (not pdfLaTeX) because of fontspec and the Charis SIL font.

## Repository Structure

- `main.tex` - Main document, includes all chapters
- `chapters/` - Individual chapter files (chapter01.tex through chapter14.tex)
- `.house-style/preamble.tex` - All LaTeX packages and custom macros
- `.house-style/style-guide.md` - Writing conventions (MUST READ before editing prose)
- `references.bib` - Bibliography (BibTeX format, Biber backend)
- `notes/` - Planning documents and research notes
- `literature/` - Topic-specific literature review notes

## House Style Conventions

### LaTeX Macros (defined in `.house-style/preamble.tex`)

```latex
\term{text}         % Technical terms (small caps)
\mention{text}      % Linguistic mentions (italics) - for words as examples
\enquote{text}      % Quotations (locale-aware quotes)
\abbr{text}         % Gloss abbreviations (small caps)
\crossmark          % Cross-linguistic subscript marker (†)
\ungram{*sentence}  % Ungrammatical
\marg{?sentence}    % Marginal
\odd{#sentence}     % Semantically odd
\eg \ie \etc        % Standard abbreviations with spacing
```

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
- **Ch 1**: Drafted and revised
- **Ch 2**: Drafted and revised
- **Ch 3**: Drafted
- **Ch 4**: Outlined (HPC introduction—species problem, mechanisms, standing-wave metaphor)
- **Ch 5**: Drafted and revised (discreteness problem, hyperreal formalization)

## Key Concepts

- **HPC (Homeostatic Property Cluster) kinds**: Categories defined by property clusters maintained by causal mechanisms
- **Mechanisms**: Acquisition, entrenchment, interactive alignment, iterated transmission
- **Projectibility**: Why categories support inductive generalizations
- **Failure modes**: Thin clustering, fat clustering, negative diagnosis

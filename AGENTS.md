# Repository Guidelines

## Project Structure & Module Organization
This is a LaTeX book project. The main entry point is `hpc-book.tex`, which includes chapter files from `chapters/` (e.g., `chapters/chapter01.tex`). Front matter and shared assets live in `frontmatter/`, with `glossary.tex` and `references.bib` at the repo root. House style and macros are in `.house-style/` (`.house-style/preamble.tex`, `.house-style/style-guide.md`). Figures go in `figures/`, research notes in `notes/`, literature PDFs in `literature/`, utility scripts in `code/`, and compiled outputs in `build/`.

## Build, Test, and Development Commands
Use the XeLaTeX toolchain; output is routed to `build/` via `.latexmkrc`.
```bash
latexmk hpc-book.tex         # preferred full build (XeLaTeX + Biber)
xelatex hpc-book.tex         # quick single pass (not for final PDFs)
python code/validate_bib.py  # parse-check references.bib
```
For faster iteration, uncomment only the chapter(s) you’re editing in `hpc-book.tex`.

## Coding Style & Naming Conventions
Follow the house style in `.house-style/style-guide.md`. Key points: use macros like `\term{}` and `\mention{}` from `.house-style/preamble.tex`, use `langsci-gb4e` examples (no `exe` environment), prefer en-dashes with spaces for parentheticals, and keep contractions. Citations use `biblatex` (`\citep{}`, `\textcite{}`).
Naming patterns: `chapters/chapterNN.tex`, `notes/chapterNN-master.md`, and `notes/chapterNN-grist.md`. Literature PDFs are named to match BibTeX keys.

## Testing Guidelines
There is no automated test suite. Validate changes by compiling with `latexmk` and running `python code/validate_bib.py`. If bibliography or glossaries change, ensure Biber and makeglossaries complete during the build.

## Commit & Pull Request Guidelines
Recent commit subjects are short and descriptive, often with a scope prefix like `Ch 11: ...`, `Draft Chapter 12: ...`, or `Glossary: ...`, with occasional `docs:` usage. Use a clear scope (chapter number or component) and sentence case.
For PRs or shared branches, include a brief summary, list updated chapters/notes, and note the build command used (e.g., `latexmk hpc-book.tex`). If figures or layout changed, call out the affected files and provide a quick before/after PDF note.

## Agent-Specific Instructions
Start new sessions by reading `CLAUDE.md` and `.agent/workflows/init.md` for workflow expectations, house style, and build conventions.

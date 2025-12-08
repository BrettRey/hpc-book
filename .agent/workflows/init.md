---
description: Initialize the HPC book project environment
---

# HPC Book Project Initialization

This workflow orients you to the project. Use it at the start of any new session.

## Quick Start (Returning Session)

1. **Read handoff notes**
   ```
   cat notes/chapter07-session-handoff.md
   ```

2. **Check current chapter outline**
   ```
   cat notes/CHAPTER_OUTLINE.md
   ```

3. **Check house style**
   ```
   cat .house-style/style-rules.yaml
   ```

4. **Compile to verify state**
   ```
   xelatex main.tex && biber main && xelatex main.tex
   ```

## Full Initialization (New to Project)

1. **Review project structure**
   - `chapters/` — LaTeX chapter files
   - `figures/` — PGF/TikZ figures
   - `notes/` — working notes, outlines, handoffs
   - `.house-style/` — preamble and style rules
   - `literature/` — PDF sources (Author_Year_Title.pdf)

2. **Key files**
   - `main.tex` — book root
   - `notes/CHAPTER_OUTLINE.md` — 14-chapter structure
   - `notes/chapter07-session-handoff.md` — current working state
   - `references.bib` — bibliography

3. **Current focus: Chapter 7 (The Stabilisers)**
   - Restructured to embody biological explanatory style
   - Next step: Draft worked case (evidentials OR quotatives)
   - See handoff notes for details

4. **Compile workflow**
   ```
   xelatex main.tex && biber main && xelatex main.tex
   ```

5. **Git workflow**
   - Currently on branch `restructure-part-1`
   - Commit and push after significant changes

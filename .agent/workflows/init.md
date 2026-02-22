---
description: Initialize the HPC book project environment
---

# HPC Book Project Initialization

This workflow orients you to the project. Use it at the start of any new session.

## Quick Start (Returning Session)

1. **Read project status**
   ```
   cat PROJECT_STATUS.md
   ```

2. **Read process log** (especially the Dec 11 reflection on quality patterns)
   ```
   cat PROJECT_LOG.md
   ```

3. **Check current chapter outline**
   ```
   cat notes/CHAPTER_OUTLINE.md
   ```

4. **Check house style**
   ```
   cat .house-style/style-guide.md
   ```

## Key Retrieval Points

**For chapter planning:** 
- `notes/handoff_to_opus.md` — EXEMPLARY template for pre-draft planning (full strategic conversation, Rapoport's rules, science communicator structures)
- `notes/chapter2_planning.md`, `notes/chapters_3_and_5_planning.md`, `notes/chapter04_hpc_intro.md` — Pre-draft planning docs that produced good drafts

**For chapter development:**
- `notes/chapterNN-master.md` — Consolidated notes for chapter NN
- `notes/chapterNN-grist.md` — Raw material/excerpts for chapter NN

**For process insights:**
- `PROJECT_LOG.md` — Session history with meta-reflection on what works
- Key finding: Pre-draft planning correlates with draft quality

**For literature:**
- `literature/` — Symlink to centralized `../../literature/` (shared across projects)
- PDFs named to match BibTeX keys
- Use `pdftotext "literature/author2024.pdf" - | grep -i "keyword"` to search

## Full Initialization (New to Project)

1. **Read CLAUDE.md** — Project overview, build commands, house style summary

2. **Review project structure**
   - `chapters/` — LaTeX chapter files (chapter01.tex through chapter14.tex)
   - `figures/` — PNG/PDF figures
   - `notes/` — planning docs, master notes, handoffs
   - `.house-style/` — preamble.tex and style-guide.md
   - `literature/` — Symlink to centralized literature folder

3. **Key files**
   - `main.tex` — book root (chapters are commented out for fast compilation)
   - `references.bib` — bibliography
   - `synopsis.md` — 880-word book summary

4. **Current state** (as of Dec 11, 2025)
   - Part I (Ch 1-3): Drafted and revised
   - Part II (Ch 4-8): Drafted, citations refined
   - Part III (Ch 9-12): Outlined only
   - Next: Pre-draft planning for Ch 9 (Countability)

## Process Reminders

**For drafting new chapters:**
1. Create pre-draft planning doc following `handoff_to_opus.md` template
2. Include: example allocation, user constraints, structure rationale, cross-chapter refs
3. Only then begin drafting

**For citation work:**
1. Check `literature/` for matching PDF
2. Use `pdftotext` + grep to find page numbers
3. Add `[page]` or `[Table~N]` to citation

**Build commands:**
```bash
# Use latexmk (routes output to build/ per .latexmkrc)
latexmk hpc-book.tex

# For quick single-pass (output stays in main folder — avoid):
# xelatex hpc-book.tex
```
⚠️ Always use `latexmk` to keep build artifacts in `build/` folder.

**Git:**
- Branch: `restructure-part-1`
- Commit after significant changes, push at session end

## Quick Status (Zero-Token)

```bash
./quick-status.sh
```
Shows chapter status, active files, last build, git state. No Claude tokens.

## Session Logging

At session end, create/update `.agent/logs/session-YYYY-MM-DD.md` following the template in `SESSION-TEMPLATE.md`. Key sections:
- **Decisions Made** - What should persist
- **Context Learned** - Patterns/preferences discovered
- **Next Session** - Where to pick up

## Project-Level Hooks

`.claude/settings.json` provides:
- **SessionStart**: Reminder to read PROJECT_STATUS.md
- **PostToolUse (.tex)**: House style and build reminders

## Other Workflows

- `/git-hygiene` — Reminders for clean commits and branch management
- `/multi-agent-review` — Spawn independent Codex agents for parallel advisory board reviews of chapters.

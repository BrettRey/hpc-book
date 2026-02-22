---
description: Spawn independent Codex agents for parallel advisory board reviews
---

# Multi-Agent Advisory Board Review (Codex-Only)

Use this workflow when the user wants multiple independent reviews on the same chapter or document.

## Project Policy

Board generation in this repo is Codex-only by default.

## When to use

- User asks for advisory board feedback
- User requests independent parallel critiques
- You need reviewer convergence/divergence before major edits

## Check CLI

```bash
which codex && codex --version
```

## Spawn pattern

```bash
codex exec --full-auto -C /path/to/project -o notes/board-feedback-[chapter]-[advisor]-codex.md \
  "Read [target files]. You are [ADVISOR NAME], [DESCRIPTION]. \
   Address: (1) [Q1] (2) [Q2] (3) [Q3]. \
   Output 3-5 short sections with concrete fixes and file references." &
```

## Status checks

```bash
ls -la notes/board-feedback-*-codex.md
ps aux | grep -E "codex" | grep -v grep
```

## Caveat

Independent agents don't share context from earlier chapters unless you provide that context in the prompt.

## After collection

1. Synthesize convergent criticisms.
2. Separate chapter-local issues from already-resolved book-level framing.
3. Apply highest-confidence edits first.

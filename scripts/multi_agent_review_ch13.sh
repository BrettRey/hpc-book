#!/bin/bash
# Chapter 13 quick board review (Codex-only)

set -euo pipefail

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

echo "Spawning Codex Goldberg..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-goldberg-codex.md \
  "Read chapters/chapter13.tex. You are Adele Goldberg (construction grammar). Review the chapter's stack argument. Do stabiliser weightings make sense? Are opaque-vs-architectural distinctions defensible? What are top fixes?" &

echo "Spawning Codex Croft..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-croft-codex.md \
  "Read chapters/chapter13.tex. You are William Croft (Radical Construction Grammar). Does the stack metaphor over-reify layers? Are negative cases convincing? What would strengthen comparative-concept discipline?" &

echo "Spawning Codex Zimmer..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-zimmer-codex.md \
  "Read chapters/chapter13.tex. You are Carl Zimmer (science writer). Is the chapter vivid and accessible? Where does jargon block comprehension? Propose concrete prose and figure improvements." &

wait
echo "Done. Check notes/board-feedback-ch13-*-codex.md"

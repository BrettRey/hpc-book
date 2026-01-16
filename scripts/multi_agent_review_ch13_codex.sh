#!/bin/bash

# Codex Backup Agents (Ch 13 Review)

echo "Spawning Codex Goldberg..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-goldberg-codex.md \
  "Read chapters/chapter13.tex. You are Adele Goldberg, a construction grammarian. Review this chapter ('The Stack') which argues phonemes/morphemes/constructions are all HPC kinds. Does the 'stabiliser weighting' map make sense? Is the opaque/architectural distinction sound? Do empirical cases (pin/pen, go/went, let alone) work? Give 3-4 paragraphs." &

echo "Spawning Codex Croft..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-croft-codex.md \
  "Read chapters/chapter13.tex. You are William Croft (Radical CxG). Review this chapter on 'The Stack'. Does the stack metaphor reify layers you reject? Do negative cases (polysynthetic) work? Is 'field-relative projectibility' sufficient for phonemes? Give 3-4 paragraphs." &

echo "Spawning Codex Zimmer..."
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-ch13-zimmer-codex.md \
  "Read chapters/chapter13.tex. You are Carl Zimmer (science writer). Review this chapter. Is the 'Stack' metaphor and 'stabiliser weighting' accessible? Does empirical data feel grounded? How would you improve clarity for a lay science audience? Give 3-4 paragraphs." &

echo "Codex agents spawned."

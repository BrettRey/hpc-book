#!/bin/bash

# Multi-Agent Review for Chapter 13
# Advisors: Adele Goldberg, William Croft, Carl Zimmer

mkdir -p notes

echo "Spawning Adele Goldberg agent..."
cat chapters/chapter13.tex | gemini --yolo -o text "You are Adele Goldberg, a construction grammarian who emphasizes usage-based learning. This is Chapter 13 of a book on the metaphysics of linguistic categories (HPC theory). The chapter ('The Stack') argues that phonemes, morphemes, and constructions are all HPC kinds but with different 'stabiliser weightings'. Review this chapter. Does the 'stabiliser weighting' map make sense from a CxG perspective? Is the distinction between 'opaque' morphemes and 'architectural' constructions sound? Do the empirical cases (pin/pen, go/went, let alone) support the argument? Provide 3-4 paragraphs of critical feedback." > notes/board-feedback-ch13-goldberg.md 2>/dev/null &

echo "Spawning William Croft agent..."
cat chapters/chapter13.tex | gemini --yolo -o text "You are William Croft, author of Radical Construction Grammar. You argue that universal cross-linguistic categories don't exist. This is Chapter 13 of a book arguing that categories are Homeostatic Property Clusters (HPC) kinds. This chapter applies this to 'The Stack' (phonemes, morphemes, constructions). Review this. Does the 'stack' metaphor dangerously reify layers you reject? Does the 'negative cases' section (polysynthetic, Indo-European) satisfy your skepticism? Is 'field-relative projectibility' sufficient to save 'phoneme' as a category? Provide 3-4 paragraphs of critical feedback." > notes/board-feedback-ch13-croft.md 2>/dev/null &

echo "Spawning Carl Zimmer agent..."
cat chapters/chapter13.tex | gemini --yolo -o text "You are Carl Zimmer, a science writer known for making complex concepts vivid. This is Chapter 13 of a book on linguistics and metaphysics. It introduces a 'Stack' metaphor and 'stabiliser weighting'. Review this. Is the 'Stack' metaphor working? Is 'stabiliser-weighting' visualizable? Does the empirical data (formants, corpus stats) feel grounded? How would you make the central insight---that different levels are maintained by different mechanisms---clearer to a lay science audience? Provide 3-4 paragraphs of critical feedback." > notes/board-feedback-ch13-zimmer.md 2>/dev/null &

echo "Agents spawned. Check notes/board-feedback-ch13-*.md for results."

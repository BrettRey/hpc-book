#!/bin/bash
# Ch 11 Advisory Board - Codex-only Parallel Execution
# Word classes: The adjective-adverb asymmetry as architectural equilibrium

set -euo pipefail

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

read -r -d '' BASE_CONTEXT << 'CONTEXT'
You are providing advisory board feedback for Chapter 11 of
"Words That Won't Hold Still: How Linguistic Categories Work" by Brett Reynolds.

THE BOOK'S THESIS: Linguistic categories are Homeostatic Property Cluster (HPC) kinds.
Core slogan: "A category is a profile, stabilised by mechanisms, projectible for a purpose."

CHAPTER 11 focus:
- Cross-linguistic stability of nouns/verbs
- Adjective/adverb variation
- Mechanism asymmetries across scales

Read notes/CHAPTER_OUTLINE.md for full context.
CONTEXT

run_codex() {
    local scholar="$1"
    local specialty="$2"
    local questions="$3"
    local slug
    slug=$(echo "$scholar" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    local output_file="notes/board-feedback-ch11-${slug}-codex.md"

    codex exec --full-auto -C "$(pwd)" -o "$output_file" \
        "You are simulating the voice of ${scholar}, known for ${specialty}.

${BASE_CONTEXT}

Write a 400-word advisory board review addressing:
${questions}

Use sections: Strengths, Major Concerns, Priority Fixes." &
}

echo "Starting Ch 11 advisory board (Codex-only, 12 reviewers)..."
echo "==========================================================="

run_codex "Martin Haspelmath" "typology, comparative concepts, cross-linguistic methodology" \
"1. How does HPC relate to comparative concepts?
2. What typological evidence on word classes is essential?
3. How should noun/verb vs adjective asymmetry be framed?"

run_codex "William Croft" "Radical Construction Grammar and cross-linguistic word class analysis" \
"1. How does HPC relate to RCG treatment of word classes?
2. What role do constructions play in stabilization?
3. How should form/function distinctions be handled?"

run_codex "R.M.W. Dixon" "adjective classes, BLT, typological fieldwork" \
"1. What does adjective-class variation imply for mechanisms?
2. How should Dixon's typology be used?
3. What generalization pitfalls should be avoided?"

run_codex "Mark Baker" "formal universals and lexical category theory" \
"1. What formalist concerns should be acknowledged?
2. Where does HPC diverge from parametric accounts?
3. What shared ground is strongest?"

run_codex "Adele Goldberg" "construction grammar and usage-based learning" \
"1. How do constructions stabilize word class membership?
2. What does HPC add beyond standard CxG?
3. Which acquisition evidence matters most?"

run_codex "Joan Bybee" "frequency, entrenchment, grammaticalization" \
"1. How do frequency/entrenchment maintain boundaries?
2. What diachronic evidence should be included?
3. How does grammaticalization map to failure modes?"

run_codex "Michael Tomasello" "usage-based acquisition and social cognition" \
"1. What acquisition evidence supports word class as HPC?
2. How do children learn membership without explicit rules?
3. What social-cognitive mechanisms should be foregrounded?"

run_codex "Simon Kirby" "language evolution and iterated learning" \
"1. How does transmission shape word class stability?
2. What does iterated learning predict for noun/verb vs adjective?
3. What cross-generational framing is most defensible?"

run_codex "Eleanor Rosch" "prototype theory and categorization" \
"1. How does HPC relate to prototype structure?
2. Where should gradience vs discreteness be clarified?
3. What categorization evidence would strengthen the chapter?"

run_codex "Ruth Millikan" "teleosemantics and proper function" \
"1. What is the proper function of word-class categories?
2. How do they reproduce across speakers?
3. What would malfunction look like?"

run_codex "Ben Ambridge" "acquisition, entrenchment, psycholinguistics" \
"1. What experimental evidence best supports learned categories?
2. How does entrenchment differ across classes?
3. Which production/comprehension asymmetries matter?"

run_codex "Edward Tufte" "data visualization and information design" \
"1. What figures best show noun/verb vs adjective asymmetry?
2. How should cross-linguistic variation be displayed?
3. What visual pitfalls should be avoided?"

echo "All agents launched. Waiting..."
wait
echo "Done. Check notes/board-feedback-ch11-*-codex.md"

#!/bin/bash
# Chapter 10 Advisory Board (Codex-only)

set -euo pipefail

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

read -r -d '' CONTEXT << 'EOF'
# Chapter 10 Planning: Definiteness and Deitality

Book thesis: linguistic categories are HPC kinds (mechanism-maintained clusters).
Chapter claim: deitality (form cluster) and definiteness (semantic cluster) overlap but dissociate.

Core diagnostics:
- there-insertion restriction
- partitive compatibility
- one-substitution asymmetry
- weak-definite dissociation cases (the bus / the hospital / the piano)

Task:
1. What's missing?
2. What objections will readers raise?
3. What evidence/examples would strengthen the chapter?
4. Where does the argument overreach or underreach?
5. Best opening hook?
EOF

run_codex() {
    local name="$1"
    local specialty="$2"
    local prompt="$3"
    local slug
    slug=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    local out="notes/ch10-review-${slug}-codex.md"

    codex exec --full-auto -C "$(pwd)" -o "$out" \
        "You are ${name}, ${specialty}.

${CONTEXT}

${prompt}

Write 350-500 words with sections: Strengths, Major Concerns, Priority Fixes." &
}

run_codex "William Croft" "Radical Construction Grammar scholar" \
"Does the deitality/definiteness distinction hold cross-linguistically or collapse into language-specific constructions? Push hard on comparative-concept discipline."

run_codex "Nick Chater" "cognitive scientist (The Mind is Flat)" \
"Are deitality and definiteness psychologically real or analyst artifacts? What decisive experiments would separate HPC from post-hoc description?"

run_codex "Joan Bybee" "usage-based and grammaticalization linguist" \
"Give the diachronic story. Which corpus-frequency signatures would support/challenge the claim?"

run_codex "Kara Federmeier" "ERP and psycholinguistics researcher" \
"What ERP predictions follow if deitality and definiteness are distinct clusters? What would disconfirm the account?"

run_codex "Chris Manning" "computational linguistics researcher" \
"What would LMs need to encode for two-cluster structure to be recoverable? Suggest concrete probing experiments."

run_codex "Douglas Hofstadter" "analogy and categorization theorist" \
"Is this two clusters or one analogy-driven family resemblance? Challenge the machinery."

run_codex "Deirdre McCloskey" "rhetoric and disciplinary persuasion" \
"How can the chapter avoid sounding sectarian? Recommend prose/rhetorical moves that reduce tribal defensiveness."

run_codex "George Lakoff" "conceptual metaphor theorist" \
"What conceptual metaphor best carries the form/function dissociation? How should it be threaded through the chapter?"

run_codex "Bruno Latour" "science studies scholar" \
"What infrastructure (annotations, parsers, teaching pipelines) currently reifies old assumptions, and what would have to change?"

echo "Waiting for Codex reviewers..."
wait
echo "Done. Files: notes/ch10-review-*-codex.md"

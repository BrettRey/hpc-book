#!/bin/bash
# Chapter 15 Advisory Board (parallel Codex agents)

set -euo pipefail

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

read -r -d '' CONTEXT << 'EOF' || true
# Chapter 15 Review Task: "Grammaticality itself"

Core chapter claim:
- Grammaticality is itself an HPC kind: a maintained coupling between morphosyntactic form and structural meaning.
- The "feeling of ungrammaticality" is a noisy detector, not an oracle.
- Illusions, satiation, and individual differences are treated as signatures of the detector architecture.

Key stress points to evaluate:
1. Is the chapter's argument mechanistic (not just metaphorical)?
2. Does the phenomenology section stay disciplined and tied to the triadic architecture?
3. Are the empirical claims genuinely risky/falsifiable and not over-precise placeholders?
4. Does acceptability-vs-grammaticality get handled rigorously?
5. What would a skeptical specialist in your field reject first?

Output format:
- Strengths
- Major Concerns
- Priority Fixes
- Decisive Tests

Length target:
400-650 words.
EOF

run_codex() {
    local name="$1"
    local specialty="$2"
    local prompt="$3"
    local slug
    slug=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' /' '--' | tr -cd 'a-z0-9-_')
    local out="notes/ch14-review-${slug}-codex.md"

    codex exec --full-auto -C "$(pwd)" -o "$out" \
        "You are ${name}, ${specialty}.

Read chapters/chapter15.tex in full before writing.

${CONTEXT}

${prompt}

Write a hard-nosed review aimed at improving publishability to skeptical linguists and philosophers of language.
Use concrete chapter-local references (section names or quoted phrases) where useful." &
}

# Core theoretical + mechanism reviewers
run_codex "Ruth Millikan" "teleosemantics and proper-function philosopher" \
"Push on normativity and proper function: does the chapter distinguish selected function, current use, and analyst-imposed utility rigorously enough?"

run_codex "Ian Hacking" "historical ontology and classification theorist" \
"Push on looping and social reactivity: does the account treat grammaticality as a target changed by its own classification practices?"

run_codex "William Croft" "Radical Construction Grammar scholar" \
"Push on comparative-concept discipline and cross-linguistic claims. Where does this chapter risk English-centric reification?"

run_codex "Adele Goldberg" "construction grammar and learning theorist" \
"Push on construction-level evidence: does the chapter operationalize claims at construction grain or stay too global?"

run_codex "Ewa Dabrowska" "individual-differences and usage-based linguist" \
"Push on heterogeneity: are variation and education effects integrated as constitutive, or treated as caveats?"

run_codex "Michael Tomasello" "usage-based acquisition researcher" \
"Push on developmental mechanism plausibility: what acquisition predictions are missing or oversold?"

# Processing / neuroscience / modeling
run_codex "Kara Federmeier" "ERP and psycholinguistics researcher" \
"Push on neural and processing signatures: which claims need explicit electrophysiological or online-processing predictions?"

run_codex "Tal Linzen" "computational linguistics and syntactic generalization researcher" \
"Push on computational falsifiability: what model comparisons (LMs, surprisal, probe tasks) would genuinely test the claims?"

run_codex "Emily Bender" "computational linguistics critic and methodology scholar" \
"Push on construct validity and framing discipline: where does terminology outrun evidence?"

# Packaging / rhetoric
run_codex "Deirdre McCloskey" "rhetoric of science scholar" \
"Push on persuasion and disciplinary uptake: identify lines that sound sectarian or overconfident, and suggest rhetorical repairs."

run_codex "Carl Zimmer" "science writer" \
"Push on explanatory clarity: where does this chapter lose an intelligent non-specialist and how to fix without dumbing down?"

# Added external specialists (not on board list) for load-bearing risks
run_codex "Jon Sprouse" "experimental syntax and acceptability-judgment methodologist" \
"Push on judgment methodology: where are the inferential leaps from acceptability data to grammatical architecture too fast?"

run_codex "Florian Jaeger" "psycholinguistics and probabilistic language modeling researcher" \
"Push on processing-vs-grammar confounds: what quantitative model comparisons are required before claims about detector architecture are warranted?"

echo "Waiting for Codex reviewers..."
wait
echo "Done. Files: notes/ch14-review-*-codex.md"

#!/bin/bash
# Chapter 15 Advisory Board (pass 2, parallel Codex agents)

set -euo pipefail

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

read -r -d '' CONTEXT << 'EOF' || true
# Chapter 15 Review Task (Pass 2): "Grammaticality itself"

Read `chapters/chapter15.tex` in full.
This is a second-pass review after a targeted revision addressing prior board concerns.

Core chapter claim:
- Grammaticality is itself an HPC kind: a maintained coupling between morphosyntactic form and structural meaning.
- The "feeling of ungrammaticality" is a noisy detector, not an oracle.
- Illusions, satiation, and individual differences are treated as signatures of detector architecture.

Pass-2 focus:
1. Did the mechanism specification become explicit enough to support test design?
2. Is triadic phenomenology now operationalized (or at least clearly staged as testable)?
3. Are over-precise claims now calibrated appropriately?
4. Is acceptability-vs-grammaticality circularity now handled as a reflexive-equilibrium dynamic rather than a vicious circle?
5. Is boundary/ownership language now calibrated to fit the whole-book field-relative framing?

Output format:
- Strengths
- Remaining Concerns
- Priority Fixes (if any)
- Decisive Tests (what now most matters)

Length target:
350-600 words.
EOF

run_codex() {
    local name="$1"
    local specialty="$2"
    local prompt="$3"
    local slug
    slug=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' /' '--' | tr -cd 'a-z0-9-_')
    local out="notes/ch14-review-${slug}-codex-pass2.md"

    codex exec --full-auto -C "$(pwd)" -o "$out" \
        "You are ${name}, ${specialty}.

Read chapters/chapter15.tex in full before writing.

${CONTEXT}

${prompt}

Write a hard-nosed pass-2 review aimed at improving publishability to skeptical linguists and philosophers of language.
Use concrete chapter-local references (section names or quoted phrases) where useful." &
}

# Core theoretical + mechanism reviewers
run_codex "Ruth Millikan" "teleosemantics and proper-function philosopher" \
"Push on normativity and proper function: does the chapter distinguish selected function, current use, and analyst-imposed utility rigorously enough?"

run_codex "Ian Hacking" "historical ontology and classification theorist" \
"Push on looping and social reactivity: does the account now make reflexive equilibrium explicit and non-circular?"

run_codex "William Croft" "Radical Construction Grammar scholar" \
"Push on comparative-concept discipline and cross-linguistic claims. Where does this chapter still risk English-centric reification?"

run_codex "Adele Goldberg" "construction grammar and learning theorist" \
"Push on construction-level evidence: does the chapter now operationalize claims at construction grain rather than chapter-global claims?"

run_codex "Ewa Dabrowska" "individual-differences and usage-based linguist" \
"Push on heterogeneity: are variation and education effects integrated as constitutive, or still treated as caveats?"

run_codex "Michael Tomasello" "usage-based acquisition researcher" \
"Push on developmental mechanism plausibility: what acquisition predictions remain missing or oversold?"

# Processing / neuroscience / modeling
run_codex "Kara Federmeier" "ERP and psycholinguistics researcher" \
"Push on neural and processing signatures: are the time-resolved predictions now specific enough to test?"

run_codex "Tal Linzen" "computational linguistics and syntactic generalization researcher" \
"Push on computational falsifiability: what model comparisons (LMs, surprisal, probe tasks) are now required, and are they sharp enough?"

run_codex "Emily Bender" "computational linguistics critic and methodology scholar" \
"Push on construct validity and framing discipline: where does terminology still outrun evidence?"

# Packaging / rhetoric
run_codex "Deirdre McCloskey" "rhetoric of science scholar" \
"Push on persuasion and disciplinary uptake: identify any lines still sounding sectarian, overconfident, or under-calibrated."

run_codex "Carl Zimmer" "science writer" \
"Push on explanatory clarity: where does this chapter still lose an intelligent non-specialist?"

# Added external specialists for load-bearing risks
run_codex "Jon Sprouse" "experimental syntax and acceptability-judgment methodologist" \
"Push on judgment methodology: where are inferential leaps from acceptability data to grammatical architecture still too fast?"

run_codex "Florian Jaeger" "psycholinguistics and probabilistic language modeling researcher" \
"Push on processing-vs-grammar confounds: what quantitative model comparisons remain necessary before strong detector claims?"

# Phenomenology specialist added in this pass
run_codex "Shaun Gallagher" "phenomenology and cognitive science philosopher" \
"Push on level distinctions: is pre-reflective disruption now clearly separated from reflective and normative layers?"

echo "Waiting for Codex reviewers (pass 2)..."
wait
echo "Done. Files: notes/ch14-review-*-codex-pass2.md"

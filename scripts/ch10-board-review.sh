#!/bin/bash
# Multi-Agent Advisory Board Review for Chapter 10 Planning
# Run from: /Users/brettreynolds/Documents/LLM-CLI-projects/HPC book

# ============================================================================
# SHARED CONTEXT (pipe this to each agent)
# ============================================================================

read -r -d '' CONTEXT << 'EOF'
# Chapter 10 Planning: Definiteness and Deitality

## Book Context
A book arguing that grammatical categories are homeostatic property cluster (HPC) kinds—maintained by mechanisms (acquisition, entrenchment, transmission), not defined by essences. The core slogan: "A category is a profile, stabilized by mechanisms, projectible relative to purposes."

## Chapter 10 Core Argument
The definite article "the" marks a MORPHOSYNTACTIC property (deitality) distinct from SEMANTIC definiteness:

**Deitality diagnostics:**
- Restriction with *there*-insertion: *There's a dog* vs *??There's the dog*
- Compatibility with partitive *of*: *some of the dogs* vs *??some of dogs*
- Incompatibility with *one*-substitution: *I want a red one* vs *??I want the red one*

**Semantic definiteness:** identifiability, uniqueness, familiarity

**The dissociation cases (weak definites):**
- "She wears the veil" — generic, no specific veil
- "I took the bus" — no particular bus intended
- "play the piano" — institutional
- "go to the hospital" (BrE) — role, not token

**The HPC claim:** These two clusters overlapping but distinct. The form-function coupling is a mechanism, maintained by:
- High-frequency co-occurrence (definite form ≈ definite meaning)
- Pragmatic inference (hearers assume identifiability on hearing "the")
- But weak definites are entrenched exceptions—institutionalized decoupling

The literature's "exceptions" dissolve once you recognize two HPCs are in play.

## Existing Grist
- Cross-linguistic: Russian/Japanese lack articles—how do they mark identifiability?
- Key references: Hawkins 1978, 1991; Lyons 1999 *Definiteness*

## Your Role
You are ONE MEMBER of a virtual advisory board. Provide your perspective on:
1. What's missing from the chapter plan?
2. What objections will readers raise?
3. What examples/evidence would strengthen the argument?
4. Where does the argument overreach or underreach?
5. What's the best opening hook for this chapter?

Be specific. Be critical. Don't just praise.
EOF

# ============================================================================
# AGENT 1: COPILOT (Claude Haiku 4.5) — William Croft perspective
# ============================================================================

echo "--- AGENT 1: Copilot as William Croft (Radical Construction Grammar) ---"
copilot -p "You are William Croft, author of *Radical Construction Grammar*. You argue cross-linguistic categories don't exist—each language has its own construction-specific categories.

$CONTEXT

Your perspective: Does the definiteness/deitality distinction hold cross-linguistically, or is it an English-specific artifact? If Russian lacks articles entirely, what does that mean for 'deitality' as a universal morphosyntactic cluster? Push back hard on whether the HPC framing saves cross-linguistic comparison or whether it should let these categories go. Be specific about typological data." > ch10-review-croft.txt &

# ============================================================================
# AGENT 2: CODEX (GPT-5.2) — Nick Chater perspective
# ============================================================================

echo "--- AGENT 2: Codex as Nick Chater (The Mind is Flat) ---"
codex -p "You are Nick Chater, author of *The Mind is Flat*. You argue the mind constructs categories on-the-fly from fragmentary evidence, not from stored category representations.

$CONTEXT

Your perspective: Are deitality and definiteness psychologically real categories, or are they analyst's constructs imposed post-hoc? What would experimental evidence for the distinction look like? Would reaction-time or ERP data show dissociation between the two clusters? Be specific about what predictions the HPC account makes that differ from a classical definitional account or a purely usage-based account. Challenge whether speakers actually represent these as distinct clusters." > ch10-review-chater.txt &

# ============================================================================
# AGENT 3: GEMINI (3 Pro) — Joan Bybee perspective
# ============================================================================

echo "--- AGENT 3: Gemini as Joan Bybee (Frequency and Grammaticalization) ---"
gemini -p "You are Joan Bybee, expert on frequency effects and grammaticalization. You study how high-frequency constructions become entrenched and undergo phonetic reduction and semantic bleaching.

$CONTEXT

Your perspective: What's the DIACHRONIC story? How did the definite article develop its dual nature? Is this a case of ongoing grammaticalization (semantic bleaching of 'the' in weak definite contexts)? What frequency data would be relevant—are weak definites high-frequency enough to be entrenched as chunks? How does the form-function decoupling emerge historically? Be specific about what Bybee-style corpus evidence would support or challenge the chapter's claims." > ch10-review-bybee.txt &

# ============================================================================
# AGENT 4: COPILOT — Kara Federmeier perspective
# ============================================================================

echo "--- AGENT 4: Copilot as Kara Federmeier (ERPs and Categories) ---"
copilot -p "You are Kara Federmeier, expert on ERPs and semantic/syntactic processing. You study neural signatures of category processing.

$CONTEXT

Your perspective: What would the ERP signature of form-function dissociation look like? Would weak definites show different N400/P600 profiles than strong definites? If deitality and definiteness are distinct clusters maintained by different mechanisms, what neural predictions does that make? Be specific about experimental designs that could test the distinction. What would DISCONFIRM the HPC account versus a classical account?" > ch10-review-federmeier.txt &

# ============================================================================
# AGENT 5: CODEX — Chris Manning perspective
# ============================================================================

echo "--- AGENT 5: Codex as Chris Manning (Computational Linguistics/NLP) ---"
codex -p "You are Chris Manning, foundational NLP researcher now working with neural methods. You think about what linguistic structure neural language models learn.

$CONTEXT

Your perspective: What do language models know about definiteness? Do transformer representations of 'the' in weak definites cluster differently than in strong definites? If there are genuinely two HPCs (deitality vs. definiteness), would unsupervised probing reveal two clusters in embedding space? What would an HPC-compliant parser look like for definiteness phenomena? Be specific about what computational experiments could test the chapter's claims." > ch10-review-manning.txt &

# ============================================================================
# AGENT 6: GEMINI — Douglas Hofstadter perspective
# ============================================================================

echo "--- AGENT 6: Gemini as Douglas Hofstadter (Surfaces and Essences) ---"
gemini -p "You are Douglas Hofstadter, author of *Surfaces and Essences*. You argue analogy is the core of cognition—all categorization is fundamentally analogical extension from exemplars.

$CONTEXT

Your perspective: Is the deitality/definiteness distinction really two separate HPCs, or is it one family-resemblance category with a gradient boundary? Do speakers reason about 'the hospital' by analogy to 'the bus' to 'the piano' without representing any underlying cluster? Does the HPC framing add explanatory power beyond family resemblance, or is it dressed-up prototype theory? Challenge the machinery—is it doing real work?" > ch10-review-hofstadter.txt &

# ============================================================================
# AGENT 7: COPILOT — Deirdre McCloskey perspective
# ============================================================================

echo "--- AGENT 7: Copilot as Deirdre McCloskey (Rhetoric of Economics) ---"
copilot -p "You are Deirdre McCloskey, author of *The Rhetoric of Economics* and *Economical Writing*. You know how disciplines protect themselves from critique and how to write INSIDE a discipline while subverting it.

$CONTEXT

Your perspective: Does this chapter SOUND like a crank or a prophet? What rhetorical moves will make semanticists and syntacticians defensive, and how can the argument be reframed to feel revelatory rather than threatening? What's the best opening hook—where's the human stake? The veil/hat example is abstract; what's the version that makes a reader feel IMPLICATED? Be specific about prose strategy." > ch10-review-mccloskey.txt &

# ============================================================================
# AGENT 8: CODEX — George Lakoff perspective
# ============================================================================

echo "--- AGENT 8: Codex as George Lakoff (Conceptual Metaphor) ---"
codex -p "You are George Lakoff, expert on conceptual metaphor and cognitive semantics. You study how abstract categories are grounded in bodily experience.

$CONTEXT

Your perspective: What's the METAPHOR underlying the form-function distinction? If asking readers to shift from 'definiteness is a semantic primitive' to 'definiteness and deitality are distinct HPCs,' that's a conceptual metaphor shift. What's the source domain? 'The article is a switch' (on/off)? 'The article is a lens' (focusing)? 'The article is a handshake' (coordination signal)? What image schema underlies the form-function coupling? Be specific about how the chapter could leverage conceptual metaphor theory." > ch10-review-lakoff.txt &

# ============================================================================
# AGENT 9: GEMINI — Bruno Latour perspective
# ============================================================================

echo "--- AGENT 9: Gemini as Bruno Latour (Science Studies) ---"
gemini -p "You are Bruno Latour, science studies scholar. You study how classifications get built into infrastructure—textbooks, parsers, annotation schemes, funding structures.

$CONTEXT

Your perspective: Is 'definiteness' a theory linguists HOLD, or a practice DISTRIBUTED across infrastructure? Are there annotation schemes (Penn Treebank, Universal Dependencies) that hardcode the definiteness/article mapping? What would it take to change?—not just convincing theorists, but rewriting parsers, retooling corpora, retraining NLP engineers. Where does the chapter acknowledge the SOCIOLOGY of the definiteness concept? Be specific about what infrastructural changes the argument implies." > ch10-review-latour.txt &

# ============================================================================
# WAIT FOR ALL AGENTS
# ============================================================================

echo "Waiting for all agents to complete..."
wait

echo ""
echo "============================================================================"
echo "ALL REVIEWS COMPLETE. Files created:"
echo "  ch10-review-croft.txt     — Typological pushback"
echo "  ch10-review-chater.txt    — Psychological reality"
echo "  ch10-review-bybee.txt     — Frequency and diachrony"
echo "  ch10-review-federmeier.txt — ERP predictions"
echo "  ch10-review-manning.txt   — Computational experiments"
echo "  ch10-review-hofstadter.txt — Analogy vs. HPC"
echo "  ch10-review-mccloskey.txt — Rhetoric and positioning"
echo "  ch10-review-lakoff.txt    — Conceptual metaphor"
echo "  ch10-review-latour.txt    — Infrastructure and sociology"
echo "============================================================================"
EOF

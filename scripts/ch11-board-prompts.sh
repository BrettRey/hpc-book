#!/bin/bash
# Ch 11 Advisory Board - Parallel Execution Script
# Word classes: The adjective-adverb asymmetry as architectural equilibrium

cd "/Users/brettreynolds/Documents/LLM-CLI-projects/HPC book"

# Base context for all board members
read -r -d '' BASE_CONTEXT << 'CONTEXT'
You are providing advisory board feedback for Chapter 11 of "Words That Won't Hold Still: How Linguistic Categories Work" by Brett Reynolds.

THE BOOK'S THESIS: Linguistic categories are Homeostatic Property Cluster (HPC) kinds—property clusters maintained by causal mechanisms, not essences. The HPC slogan: "A category is a profile, stabilised by mechanisms, projectible for a purpose."

CHAPTER 11: Word classes
Subtitle: The adjective-adverb asymmetry as architectural equilibrium

Key points from the outline:
- Cross-linguistic stability of nouns/verbs
- Adjective-adverb variation across languages
- Architectural equilibrium: mechanisms at different scales

The chapter must explain:
1. Why noun/verb is so stable cross-linguistically (strong HPC)
2. Why adjective classes vary dramatically (sometimes merged with nouns, sometimes with verbs)
3. Why adverb is often a "wastebasket" category (weak/no HPC?)
4. How mechanisms at different scales (cognitive, discourse, transmission) produce this asymmetry

Read notes/CHAPTER_OUTLINE.md for full context on the book's structure.

CONTEXT

# Function to run board member on codex
run_codex() {
    local scholar="$1"
    local specialty="$2"
    local questions="$3"
    local output_file="notes/board-feedback-ch11-$(echo "$scholar" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"

    codex exec --full-auto "You are simulating the voice of $scholar, known for $specialty.

$BASE_CONTEXT

Write a 400-word advisory board review to $output_file addressing:
$questions

Format with markdown headers. Include the scholar's characteristic concerns and methodological commitments." 2>&1 &
}

# Function to run board member on gemini
run_gemini() {
    local scholar="$1"
    local specialty="$2"
    local questions="$3"
    local output_file="notes/board-feedback-ch11-$(echo "$scholar" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"

    gemini --yolo "You are simulating the voice of $scholar, known for $specialty.

$BASE_CONTEXT

Write a 400-word advisory board review and save it to $output_file addressing:
$questions

Format with markdown headers. Include the scholar's characteristic concerns and methodological commitments." 2>&1 &
}

# Function to run board member on copilot
run_copilot() {
    local scholar="$1"
    local specialty="$2"
    local questions="$3"
    local output_file="notes/board-feedback-ch11-$(echo "$scholar" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"

    copilot -p "You are simulating the voice of $scholar, known for $specialty.

$BASE_CONTEXT

Write a 400-word advisory board review and save it to $output_file addressing:
$questions

Format with markdown headers. Include the scholar's characteristic concerns and methodological commitments." --allow-all-tools 2>&1 &
}

echo "Starting Ch 11 Advisory Board (12 members across 3 CLIs)..."
echo "============================================================"

# CODEX (4 members) - typology focus
run_codex "Martin Haspelmath" "typology, comparative concepts, and cross-linguistic methodology" \
"1. How does HPC relate to comparative concepts methodology?
2. What cross-linguistic evidence on word classes should be included?
3. How to handle the noun/verb vs adjective asymmetry typologically?"

run_codex "William Croft" "Radical Construction Grammar and cross-linguistic word class analysis" \
"1. How does the HPC framing relate to RCG's treatment of word classes?
2. What role do constructions play in stabilizing word class distinctions?
3. How should the chapter handle the form/function distinction for word classes?"

run_codex "R.M.W. Dixon" "adjective classes, basic linguistic theory, and typological fieldwork" \
"1. What does the cross-linguistic variation in adjective classes tell us about mechanisms?
2. How should the chapter use Dixon's typology of adjective-like words?
3. What pitfalls should the chapter avoid when generalizing about word classes?"

run_codex "Mark Baker" "Chomskyan universals and the lexical category problem" \
"1. What would a generativist want to see acknowledged about word class universals?
2. Where does HPC diverge from formal approaches to lexical categories?
3. What shared ground exists between mechanistic and parametric accounts?"

# GEMINI (4 members) - usage-based focus
run_gemini "Adele Goldberg" "construction grammar, argument structure, and usage-based learning" \
"1. How do constructions stabilize word class membership?
2. What does HPC add beyond standard construction grammar accounts?
3. How should acquisition evidence be integrated?"

run_gemini "Joan Bybee" "frequency effects, grammaticalization, and phonological reduction" \
"1. How do frequency and entrenchment maintain word class boundaries?
2. What diachronic evidence on word class change should be included?
3. How does grammaticalization relate to HPC failure modes?"

run_gemini "Michael Tomasello" "usage-based acquisition and social-cognitive mechanisms" \
"1. What acquisition evidence supports word class as HPC?
2. How do children learn word class membership without explicit instruction?
3. What role does intention-reading play in word class learning?"

run_gemini "Simon Kirby" "language evolution, iterated learning, and cultural transmission" \
"1. How does cultural transmission shape word class stability?
2. What does iterated learning predict about noun/verb vs adjective?
3. How should the chapter frame cross-generational mechanisms?"

# COPILOT (4 members) - categorization/philosophy focus
run_copilot "Eleanor Rosch" "prototype theory and categorization research" \
"1. How does HPC relate to prototype structure for word classes?
2. Is word class membership graded or discrete?
3. What categorization evidence should be included?"

run_copilot "Ruth Millikan" "teleosemantics, proper functions, and biological categories" \
"1. What is the proper function of word class categories?
2. How do word classes reproduce themselves across speakers?
3. What would 'malfunction' look like for a word class?"

run_copilot "Ben Ambridge" "acquisition, entrenchment, and psycholinguistic evidence" \
"1. What experimental evidence supports word class as learned category?
2. How does entrenchment differ across word classes?
3. What production/comprehension asymmetries are relevant?"

run_copilot "Edward Tufte" "data visualization and information design" \
"1. What figures would best illustrate the noun/verb vs adjective asymmetry?
2. How should cross-linguistic data be displayed?
3. What visual pitfalls should the chapter avoid?"

echo ""
echo "All 12 advisory board agents launched. Waiting for completion..."
wait
echo ""
echo "============================================================"
echo "All agents complete. Check notes/board-feedback-ch11-*.md"

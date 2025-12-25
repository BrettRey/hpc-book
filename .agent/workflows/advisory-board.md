# Advisory Board Workflow

Run simulated advisory board reviews for chapter planning using parallel LLM CLI agents.

## Prerequisites

Check that all three CLIs are available:
```bash
which codex gemini copilot
```

## Step 1: Gather Chapter Materials

Before running agents, read ALL relevant planning files:

```bash
# Check for chapter-specific materials
ls notes/chapterNN-grist.md      # Raw ideas, worked examples
ls notes/chapterNN-master.md     # Consolidated structure
ls notes/chapterNN_planning.md   # Planning notes (varies)
```

**Critical**: The grist file often contains the richest material (worked examples, key insights, mechanism details). Don't rely only on CHAPTER_OUTLINE.md.

## Step 2: Select Board Members

Choose 9-12 scholars relevant to the chapter topic. Distribute across CLIs:

| CLI | Best for | Command pattern |
|-----|----------|-----------------|
| **Codex** | Detailed reasoning, file operations | `codex exec --full-auto 'prompt'` |
| **Gemini** | Fast, good at reading multiple files | `gemini --yolo 'prompt'` |
| **Copilot** | Reliable file writing | `copilot -p 'prompt' --allow-all-tools` |

### Standard Board (adapt per chapter)

**Typology/Cross-linguistic**: Haspelmath, Croft, Dixon
**Construction Grammar**: Goldberg, Bybee
**Acquisition**: Tomasello, Ambridge
**Philosophy**: Millikan, Boyd, Rosch
**Evolution/Transmission**: Kirby
**Visualization**: Tufte
**Generative contrast**: Baker, Chomsky

## Step 3: Craft Prompts

Each prompt should include:

1. **Scholar identity**: Name and known-for
2. **Files to read**: `Read notes/CHAPTER_OUTLINE.md AND notes/chapterNN-grist.md`
3. **Key insights**: Quote specific material from grist file
4. **Targeted questions**: 2-3 questions specific to that scholar's expertise
5. **Output file**: `notes/board-feedback-chNN-lastname.md`
6. **Word count**: 300-400 words

### Template

```
You are simulating [Scholar Name], known for [specialty].

Read notes/CHAPTER_OUTLINE.md AND notes/chapterNN-grist.md.

Key insight from grist: [Quote the specific material]

Write [N] words to notes/board-feedback-chNN-[lastname].md addressing:
1. [Question targeting their expertise]
2. [Question about the key insight]
3. [Question connecting to book's broader argument]
```

## Step 4: Run in Parallel

Launch all agents simultaneously using background processes:

```bash
cd "/Users/brettreynolds/Documents/LLM-CLI-projects/HPC book"

# Codex batch (3-4 agents)
codex exec --full-auto 'prompt1' 2>&1 &
codex exec --full-auto 'prompt2' 2>&1 &
codex exec --full-auto 'prompt3' 2>&1 &

# Gemini batch (3-4 agents)
gemini --yolo 'prompt4' 2>&1 &
gemini --yolo 'prompt5' 2>&1 &
gemini --yolo 'prompt6' 2>&1 &

# Copilot batch (3-4 agents)
copilot -p 'prompt7' --allow-all-tools 2>&1 &
copilot -p 'prompt8' --allow-all-tools 2>&1 &
copilot -p 'prompt9' --allow-all-tools 2>&1 &

wait
echo "All agents complete"
```

## Step 5: Review and Iterate

After first wave, check for gaps:

```bash
ls notes/board-feedback-chNN-*.md
```

Run second wave (`-v2` suffix) if:
- First wave missed key grist material
- Need deeper engagement with specific insights
- Want contrasting perspectives on same question

## Rate Limits

- **Gemini**: May hit quota; retry after ~30 seconds
- **Codex**: Slower but reliable; uses more reasoning tokens
- **Copilot**: Fast, uses Haiku by default

## Output Naming Convention

```
board-feedback-ch[NN]-[lastname].md      # First wave
board-feedback-ch[NN]-[lastname]-v2.md   # Second wave with more context
```

## Chapter-Specific Board Suggestions

### Ch 9 (Countability)
Goldberg, Rosch, Bybee, Tomasello, Millikan, Becker, Zimmer, Tufte, Holmes

### Ch 10 (Definiteness)
Same as Ch 9, plus semanticists

### Ch 11 (Word Classes)
Haspelmath, Croft, Dixon, Baker, Goldberg, Bybee, Tomasello, Kirby, Rosch, Millikan, Ambridge, Tufte

### Ch 12 (The Stack - non-grammar cases)
**Phonology case**: Labov, Bybee (sound change), Pierrehumbert, Kirby
**Register case**: Eckert, Biber, Silverstein, Agha
**Philosophy**: Millikan, Boyd
**Visualization**: Tufte

### Ch 13 (Grammaticality)
Schütze, Sprouse, Phillips, Fedorenko, Chomsky (contrast), Miller (collab)

### Ch 14 (Methodology)
All previous board members for synthesis

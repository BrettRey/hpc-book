# Advisory Board Workflow (Codex-Only)

Run simulated advisory board reviews for chapter planning using parallel Codex agents.

## Project Policy

Use `codex` only for board generation in this repository unless the user explicitly requests otherwise.

## Prerequisites

Check Codex availability:
```bash
which codex && codex --version
```

## Step 1: Gather Chapter Materials

Before running agents, read all relevant planning files:

```bash
ls notes/chapterNN-grist.md
ls notes/chapterNN-master.md
ls notes/chapterNN_planning.md
```

## Step 2: Select Board Members

Choose 6-12 scholars relevant to the chapter topic. Use a mix of:
- Theory/mechanism reviewers (e.g., Croft, Goldberg, Millikan, Rosch, Tomasello)
- Packaging reviewers (e.g., Zimmer, McCloskey, Tufte, Holmes)

## Step 3: Prompt Template

```text
You are simulating [Scholar Name], known for [specialty].
Read [target files].
Write 300-500 words to notes/board-feedback-chNN-[lastname]-codex.md addressing:
1) [question 1]
2) [question 2]
3) [question 3]
Use sections: Strengths, Major Concerns, Priority Fixes.
```

## Step 4: Run in Parallel

```bash
cd "/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book"

codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-chNN-name1-codex.md "prompt 1" &
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-chNN-name2-codex.md "prompt 2" &
codex exec --full-auto -C "$(pwd)" -o notes/board-feedback-chNN-name3-codex.md "prompt 3" &
wait
```

## Step 5: Synthesize

```bash
ls notes/board-feedback-chNN-*-codex.md
```

Capture:
- Convergent concerns (3+ reviewers)
- High-priority edits
- Remaining disagreements

## Naming Convention

```text
board-feedback-ch[NN]-[lastname]-codex.md
board-feedback-ch[NN]-[lastname]-codex-v2.md
```

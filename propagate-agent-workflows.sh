#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SRC_WORKFLOWS_DIR="${SCRIPT_DIR}/.agent/workflows"

if [[ ! -d "${SRC_WORKFLOWS_DIR}" ]]; then
  echo "ERROR: Source workflows not found at: ${SRC_WORKFLOWS_DIR}" >&2
  exit 1
fi

paper_projects=(
  "CGEL-25th-anniversary"
  "countability"
  "echolocation"
  "Functions_as_Comparanda__Categories_as_Kinds__A_Homeostatic_Approach_to_Typology"
  "Grammaticality_de_idealized"
  "Grammaticality_talk_for_TESL_5002"
  "How_to_Study_Boundary_Phenomena_English_Reciprocals_and_the_Limits_of_Categorization"
  "Independent_relative_whose"
  "Labels_to_Stabilisers"
  "linguistics-mereology"
  "linguistics-metrology"
  "Personhood_and_proforms"
  "SSHRC-IDG-2026"
)

write_init_md() {
  local project_name="$1"
  local out_path="$2"

  cat > "${out_path}" <<EOF
---
description: Initialize the ${project_name} project environment
---

# ${project_name} Project Initialization

This workflow orients you to the project. Use it at the start of any new session.

## Quick Start (Returning Session)

1. **Scan the repo for orientation docs**
   \`\`\`
   ls -la
   \`\`\`

2. **Read orchestration + status files (if present)**
   \`\`\`
   [ -f AGENTS.md ] && cat AGENTS.md
   [ -f STATUS.md ] && cat STATUS.md
   [ -f TODO.md ] && cat TODO.md
   \`\`\`

3. **Check house style (if present)**
   \`\`\`
   [ -f .house-style/style-guide.md ] && cat .house-style/style-guide.md
   [ -f .house-style/style-rules.yaml ] && cat .house-style/style-rules.yaml
   \`\`\`

4. **Identify the build entrypoint**
   \`\`\`
   ls -la *.tex 2>/dev/null || true
   [ -f Makefile ] && sed -n '1,160p' Makefile
   \`\`\`

## Key Retrieval Points

**For argument/outline:**
- \`outline.md\`, \`PLAN.md\`, \`docs/\`, \`notes/\`

**For current draft:**
- \`main.tex\` (or the largest \`*.tex\` in the repo root)

**For bibliography:**
- \`references.bib\` or \`refs.bib\`

**For figures/data:**
- \`figures/\`, \`Fig/\`, \`data/\`

**For source PDFs (if present):**
- \`literature/\`, \`sources/\`, \`pdf/\`

Search PDFs quickly:
\`\`\`
pdftotext "PATH/filename.pdf" - | rg -n "keyword"
\`\`\`

## Full Initialization (New to Project)

1. **Read \`CLAUDE.md\` and \`AGENTS.md\` (if present)** — overview, build commands, house style
2. **Skim the main TeX file** (\`main.tex\` or equivalent) for structure and macro conventions
3. **Locate bibliography + figure folders** so you know where to add assets
4. **Run a quick build** (optional, if you have TeX installed)
   - \`make quick\` or \`make\`
   - otherwise: \`latexmk -pdf main.tex\`

## Process Reminders

**For drafting/revision:**
1. Start from an outline and the target venue constraints
2. Make one coherent pass at a time (structure → prose → citations)
3. Keep changes small enough to review

**For citation work:**
1. Add BibTeX entries carefully (protect capitalization)
2. Prefer \`\\textcite{}\` / \`\\parencite{}\` or project-standard macros
3. Rebuild after citation edits to catch missing keys

**Git:**
- Commit after each logical unit of work; use \`/git-hygiene\` if you need reminders

## Other Workflows

- \`/git-hygiene\` — Reminders for clean commits and branch management
- \`/multi-agent-review\` — Spawn independent LLM agents (Codex, Gemini) for parallel advisory board reviews of the draft. Useful for getting diverse, unbiased feedback.
EOF
}

write_git_hygiene_generic_md() {
  local out_path="$1"

  cat > "${out_path}" <<'EOF'
---
description: Git hygiene reminders for this paper project
---

## During work sessions

After completing any of these, prompt the user to commit:
- Finishing a section or subsection revision
- Adding or modifying figures
- Adding bibliography entries
- Any change that took more than 10 minutes of back-and-forth

Suggested prompt: "That's a good stopping point — want to commit?"

## Commit message format

```
<short summary line>

- Bullet points for specific changes
- Reference figures, citations, sections by name
```

## End of session

Before ending a session, check:
1. `git status` — anything uncommitted?
2. `git push` — anything unpushed?

If yes to either, prompt: "You have uncommitted/unpushed changes. Want to save your work?"

## Frequency target

Aim for commits every 15-30 minutes of active editing, or after each logical unit of work.
EOF
}

update_project_workflows() {
  local project_name="$1"
  local project_dir="${ROOT_DIR}/${project_name}"
  local dest_dir="${project_dir}/.agent/workflows"

  if [[ ! -d "${project_dir}" ]]; then
    echo "WARN: Missing project dir: ${project_dir} (skipping)"
    return 0
  fi

  mkdir -p "${dest_dir}"
  cp "${SRC_WORKFLOWS_DIR}/git-hygiene.md" "${dest_dir}/git-hygiene.md"
  cp "${SRC_WORKFLOWS_DIR}/multi-agent-review.md" "${dest_dir}/multi-agent-review.md"
  write_init_md "${project_name}" "${dest_dir}/init.md"

  echo "Updated: ${project_name}/.agent/workflows/"
}

for project in "${paper_projects[@]}"; do
  update_project_workflows "${project}"
done

template_dir="${ROOT_DIR}/.house-style/templates/paper-template"
if [[ -d "${template_dir}" ]]; then
  template_workflows_dir="${template_dir}/.agent/workflows"
  mkdir -p "${template_workflows_dir}"

  write_init_md "{{PAPER_TITLE}}" "${template_workflows_dir}/init.md"
  write_git_hygiene_generic_md "${template_workflows_dir}/git-hygiene.md"
  cp "${SRC_WORKFLOWS_DIR}/multi-agent-review.md" "${template_workflows_dir}/multi-agent-review.md"

  echo "Updated: .house-style/templates/paper-template/.agent/workflows/"
else
  echo "WARN: Missing template dir: ${template_dir} (skipping)"
fi

echo "Done."

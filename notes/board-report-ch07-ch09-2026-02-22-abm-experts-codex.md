# ABM Expert Board Report (Codex-only)

**Date**: 2026-02-22  
**Scope**: Chapter 7/9 ABM prose + `code/volcano_abm.py` + `code/countability_abm.py`  
**Reviewers**:
- Doyne Farmer (`notes/board-ch07-ch09-2026-02-22-farmer-codex.md`)
- Simon Kirby (`notes/board-ch07-ch09-2026-02-22-kirby-codex.md`)
- Joshua Epstein (`notes/board-ch07-ch09-2026-02-22-epstein-codex.md`)

## Convergent Findings

1. Epistemic-status framing is now much better.
- All three reviewers explicitly approve the "illustrative, not probative" direction in both prose and code.

2. Main residual risk: some outcomes are partly architecture-driven.
- Hard-coded threshold ordering + intent conditioning + exogenous anchor decay can predetermine parts of the observed asymmetry.
- Recommended framing: mechanism plausibility under assumptions, not evidential adjudication.

3. Main methodological gap: uncertainty reporting.
- Single-seed trajectories are informative but insufficient.
- Reviewers request explicit seed-ensemble summaries and sign consistency for ablation deltas.

4. Transmission caveat needed to stay explicit.
- Any turnover shortcut can be mistaken for full developmental acquisition.
- Keep language explicit about what the transmission routine does and does not model.

5. Volcano ABM still needs stronger control logic if used as a mechanism-isolation demonstration.
- Suggested future additions: no-switch control, freeze-`w` and freeze-`theta` controls, parameter sweeps.

## Divergence

- Kirby is most concerned about acquisition realism and generational overinterpretation.
- Farmer emphasizes hidden assumptions and over-strong wording in internal packet language.
- Epstein emphasizes reproducibility infrastructure (run manifests, uncertainty summaries, parameter transparency).

## Priority Actions

1. Keep Chapter 7/9 ABM claims conditional and language-scoped.
2. Report multi-seed uncertainty (not just one run).
3. Keep turnover assumptions explicit in prose and docstrings.
4. Keep packet wording synchronized with chapter-level caution.
5. Add reproducibility manifests for figure-generating runs.

## This Pass

Implemented in this pass:
- Stronger Chapter 7/9 caveat wording and seeded-trajectory disclaimer.
- Chapter 9 transmission caveat retained, with tutor-bootstrap turnover implementation.
- Countability ABM `--exp=sensitivity` multi-seed summary + manifests.
- Volcano ABM run manifest + default seed harmonized to 42.
- Advisory-board workflows/scripts switched to Codex-only defaults.

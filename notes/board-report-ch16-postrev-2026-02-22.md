# Board Report: Chapter 16 Post-Revision (2026-02-22)

## Inputs
- `notes/board-feedback-ch16-postrev-lesser-codex.md`
- `notes/board-feedback-ch16-postrev-mccloskey-codex.md`
- `notes/board-feedback-ch16-postrev-tufte-codex.md`
- `notes/board-feedback-ch16-postrev-croft-codex.md`
- `notes/board-feedback-ch16-postrev-goldberg-codex.md`
- `notes/board-feedback-ch16-postrev-godfreysmith-codex.md`
- `notes/board-feedback-ch16-postrev-jackendoff-codex.md`

## Board-level verdict
All 7 reviewers converged on the same verdict: **Improved but still missing core work**.

## Where the revision clearly worked
1. The new synthesis section (`chapters/chapter16.tex:34`) improved architecture by making commitments explicit before predictions.
2. The synthesis ledger (`chapters/chapter16.tex:47`) was widely seen as a real upgrade in accountability (mechanism -> observable -> defeat hook).
3. Chapter 15 handoff integration improved, especially around conditioning/no-lift logic (`chapters/chapter15.tex:217`, `chapters/chapter16.tex:155`).

## Main unresolved concerns
1. **Role overlap / pacing drag**: many reviewers flagged partial duplication between the synthesis ledger and gauntlet table (`chapters/chapter16.tex:47`, `chapters/chapter16.tex:142`).
2. **Underspecified adjudication**: defeat hooks still read as too absolute or too verbal in places (e.g., random drift / lockstep language), leaving room for post hoc rescue (`chapters/chapter16.tex:56`, `chapters/chapter16.tex:58`, `chapters/chapter16.tex:115`, `chapters/chapter16.tex:120`).
3. **Threshold grounding**: the `5%` / `3 datasets` rule appears useful but currently under-justified (`chapters/chapter16.tex:161`).
4. **Bridge clarity**: reviewers repeatedly asked for an explicit mapping from Ch.15 conditioning architecture to Ch.16 predictions/tests (`chapters/chapter15.tex:183`, `chapters/chapter16.tex:74`).

## Highest-leverage next edit (cross-review consensus)
Insert a short bridge paragraph near the start of empirical commitments (right after `chapters/chapter16.tex:74`) that:
- maps each commitment/ledger row to a specific gauntlet test,
- states that evaluation is on conditioned models (not pooled marginals), and
- clarifies whether the `5%`/`3 datasets` rule is global or domain-specific.

This single move addresses the most frequent concerns without large structural surgery.

## Notable minority pushes
- One reviewer suggested removing the synthesis table entirely for pace and keeping only prose + gauntlet table.
- One reviewer pressed for stronger cross-linguistic confirmation criteria for comparative-tier claims.
- One reviewer asked for an explicit constructional transfer prediction block around the `data` case.

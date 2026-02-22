# Chapter 15 Packaging Synthesis (2026-02-22)

## Inputs
- `notes/board-feedback-ch15-mccloskey-codex-pack.md`
- `notes/board-feedback-ch15-lesser-codex-pack.md`
- `notes/board-feedback-ch15-zimmer-codex-pack.md`
- `notes/board-feedback-ch15-tufte-codex-pack.md`
- `notes/board-feedback-ch15-becker-codex-pack.md`
- `notes/board-feedback-ch15-morris-codex-pack.md`

## Executive Judgment
The consensus diagnosis is clear: Chapter 15 is conceptually strong, but packaging is the bottleneck. The opening and core mechanism are persuasive; the middle loses narrative traction, and the close gets more declarative than operational. This is primarily a rhetoric/structure problem, with a secondary evidence-density problem.

## Convergences Across Reviewers
- Keep and reuse the red-pen opening. It is the chapter's strongest entry point (`chapters/chapter15.tex:6`).
- Preserve the mixed-bin logic, but compress metaphor stretch to prevent drift into lecture mode (`chapters/chapter15.tex:54`).
- Reduce repetition in dialect/register/community by turning the triad into one unfolding case instead of three parallel mini-essays (`chapters/chapter15.tex:88`, `chapters/chapter15.tex:105`, `chapters/chapter15.tex:124`).
- Delay formalism by one beat: concrete first, notation second (`chapters/chapter15.tex:73`, `chapters/chapter15.tex:173`).
- Add operational and test hooks now, not only in Chapter 16 (`chapters/chapter15.tex:152`, `chapters/chapter16.tex:99`).
- Recalibrate high-friction phrasing to cumulative language (`chapters/chapter15.tex:21`, `chapters/chapter15.tex:95`, `chapters/chapter15.tex:194`, `chapters/chapter15.tex:206`).
- End with explicit handoff: what changes in research workflow tomorrow (`chapters/chapter16.tex:137`).

## Priority Edit Plan

### 1) Structural Packaging (highest ROI)
- Keep one running case onstage from first paragraph to conclusion (double copula + correction context).
- Rebuild Sections 15.3-15.6 as a single arc:
- Step 1: mixed bin diagnosis.
- Step 2: dialect as persistent conditioning.
- Step 3: register as situational reweighting.
- Step 4: discourse community as source attribution.
- Step 5: acquisition as learning that conditioning structure.
- Cut one illustrative detour (recommended cut target: violinist paragraph) unless it carries unique evidence (`chapters/chapter15.tex:86`).

### 2) Evidence Packaging
- Add one compact evidence table in Chapter 15 (not decorative), with columns:
- Claim.
- Conditioning variables.
- Observable signature.
- Data/source anchor.
- Defeat condition.
- Place table after mixed-bin formalization so it anchors the rest of the chapter (`chapters/chapter15.tex:73`).
- For high-confidence numeric claims without immediate support, either add concrete scope/statistics or downgrade modality (`chapters/chapter15.tex:8`, `chapters/chapter15.tex:41`, `chapters/chapter15.tex:65`, `chapters/chapter15.tex:166`).

### 3) Operationalization (Becker/Tufte bridge)
- Add a short subsection: "Minimal protocol for conditioning analyses."
- Define token-level coding proxies for D/R/C.
- Add borderline-case adjudication rule.
- Add minimum reliability criterion (for example, report inter-coder agreement).
- Add a fallback design for small corpora (contingency-table baseline + simple mixed model option).
- This directly sets up Chapter 16's gauntlet style instead of postponing method (`chapters/chapter16.tex:99`, `chapters/chapter16.tex:123`).

### 4) Tone and Closing Handoff
- Rewrite adversarial sentences into "extends prior work" framing:
- `chapters/chapter15.tex:21`
- `chapters/chapter15.tex:95`
- `chapters/chapter15.tex:194`
- Replace ontological crescendo with test-forward close:
- Soften `chapters/chapter15.tex:206`.
- Add 6-8 sentence bridge that states:
- What to measure.
- What would falsify the Chapter 15 claim.
- What design step changes immediately (explicit handoff to Chapter 16).

## Surgical Edit Map (line-anchored)
- `chapters/chapter15.tex:21` tone-neutral opening of variation section.
- `chapters/chapter15.tex:54` to `chapters/chapter15.tex:63` compress bolt metaphor by ~35%.
- `chapters/chapter15.tex:88` to `chapters/chapter15.tex:133` convert parallel triad into one continuous mechanism trace.
- `chapters/chapter15.tex:154` split long abstraction paragraph into shorter concrete-first sequence.
- `chapters/chapter15.tex:173` start with listener inference sentence, then equation.
- `chapters/chapter15.tex:190` to `chapters/chapter15.tex:206` cut ~25-30%, remove victory-tone language, hand off to gauntlet.

## "Done" Criteria For This Revision Pass
- A skeptical reader can state the mechanism in one sentence without using your terminology.
- Each major section contains at least one concrete observable, not only conceptual framing.
- The chapter ends with a practical testing handoff rather than a metaphysical declaration.
- No sentence invites tribal resistance unnecessarily.


# HPC Book Project Status

**Date**: March 3, 2026
**Current Phase**: 17-chapter draft + postscript; new Ch 13 (sign language anaphor) planned. Revision/polish phase.

### Session (Mar 3, 2026): Ch 5 revisions from ChatGPT 5.2 feedback

- ✅ **7 surgical edits** to `chapters/chapter05.tex` (clear wins + worth doing from ChatGPT 5.2 pro review)
  - ω → H notation fix (avoids confusion with first infinite ordinal)
  - K's status clarified (not psychologically real)
  - Invariant prediction named explicitly (latent-threshold model vs hyperreal contribution)
  - "That's exactly what we find" softened
  - "stable manifolds of saddle points" jargon dialled back
  - Bivalence indexed to individual speaker's maintained grammar
  - Probabilistic-competence alternatives acknowledged (3 sentences, cross-refs Ch 14)
- ✅ **Verified:** No remaining `$\omega$`; XeLaTeX compiles cleanly (480 pages)

### Session (Mar 3, 2026): Ch 13 sign anaphor drafted

- ✅ **Chapter 13 drafted** (`chapters/chapter13-sign-anaphor.tex`): ~5500 words, 7 sections, 2 tables
  - Core move: anaphoric tracking ≠ spatial agreement (two HPC clusters, not one)
  - Schlenker/Kuhn debate resolved as each describing a different cluster
  - Coupling gradient table: ASL → BSL → ISL → NSL → ABSL → Kata Kolok → homesign
  - Labels: `sec:sign:` prefix, `ch:sign-anaphor` chapter label
- ✅ **18 bib entries** added to `references-local.bib` (verified against PDFs)
- ✅ **Compiled successfully** (no LaTeX errors); PDF reviewed
- ✅ **Inserted in `hpc-book.tex`** after Ch 12, before zipper chapter
- **Pending:** Brett's review, chapter renumbering infrastructure, flagged bib verifications

### Session (Mar 3, 2026): Editorial decisions + new chapter decision

**Editorial decisions resolved:**
- ✅ **PA → footnote** (Ch 1): Jackendoff paragraph moved to footnote on "third possibility" pivot
- ✅ **Peirce tightening** (Chs 9, 12): Reduced would-be repetition in Ch 9 (8→3); cut Ch 7 recap and redundant Peirce attribution in Ch 12
- ✅ **Discourse scope-limit** (Ch 13): Visible sentence before stabilizer-weighting map + table footnote
- ✅ **Budding expansion** (Ch 17): 4 sentences → ~450 words. New terms: budding, mechanism parasitism
- ✅ **CC-BY 4.0** on colophon; GitHub repo URL added
- ✅ **"Foundations of linguistics"** named as subfield in preface

**Architectural decision:**
- ✅ **New Ch 13: Sign language anaphor** -- tests modality independence of HPC architecture. Spatial loci as formal cluster, referent tracking as semantic cluster. Current Ch 13 (stack) → Ch 14; Part IV chapters renumber (15--18). Full scoping notes: `notes/ch13-sign-anaphor-scope.md`
- Book becomes **18 chapters** + postscript
- Literature pass needed before writing (Sandler & Lillo-Martin 2006, Schlenker 2018, Padden 1988, Cormier et al., village sign languages)

**Next session:** Start with `notes/ch13-sign-anaphor-scope.md`. Literature pass first, then chapter structure, then drafting.

### Session (Mar 3, 2026): HPC formalization appendix + citation bridge

- ✅ **Appendix A formalization added** (`chapters/appendix_diagnostics.tex`):
  - Triad definition: `HPC_F(C)=⟨P(C), M(C), Π_F(C)⟩`
  - Profile layer with MI-based dependence score `S(C)`
  - Maintenance layer as dynamical mechanism with intervention form `do(A_t=a)` and return-to-basin criterion `τ_δ(a)`
  - Projectibility layer as field-relative predictive lift `Π_F(C)`
  - Four-check decision rule (profile, homeostasis, projectibility, ablation)
  - Thin/fat/negative failure-mode mapping to formal quantities
- ✅ **Named literature bridge inserted** in Appendix A:
  - Martínez (informationally connected property clusters)
  - Rehder (causal-model categorization)
  - van Rooij & Schulz (Pearl-style causal analysis of natural kinds/dispositions)
- ✅ **Local bibliography updates** in `references-local.bib`:
  - Added `martinez2015informationally`, `rehder2003causal`, `vanrooijschulz2019`
  - DOI metadata verified via Crossref API before insertion
- ✅ **Verification complete**:
  - `latexmk hpc-book.tex` successful; no undefined-citation warnings; output `build/hpc-book.pdf` at **498 pages**
  - `python code/validate_bib.py` successful (`references.bib` parsed cleanly)
- ⚠️ **Scope note:** The three new bibliography records are currently local (`references-local.bib`) and not yet promoted to shared `references.bib`.

### Multi-day instance (Feb 28 -- Mar 2, 2026): 18 commits, major structural and editorial work

**Structural:**
- ✅ **Split Ch 16 → Ch 16 + Ch 17**: Ch 16 ("How Categories Travel") and Ch 17 ("The Gauntlet") now separate chapters. With the signed-language insertion, the current structure is 18 chapters + postscript.
- ✅ **Predictions appendix (Appendix C)**: 30 numbered predictions + 2 defeat conditions gathered from across the book.
- ✅ **Postscript created**: ~370 words on "language" as a category the book doesn't address.
- ✅ **Cross-reference infrastructure**: index tags, section labels, `\ref` conversions, Ch 15 prose fixes.
- ✅ **Definiteness thread**: new `\definiteness` environment, added to Ch 9, removed from Chs 14-15.

**Ch 16 (How Categories Travel):**
- ✅ Metaphor paper integration, projectibility restoration, embodiment reply
- ✅ Counting diagnostic, functional domain definition, painted-line case, Noyes & Keil development
- ✅ Trail passage: show-first-name-second rewrite
- ✅ Prose tightening, LLM nuance, covariation honesty
- ✅ TCM-gauntlet connection; Canudas-Grabolosa et al. (2026) homesigner study integrated

**Ch 17 (The Gauntlet):**
- ✅ Ladyman & Ross attribution, Figure 17.1 revision, Sancho Panza epigraph
- ✅ **§17.2 full rewrite** ("What HPC opens"): 5 expert-perspective Sonnet agents (Boyd, Haspelmath, Kendler, Bybee, Borsboom) identified convergent criticisms. Disentangled Kendler MPC from Borsboom network theory; fixed DSM to polythetic; acknowledged Mayr's BSC already mechanistic; addressed Haspelmath's cross-linguistic gap; three psychiatry-linguistics disanalogies. Now distinguishes "reframes" / "imports" / "opens."

**Projectibility-as-constitutive correction:**
- ✅ ~20 edits across 8 chapters restoring projectibility as third constitutive leg of Boyd's HPC (not downstream bonus). Ch 16 synthesis ledger fully rewritten.

**Humour audit:**
- ✅ Full-book scan with Sonnet + Codex agents; combined report in `notes/humour-audit-combined.md`
- ✅ Ch 3: evaluated ~20 additions critically (Tier 1/2/3), applied 17 (Tiers 1+2)
- ✅ Ch 13: 8 meaning-bearing inserts

**Prose and voice:**
- ✅ Revoiced Chs 11, 13; aphoristic prose audit
- ✅ Ch 12: sex/social-gender/grammatical-gender diagnostic
- ✅ Boyd circle fix (textcite for inline citations)
- ✅ Ch 15: five prose fixes

**Gauntlet reframing (conceptual):**
- Diagnosed that gauntlet predictions test maintenance degradation, not projection
- Budding-not-fission insight for grammaticalization
- Diff-in-diff across biology/psychiatry/ecology/linguistics
- Full notes: `notes/gauntlet-reframing-2026-02-28.md`

**Bibliography:** `borsboom2017` added; zero undefined citations; 492 pages clean.

**Process note:** Brett corrected me for implementing humour additions without critical evaluation. Always evaluate before implementing.

### Session Work (Feb 25, 2026: Index cleanup + lexical gloss audit)
- ✅ **HPC "applied to linguistics" reclassification completed**: 4 straggler tags fixed (ch03→`!defined`, ch05→`!cross-linguistic`, ch09→`!lexical categories`, ch14→`!grammaticality`). Zero bare or `!applied` tags remain.
- ✅ **Lexical index gloss audit**: all 16 unglossed foreign-language entries now glossed across ch06, ch10, ch11, ch12 (Japanese, Turkish, Swahili, Latin, French, German, Greek). Rule: every non-English entry gets a gloss.
- ✅ **Build verified**: 453 pages, all 4 indexes regenerate cleanly (0 makeindex warnings)
- **Not yet committed**

### Session Work (Feb 25, 2026: Bibliography audit complete)
- ✅ **Two-pass bibliography audit** across ~292 entries in central bib
  - Pass 1: 17 fixes (fabricated authors, wrong entry types, incorrect pages/years/DOIs)
  - Pass 2: 3 fixes (ross1967 redundant note, pullum2025 pages, ekstrom2025 now published)
  - All fixes verified via Crossref API
- ✅ **Local bib/chapter fixes**: fortson2004 author format, chapter11 citation key Gibson2026→gibson2025
- ✅ **Cover page**: removed provisional-citations warning; draft disclaimer retained
- ✅ **Final scan**: 2 remaining "advance online" / "forthcoming" entries confirmed genuinely unpublished (O'Doherty, Scott-Phillips)
- **Commits:** `a092be0`, `6ea519e` on `ch16-prose-rewrite`, pushed
- **Note:** Biber 2.19 cache corruption encountered; fixed by clearing PAR temp cache

### Session Work (Feb 24, 2026 late: House-style batch fixes from editorial reports)
- ✅ **All 9 editorial batch-fix tasks completed** across 16 chapter files (-64 lines net):
  - Em-dash → en-dash in epigraph attributions (11 files)
  - Backtick-tick quotes → `\enquote{}` (10 files)
  - Bare `*` → `\ungram` markers (6 files, 11 instances)
  - `\begin{exe}`/`\begin{xlist}` → `\ea`/`\z` in Ch 15
  - Capitalise sentence-initial it's/that's (4 files, 15 instances)
  - `\bigskip` removal (6 files, 32 instances)
  - `\citet` → `\textcite` standardisation (11 files, 68 instances)
  - Semantic macro fixes: `\emph{}` → `\term{}` for term introductions; `\textit{}` → `\mention{}` for linguistic forms (6 files, 10 instances)
  - "HPC kind" → "HPC category" in book's own voice (7 files, ~23 instances); kept "kind" in Boyd attributions and philosophical contrasts
  - Mechanical: Ch 4 grammar fix, Ch 2 table caption, Ch 14 LBE expansion, Ch 6 forward-reference tense (4 instances), Ch 4 `\term{Noun}` → `\term{noun}`
- ✅ **Decision:** Ch 15 stays in Part IV
- **Commit:** `20994a3` on `ch16-prose-rewrite`, pushed
- **Remaining editorial work:**
  - Ch 16 weak landing (second worked example, Ladyman & Ross, practical methodology)
  - Peirce earned-or-imposed audit (Chs 7, 9–14)
  - Discourse level missing from Ch 13 summary table
  - Stabiliser vs mechanism terminology consistency
  - Parallel Architecture paragraphs (Chs 1, 3)
  - Bold labels in prose (~40+ instances, Chs 6, 7, 8, 10, 13)
  - Peirce branch merge (`projectibility-pivot` → `ch16-prose-rewrite`)
  - Bib style-field normalisation

### Session Work (Feb 24, 2026 PM: Full editorial review + critical bug fixes)
- ✅ **16 chapter précis** written (parallel agents), 300-500 words each
- ✅ **Book-level editorial report** identifying 11 cross-chapter issues
- ✅ **16 chapter-level editorial reports** (deep reads, parallel agents)
- ✅ **Critical bugs fixed**:
  - Ch 12: removed spurious `[*]` from ~27 grammatical examples (was marking everything ungrammatical)
  - Ch 14: fixed Markdown `*emphasis*` → `\emph{}` (2 instances)
  - Ch 14: replaced undefined MMMG abbreviation (4 instances)
  - Ch 9: fixed `\\mention` double-backslash + deleted orphaned draft line
- ✅ **Structural additions**: Ch 8 coupling-coda framing, Ch 9 evidential gradient flag, Ch 16 research agenda (§16.7), CHAPTER_OUTLINE.md rewritten
- ✅ **Editorial followups tracker** created (`notes/precis/editorial-followups.md`)
- **Commit**: `53f0e12` on `ch16-prose-rewrite`
- **Next**: Batch house-style fixes (bold labels, backtick quotes, `\mention{}`, "HPC kind" → "HPC category", `\begin{exe}` → `\ea/\z`)

### Session Work (Feb 24, 2026: Figure/table audit + new figures)
- ✅ **Table/figure audit completed** (carried over from prior session):
  - Added cross-references to 16 previously unreferenced floats across 9 chapters
  - Relabelled `fig:10:decoupling` → `tab:10:decoupling` (tabular in figure env)
  - Renamed Ch 7 images from `6.*` to `7.*` prefix
  - Archived 17 orphaned images to `figures/archive/`
- ✅ **New Fig 13.1** (coupling-tightness spectrum): Gemini-generated four-panel image (crystalline→emergent-web), LaTeX label wrapper with small-caps coupling types and mediation axis. Placed before §13.1.
- ✅ **New Fig 16.1** (evaluation gauntlet): TikZ flowchart — three debts → gauntlet box (predictions + stress tests) → confirm/narrow/downgrade verdicts. Placed in §16.1 intro.
- ✅ **Phase-transition figure (Ch 3) reviewed**: Identified flat-honeycomb ice as chemically inaccurate. Attempted matplotlib replacement (saved as `3.phase-transition-v2.png`); visually not publication-grade. Parked — options: better Gemini prompt with crystallography instructions, Wikimedia CC composite, or leave as-is.
- ✅ **All committed** in `e7e503a` on `ch16-prose-rewrite` branch.
- **New files**: `figures/13.coupling-spectrum.png`, `notes/fig-13-coupling-spectrum-prompt.md`, `code/phase_transition_figure.py`, `figures/3.phase-transition-v2.png`

### Session Work (Feb 23, 2026: Ch 15 substantive revision)
- **Value proposition clarified**: Ch 15 explains why categories are *shared* (individual mechanisms don't explain community convergence). Social mechanisms complete the maintenance story.
- **Variationist calibration**: Honest about limits — HPC doesn't give variationists new empirical questions; it makes their implicit ontology explicit. Vindicates Milroy/Eckert mechanism requirement. Mechanism ablation prediction made explicit (network dissolution → dialect levelling).
- **Two-plus-overlap model**: Dialect (community) and register (activity) as two mechanistic dimensions; discourse community reframed as their convergence zone, not a third kind. Reflexive HPC paragraph added.
- **Ch 14 callbacks**: Register mismatch ≠ ungrammaticality (double-copula); grammaticality judgments as partly indexical products (§15.5 closing).
- **De-jargoned**: All Bayesian notation removed; O'Connor similarity-maximizing models passage simplified.
- **Protocol subsection (§15.4.1) cut**: Methods-manual voice; defeat test folded into preceding paragraph.
- **Pagination fixes (global, preamble.tex)**: Widow/orphan 10000→150; parskip 0pt→0pt plus 1pt; needspace sections 5→4, subsections 4→3. Net: 407→401 pages.
- **Stale transitions fixed**: Ch 10 was skipping Ch 11 (lexical categories) and pointing to Ch 12 (gender); Ch 12 was pointing backward to Ch 11 as "the final case study" instead of forward to Ch 13 (zipper); Ch 13 phoneme Object gloss tightened with "its value."
- **Commits**: `79d7a55`, `2fef3f0`, `bcfbb5b`, `3f00e36` on `ch16-prose-rewrite`

### Session Work (Feb 22, 2026: shared-bib cleanup tranche C completed)
- ✅ **All remaining duplicate-signature groups resolved** in shared `references.bib`:
  - Closed all 19 `possible_duplicate_record` groups with canonical-record consolidation.
  - Removed duplicate records and kept canonical metadata (including validated DOI/title fixes for high-ambiguity items).
  - Updated in-text cites to canonical keys where needed (`bybee2015`→`bybee1994`, `croft2001radical`→`croft2001`, `pickeringgarrod2004`→`pickering2004`).
- ✅ **Audit tooling improved**:
  - `code/audit_cited_bib.py` now resolves BibLaTeX `ids={...}` aliases, so cited-audit output reflects true Biber resolution behavior.
- ✅ **Verification pass completed**:
  - `latexmk -g hpc-book.tex` successful (existing non-fatal warnings unchanged).
  - `python3 code/audit_full_bib.py --bib references.bib --date 2026-02-22`: **770 entries, 2 info issues, 0 warnings, 0 duplicate-record groups**.
  - `python3 code/audit_cited_bib.py --bcf build/hpc-book.bcf --date 2026-02-22`: **292/292 cited keys resolved, 0 missing, 0 cited-entry warnings** (3 keys resolved via aliases).
  - Refreshed reports:
    - `notes/full-bib-audit-2026-02-22.md`
    - `notes/full-bib-audit-2026-02-22.json`
    - `notes/cited-bib-audit-2026-02-22.md`
- ⚠️ **Scope note**: tranche-C bib edits were made in the symlink target (`../../.house-style/references.bib`), not as tracked changes in this repo.

### Session Work (Feb 22, 2026: shared-bib cleanup tranche B completed)
- ✅ **All tranche-B warnings resolved** in shared `references.bib`:
  - Merged DOI-duplicate record groups using canonical keys plus alias preservation via `ids={...}`.
  - Normalized invalid year format (`Davies2008COCA`: `year={2008}` with status/access details moved to `note`).
  - Repaired required-field gaps by correcting entry types/fields:
    - `GelmanLoken2013` → `@unpublished`
    - `bechtel2005explanation` → `@article` with `journal`, `number`, `doi`
    - `baird2001` → `@mastersthesis` + `school`
    - `winter2002` → `@phdthesis` + `school`
- ✅ **Metadata sanity checks run** against Crossref for high-uncertainty items:
  - `10.1016/j.shpsc.2005.03.010`
  - `10.1177/0142723719869731`
  - `10.1017/9781009085748`
- ✅ **Verification pass completed**:
  - `latexmk hpc-book.tex` successful.
  - `python3 code/audit_cited_bib.py --bcf build/hpc-book.bcf --date 2026-02-22 --strict`: `292/292` cited keys resolved, `0` missing.
  - Biber case-mismatch warnings eliminated.
  - Updated full-bib state: **790 entries, 22 issues, 0 warnings** (down from 799/41/13 warnings after tranche A).
- ⚠️ **Scope note**: tranche-B bib edits were made in the symlink target (`../../.house-style/references.bib`), not as tracked changes in this repo.

### Session Work (Feb 22, 2026: shared-bib cleanup tranche A completed)
- ✅ **Case-collision normalization completed** in shared `references.bib`:
  - Removed duplicate case-variant keys for the same works (e.g., `Huddleston2002`, `Sperber1996`, `Haspelmath2010`, `Rosch1973`, `Rosch1975`).
  - Renamed the true non-duplicate collision pair key `Downing1996` to `downing1996propernames` to avoid key-space collision with `downing1996`.
- ✅ **In-repo citation updates** applied:
  - `chapters/chapter11.tex`: `Haspelmath2010` → `haspelmath2010`
  - `chapters/chapter15.tex`: `Sperber1996` → `sperber1996`
- ✅ **Verification pass completed**:
  - `latexmk hpc-book.tex` successful; no undefined-citation warnings.
  - `python3 code/audit_cited_bib.py --bcf build/hpc-book.bcf --date 2026-02-22 --strict`: `292/292` cited keys resolved, `0` missing, `0` cited-entry warnings.
  - Updated full-bib reports: `notes/full-bib-audit-2026-02-22.md` and `notes/full-bib-audit-2026-02-22.json`.
  - Full-bib state now: **799 entries, 41 issues, 0 case-collision groups** (down from 811 entries / 69 issues / 13 case-collision groups).
- ⚠️ **Scope note**: shared bib edits were made in the symlink target (`../../.house-style/references.bib`), not as tracked changes in this repo.

### Session Work (Feb 22, 2026: full shared-bib audit workflow)
- ✅ **Implemented full-bib audit tool**: `code/audit_full_bib.py` (full source integrity checks with suggestions).
- ✅ **Produced baseline reports**:
  - `notes/full-bib-audit-2026-02-22.md`
  - `notes/full-bib-audit-2026-02-22.json`
- ✅ **Current full-bib baseline** (shared `references.bib`):
  - 811 entries, 69 issues total
  - 13 case-collision key groups
  - 12 DOI-level duplicate-record groups
  - 1 non-standard year format (`2008--2025`)
  - 4 missing required fields
  - style-mix signals (`journal`/`journaltitle`, `year`/`date`, `address`/`location`)

### Session Work (Feb 22, 2026: cited-only BibTeX audit + citation resolution)
- ✅ **Resolved all currently missing cited keys** in full-book build:
  - Loaded local source in preamble (`\addbibresource{references-local.bib}`).
  - Added `eckert2008indexical` to `references-local.bib`.
  - Corrected key mismatches in chapter prose (`wiese2023grammatical` → `wiese2023`; `Reynolds2026` remapped to specific existing keys).
- ✅ **Implemented cited-only audit tooling**:
  - Added `code/audit_cited_bib.py` (reads citekeys from `build/hpc-book.bcf`, audits only cited entries).
  - Generated report: `notes/cited-bib-audit-2026-02-22.md`.
- ✅ **Verification complete**:
  - `latexmk hpc-book.tex` completed successfully.
  - `build/hpc-book.log` no longer reports undefined citations.
  - Audit result: `292/292` cited keys resolved, `0` missing.
- ✅ **Bibliography hygiene follow-through completed**:
  - Cited-entry metadata warnings resolved (date-only entries normalized with explicit `year`; `forthcoming` year fields converted to integer year plus `note`).
  - Audit parser hardened to ignore commented-out BibTeX stubs and accept `date`/`journaltitle` when auditing cited records.
  - Updated audit result: `292/292` cited keys resolved, `0` missing, `0` cited-entry warnings, `0` duplicate keys in loaded sources.
- ⚠️ **Remaining upstream bib noise (outside cited-only scope)**:
  - Biber still reports 13 case-mismatch key pairs in shared `references.bib` (e.g., `huddleston2002`/`Huddleston2002`).

### Session Work (Feb 22, 2026: Ch 16 gauntlet finalization + board loop)
- ✅ **Ch 16 rebuilt as a true gauntlet**: risky predictions, explicit falsifiers, serious-downgrade criterion, and operational thresholds consolidated in `chapters/chapter16.tex`.
- ✅ **Running case hardened** (`\mention{data}`): diagnostics now aligned to Ch 9 framing (agreement + tight/loose packaging + anchoring recession) rather than generic variation talk.
- ✅ **ABM evidentiary discipline aligned to Ch 7/9 updates**: Ch 16 now states that didactic ABMs are mechanism sketches; defeat claims must rely on replicated corpus/behavioural data, with seed distributions and ablation controls treated as internal checks.
- ✅ **Review-board cycle completed**:
  - `notes/board-report-ch16-2026-02-22.md` (revamp board synthesis)
  - `notes/board-report-ch16-post-revision-2026-02-22.md` (post-revision readiness verdict)
- ✅ **Build verification**: repeated `latexmk hpc-book.tex` runs successful; pre-existing repo warnings remain (multiply-defined label, missing glyph).
- ✅ **Pushed commits**:
  - `f7eff65` Ch 16 gauntlet revisions + board follow-up
  - `6b626da` Ch 16 ABM criteria alignment with Ch 7/9

### Session Work (Feb 22, 2026: Ch 7/9 ABM robustness pass)
- ✅ **Chapter 7 ABM refinement**: explicit 20-seed robustness summary and clearer calibration limits for the volcanic-island toy model.
- ✅ **Chapter 9 ABM refinement**: scaling-control clarification, 20-seed distributional summaries, and freeze-learning control added to reinforce mechanism-claim discipline.

### Immediate
1. Normalize remaining style-mix fields (`journal`/`journaltitle`, `address`/`location`) in shared `references.bib`.
2. Run a targeted overfull/underfull pass on high-visibility tables/figures in Chs 9, 13, and 16.
3. Optional tooling follow-up: add `bibtexparser` to local env or make `code/validate_bib.py` fallback-compatible.

### Session Work (Feb 20, 2026 evening: Ch 11 + Ch 8 + Ch 9 polish with Brett)
- ✅ **Ch 11 HPC-consistency pass**: Fixed "semantics comes along for the ride" (essentialist smuggling → coupling framing); rewrote compressed Reynolds 2024 paragraph for accessibility; /w/ → /hw/ (Brett's dialect); "wh-in-situ" → "languages where IRE words remain in situ"; maintenance-only paragraph → maintenance + projection profiles; Ch 12 transition rewritten (morphological gender absence → pro-form diffusion); "adjective" carving: epistemologically and ontologically distinct, terminologically identical; "at least three" categories for *who*; dropped redundant Ch 12 forward reference
- ✅ **Ch 8 structural fix**: Moved curtain line ("Categories generate habits; classes are merely named") from §8.7 to actual chapter end after §8.9 coupling coda. Added "Two tools make them operational" transition.
- ✅ **Ch 9 tricolon**: LEGO opening reordered (law, money, style guide) for bathetic punchline
- ✅ **Bib cleanup**: Deleted duplicate `reynolds2024` entry; citation now uses `reynolds2024why`
- ✅ **Coupling vs braiding**: Confirmed as distinct concepts (form-meaning poles vs mechanism convergence). Both terms stay.

### Session Work (Feb 20, 2026: Ch 11 Review Board + Polish)
- ✅ **Six-reviewer board** (Bybee, Tomasello, Croft, McCloskey, Chater, Zimmer): 24 edits from convergent criticisms (type/token frequency, structural analogy qualification, Baker grant-before-take, constructional thickness, IRE cross-linguistic caveat, lyrebird mapping, HPC-vs-definitional disconfirmation)
- ✅ **Structural rhetorical figures** (9): epistrophe, gradatio, anadiplosis, inclusio, isocolon, diacope, anadiplosis cycle, antithesis, ring composition (Wallace callback)
- ✅ **Selective humor** (10 of 26 evaluated): "wrong enough to be interesting" opener, "embarrassingly practical" deflation, "nobody will be harmed", "drawer not theory", "doing no work whatsoever", "English declines to issue a ruling", "family colours", lyrebird caption, table caveat
- ✅ **Ch 11 complete**: 6 sections (Intro, Skeleton, Thin, Wastebasket, Braid, Looking Forward). Not final-final, but put to bed.

### Session Work (Feb 19–20, 2026: Ch 11 §11.4–§11.5 + Ch 13 Architecture)
- ✅ **§11.4 (Adverbs) polished**: reynolds2024 integrated, grammar-teaching sociology, Penn Treebank claim fixed, meta-HPC typological grounding (Rijkhoff 2007)
- ✅ **§11.5 (Pronouns/Mimics) drafted**: Two-faced cluster (syntactic + semantic), core personal pronouns + Ch 12 gender connection, three saturation routes, IRE words coined, braiding conclusion
- ✅ **Terminology hardened**: category vs. class vs. label; no "kind"; wh- = phonology not morphology; "participates in the system of case"
- ✅ **Anti-essentialist discipline**: Multiple essentialist gatekeepers caught and fixed
- ✅ **Ch 13 restructuring decided**: Coupling concept as Ch 8 coda, Ch 13 as synthesis chapter. Analysis in `notes/ch13-restructuring-analysis.md`. Status: "try"

### Session Work (Feb 19, 2026: Sync Conflict Resolution)
- ✅ **Major Sync Conflict Resolved**: 
  - Identity 130 duplicate files (e.g., `chapter11 2.tex`, `.git/refs/heads/master 2`) caused by iCloud sync error.
  - Automated diff verification: 129 project files were identical; 3 git metadata files were stale pointers to Dec 2024.
  - All duplicates deleted from filesystem and `.git` internal structure.
- ✅ **Repository Health**: 
  - Restored `chapters/chapter15.tex` and `notes/chapter15_planning.md` from Git (missing from disk).
  - Deleted stale/partial `literature2` folder.
  - `git status` now clean; "U" markers removed from explorer.
- ✅ **Documentation Update**: `PROJECT_STATUS.md` and session logs back-filled for Feb 15-17 gap.
- 🔄 **Chapter 11 Reset**: Archived old draft and starting fresh to better align with HPC maintenance framing.

### Session Work (Feb 17, 2026: Nefdt Response Analysis)
- ✅ **Nefdt (2025) Analysis**: Conducted deep-dive into "real patterns" and linguistic communities.
- ✅ **Synthesis**: Compared Nefdt's structuralism extension to metasemantics with HPC maintenance view. Outlined response strategy focusing on overgeneration and grounding.

### Session Work (Feb 16, 2026: Multi-Agent Peer Review)
- ✅ **Review Simulation**: Dispatched 6 independent LLM agents (personas: expert to outsider) to simulate peer reviews for tree independence polynomials / network motifs paper.
- ✅ **Revision**: Revised paper based on round 1 feedback; evaluated in round 2.

### Session Work (Feb 15, 2026: Mode-Mean Bound & Cluster Slack)
- ✅ **Mode-Mean Bound**: Integrated computational evidence and investigation findings into the manuscript.
- ✅ **Cluster Slack Hypothesis**: Derived rigorous proof using hard-core recurrence relation to bound cluster load $\le |C_v|/3$.

### Session Work (Jan 31, 2026: Reviewer Synthesis)
- ✅ **Feedback Synthesis**: Consolidated critiques from Peirce, Plato, and Aristotle personas. Prioritized revisions to address core philosophical grounding and argument marginal gains.

### Session Work (Jan 23, 2026: Formal Architecture Reconciliation)
- ✅ **Architecture Refined**: "Six components" reframed as diagnostic failure modes.
- ✅ **Variables established**: Three constitutive variables + dynamics (HPC energy function $E(\omega;u,c)$).
- ✅ **Dynamics**: discrete-time Bayesian/Beta update established as primary model.
- ✅ **Chapter 15 Substantially Expanded** ("The Social Stabilization of Kinds"):
  - **Dialect subsection**: Added Halliday 1978 "variety according to user", Labov's "orderly heterogeneity" with AAVE example, HPC resolution (boundaries ontologically sharp but epistemically inaccessible per Ch 5)
  - **Register subsection**: Added Halliday's field/tenor/mode, Biber 1988 multidimensional analysis, HPC resolution (registers as attractor basins maintained by gatekeeping)
  - **Discourse Community subsection**: Added Swales 1990 definition and six criteria, HPC resolution (communities as latent mixture components, coordination equilibria)
  - **New "Conditioning Structure" subsection**: Synthesizes three mechanisms as unified conditioning structure (dialect=persistent parameterization, register=situational conditioning, community=mixture component)
- ✅ **Bibliography entries added** (all verified via web search):
  - `halliday1978` – *Language as Social Semiotic*, Edward Arnold
  - `biber1988` – *Variation across Speech and Writing*, CUP
  - `swales1990` – *Genre Analysis*, CUP
- ✅ **Build verified**: 379 pages, compiles cleanly
- **Key decision**: Gradience is within categories; boundaries are ontologically sharp but epistemically inaccessible

### Session Work (Jan 20, 2026: Chapter 15 Creation & LBE Integration)
- ✅ **New Chapter 15 Created** ("The Social Stabilization of Kinds"):
  - Split from Part IV to give "Varieties as Conditioning" its own chapter.
  - Core argument: Variation is a latent mixture; varieties are the stabilizers.
  - Old Chapter 15 ("Nominalist Challenge") moved to Chapter 16.
  - `hpc-book.tex` updated to include `chapter15.tex` and `chapter16.tex`.
- ✅ **LBE Integrated** (Reynolds 2026):
  - **Ch 8**: "Left Branch Gap" added as Negative Diagnosis case study.
  - **Ch 13**: $k=4$ packaging tightness added as evidence for coupling strength.
  - **Ch 14**: Satiation resistance added to Entrenchment section.
- ✅ **Infrastructure**:
  - `STATUS.md` updated to reflect 16-chapter structure.
  - `task.md` maintained.

### Session Work (Jan 16, 2026: Chapter 13 Empirical Integration)
- ✅ **Chapter 13 Enhanced ("The Stack")**: Integrated empirical content from new stack paper (`literature/main.pdf`)
  - **Hook**: Explicit two-diagnostic framework (projectibility + homeostasis as independent tests) added to §13.1
  - **Phonemes**: Added PHOIBLE cross-linguistic signatures (inventory clustering, /y/ scaling) to §13.2
  - **Morphemes**: Added HistWords persistence analysis (high-drift adjectives) to §13.3
  - **Constructions**: Added *or even* cross-corpus transfer evidence & ablation signatures to §13.4
  - **Negative Cases**: Refined academic register/polysynthetic failure modes
  - **Citations**: Added `ekstrom2025` (Phoneme as Cognitive Tool) & `hamilton2016` (Diachronic Word Embeddings)
- ✅ **Verification**: 
  - Compilation successful (357 pages)
  - Pre-existing missing citations identified (`stevens1989`, `lindblom1990` etc.) - to be fixed
- **Status**: Chapter 13 now empirically grounded; narrative structure intact.

### Session Work (Jan 13, 2026: House Style Enforcement)
- ✅ **langsci-gb4e format corrected** in style documentation:
  - `.house-style/style-guide.md`: Fixed Numbered Examples section to show correct `\ea[]{}` bracket-brace syntax
  - `.house-style/style-rules.yaml`: Updated examples commands and judgments
  - **Correct format**: `\ea[JUDGMENT]{\label{ex:name}\mention{example text}}` with `\z` to close
  - Judgment markers (`\ungram{}`, `\marg{}`, `\odd{}`) go in square brackets
- ✅ **Chapter 13 examples converted** from linguex-style `\ex.` to langsci-gb4e:
  - `\label{ex:letalone}` — let-alone grammatical
  - `\label{ex:letalone-bad}` — let-alone ungrammatical  
  - `\label{ex:ditransitive}` — ditransitive subexamples
- ✅ **Committed and pushed**: `e646867` on `restructure-part-1`

### Session Work (Jan 8, 2026: Chapter 12 Polish)
- ✅ **Chapter 12 substantially revised** ("Pro-form Gender"):
  - Demonstratives (*this*/*that*) reanalyzed as constructionally-conditioned (new §12.6.5)
  - Table 12.1 footnote added for demonstratives
  - French/English coherence comparison added
  - Capstone sentence: "This coupling is the category we recognize as English gender"
  - Mechanism claims softened (incomplete list acknowledged)
  - Singular-they alignment example added (generational norm conflict)
  - Prediction: *it* for infants may wane as singular *they* spreads
  - *Much* observation added (count/mass interface with personhood)
  - Terminology fixed for Ch5 consistency ("instability" not "graded membership")
  - House style enforced (contractions, dashes, `\ungram{}` markers)
- ✅ **Chapter 5 fixes**: Resolved `sec:5:testing-stability` and `fig:iterated-learning` undefined refs
- ✅ **Snapshot saved**: `snapshots/hpc-book-2026-01-08-ch12-polish.pdf`
- **Status**: Chapter 12 stable; ready for next chapter

### Session Work (Dec 31, 2025: Literature Integration & Mechanisms Expansion)
- ✅ **Three new papers integrated** (Raviv 2019, Wolters 2024, Koriat 2017):
  - Added to `references.bib` with verified DOIs
  - Analysis notes filed: `notes/new-literature-2025-12-31.md`
  - Integrated citations into Chapter 4:
    - Koriat 2017 (cue-sampling model) → supports HPC view of categorization
    - Wolters 2024 (Zipfian distributions) → input structure as stabilizer
    - Raviv 2019 (compositionality without transmission) → alignment as mechanism
- ✅ **Chapter 7 expanded** with additional mechanisms paragraph:
  - Analogy, Standardisation, Indexicality, Error-and-repair, Creativity
  - Aligns book with fuller inventory in Labels_to_Stabilisers paper
- ✅ **Hoeksema (2012) citation refined** in Chapter 6:
  - Added page number (p. 30) for "twelve distinct licensing patterns" claim
  - Changed "at least twelve" → "twelve" for precision
- ✅ **Chapter 4 wording adjusted**:
  - "a fuller picture" → "a more detailed treatment" (re: Ch 7 mechanism coverage)
  - Fixed jarring Koriat→Ambridge transition with bridging sentence
- ✅ **Root folder tidied**: Build artifacts moved to `build/`

### Session Work (Dec 27, 2025: Kim Correspondence)

- ✅ **Jong-Bok Kim feedback received** on definiteness/deitality chapter
  - Endorses two-cluster separation (SYN[DEITALITY...] + SEM[DEFINITENESS...])
  - Favors construction-internal constraints over lexical listing
  - Korean evidence: demonstratives don't compete with bare NPs + topic (supports HPC prediction)
  - On grammaticality: "licensing-based theory has no clear distinction between ? and ??" - useful for Ch 14 MMMG argument
  - Filed: `correspondence/kim-jongbok-2025-12.md`
  - Cross-referenced in: `countability/NOTES.md`

### Session Work (Dec 26, 2025: Ch 12 Draft + Glossary)
- 🔄 **Chapter 12 First Draft** ("Gender and the Maintenance Spectrum"):
  - Ship/table hook contrasting live vs. dead gender
  - Three cases: English (tuning fork), French (ID card), German (conflict zone)
  - Maintenance spectrum table (transparent → entrenched)
  - Implications: singular *they*, typological distinction, neural architecture prediction
  - **Status**: Rough draft; may restart from scratch
- ✅ **Glossary Redone** (`glossary.tex`):
  - 50+ entries with consistent microstructure (definition → mechanism → diagnostic → note → see-also)
  - Murray epigraph (OED Vol. 1)
  - Covers core framework + chapter-specific terms (countability, definiteness, deitality)

### Session Work (Dec 24, 2025: "The Field-Relativity Breakthrough")
- ✅ **Field-Relative Projectibility** principle established as a core book lens:
  - Projectibility is indexed to analytical purpose (semantics vs. syntax vs. phonology).
  - Proper noun (syntax) vs. proper name (semantics) as prime example.
  - Resolves "fat category" issues by recognizing multiple overlapping HPCs.
- ✅ **HPC Slogan** finalized through tripartite analysis:
  - *"A category is a profile, stabilised by mechanisms, projectible relative to purposes."*
  - Developed through "Tabarok critique" (avoiding market-mechanic framing).
- ✅ **Advisory Board Consultation** (Round 2: 10 reviewers):
  - Integrated feedback from Boyd, Millikan, Goldberg, Rosch, Khalidi, Tomasello, Bybee, Sperber, Fedorenko, Zimmer.
  - "Tomato Hook" (Botanist vs. Chef) established as opening phenomenological bridge.
  - "Relative to purposes" wording chosen to avoid teleological/voluntarist misreadings.
- ✅ **Chapter 6 Revision Implemented**:
  - Added HPC slogan subsection (~200 words) near chapter opening.
  - Added new "Field-Relative Projectibility" section (~1,000 words) with:
    - "Tomato Hook" (botanist vs. chef) for lay-accessibility.
    - Proper noun/name example with table.
    - Part III preview (Ch 9, 10, 11).
    - Three-check discipline (cluster, homeostasis, projectibility).
  - Threaded field-relativity through interest-relativity and degrees sections.
  - Added closing transition forward-referencing Part III.
- ✅ **CLAUDE.md Updated**:
  - Added "Intellectual Engagement" section (methodology for deep theoretical work).
  - Added new project structure entries (hpc-book.tex, code/).
## Status Update (2026-01-17)

### Session Work (Jan 17 evening): Chapter 9 ABM Implementation
- ✅ **Countability ABM Created** (`code/countability_abm.py`, ~1300 lines):
  - Didactic mechanism sketch (explicit: intuition pump, not evidence)
  - Agents with individuation confidence per noun
  - Constructions as "locks" with tolerance thresholds (tight to loose)
  - Bidirectional inference, entrenchment, functional anchoring, generational turnover
  - Mass construction (MUCH) with proper licensing
- ✅ **Five Experiments Implemented**:
  - Baseline hierarchy (implicational matrix matches Table 9.1)
  - Data drift (tight-before-loose erosion, emergent not forced)
  - Functional anchoring (cattle stable with cow available)
  - Prescriptivism (LEGO campaign dynamics)
  - Folks instability (inter-speaker variation)
- ✅ **Stress Test Added** (mechanism ablation):
  - Proves results aren't tautological
  - Disabling entrenchment/anchoring/learning changes outcomes
- ✅ **Visualizations Generated**:
  - `data_drift_experiment.png`, `prescriptivism_experiment.png`, `count_basin_visualization.png`
- **Status**: ABM complete; ready for optional integration into Ch 9 prose

### Completed (earlier Jan 17)
- **Cover Page Fixed**: Reinstated absolute positioning by reverting conflicting `gb4e` move and adding `\null` shipout fix. Verified clean PDF build.
- **Chapter 13 Empirical Depth**: Integrated PHOIBLE 2.0 (**moran2019phoible**) and Mark Baker (**baker1996**) evidence into §13.4.
- **Infrastructure Stability**: Resolved `headheight` warnings in `preamble.tex`.
- **BibTeX Audit**: Verified `stevens1989` and `lindblom1990` are correctly cited and present in `references.bib`.

### In Progress
- **Index Analysis**: `analyze_index.py` is ready for implementation/execution for Chapters 13 & 15.

### Next Actions
- [ ] Integrate LBE paper into Chapters 8, 13, and 14.
- [ ] Final polish of Chapter 13 narrative flow.
- [ ] Review Chapter 14 stubs.
### Session Work (Dec 25, 2025: Slogan Deployment & Ch 10 Planning)
- ✅ **Slogan Deployment**: Implemented the "buried payoff" slogan arc:
  - **Ch 4**: First appearance (~lines 197–199) as payoff to HPC explanation.
  - **Ch 6**: Dialed back to inline reference ("Unpacking the framework").
  - **Ch 7**: Front-loaded restatement after epigraph.
  - **Ch 14**: "Transformed return" note added to grist.
  - **House Style**: Standardized spelling to *stabilized* (z-spelling) across 17 files.
- ✅ **Chapter 10 Planning**:
  - Ran 17-agent **Advisory Board Review** (Khalidi, Latour, Croft, etc.).
  - Generated `notes/ch10-board-report.md` (full multi-perspective critique).
  - Integrated insights into `notes/chapter10-grist.md` (drafting spine established).
  - Created reproducible script `scripts/ch10-board-review.sh`.
- ✅ **Chapter 10 Drafted and Revised**:
  - Full 11-section chapter (~6,000 words): Hook → Two Functions → Definiteness Cluster → Form Cluster → Coupling → Five Mechanisms → Slippage → Tests → Deitality → Cross-Linguistic → Looking Forward
  - **Millikan proper-function framework** integrated (§10.5): proper function, Normal conditions, derived functions, parasitism
  - **Definiteness acquisition evidence** added (§10.3): familiarity → uniqueness → identifiability sequence (brockmann2018, keysar2000, decat2011)
  - **Three-agent feedback** addressed: BrE hospital error fixed, 'deitality' introduced earlier, weak-definite productivity acknowledged, Boyd's falsification diagnostic added, Gasparri paragraph expanded with Dupré's 'social-practice-unified collections'
  - **Funes epigraph** (Borges) integrated with callback in Generic Definites section
  - **Rhetorical audit** completed (McCloskey 'disciplinary judo' applied to all 10 chapters)
- ✅ **Citations Verified**:
  - brockmann2018 (SuB 22), keysar2000 (Psych Sci), decat2011 (J Child Lang), dupre1993 (Harvard UP), gasparri2025 (J Semantics)
- ✅ **Docs Updated**:
  - `notes/project-log.md` updated.
  - `task.md` reset for Ch 10 drafting phase.

### Session Work (Dec 25, 2025 afternoon: Ch 10 Refinements)
- ✅ **ChatGPT Feedback Addressed**:
  - Fixed typos (deictic, \\mention)
  - Added cross-linguistic developmental evidence sentence
  - Added Birner & Ward 1994 citation, updated De Cat 2011 → De Cat 2013
  - Hedged Keysar claim (71% Director Task, not 20-30%)
  - Added table footnote for narrative-*this* exception
- ✅ **Structural Rhetorical Figures Deployed**:
  - Antimetabole: "Definite without the article; the article without definiteness"
  - Gradatio: developmental sequence as cognitive climb
  - Isocolon: binding mechanisms parallel structure
  - Sorites: convergence inferential chain
  - Anaphoric template: "X looks like a failure of Y" across slippage subsections
- ✅ **Harris/Joseph Synthesis Implemented**:
  - Harris: "Positions on the board" typology (4 competing accounts)
  - Harris: Decision criterion paragraph (forced-choice moment)
  - Joseph: Historiographic note on definiteness conflation
  - Joseph: Widened genealogy (grammar/pedagogy/typology)
  - Joseph: Greek proper-name counterpattern
- ✅ **Khalidi Looping Effects**: Metalinguistic feedback sentence added to mechanisms interlock
- ✅ **Definiteness Cluster Consistency Fix**: 3 core properties + anaphoric recoverability as downstream
- ✅ **New Bib Entries Verified**: heim1991, christophersen1939, roberts2003, decat2013, birnerward1994
- ✅ **Chapter 10 Final Polish**:
  - **Conclusion Punched Up**: Tight/loose/scarce coupling arc established (§10.11)
  - **Rhetorical Audit**: Ticks removed (intensifiers, repetitive openers)
  - **Historical Precision**: Russell/definiteness conflation paragraph refined (avoiding "the" formalization claim)
  - **Build**: Verified successful compilation
- ✅ **Chapter 10 Visualizations**:
  - **Decoupling Figure (Fig 10.1)**: 2x2 grid in §10.2 showing Core vs. Decoupled items.
  - **Derived Functions Figure (Fig 10.2)**: TikZ flowchart in §10.5 showing historical path vs. functional parasitism.
  - **Diagnostics Table (Table 10.1)**: Refined with grouping headers (Core/Mixed/Non-members).

### Session Work (Dec 25, 2025 evening: Typography + Ch 11 Planning)
- ✅ **Bringhurst Typography Refinements**:
  - Section headings: small-caps with marginal numbers
  - Subsection headings: italics with marginal numbers
  - `\mentionhead{}` macro for linguistic mentions in headings (math-mode angle brackets)
  - `\abbr{}` macro: letterspaced small-caps via fontspec
  - Block quotations: quoting package (same size, indented)
  - Microtype protrusion enabled
  - Document class: removed a4paper (geometry controls size)
  - All heading mentions updated to use `\mentionhead{}`
- ✅ **Epigraph Consistency**: All 5 epigraphs standardized (em-dash before attribution, dates added)
- ✅ **Full Book Build**: 285 pages, 51MB PDF verified
- ✅ **Chapter 4 Title Fixed**: "Categories without essences" (not "Kinds")
- ✅ **Colophon Fixed**: Georg Duffner (not Mayr-Duffner) for EB Garamond
- ✅ **Chapter 11 Implementation Plan Created**:
  - Read all 32 files in `notes/ch11/` (25+ advisor feedback files)
  - **Three-act structure approved**: Wastebasket → Skeleton → Mimics
  - **Shark/Dolphin/Ichthyosaur metaphor approved**: convergent evolution for mechanism-braiding
  - **Wallace epigraph approved** (1867 mimicry quote)
  - Title: "Lexical categories and their maintenance"
  - Scope framing: four major classes + pronouns; functional categories deferred
  - §11.4 (Adjectives) fully developed with mechanism table
  - Field-relative projectibility integrated into summary section
  - Target: ~6200 words, 8 sections
  - Plan saved to `notes/ch11/ch11-implementation-plan.md`
- ✅ **CHAPTER_OUTLINE.md Updated**: Ch 11 entry revised with new title and key points

## Completed

- ✅ Project repository initialized with Git
- ✅ `.gitignore` configured for LaTeX/academic project
- ✅ README.md with project overview
- ✅ Synopsis finalized (~880 words)
- ✅ Core thesis articulated (HPC kinds for linguistic categories)
- ✅ 15-chapter structure (4 parts: Problem, Fix, Categories, Implications) — gender chapter added Dec 26
- ✅ House style guide established (`.house-style/style-guide.md`)
- ✅ LaTeX preamble with custom macros (`.house-style/preamble.tex`)
- ✅ Bibliography system (BibTeX with Biber backend)

### Part I: The Problem (Chapters 1-3)
- ✅ **Ch 1**: Words That Won't Hold Still - drafted and revised
- ✅ **Ch 2**: Essentialism and its Discontents - drafted and revised
- ✅ **Ch 3**: What We Haven't Been Asking - drafted and revised

### Part II: The Fix (Chapters 4-8)
- ✅ **Ch 4**: Homeostatic Property Clusters - drafted and revised
- ✅ **Ch 5**: Discrete from Continuous - drafted and revised
- ✅ **Ch 6**: Projectibility and the Good Bet - drafted and revised
- ✅ **Ch 7**: The Stabilisers - drafted and revised (quotatives case study)
- ✅ **Ch 8**: Failure Modes - drafted (thin/fat/negative taxonomy)

### Part III: Categories Reconsidered (Chapters 9-14)
- ✅ **Ch 9**: Countability - drafted and refined (LEGO/emoji hooks, cross-linguistic section)
- ✅ **Ch 10**: Definiteness - complete and audited (Dec 25, 2025)
- ✅ **Ch 11**: Lexical Categories - complete (Feb 20, 2026). Six sections, review board, rhetorical polish.
- ✅ **Ch 12**: Gender and the Maintenance Spectrum - drafted (Dec 26), polished (Jan 8). Ship/table hook, transparent→entrenched spectrum, English/French/German cases.
- ✅ **Ch 13**: Sign-language discourse reference - drafted and revised as a modality stress test for the Part III diagnostics.
- ✅ **Ch 14**: The category zipper - drafted and revised as Part III synthesis across the coupling gradient.

### Session Work (Dec 15-16, 2025)
- ✅ Terminology standardized: "linguistic categories" throughout (Chs 2, 3, 5)
- ✅ Ch 13 theoretical framework developed:
  - MMMG (Morphosyntactic-Meaning Model of Grammaticality)
  - CP/effect-space analysis (why phonemes don't carry propositional meaning)
  - Information-theoretic framing (Shannon mutual information, Kolmogorov complexity)
  - Turkish vowel harmony as key evidence
  - "A orange" edge case analysis (allomorphy, not phonotactics)
- ✅ Notes consolidated:
  - `chapter13-master.md` — quick-reference theoretical framework
  - `chapter13_planning.md` — structural planning (double-copula vignette)
  - `morphosyntax-systematicity-zone.md` — comprehensive deep-dive (~8,700 words)
- ✅ Ch 5 TODO added: synchronic terrain warping (context shifts basin boundaries)
- ✅ CxG foundational arguments notes created

### Session Work (Dec 17, 2025)
- ✅ Scott-Phillips 2025 (byproduct hypothesis) integrated:
  - Ch 7 Table 7.1: optimal relevance as forcing function
  - Ch 8: methodological caution about acceptability judgments
- ✅ Fedorenko 2024 papers integrated:
  - "Language network as natural kind" → Ch 4 (neural evidence for HPC)
  - "Communication rather than thought" → Ch 7 (dissociation confirms communicative forcing function)
- ✅ Advisory board consultations (4 agents each) for both papers
- ✅ Build workflow fixed: `latexmk` now recommended for `build/` output
- ✅ Bib entries updated/added for new citations

### Session Work (Dec 20, 2025)
- ✅ Chapter 11 grist developed:
  - Deixis/anaphor/interrogative theoretical discussion
  - Mechanism-braiding insight: semantic redundancy → syntactic distribution
  - Focus-modifier squib sparked parallel project
  - Pro-form as semantic category — cross-reference to `reynolds2025proform`
- ✅ Pro-form gender paper (`literature/pro-form_gender.tex`) integrated as Ch 11 source
- ✅ Bib entry added: `reynolds2025proform` (manuscript in preparation)
- ✅ `notes/chapter11-grist.md` created with clustering tables and mechanism analysis

## Current Phase

**All 18 chapters drafted**. Book is now in revision/polish phase.

### Outstanding structural work
- Peirce integration on `projectibility-pivot` branch (Chs 7, 9-14 touched; not yet merged)
- Remaining visualizations and figures
- Review-board passes for chapters that haven't had them
- Bib style-field normalization (`journal`/`journaltitle`, `address`/`location`)

## Key Decisions Made

1. **Quotatives case study** selected for Ch 7 (cross-linguistic, recent data)
2. **O'Connor integration** for Ch 8 (payoff vs property distinction)
3. **Madagascar analogy** for grain-of-analysis problem
4. **Two-Diagnostic Test** framework (projectibility + homeostasis)
5. **PDF naming convention**: Match BibTeX keys exactly

## Key Files

- `chapters/chapter01.tex` through `chapter08.tex` - Main chapter files
- `notes/CHAPTER_OUTLINE.md` - Authoritative chapter structure
- `notes/chapter07-master.md` - Consolidated Ch 7 notes (pattern for other chapters)
- `notes/chapter08-master.md` - Ch 8 failure modes notes
- `notes/oconnor-and-hpc-levels.md` - O'Connor engagement and grain-of-analysis
- `literature/stack.tex` - Standalone paper manuscript (HPC stack)
- `synopsis.md` - Book synopsis

## Recent Session Work (Dec 11, 2025)

### Citation Refinement
| Chapter | Citation | Added |
|---------|----------|-------|
| 1 | `huddleston2002` | `[ch.~1]` |
| 3 | `spike2020` | `[13--15]` |
| 3 | `dahl2016` | `[435--436]` |
| 4 | `millikan1984` | `[ch.~1]` |
| 4 | `craver2009` | `[575]` |
| 5 | `kirby2008` | `[10681]` |
| 6 | `favier2021` | `[Table~2]` |
| 8 | `miller2021` | `[25--26]` |

### Verbatim Quotations Added
- **Millikan 2017 p. 17** (Ch 4): Self-maintaining kinds depleting resources
- **Craver 2009 p. 575** (Ch 4): "Kind concepts cut nature at its joints"
- **Kirby 2008 p. 10681** (Ch 5): "invisible hand" process

## Research Questions Addressed

- ✅ What are the specific mechanisms for linguistic categories? (Ch 7)
- ✅ How do we empirically test for homeostasis? (Ch 7 robustness tests)
- ✅ What are the clearest failure cases? (Ch 8 thin/fat/negative)
- ✅ How does this interact with formal/computational approaches? (Ch 8 criteria)
- ✅ What predictions does HPC make that essentialism doesn't? (Ch 6, 7)

---

*This is a living document. Update regularly as the project progresses.*

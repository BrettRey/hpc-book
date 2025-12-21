# Project Log

## Progress Tracker

> **Last updated:** 17 December 2025  
> **Data source:** Git commit history (`git log --date=short`)

### Chapter Timeline

| Chapter | Title | Started | Peak Activity | Status | Lines |
|---------|-------|---------|---------------|--------|-------|
| **1** | Words That Won't Hold Still | Nov 29 | Nov 30 (79 commits) | ✅ Complete | 257 |
| **2** | Essentialism and Its Discontents | Dec 1 | Dec 1–6 | ✅ Complete | 330 |
| **3** | What We Haven't Been Asking | Dec 3 | Dec 5 (7 commits) | ✅ Complete | 236 |
| **4** | Kinds Without Essences | Dec 4 | Dec 5 (30 commits) | ✅ Complete | 311 |
| **5** | Dynamic Discreteness | Dec 4 | Dec 5 (22 commits) | ✅ Complete | 461 |
| **6** | Projectibility | Dec 4 | Dec 6–7 (70 commits) | ✅ Complete | 255 |
| **7** | Stabilisers | Nov 30 | Dec 9 (73 commits) | ✅ Complete | 625 |
| **8** | Failure Modes | Dec 10 | Dec 13 (7 commits) | ✅ Complete | 374 |
| **9** | Countability | Dec 13 | Dec 14 (23 commits) | ✅ Complete | 415 |
| **10** | Definiteness | — | — | 📌 Stub | 4 |
| **11–14** | (Part III–IV) | — | — | 📌 Stub | — |

### Daily Activity Log

| Date | Commits | Key Work |
|------|---------|----------|
| **Nov 29** | ~5 | Project folder created; Ch 1 initial draft |
| **Nov 30** | 80+ | Ch 1 massive polish; Ch 7 stub created |
| **Dec 1** | ~15 | Ch 2 drafted and refined |
| **Dec 2** | ~5 | Ch 2 continued polish |
| **Dec 3** | ~10 | Ch 3 drafted; Part I restructuring |
| **Dec 4** | ~10 | Ch 4/5/6 initial work; stubs for 8–14 |
| **Dec 5** | 60+ | Ch 4 (30), Ch 5 (22), figures added |
| **Dec 6** | 25+ | Ch 6 (21), Ch 7 starts (4) |
| **Dec 7** | 60+ | Ch 6 (49), Ch 7 (9) intensive work |
| **Dec 8** | 35+ | Ch 7 (31), transition day |
| **Dec 9** | 75+ | Ch 7 massive expansion (73 commits) |
| **Dec 10** | 10+ | Ch 7 final polish; Ch 8 drafted |
| **Dec 11** | 20+ | Citation pass across all chapters; Ch 8 revisions |
| **Dec 12** | 5+ | Ch 8 major revisions; cross-reference audit |
| **Dec 13** | 25+ | Ch 8 final polish; Ch 9 drafted; Précis created |
| **Dec 14** | 25+ | Ch 9 restructuring and calibration; handoff prep |
| **Dec 15** | 5+ | Scope widened to linguistic categories; CxG connection notes |
| **Dec 16** | 10+ | Ch 13 theory framework (MMMG, CP analysis, info-theory); notes consolidation |
| **Dec 17** | 5+ | Scott-Phillips + Fedorenko integration; advisory board consultations; build workflow fix |

### Velocity Observations

- **Fastest drafts:** Ch 1 (1 day), Ch 2 (1 day), Ch 4/5 (same day)
- **Most intensive:** Ch 7 — 128 total commits over 5 days
- **Average chapter:** ~2 days drafting + 1–2 days polish
- **Total project span:** 19 days (Nov 29 – Dec 17)
- **Total lines (chs 1–9):** ~3,264 lines of LaTeX

---

## 17 December 2025 — Literature Integration Session

### Papers Integrated

| Paper | Placement | Type |
|-------|-----------|------|
| Scott-Phillips 2025 (byproduct hypothesis) | Ch 7 (table) + Ch 8 (diagnostic) | Methodological |
| Fedorenko 2024 (language network as natural kind) | Ch 4 | Neural evidence |
| Fedorenko 2024 (communication not thought) | Ch 7 | Forcing function |

### Advisory Board Consultations
- Spawned 4-agent boards (Gemini + Codex) for Scott-Phillips and Fedorenko papers
- Strong consensus: papers highly compatible with HPC framework
- Both papers strengthen the "communicative pressure as forcing function" argument

### Key Additions
- **Ch 4**: Neural evidence paragraph — language network exhibits HPC signature (stability without sameness)
- **Ch 7**: Double dissociation paragraph — language/reasoning separable confirms forcing function is communicative
- **Ch 7 Table 7.1**: Optimal relevance as selection pressure in functional feedback row
- **Ch 8**: Methodological caution — acceptability judgments are byproducts of relevance-seeking, not direct grammar reports

### Infrastructure
- Fixed build workflow: `latexmk` now recommended (routes output to `build/` per `.latexmkrc`)
- Updated `/init` workflow with build reminder
- Cleaned up stray build artifacts from main folder

### Created Notes
- `scottphillips2025-analysis.md`, `fedorenko2024-analysis.md`
- 8 board feedback files (`board-scottphillips-*.md`, `board-fedorenko-*.md`)

---

## 16 December 2025 — Infrastructure & indices (session 2)

### Glossary & Index Infrastructure
- Added **glossaries-extra** package with 5 mechanism-focused entries (HPC, projectibility, homeostasis, entrenchment, essentialism)
- Added **triple index** (Subject, Names, Lexical) using imakeidx with helper macros
- Fixed lexical index to use sort key syntax for proper alphabetization
- Added sample tags across Chs 1, 2, 4

### Two-Diagnostic Preview
- Added paragraph to Ch 6 opening previewing projectibility + perturbation-sensitivity diagnostics

### Build Infrastructure Cleanup
- Renamed `main.tex` → `hpc-book.tex`
- Created `.latexmkrc` routing artifacts to `build/`
- Created `snapshots/` for dated PDF versions
- Created `frontmatter/` for cover, precis, dedication
- Moved Python scripts to `code/`
- Root directory: 8 files (was 23)

---

## 16 December 2025 — Book cover (session 3)

### Cover Design
- Created book cover (170mm × 240mm) with braided river delta background
- Typography: EB Garamond (installed via Homebrew)
- Title/subtitle positioned in neutral grey sky area
- Author name with subtle glow effect (TikZ multi-layer technique)
- Iterative refinement based on feedback (position, shadow intensity, font size)

### Files Created
- `figures/cover-braided-river.jpg` — background image
- `frontmatter/cover.tex` — standalone cover (for separate PDF)
- `frontmatter/coverpage.tex` — includable version for main book

### Additional Fixes
- Fixed frontmatter page numbering (TOC starts at page i)
- All three indices now appear in TOC

---

## 16 December 2025 — Ch 13 theoretical framework (session 1)

Developed comprehensive theoretical framework for Chapter 13 (Grammaticality itself):

### Core Framework: MMMG
- **G(u) = C^t(u) · K(u) · map** — only morphosyntax-meaning pairing failures trigger ungrammaticality
- Phonology and discourse affect F(u) (subjective feeling), not G(u) (grammaticality)

### Information-Theoretic Framing
- Shannon: Mutual information peaks at constructions (form-meaning bidirectional constraint)
- Kolmogorov: Morphosyntax is Goldilocks zone (compositional + obligatory)
- CP is effect-space relative: phonemes have low CP for propositions, high CP for lexical identity

### Key Evidence
- Turkish vowel harmony (stem vs suffix disharmony)
- "A orange" as allomorphy, not pure phonotactics
- Indexical vs semantic meaning distinction

### Notes Consolidation
- Merged three overlapping files into linked set:
  - `chapter13-master.md` — quick reference
  - `chapter13_planning.md` — structural planning
  - `morphosyntax-systematicity-zone.md` — comprehensive deep-dive

### Terminology Standardization
- "Grammatical categories" → "linguistic categories" in Chs 2, 3, 5

---

## 15 December 2025 — Scope broadened beyond grammar

Reframed the book as a sieve for *linguistic* categories rather than only grammatical categories.

- Updated working title to "How Linguistic Categories Work"
- Revised the outline to add major non-grammar cases (one positive, one negative) and to sprinkle non-grammar examples earlier

## 5 December 2025 — Genesis of Chapter 5

### Timeline

- **October 2025**: Ord's paper comes out. Brett thinks "cool idea/tool" and writes Sorites paper despite never having written a math/logic paper. Sends to Bruno Dinis for comment. Bruno responds, but Brett has moved on; comments sit unread.
- **Saturday 29 November 2025, 8:34 PM**: HPC book folder created.
- **Wednesday 3 December 2025**: Email from Ryan Nefdt:

> Hi Brett
>
> I think this book is needed indeed! I like your use of HPC and the motivation.
>
> I just reviewed a proposal for CUP by András Kertész who argues for moderate relativism about grammatical categories as opposed to what he calls absolutism (basically your essentialism). He imports some interesting stuff from the faultless disagreement literature for some of his claims. Might want to check his p-model idea out.
>
> Of course, in philosophy, as I am sure you know, James Miller has written quite a bit on HPC as a metaphysics of words. But his linguistics is shaky though.
>
> Martin Haspelmath's work seems most relevant. He constantly makes deflationary arguments about strict categories and assumptions of discreteness in theoretical linguistics from a typological perspective. He has a chapter on this in a more philosophical vein in my forthcoming OUP handbook (I can share, if you want to see it).
>
> I have my own take on these issues. I personally favour a phase transition approach in which discreteness really is a feature of a system under a particular kind of measurement and context and continuity under a different one (like water moving from liquid to gas takes on different properties). So borrowing more from physics than biology.
>
> But your methodical and clear style should bode well for a potential book deal and be a genuine contribution to the literature!
>
> Best
> Ryan

- **Thursday 4 December 2025, ~4:15 AM**: Brett wakes thinking about phase transitions. **Ryan's email directly sparked Chapter 5** — the phase-transition framing wasn't planned and hadn't been thought through before his message. The dormant Sorites paper resurfaces as the formal backbone for the physics-to-linguistics bridge Ryan suggested. Morning: rework Sorites paper, publish on PhilPeople and arXiv. Rest of day: write what becomes Chapter 5.

### The causal chain

Ryan's email → phase-transition idea → Sorites paper as formalization → Chapter 5

This was not independent convergence. Ryan's suggestion created Chapter 5.

### Leads from Nefdt email

- [ ] **András Kertész** — CUP proposal on moderate relativism, p-model, faultless disagreement literature
- [ ] **Ryan Nefdt's phase transition approach** — asked for papers, awaiting response
- [ ] **Haspelmath chapter in OUP handbook** — Ryan offered to share

### Technical note

This book has been written with substantial assistance from LLMs (Claude Opus via Anthropic and Google's Antigravity interface). Project started 29 Nov; by 5 Dec, Chapters 1, 2, and 5 are drafted and revised. The speed is unprecedented.

---

## 5 December 2025 (evening) — Humour, Rhetoric, Figures, Feedback

### Session summary

Refined Chapters 4 and 5 for style, arguments, and visual clarity.

### Humour and rhetoric
- Added 3 humorous insertions (hyperreals eyebrow, alignment micro-exchange, streetcar metaphor)
- Removed duplicate "sounds glib" aside (too similar to hyperreals line)
- Added 3 rhetorical figures:
  - Chiasmus at virtuous circle (Ch 4)
  - Tricolon at thesis pivot (Ch 4)
  - Antithesis at two-failures framing (Ch 5)

### New figures
- **3.phase-transition.png**: Ice/water/steam phase diagram (user-generated via Nano Banana Pro)
- **4.top-vs-ball.png**: Passive equilibrium vs. dynamic stability (user-generated)
- Added `\listoffigures` to front matter
- Removed 5.diachronic-trajectory.png (figure cut)

### Reviewer feedback integration
- **Chapter 4 edits**:
  - Cut "mechanism as HPC" hedging joke
  - Clarified that biology parallels are functional analogues, not homologues
  - Fixed "almost essentialist" → "tight maintenance produces a surface that *looks* essentialist"
- **Chapter 5 edits**:
  - Sharpened Rosch paragraph: gradience is typicality/stability, not degrees of membership
  - Added footnote distinguishing Hull's replicators from Millikan's copies

### Deferred feedback
Created `notes/chapter-feedback-deferred.md` capturing items for:
- Chapter 5 (structural improvements, theoretical clarifications)
- Chapter 8 (homeostasis test, diverging populations)
- Chapter 10 (cross-linguistic divergence)
- Chapter 12 (looping effect, grammaticality as HPC kind)

### State at end of session
- 107 pages compiled
- Chapters 3, 4, 5 revised
- Ready to move to a new chapter tomorrow

---

## 11 December 2025 — Citation Refinement & Quotation Integration

### Session summary

Systematic review of all chapters (1-8) to add page numbers and verbatim quotations from source PDFs.

### Literature folder reorganization
- Moved 9 PDFs from `literature/islands/` subfolder to main `literature/` directory
- Renamed all PDFs to match BibTeX keys:
  - `kallini2024.pdf`, `piantadosi2024.pdf`, `cuneogoldberg2023.pdf`, etc.
  - Corrected: `onishi2021.pdf` → `onishi2022.pdf`, `favierhuettig2021.pdf` → `favier2021.pdf`
- Deleted empty `islands/` subdirectory

### Page references added

| Chapter | Citation | Reference Added |
|---------|----------|-----------------|
| 1 | `huddleston2002` | `[ch.~1]` |
| 3 | `spike2020` | `[13--15]` |
| 3 | `dahl2016` | `[435--436]` |
| 4 | `millikan1984` | `[ch.~1]` |
| 4 | `craver2009` | `[575]` |
| 5 | `kirby2008` | `[10681]` |
| 6 | `favier2021` | `[Table~2]` |
| 8 | `miller2021` | `[25--26]` |

### Verbatim quotations added

1. **Millikan 2017 p. 17** (Ch 4): *"Anything with a structure that tends actively to maintain or reconstitute itself over time [...] maintains or increases its own kind while depleting materials and resources for constituting other kinds"*

2. **Craver 2009 p. 575** (Ch 4): *"Kind concepts cut nature at its joints, and [...] nature's joints are located at the boundaries of mechanisms"*

3. **Kirby 2008 p. 10681** (Ch 5): *"cultural evolution is an 'invisible hand' process leading to phenomena that are the result of human action but are not intentional artifacts"*

### PDFs without matches (cannot add page numbers)
Many citations still lack matching PDFs: `quine1969`, `kornblith1993`, `gardenfors2000/2014`, `williamson1994`, `labov2001`, `milroy1987`, `erikson1968`, `pickering2004`, etc.

### Documentation updates
- Updated `PROJECT_STATUS.md` with session summary
- Updated `CLAUDE.md` chapter status
- Updated `project-log.md` (this file)

### Reflection: Draft quality differences (Chs 1-5 vs 6-8)

**Observation:** The first drafts of chapters 1-5 were notably good — often requiring only polish rather than structural rewriting. Chapters 6-8, by contrast, required extensive reworking: multiple "major rewrite" commits, repeated editorial passes, and significant structural changes.

**Evidence from git history:**
- **Chapters 1-5** (Dec 1-5): Commits show polish-level work: "Style fixes," "Small polish," "phrasing, contractions," "humour, rhetoric, figures." The arc is refinement, not reconstruction.
- **Chapters 6-8** (Dec 6-10): Commits show deep rework: "major rewrite of 'What this commits us to' section," "restructure mechanism tests," "merge redundant paragraphs," "major rewrite of 'Refactoring' section." The arc is repeated surgery.

**KEY FINDING: Pre-draft planning documents correlate with quality.**

| Chapter | Pre-draft Planning Doc | Size | Notes |
|---------|------------------------|------|-------|
| Ch 1 | (synopsis.md, ontology_of_grammar.md) | 30KB+ | Core thesis docs |
| Ch 2 | `handoff_to_opus.md` + `chapter2_planning.md` | 16.9KB + 8.4KB | Full transcript, strategic example allocation, Rapoport's rules |
| Ch 3 | `chapters_3_and_5_planning.md` | 11.2KB | Material identified, forward pointers |
| Ch 4 | `chapter04_hpc_intro.md` | 5.3KB | Detailed section outline |
| Ch 5 | `chapters_3_and_5_planning.md` | 11.2KB | 13 subsections of material, epigraph, revision history |
| **Ch 6** | `chapter06-feedback.md` **only** | **1.9KB** | **Feedback on draft, not pre-draft planning** |
| **Ch 7** | `chapter07-master.md` | **29KB** | **Post-draft consolidation** (contains "Packaging Board Feedback (2025-12-07)") |
| **Ch 8** | `chapter08-master.md` | **9KB** | **States "Initial draft complete"** — planning happened during or after drafting |

**Pattern:**
- Chapters with detailed PRE-draft planning (~5-17KB of strategic structure, example allocation, and explicit constraints) produced good first drafts.
- Chapters where planning was done DURING or AFTER drafting required extensive revision.

**The `handoff_to_opus.md` document (Dec 1) is exemplary:**
- Full conversation transcript with explicit questions and user constraints
- Rapoport's rules discussion (steel-man before critique)
- Great science communicators analysis (Gould, Dennett, Dawkins, Sacks)
- Domain-by-domain structure with explicit example allocation
- Forward/backward references to other chapters

**Recommendation for Part III development:**
Create pre-draft planning documents following the `handoff_to_opus.md` template:
1. Conversation transcript capturing strategic decisions
2. Explicit example allocation (what goes here vs reserved for later)
3. User constraints restated clearly
4. Structure choices with rationale
5. Forward/backward chapter connections

---

### Process Observations (Meta-reflection)

**Successful patterns in this project:**

1. **Simulated advisory board reviews:** Using named scholars (Boyd, Rosch, Dąbrowska, Fahnestock, Tufte, Goldberg, Croft, Godfrey-Smith, McCloskey) to generate targeted feedback from different perspectives. See `chapter06-feedback.md` and `chapter07-master.md` (Part O: Packaging Board Feedback). This produced discipline-specific critiques rather than generic suggestions.

2. **Science communicators as structural models:** Explicit discussion of how Gould, Dennett, Dawkins, and Sacks structure arguments. Each has a signature move (Concrete→Pattern→Principle, Intuition→Violation→Reconstruction, etc.). This informed chapter architecture. See `handoff_to_opus.md` lines 84-107.

3. **Multi-model workflow:** Gemini 2.0 Flash for planning/brainstorming, Claude Opus for drafting, Antigravity for revision and integration. Different interfaces seem suited to different phases (though this needs more systematic investigation).

4. **House-style enforcement:** `.house-style/style-guide.md` and `.house-style/preamble.tex` establish conventions that multiple sessions can follow. Reduces iteration on surface-level fixes.

5. **Literature PDF integration:** Keeping PDFs named to match BibTeX keys enables systematic citation work. Today's session demonstrated this: `pdftotext` + grep + targeted edits.

6. **Master notes as consolidation:** For chapters 7-8, the master notes became post-hoc consolidations of scattered material. This is useful for handoff but doesn't replace pre-draft planning.

**Patterns to improve:**

1. **Pre-draft planning for every chapter:** The quality correlation is clear enough to make this mandatory.

2. **Citation pass as separate phase:** Today's work (adding page numbers, quotations) is best done after drafting but before final polish. Build this into the workflow.

3. **Transcript preservation:** `handoff_to_opus.md` captured a valuable strategic conversation. Consider doing this more systematically, especially for planning phases.

### State at end of session
- All changes committed and pushed to `restructure-part-1` branch
- Citations across all 8 chapters reviewed
- Ready for Part III development

**Next session (Dec 12):** Flesh out Chapter 8, which is still skeletal.

---

## 11 December 2025 — Chapter 8 Development + Polish Phase Notes

### Chapter 8 revisions

Chapter 8 expanded from 333 → 358 lines:
- Heritage attrition example (§8.2) — natural experiment for perturbation testing
- Table 8.1 — failure-mode summary
- Figure 8.1 — decluttered quadrant labels
- §8.6.2 expanded — Haspelmath comparative concepts + evidentiality worked example

### Polish phase: Humour and rhetoric

**As each chapter nears completion**, a final polish pass should look for opportunities to:

1. **Add a little humour** — not jokes, but moments of wit, self-awareness, or unexpected phrasing that reward close reading. Examples from the project:
   - Ch 4: "which is more than most PhD students manage" (line 95)
   - Ch 8: "Good luck." after noting how entrenched *thing* is

2. **Add structural rhetorical figures** — not ornament but architecture:
   - **Tricolon** — groupings of three for rhythm and memorability
   - **Chiasmus** — A-B-B-A reversal for emphasis
   - **Anaphora** — repeated opening phrase across sentences or paragraphs
   - **Antithesis** — balanced contrast (X, not Y)
   - **Antimetabole** — "categories are real because they are maintained" (near-chiasmus)

These should be **subtle and functional**, not showy. The goal is prose that rewards re-reading without signalling cleverness.

---

## 13 December 2025 — Cross-Reference Audit

### Session summary

Systematic audit and refinement of all cross-references across chapters 1-8 to ensure dynamic LaTeX linking and section-level precision.

### Issues identified and fixed

**Broken references:**
- Ch 2:164/174 — References to `ch:what-changes` (stub chapter) changed to hard-coded CGEL chapter numbers ("Chapter 1", "Chapter 15")
- Ch 5 label — `ch:discrete-from-continuous` renamed to `ch:dynamic-discreteness` to match existing forward reference in Ch 4:306

**Section-level upgrades (12 total):**

| Location | Original | Upgraded to |
|----------|----------|-------------|
| Ch 4:31 | `ch:essentialism` | `sec:2:a-parallel` (Smilodon example) |
| Ch 4:284 | `ch:essentialism` | `sec:2:what-essentialism-built` (Aristotle) |
| Ch 5:143 | `ch:kinds-without-essences` | `sec:4:heterogeneity` (thin kinds) |
| Ch 5:352 | `ch:what-we-havent-been-asking` | `sec:3:lexeme-obsession` (feature debates) |
| Ch 5:358 | `ch:what-we-havent-been-asking` | `sec:3:lexeme-obsession` (Shilluk) |
| Ch 7:174 | `ch:projectibility` | `sec:6:generalising-lesson` (quotatives) |
| Ch 7:361 | `ch:kinds-without-essences` | `sec:4:the-mechanisms` (mechanism list) |
| Ch 7:467 | `ch:projectibility` | `sec:6:mechanistic-alternative` (Boguraev) |
| Ch 7:525 | `ch:failure-modes` | `sec:8:homeostasis-diagnostic` |
| Ch 7:527 | `ch:projectibility` | `sec:6:definitional-bet` (Polish aspect) |
| Ch 7:590 | `ch:projectibility` | `sec:6:degrees-projectibility` (accuracy) |
| Ch 8:23 | `ch:stabilisers` | `sec:7:stabilisers-at-scales` |
| Ch 8:47 | `ch:projectibility` | `sec:6:definitional-bet` (good bet) |

### Full build verification

- Compiled full 8-chapter PDF: 143 pages
- Only undefined references are forward refs to unwritten chapters (9-14)
- Saved as `main-full-8ch-2025-12-13.pdf`
- Restored `main.tex` to development state (most chapters commented)

### State at end of session
- All cross-references audited and refined
- Committed and pushed
- Ready for Part III development

---

## 13 December 2025 (afternoon) — Précis + Chapter 8 Final Polish + Full Build

### Précis for general reader

Created a 5-page (~2,500 word) précis targeting a smart, curious general reader:

1. **The Puzzle** — Huddleston's *otherwise* email as framing device
2. **The Fix** — HPC kinds via spinning-top metaphor
3. **The Diagnostics** — Projectibility + homeostasis; thin/fat/negative failure modes
4. **What This Changes** — Universals, gradience, methodology debates dissolved
5. **The Larger Stakes** — Third way between Platonism and nominalism

**Rhetorical figures added:**
- Tricolon (three uses, three environments, one word)
- Anaphora (fits where...fits where...fits where)
- Antithesis (not because it's fixed...because something is holding it)
- Asyndeton (frequency vanishing, no child learning it, no social group marking it)

**Wry lines from packaging board:**
- "There is no master filing cabinet."
- "Nobody has ever been mauled by a merely convenient label."
- "When a framework can explain everything, it stops explaining anything in particular."
- "excellent storage capacity and terrible explanatory power"

**Files created:**
- `precis/general-reader-precis.md` — Markdown source
- `precis.tex` — LaTeX version with house style macros

### Chapter 8 final polish

- House style compliance pass (contractions, dashes, citations)
- Parataxis reduction: 6 fixes adding coordination and subordination
- Examples: "Here's the trap:" instead of "This is the trap.", asyndeton in thin-category description

### Full book PDF

- Updated `main.tex` to include précis in frontmatter
- Uncommented all chapters (1-14 + appendix)
- Built with `latexmk -xelatex`
- Result: 163 pages (`main.pdf`)

### State at end of session

- All changes committed and pushed to `restructure-part-1`
- PROJECT_STATUS.md and project-log.md updated
- Ready for Part III development or handoff

**Next priorities:**
1. Part III planning (Chapters 9-12 case studies)
2. Ch 9 outline (Countability as first case study)
3. Consider PR to merge `restructure-part-1` to main

---

## 14 December 2025 — Chapter 9 restructuring

### Session summary

Major restructuring of Chapter 9 (Countability) around the two-HPC architecture: individuation cluster (semantic) + count cluster (morphosyntactic), coupled by bidirectional inference.

Key changes:
- Fixed category/function error (LEGO as noun modifier, not adjective)
- Terminology update: count/non-count (morphosyntax), individuated/non-individuated (semantics)
- Replaced bats with macrophages for cross-scale individuation — callback to Ch7 opening
- Reframed: the two-cluster structure is *typical* of HPCs at the right grain, not peculiar to countability
- Softened: categories "often reveal internal structure" (not "always decompose into two")

### Research note: Investigate "twoness"

Is the form-meaning pairing a deep structural principle for grammatical HPCs?

- **Observation**: Countability decomposes into semantic (individuation) + morphosyntactic (count cluster). Definiteness may show the same pattern. Word classes may too.
- **Connection**: This maps directly onto CxG's central claim that constructions are form-meaning pairings. If HPCs typically have this dual structure, that's a convergence worth exploring.
- **Question**: Is the form-meaning split a contingent pattern (just happens to be salient in these cases) or a principled structural necessity (interface systems require two poles)?
- **Potential chapter**: Could become a theoretical chapter in Part IV — "Why two?" connecting HPC architecture to Construction Grammar.

### Commits on restructure-part-1

- `db66ea2` Restructure Ch9: Two HPCs architecture
- `b365dcc` Fix category/function error (LEGO)
- `f772390` Terminology: count/non-count, individuated/non-individuated
- `962eb9d` Macrophages callback to Ch7
- `153c7db` Reframe: two-cluster structure is typical
- `6e46b13` Carry framing through chapter
- `bec00e4` Soften 'sub-clusters' framing

---

## 14 December 2025 (afternoon) — Chapter 9 Citation Verification & Calibration

### Session summary

Major calibration pass on Chapter 9's cross-linguistic section to ensure claims are accurate and appropriately hedged.

### Citation verification

1. **Grimm (2018)** — Verified against extracted PDF text:
   - Welsh collective/singulative system accurately described
   - Table 3 (semantic classes: insects, vegetation, granular mass) matches chapter text
   - Added page 532 reference to citation

2. **Wiltschko (2008)** — Verified against extracted PDF text:
   - Confirms plural marking is optional with "no meaning difference"
   - Her analysis: plural modifies *roots* (category-neutral), not Nouns
   - Supports our "less cohesive" prediction (actually zero projectibility syntactically)
   - Explicitly states "no syntactic rule that is sensitive to such a distinction" (mass/count)

### Calibration changes

- **Removed**: Over-claiming "geometry shifts" table (made claims too strong)
- **Reframed**: Cross-linguistic variation as "mechanism-sensitive" rather than proving universal patterns
- **Added**: Triangulation caveat ("No single language comparison is a controlled ablation")
- **Welsh**: Now framed as conditional ("*if* the count cluster is homeostatically maintained...")
- **Emoji/AP**: Reframed as diagnostic oscillation (AP endorsed *emojis*, then reversed)
  - Added LEGO Group callback ("like the LEGO Group's lawyers fighting *Legos*")
- **Disconfirmation**: Stronger framing — finding a language with no morphosyntactic maintenance but English-like projectibility

### "Looking forward" section rewrite

- **New framing**: "Countability is the clean baseline case" — coupling is unusually tight
- **New phrase**: "individuation, which languages get 'for free' from domain-general object cognition"
- **Definiteness preview**: Form cluster and function cluster may not line up as neatly
- **Lexical categories preview**: Noun/verb contrast stable; adjectives vary; mechanisms not uniform

### Full build

- Reinstated all chapters in `main.tex` (Parts I-III)
- Compiled full book PDF: 160 pages
- Created dated copy: `HPC-Book-Full-2025-12-14.pdf`

### Commits on restructure-part-1

- `eb1e6e9` Chapter 9: Refine natural experiments section, move emoji example, fix citations
- `db7fffd` Chapter 9: Calibrate claims, restore LEGO callback, refine Looking forward

### State at end of session

- Chapter 9 complete and calibrated
- All changes committed and pushed
- Full book PDF built and renamed
- Documentation updated for handoff

**Next priorities:**
1. Ch 10 (Definiteness) planning and drafting
2. Ch 11 (Lexical categories) planning and drafting
3. Consider PR to merge `restructure-part-1` to main

---

## 20 December 2025 — Deixis, Anaphor, Interrogatives, and Mechanism Braiding

### Session summary

Theoretical discussion prompted by CGEL's classification of *today/tomorrow/tonight/yesterday* as pronouns. Led to a squib on focus modifiers (*exactly who* vs. *the person exactly who*) and key insight for Chapter 11.

### The intellectual chain

1. **Starting observation**: CGEL classifies *today/tomorrow* as pronouns on semantic/distributional grounds, but morphologically they're unlike typical pronouns. Similar to *Monday* — deictic, resists determiners.

2. **The question**: Is determiner resistance from *deixis* or from *anaphor*?

3. **Key puzzle**: Interrogative *who/what* resist determiners too, but they're *neither* deictic *nor* anaphoric — they're open variables over alternatives.

4. **Resolution**: The resistance comes from **referential saturation at the DP level**, achieved by different routes:
   - Deixis: contextually saturated
   - Anaphor: bound variable
   - Interrogatives: variable over alternatives (the question semantics provides the domain)

5. **The HPC insight** (required explicit prompting): What starts as a **semantic fact** (redundancy — no need for determiners when reference is clear) becomes a **syntactic fact** (distributional resistance) **because the category is maintained by braided mechanisms**. Functional pressure → entrenchment → distributional pattern.

6. **Tangent → squib**: Interrogatives allow focus modifiers (*exactly who*) that integrated relatives don't (*the person exactly who*). Wrote squib applying Cuneo & Goldberg's BCI principle (backgrounded constituents resist foregrounding).

### Files created/updated

- `notes/chapter11-grist.md` — New file with the clustering table and mechanism-braiding insight
- `/Users/brettreynolds/Documents/LLM-CLI-projects/Focus_modifiers_interrogative_heads/SESSION_LOG.md` — Added intellectual origin section

### Meta-observation on LLM limitations

> The LLM didn't spontaneously see the mechanism-braiding insight (that semantic redundancy becomes syntactic distribution through entrenchment). It organized the data into tables and noted the clustering, but the *theoretical* move — "this is an instance of the book's core argument" — required explicit prompting from the human.

This confirms the pattern noted in the squib project: the human notices the interesting issues and theoretical connections; the LLM can execute once pointed in the right direction but is unlikely to make the conceptual leap unprompted.

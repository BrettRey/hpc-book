# HPC Book Project Status

**Date**: January 16, 2026
**Current Phase**: Part III Development; Ch 10 complete; Ch 11 drafted; Ch 12 polished draft; Ch 13 empirically enhanced

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

### Part III: Categories Reconsidered (Chapters 9-12)
- ✅ **Ch 9**: Countability - drafted and refined (LEGO/emoji hooks, cross-linguistic section)
- ✅ **Ch 10**: Definiteness - complete and audited (Dec 25, 2025)
- 🔄 **Ch 11**: Lexical Categories - plan approved; awaiting draft
- 🔄 **Ch 12**: Gender and the Maintenance Spectrum - rough first draft (Dec 26); may restart (ship/table hook, transparent→entrenched spectrum, English/French/German cases)

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

## In Progress

- 🔄 **Ch 11** (Lexical Categories): Plan approved, ready to draft
- 🔄 **Ch 12** (Gender): Rough draft exists; may restart
- 🔄 **Ch 13** (The Stack): Empirically integrated (Jan 16); pending final citations and polish
- 🔄 Ch 14 (Grammaticality): Theoretical framework developed; needs prose
- 🔄 Ch 15 (Methodological Consequences): Was Ch 14

**Note:** Book now 15 chapters (gender added Dec 26)

## Next Actions

### Immediate
1. **Ch 11 Draft** - Lexical categories; implementation plan approved (`notes/ch11/ch11-implementation-plan.md`)
2. **Ch 12 Revision** - Gender draft needs work (or restart from scratch)
3. **Ch 15 Mereology Section** - Typed mereology content from `linguistics-mereology/` project (was Ch 14)

### Medium-term (Next 2-3 Months)
1. Draft Part III chapters (11-12)
2. Draft Part IV chapters (13-15)
3. Create visualizations and figures

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

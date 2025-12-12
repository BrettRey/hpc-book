# Project Log

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

**Possible factors (hypotheses for future investigation):**
1. **Cumulative context loss**: Chat transcripts early in the project carried full context; later sessions may have lost crucial framing from truncation.
2. **Outline specificity**: Chapters 1-5 had more detailed prior planning (`synopsis.md`, `ontology_of_grammar.md`); chapters 6-8 were drafted with less scaffolding.
3. **Conceptual maturity**: The HPC framework itself was clearer in the author's mind for chapters 1-5; chapters 6-8 required the model to extrapolate further from less crystallized ideas.
4. **Model/interface changes**: Different models or interfaces (Claude Opus, Antigravity) may have been used in different phases.
5. **Prompting style drift**: Early sessions may have included more explicit structural prompts; later sessions may have become more conversational.

**TODO:** Excavate early chat transcripts (if available) to compare prompting patterns. Check which model versions were used for which chapters.

### State at end of session
- All changes committed and pushed to `restructure-part-1` branch
- Citations across all 8 chapters reviewed
- Ready for Part III development


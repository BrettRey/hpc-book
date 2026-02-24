# Chapter 9: Countability -- Editorial Report

---

## 1. Argument

The chapter's argument is sound and does exactly what it needs to do: it delivers the first and tightest Part III case study, demonstrating that the HPC apparatus built in Part II can be deployed on a real grammatical category. The two-cluster architecture (individuation + count cluster, coupled by bidirectional inference) is the chapter's central theoretical contribution and it is well-motivated. The argument builds cleanly from profile to mechanism to hierarchy to diachronic signature to cross-linguistic test, and the audit table at the end closes the loop against the Ch 8 template. One logical seam: the section "Why the coupling produces an HPC" (SS9.4.1) rehearses the furniture-vs-countability contrast that was already made in SS9.2; the second pass doesn't add enough new content to justify the repetition. The chapter also promises (line 123) that "Chapter 13" will develop the grammaticality-coupling point, but the relevant chapter is actually Ch 14 (grammaticality itself); Ch 13 is the zipper synthesis.

## 2. Structure

The section order is well-judged: two-cluster introduction, individuation, count cluster, coupling, hierarchy, quasi-count cases, diachrony, cross-linguistic parallels, hyperreal boundaries, audit, looking forward. This tracks the logic cleanly. Two structural observations. First, SS9.7 ("Sharp boundaries in fuzzy territory") is only 18 lines and feels like a pendant rather than a section; it could be folded into SS9.5 ("The hierarchy") as a closing subsection, since it is really about what the hierarchy predicts for judgments. Second, SS9.8 ("Passing the tests") and SS9.9 ("What does this buy us?") are both summative, and the distinction between them is thin -- "passing the tests" is about whether countability qualifies as HPC, and "what does this buy us" is about what the HPC framing adds. These could be merged without loss.

## 3. Prose

The opening is outstanding. "And they are losing." (line 12) lands perfectly -- economical, punchy, and it earns the LEGO case as a running thread. The lock-and-key metaphor (SS9.5.1) is vivid and does genuine explanatory work; the integration with the basin metaphor in SS9.5.2 is the chapter's best piece of prose architecture. The pea back-formation narrative (SS9.6.1) is another high point -- tight, diachronic storytelling with mechanism visible at every step. The Minnesota legislature anecdote (line 274) is a gem.

Where the prose drags: the introductory section (SS9.1, "One word, two categories") runs to nearly 700 words and says some things twice (the furniture contrast appears at lines 26--27 and again at lines 28--34, then once more in SS9.4.1). The ABM disclaimer paragraph (line 286) is necessary but reads like a methods appendix dropped into the narrative; it breaks the chapter's momentum at a point where the data-drift story should be landing. Consider moving it to a footnote or a clearly delineated aside.

## 4. Evidence

The evidence is well-chosen and well-layered. The implicational matrix (Table 9.1) is the chapter's empirical centrepiece and earns its space. The COCA data on *folks* vs *people* (8.6-fold suppression, line 249) is concrete and falsifiable. The ABM simulation is appropriately hedged as didactic. The cross-linguistic section (Welsh singulatives, Mandarin classifiers, Halkomelem optional number, Yudja numeral-mass combinations) is a strength, but two of the four cases are explicitly programmatic (Mandarin, Yudja). The Welsh case carries most of the cross-linguistic weight; adding even a sentence of actual Mandarin classifier data (rather than just the prediction) would strengthen the triangulation. The macrophage/echolocation material in SS9.2 is suggestive but does a lot of inferential work for its length -- the chapter asks the reader to accept that edge-detection recurrence across levels of biological organisation constitutes evidence for the individuation cluster's stability. This is the weakest evidential link; the chapter knows this but could be more explicit about the gap.

## 5. Cross-chapter coherence

The chapter connects backward to Part II thoroughly and accurately: the spinning-top/basin metaphor (Ch 4), dynamic discreteness (Ch 5), stabilisers (Ch 6), projectibility (Ch 7), and the failure-mode audit template (Ch 8) are all invoked and deployed. Forward references to Ch 10 (definiteness) and Ch 11 (lexical categories) are well-placed. However, the forward reference at line 123 points to "Chapter 13" for the grammaticality-coupling claim, when Ch 14 is the grammaticality chapter; Ch 13 is the zipper synthesis. The book-level report flags that the evidential gradient across Part III (strongest case first, deliberately loosening) should be signalled to the reader; the opening paragraph of Ch 9 (lines 16--18) does gesture at this ("each case study that follows loosens the coupling") but could be sharper about the deliberate design: one sentence saying "we begin with the tightest case because the framework's credentials should be established where the evidence is strongest" would discharge this. The terminology note about "HPC kind" (see House Style below) also creates a cross-chapter consistency issue, since the CLAUDE.md specifies "category" throughout.

## 6. House style issues

1. **"HPC kind" vs "HPC category"**: The project CLAUDE.md states: "Do NOT use 'kind' -- the book uses 'category' throughout." The chapter uses "HPC kind" at lines 332, 356, 358, and 454. These should all be "HPC category" (or equivalent rephrasing).

2. **Double backslash before `\mention`**: Line 134 has `\\mention{Legos}` -- a stray extra backslash that will render a linebreak before the mention. Should be `\mention{Legos}`.

3. **Epigraph quotation marks**: Line 8 uses `` `LEGO Bricks or Toys' `` and `` `LEGOS' `` with TeX-style single open/close quotes. The house style requires `\enquote{}` for quotations. However, since this is a direct quotation inside `\epigraph{}`, the single-quote marks may be acceptable as part of the original text. Worth a decision.

4. **`\textit{}` in epigraph**: Line 8 uses `\textit{The word LEGO...}` for the epigraph body. The `\epigraph` command presumably handles formatting; the raw `\textit{}` is not a semantic macro. If the italics are conventional for epigraph styling, this may be fine, but check whether the epigraph class handles this automatically.

5. **`\textit{CGEL}` at line 82 and 211**: Both use `\textit{CGEL}` rather than a semantic macro. Since *CGEL* is a book title, `\textit{}` is arguably correct, but the rest of the book should be checked for consistency. If there is a `\booktitle{}` macro or similar, use that.

6. **Stray sentence fragment at line 348**: "We've identified the mechanisms:" appears as a standalone line immediately before a paragraph that begins "We have identified five interlocking mechanisms." The first sentence is a leftover that should be deleted.

7. **Truncated contraction at line 404**: The sentence ends "and it's." -- this should be "and it is" (the contraction is hanging without a complement; the intended reading is apparently "and it is [less cohesive]"). The elided predicate needs to be supplied, or the sentence restructured.

8. **`\emph{}` for emphasis vs semantic macros**: The chapter uses `\emph{}` for rhetorical emphasis (e.g., `\emph{within}` at line 169, `\emph{is}` at line 175, `\emph{why}` at line 367). This is acceptable for emphasis. But `\emph{same set of morphosyntactic properties}` (line 32), `\emph{interface system}` (line 30), and `\emph{passive}` (line 237) walk close to the line where `\term{}` might be more appropriate. Review case by case: if the phrase is being introduced as a technical concept, use `\term{}`; if it is ordinary emphasis, `\emph{}` is fine.

9. **Backtick quotes in cross-linguistic data**: Lines 310, 392, 416 use backtick-style quotes (`` `birds' ``, `` `three blood' ``). These should use `\enquote{}` for consistency.

10. **En-dash in epigraph attribution**: Line 8 uses `—` (em-dash) before the attribution. The house style prefers en-dashes with spaces. However, this may be conventional formatting for `\epigraph` attribution fields; check the epigraph package's default handling.

## 7. Specific recommendations

1. **Delete the orphaned sentence at line 348.** "We've identified the mechanisms:" is a vestigial draft line. Remove it; the paragraph beginning "We have identified five interlocking mechanisms" does the job.

2. **Fix the double backslash at line 134.** Change `\\mention{Legos}` to `\mention{Legos}`.

3. **Fix the truncated sentence at line 404.** "and it's." needs its predicate restored: "and it is" or, better, restructure: "...the 'count' category should be less cohesive -- and the evidence suggests it is."

4. **Replace "HPC kind" with "HPC category" at lines 332, 356, 358, 454** (and the table caption at line 439, which reads "HPC-kind audit"). The book's terminology convention reserves "category" for this role.

5. **Correct the forward reference at line 123.** "Chapter~13" should be "Chapter~14" (or `\ref{ch:grammaticality}`) -- the grammaticality chapter, not the zipper synthesis.

6. **Cut the repeated furniture contrast.** The furniture example appears at lines 26--27 (SS9.1), lines 28--34 (same section), line 90 (SS9.3.1), and lines 115--121 (SS9.4.1). The first and third occurrences do structural work; the fourth (SS9.4.1) is the weakest -- it restates SS9.2's argument almost verbatim. Trim SS9.4.1 to a cross-reference: "As Section 9.2 argued, lexical semantics alone doesn't generate HPC-grade clustering. Countability does, because..." and proceed directly to the coupling-as-reinforcement argument.

7. **Relocate or compress the ABM methods paragraph (line 286).** The paragraph beginning "For readers new to ABM..." breaks the narrative momentum of the data-drift case study. Move the technical assumptions to a footnote or a boxed aside, keeping only the sentence about epistemic status ("this is illustrative rather than probative") in the main text.

8. **Consider merging SS9.7 into SS9.5.** "Sharp boundaries in fuzzy territory" is short (18 lines) and thematically continuous with the hierarchy discussion. It would work well as SS9.5.4, "Boundaries within the hierarchy."

9. **Consider merging SS9.8 and SS9.9.** "Passing the tests" and "What does this buy us?" are both summative. A single section ("The verdict and its payoff") would tighten the chapter's close before the natural-experiments section.

10. **Strengthen the Part III design signal.** In the opening paragraph (lines 16--18), add one sentence making the deliberate evidential gradient explicit: something like "We begin with the tightest coupling because the framework's credentials should be established where the evidence is strongest, before we test it against weaker cases."

11. **Replace backtick-style quotes with `\enquote{}`** at lines 310, 392, 416 (and any others using `` ` ... ' `` for translated glosses outside of `\glt` contexts).

12. **Audit `\emph{}` uses.** Review whether `\emph{interface system}` (line 30), `\emph{passive}` (line 237), and `\emph{same set of morphosyntactic properties}` (line 32) should be `\term{}`. If these are meant as introduced concepts rather than ordinary emphasis, use the semantic macro.

---

*Report generated from full chapter read against the book-level editorial report, all 16 chapter precis, and the house style guide.*

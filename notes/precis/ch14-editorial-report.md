# Chapter 14: Grammaticality Itself -- Editorial Report

---

## 1. Argument

The chapter's central claim -- that grammaticality is itself an HPC kind, a maintained coupling between morphosyntactic form and structural meaning -- is the book's deepest recursive move and it works. The "structural meaning" concept is carefully distinguished from compositional semantics and pragmatic felicity, giving the claim bite: grammaticality is specifically the morphosyntactic zipper, not a general evaluative attitude. The dual-role thesis (grammaticality as both category and mechanism, the immune system and the thing the immune system protects) is logically sound and the spinning-top metaphor earns its keep. One argumentative gap: the Homer Simpson thought experiment (line 351) is insufficiently constrained. It asserts that LBE could in principle emerge if social uptake shifts, but nothing in the chapter establishes limits on what maintenance-based contingency rules out. If any constraint can be overridden by enough memetic cachet, the framework loses discriminatory power. The chapter needs either a principled account of why some couplings are harder to shift than others (perhaps via the workaround-density argument from the satiation section, which is already in-chapter but not connected forward to the Homer passage) or an explicit concession that this is an open question.

## 2. Structure

The chapter's section order is well-motivated and builds cleanly: HPC claim, stabilizer, phenomenology, illusions, negative space, gradient, dual role, empirical signatures, relevance, audit, definiteness thread, looking forward. Two structural quibbles. First, the "What doesn't count" section (SS14.4) and its subsection "Grammaticality as a species of appropriateness" (SS14.4.1) do distinct work -- the former carves grammaticality's negative space, the latter positions grammaticality within a broader appropriateness taxonomy. The appropriateness-channel material (Table 14.3, the raised-eyebrow discussion) is substantial enough that it could be its own section rather than a subsection of "What doesn't count." As it stands, the reader encounters the appropriateness argument as a subordinate point when it is in fact a major theoretical commitment. Second, the "Gradient at the boundary" section (SS14.5) is only four paragraphs and largely recaps basin-of-attraction ideas from Ch 5. It reads as a transition paragraph that grew into a section heading. Either give it more distinctive content or fold it into the dual-role section.

## 3. Prose

The chapter's voice is at its best in the opening paragraphs and the illusions section: "The asterisk's the most common symbol in syntax, and one of the least likely to come with operating instructions" (line 5) is excellent, and the Muller-Lyer analogy at line 159 lands perfectly. The mechanism sketch (lines 46--56) is admirably clear. The prose drags in the "Value at every grain" subsection (lines 173--207), which walks through the form-value table grain by grain in a systematic but plodding way -- the reader gets the point by the morpheme level and the remaining grains feel dutiful. The entrenchment-in-action subsection (lines 60--81) is the chapter's strongest sustained passage: the age-expression example, the progressive-aspect cross-linguistic contrast, and the countability callback all land with the right weight and the paragraph on community-indexed entrenchment ("But speakers flow between communities," line 78) is genuinely lively. The phenomenology section's triadic mapping (lines 91--105) is carefully hedged but still feels somewhat schematic -- the qualitative jolt / reactive resistance / normative correction labels are asserted rather than motivated from evidence, and the Peircean connection ("This is the sign-vehicle doing its work," line 95) arrives by fiat.

## 4. Evidence

The evidence base is well-chosen but narrow. The chapter relies on three empirical anchors: garden paths and comparative illusions (Phillips, Wagers, and Lau 2011), syntactic satiation (Snyder 2000, 2022; Reynolds 2026), and individual differences (Dabrowska 2012). These are the right three, but two of the three are handled through summary rather than engagement with specifics -- only the satiation section develops a concrete example at resolution (left-branch extraction with named workarounds). The comparative-illusion example (line 154) is stated but not analysed: *why* does "More people have been to Russia than I have" feel grammatical? The chapter says "each local chunk parses" but doesn't connect this to the mechanism sketch (which local-parsing failure mode does it illustrate?). The cross-linguistic evidence (French/Spanish age expressions, progressive aspect, British/American hospital) is effective as illustration but entirely introspective -- no corpus or experimental data is cited for these contrasts. The schema-drift work (Vagnino and Walker 2026) is a valuable addition, but it is presented as bearing on syntactic satiation without establishing that the conceptual-learning paradigm transfers to morphosyntactic categories.

## 5. Cross-Chapter Coherence

The chapter honours its backward references well: Ch 3 (the question of grammaticality as a kind), Ch 5 (the two-layer model), Ch 8 (the two-diagnostic test), and Ch 13 (the triadic architecture) are all explicitly connected. The forward reference to Ch 15 appears mid-chapter (line 239) but the "Looking forward" section (lines 340--353) skips Ch 15 entirely, jumping from the Homer Simpson thought experiment straight to "the final chapter" (Ch 16). Since Ch 14's own argument about community-indexed entrenchment depends heavily on the social layer that Ch 15 develops, the Looking Forward section should hand off to Ch 15 explicitly.

The term "MMMG" (Morphosyntactic-Meaning Model of Grammaticality) appears three times (lines 311, 313, 315) without being defined anywhere in the chapter or, as far as I can tell, anywhere else in the book manuscript. It is defined in `notes/chapter14-master.md` but that expansion never made it into the chapter. The reader will encounter an undefined acronym. Separately, line 7 uses "natural kind" where the book's own terminological discipline (CLAUDE.md: "Do NOT use 'kind'") calls for "category." The phrase "natural kind" may be deliberately deployed here because the chapter is asking whether grammaticality passes a philosophical test, but if "kind" has been systematically replaced with "category" elsewhere, this instance needs either a footnote justifying the exception or a rewrite.

The "LBE" abbreviation (line 351) is not introduced in this chapter; "left-branch extraction" is written out at lines 277 and 285 but the abbreviation appears only in the Looking Forward section without prior establishment.

## 6. House Style Issues

1. **Markdown emphasis in LaTeX.** Line 285: `the *potential* for extraction is visible` and line 287: `the community has tacitly agreed *not* to use the available mechanism`. These are Markdown-style asterisks that will not render as italics in LaTeX. Should be `\emph{potential}` and `\emph{not}`.

2. **`\emph{}` vs `\mention{}` / `\term{}`.**  Line 23 uses `\mention{Colorless green ideas sleep furiously}` (correct -- it is a cited sentence). Line 237 uses `\emph{feel}` and `\emph{ungrammatical}` where `\emph{}` is fine for emphasis rather than mention. No violations here, but note that line 97 uses `\emph{can't}` for emphasis in the phenomenology section -- consistent.

3. **`\term{kind}` on line 11.** The text reads: "what \term{kind} of thing grammaticality is." Here `\term{}` marks "kind" as a technical term, but the book's terminology has systematically replaced "kind" with "category." If this is a deliberate philosophical use (asking whether grammaticality meets the philosophical threshold for kindhood), it should be flagged with a parenthetical or footnote. If it is an oversight, it should read "category."

4. **Undefined abbreviation.** "MMMG" at lines 311, 313, 315 is never expanded. Either introduce it parenthetically on first use or (better) replace it with a descriptive phrase, since the abbreviation appears only in one subsection and is not used elsewhere in the book.

5. **Undefined abbreviation.** "LBE" at line 351. First use in the chapter should be "left-branch extraction (LBE)" or the abbreviation should be replaced with the full term, given that it appears only once.

6. **`\bigskip` usage.** Line 129 (between phenomenology subsections and the summary) and line 330 (before the definiteness thread). Line 129's `\bigskip` is doing the work of a section break or a `\medskip`; the definiteness thread `\bigskip` is consistent with the running-thread format used in other chapters, so it is fine. But line 129 could be replaced with a proper subsection heading or a `\medskip` for consistency.

7. **Missing `\term{}` on first introduction.** Line 151: "the \term{comparative illusion}" is correctly marked. Line 151 also introduces "Escher sentence" with `\term{}`. Line 247: `\term{standing wave}` is correctly marked. No violations found on first-introduction marking.

8. **Table column widths.** Table 14.1 (lines 107--121) uses `p{0.13\textwidth}` etc., which may cause text to be very cramped in the "Observable marker" and "Falsifier" columns. Worth checking rendered output.

9. **Epigraph dash.** Line 3 uses a Unicode em-dash "---" character before the attribution. This is consistent with other chapters' epigraphs and appears to be the book's convention for epigraph attributions specifically, so not a violation, but worth noting as a departure from the en-dash house style used in running prose.

## 7. Specific Recommendations

1. **Define or replace "MMMG."** Either expand the abbreviation on first use (line 311: "The MMMG (Morphosyntactic-Meaning Model of Grammaticality) framework shares...") or, preferably, remove the abbreviation entirely and use a descriptive phrase ("The maintenance framework" or "the form-value coupling account"), since "MMMG" appears nowhere else in the book and an acronym used only in one subsection adds jargon without earning it.

2. **Fix Markdown emphasis.** Replace `*potential*` (line 285) with `\emph{potential}` and `*not*` (line 287) with `\emph{not}`. These will not render in LaTeX as-is.

3. **Connect the Homer Simpson passage to the workaround-density argument.** The satiation section (lines 277--287) argues that left-branch extraction resists because entrenched workarounds are dense. The Homer passage (line 351) claims LBE could emerge if social uptake shifts. These two claims need explicit connection: does social uptake override workaround density? Would the workarounds have to erode first? A sentence or two bridging the two would prevent the thought experiment from undercutting the chapter's own earlier argument.

4. **Add Ch 15 handoff to "Looking forward."** Line 353 references "the final chapter" (Ch 16) but skips Ch 15 entirely. Add a sentence after line 351 acknowledging that Ch 15 develops the social-stabilization argument that the Homer Simpson thought experiment depends on, before pivoting to Ch 16.

5. **Expand "LBE" at line 351.** Either write "left-branch extraction" in full or add "(LBE)" after the first use at line 277 so the abbreviation is established before the Looking Forward section.

6. **Tighten SS14.4.2 ("Value at every grain").** The grain-by-grain walkthrough (lines 195--207) is dutiful but predictable after the table. Consider cutting the phoneme and morpheme paragraphs to single sentences each and spending the recovered space on the constructional and clause-type levels, which do more distinctive work.

7. **Promote "Grammaticality as a species of appropriateness" to a full section.** The appropriateness-channel argument (lines 209--241) is a major theoretical commitment currently buried as a subsection of "What doesn't count." Promote it to `\section{Grammaticality as a species of appropriateness}` and rename the residual negative-space material to `\section{What doesn't count}`.

8. **Decide on the status of SS14.5 ("The gradient at the boundary").** It currently recaps Ch 5's basin-of-attraction model in four paragraphs. Either give it new content specific to grammaticality (e.g., a concrete case of a sentence poised on the rim, with the basin metaphor applied to a specific construction) or fold the section into the dual-role section as a transition paragraph.

9. **Motivate the three-register phenomenology independently of Peirce.** The qualitative jolt / reactive resistance / normative correction triad is introduced as mapping onto sign / object / interpretant, but the phenomenological evidence for three distinct registers (rather than one gradient) is thin. Either cite independent evidence for the dissociability of the three layers (the table's falsifiers point to this but the text does not develop it) or explicitly concede that the triad is a structuring heuristic pending empirical decomposition.

10. **Resolve "natural kind" vs "category" at line 7.** If the philosophical question specifically requires "natural kind" (because the chapter is asking whether grammaticality passes Boyd's test), add a parenthetical: "a natural kind -- or, in this book's terms, a genuine HPC category." If the term is unintentional, replace with "category."

11. **Develop the comparative-illusion example.** Line 154 states the example but does not connect it to the mechanism sketch. Add a sentence explaining which component of the detector loop is misfiring: local-constraint satisfaction passes (processing channel reports low load), but global compositionality fails (coupling state is actually broken). This would demonstrate that the mechanism sketch has diagnostic utility, not just descriptive elegance.

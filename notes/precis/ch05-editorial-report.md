# Chapter 5: Editorial Report

*"Discrete from continuous" -- deep editorial read against the full book arc, house style guide, and all 16 chapter precis.*

---

## 1. Argument

The chapter's core argument is sound and well-sequenced: continuous substrates produce discrete categories via scale-dependent tolerance, formalised with hyperreals and maintained by HPC mechanisms. The two-component answer (geometry + maintenance) is the right move for the book at this stage, and the chapter earns its place as the bridge between Ch 4's introduction of HPC kinds and Ch 6's mechanism inventory. One logical gap: the chapter asserts that the hyperreal formalism yields predictions that "simpler threshold-plus-noise models" cannot (the precis flags this too), but never actually shows what a threshold-plus-noise model would predict differently. Without that contrast, the reader has to take on trust that the hyperreal apparatus is doing work beyond licensing the vocabulary of "sharp but inaccessible." A second, smaller gap: the claim that "fuzzy realism doesn't" capture scale-dependent tolerance (line 135) is asserted but not demonstrated -- Khalidi's position is stated fairly, but the argument against it is phenomenological ("speakers don't behave as if categories shade continuously") rather than structural. What specific behavioural evidence distinguishes the hyperreal prediction from the fuzzy-realist prediction?

## 2. Structure

The chapter's three-act structure (puzzle, formal solution, empirical consequences) is clear and well-paced. The skip path for the formal section (line 72) is a smart concession to the dual audience. Two structural issues. First, the "From heaps to categories" section (5.3.1) does double duty: it introduces the multi-dimensional generalisation *and* develops the metric question *and* works the evidentiality example *and* introduces the basin visualisation. This is the longest subsection in the chapter and it sags in the middle -- the Gower-distance material (lines 163-184) is necessary but reads like a methods appendix inserted into a conceptual narrative. Consider splitting: the metric construction could be a boxed aside (parallel to the skip path) or a dedicated subsection. Second, the multi-category section (5.3.3) runs from *fun* through reciprocals through Shilluk through the convergence/homology question to the "have we learned anything?" coda -- five distinct moves in one subsection. The reciprocals discussion alone runs ~100 lines. This material is excellent but its structural subordination (all under "Multi-category spaces") understates its importance.

## 3. Prose

The opening autobiographical paragraph is the chapter's strongest writing -- it earns the personal register by being precise about dates, names, and intellectual debts, and "I've learned to treat the act of naming a folder as the weakest possible form of commitment" is a line that rewards re-reading. The prose stays sharp through the formal section, which is a genuine achievement. It softens in the middle of 5.3.1, where the Gower-distance exposition and the basin-landscape footnote (line 196) shift into textbook register -- competent but less distinctive. The summary section (5.3.5) recovers well; the streetcar simile (line 417) lands. One tonal risk: the chapter opens in first person and closes in third-person theoretical voice, and the transition is unmarked. The first person disappears after the opening and resurfaces only once ("My aim isn't to force a verdict," line 308). This is fine, but a sentence acknowledging the shift when it happens (around the formal section) would smooth the seam.

## 4. Evidence

The evidence is well-chosen and well-layered. The *fun* COHA heatmap (Figure 5.3) is the chapter's showpiece -- it operationalises "convergent adjectivalisation" in a way no prose description could. The reciprocals case study, drawing on Reynolds (2025), is the strongest empirical anchor: it demonstrates that "distance to boundary" is measurable and that in-betweenness is robust under analytic perturbation. The Shilluk comparison does useful cross-linguistic work. Two evidence concerns. First, the chapter's empirical predictions (variance peaks near boundaries, structured drift under perturbation) are stated but not tested here -- the chapter relies on Sprouse et al. (2013) and Dabrowska (2010) as partial confirmation, but both are cited in a single paragraph (line 366) and neither is discussed in enough detail to assess how well the prediction actually matches. The reader is told the data "already points in this direction" but not shown. Second, the evidentiality example (lines 192-194) is introduced and dropped in three sentences. It does conceptual work (alignment failure without semantic loss), but it feels like a drive-by illustration rather than a developed case.

## 5. Cross-chapter coherence

The chapter's backward connections are solid: it picks up the phase-transition analogy from Ch 3, the HPC commitment from Ch 4, and the mechanism list from Ch 4's preview. Its forward connections are well-placed: the definiteness thread (line 434) sets up Ch 10; the grammaticality-as-HPC promise (line 386) sets up Ch 14; the mention of "the stabilisers" defers properly to Ch 6. One missed connection: the chapter discusses dual membership (5.3.4) and the overlap of preposition/adjective basins, but doesn't connect to Ch 11's later treatment of lexical categories, where the adjective-as-plumage diagnosis and the "mechanism density gradient" are the core moves. A forward reference here would strengthen the payoff when Ch 11 arrives. A terminology note: the chapter uses "natural kind" (lines 323, 325, 337) in several places, but the book's CLAUDE.md notes a terminological decision to use "category" throughout and avoid "kind." The usage here is defensible (it's engaging with philosophy-of-science literature that uses the term), but the reader may wonder whether "natural kind" and "HPC category" are the same thing -- a parenthetical clarification on first use would help. The "two-layer model" (grammaticality vs. acceptability) introduced here becomes load-bearing in Ch 14; the connection is flagged but the label "two-layer model" doesn't appear to recur in Ch 14's precis, which uses "coupling" and "zipper" instead. Worth checking for terminological consistency.

## 6. House style issues

**En-dash/em-dash:** The chapter uses `~--` consistently for parenthetical dashes throughout (good). No em-dashes found.

**`\term{}` vs. `\mention{}` vs. bare italics:** Generally correct. However:
- Line 32: `\term{dynamic discreteness}` -- correct (introducing a technical term).
- Line 213: `\term{real gradience}` -- correct.
- Line 247: `\term{crosscutting kinds}` -- correct (introducing Khalidi's term).
- Line 83: `\emph{infinitesimals}` -- should be `\term{infinitesimals}` if introducing the technical term, or left as `\emph{}` if merely emphasising. Given the context ("extend the reals with *infinitesimals*"), this is introducing a term and should be `\term{}`.
- Line 83: `\emph{negligible relative to the current scale}` -- emphasis, not mention or term introduction. `\emph{}` is appropriate here.
- Lines 93, 104, 110, 111, 127, 135, and elsewhere: `\emph{}` is used for emphasis throughout the formal section. Most of these are genuine emphasis and are fine. But line 127 ("predicts structured boundary *drift*") introduces "drift" as a semi-technical concept that recurs later; consider `\term{}`.

**`\enquote{}` vs. bare quotes:** Correctly used throughout. No bare double-quote marks found.

**`\mention{}` for linguistic forms:** Consistently used for *fun*, *near*, *otherwise*, *pin*, *pen*, *each other*, *one another*, etc. Correct.

**Contractions:** Present and natural throughout ("don't," "can't," "isn't," "won't"). Good.

**Paragraph length:** Most paragraphs are within the ~60-100 word target. The paragraph at lines 196 (basin-landscape footnote) is a single footnote running ~120 words -- acceptable for a footnote. The paragraph beginning "Basin structure emerges" (line 205) runs long (~130 words) and could be split after "balanced."

**Section headings:** The `\subsection{Summary: discreteness without essence}` heading uses a colon, which is fine but unusual in the book. Check consistency with other chapters' summary headings.

**Cross-reference style:** Line 72 uses `§\ref{sec:5:geometry-to-mechanism}` -- correct. Line 137 uses `§\ref{sec:4:heterogeneity}` -- cross-chapter reference, fine. Line 323 uses `§\ref{sec:3:lexeme-obsession}` -- fine.

**`\textsc{}` for cross-linguistic categories:** Lines 323-325 use `\textsc{gender}` and `\textsc{number}` -- correct. Line 335 uses `\textsc{noun}` and `\textsc{verb}` -- correct.

**One potential issue:** Line 306 has `*\mention{Each other left}` -- the asterisk is outside the `\mention{}` macro. The house style uses `\ungram{}` for ungrammaticality markers. This should be `\ungram{\mention{Each other left}}` or the construction used elsewhere with `\ea` examples. Similarly, line 308 has `*\mention{each other friends}` -- same issue. And 2 more instances in the dual-membership section.

## 7. Specific recommendations

1. **Add a threshold-plus-noise comparison.** After the hyperreal formalism (end of 5.2.2 or start of 5.3), add 3-5 sentences explicitly stating what a simpler threshold model would predict and where the hyperreal model diverges. This is the chapter's most important promissory gap -- the formalism needs to earn its keep against a simpler competitor, or the skip-path readers will reasonably conclude they missed nothing.

2. **Split section 5.3.1 ("From heaps to categories").** The Gower-distance construction (lines 163-184) should be either a boxed aside or a separate subsection (e.g., "5.3.2 The metric question"), with the current 5.3.2 and following renumbered. This section currently runs ~200 lines and covers five distinct topics.

3. **Fix ungrammaticality marking.** Lines 306 and 308 use bare `*` before `\mention{}`. Replace with `\ungram{}` per house style, or restructure as numbered examples with judgment markers.

4. **Add a forward reference to Ch 11 in the dual-membership section (5.3.4).** Something like: "Chapter 11 develops this gradient in detail, showing that adjective-hood is thinner than noun-hood or verb-hood because the mechanisms maintaining it are shallower."

5. **Develop the Khalidi contrast (line 135-137).** The dismissal of fuzzy realism rests on "speakers don't behave as if categories shade continuously." Name the specific behavioural evidence: abrupt transitions in categorisation tasks, bimodal rather than unimodal judgment distributions, structured (not uniform) variance near boundaries. Three sentences would do it.

6. **Clarify "natural kind" vs. "category" on first use.** Line 323 is the first occurrence of "natural kind" in the chapter. Add a parenthetical: "(the philosopher's term for what this book calls a category)" or similar. This prevents a terminological collision that will only get worse as the book proceeds.

7. **Convert `\emph{infinitesimals}` (line 83) to `\term{infinitesimals}`.** This is a term introduction, not emphasis.

8. **Trim or develop the evidentiality example (lines 192-194).** As it stands, three sentences introduce and discard an entire cross-linguistic phenomenon. Either develop it into a proper contrast case (4-5 sentences, with a specific language example) or cut it and let the Shilluk case in 5.3.3 carry the cross-linguistic weight.

9. **Break the long paragraph at line 205.** Split after "balanced" (around "This is Gardenfors's criterion...") to keep paragraph length within the ~100-word target.

10. **Check "two-layer model" terminology against Ch 14.** Ensure the label recurs when Ch 14 develops the grammaticality/acceptability distinction. If Ch 14 uses different terminology ("zipper," "coupling"), add a bridging sentence in Ch 14 linking back to the "two-layer model" introduced here.

11. **Consider whether the convergence/homology discussion (lines 334-337) should be deferred.** The distinction between convergent and homologous mechanisms is important for the book but is introduced here in a single paragraph and then dropped. It would be more powerful in Ch 13 (the synthesis chapter), where the full typological evidence is in view. Here it reads as a promissory aside.

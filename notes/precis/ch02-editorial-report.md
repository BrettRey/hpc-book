# Chapter 2: Editorial Report

*Based on a full read of `chapters/chapter02.tex` against the book-level editorial report, all 16 chapter precis, and the house style guide.*

---

## 1. Argument

The chapter's argument is sound and does precisely what the book needs at this position: it converts the accessible, example-driven "words won't hold still" survey of Ch 1 into a theoretical diagnosis. The move from "definitions fail" to "definitions fail in a specific way that blocks a specific question" (SS2.5) is the chapter's best contribution, and the verbless-clause microcosm earns its load-bearing role by returning three times with increasing depth. The distinction between essence and determinacy in SS2.1 is well-handled and genuinely needed for what comes later (Ch 4's HPC apparatus requires determinacy without essence). One gap: the chapter asserts that structuralism's relational metaphysics "didn't translate into tolerance for indeterminate membership" but does not demonstrate this. A structuralist familiar with glossematics or Firthian prosodic analysis might object. A sentence acknowledging that some structuralist traditions did tolerate indeterminacy -- but that this tolerance was not transmitted to the descriptive and generative mainstream -- would close the gap without slowing the pace.

## 2. Structure

The chapter's organisation is strong. The sequence -- what essentialism built (SS2.1), where it works (SS2.2), when criteria diverge (SS2.3), the microcosm (SS2.4), the diachronic problem (SS2.5), the blocked question (SS2.6), the biological parallel (SS2.7), why essentialism persists (SS2.8), conclusion (SS2.9) -- builds cumulative force. The placement of the "where essentialism works" section before the critique is a shrewd rhetorical move (Rapoport's Rules in action). One structural issue: the five `\bigskip` markers (lines 27, 62, 74, 80, 170) function as section breaks within sections but lack headings, creating a somewhat episodic feel in SS2.1--2.2. The `\bigskip` at line 27 before the Aristotle clarification is particularly notable: this is important intellectual history that deserves either integration into the preceding flow or its own subsection heading. As it stands, it reads like an inserted note.

## 3. Prose

The prose is at its best in the opening and the diachronic section. The first four paragraphs are devastating: the CGEL verbless-clause contradiction is delivered with surgical precision, and the rhythm of "Clauses are identified by their verbs. These clauses have no verb." lands perfectly. The diachronic section (SS2.5) achieves the book's characteristic voice -- analytically rigorous but propulsive, with the standing-wave metaphor doing real conceptual work rather than decorating. The sociology-of-essentialism section (SS2.8) is efficient but slightly flat compared to what precedes it; the publication-norms paragraph tries to be witty ("The library's classification system would be disputed") but the setup is long enough that the payoff arrives late. A few passages run hot: "The framework treats this as normal procedure -- but the error lies in the framework itself" (line 153) is tonally confident in a way that earns its force; "Definitions feel like progress" (line 276) is an excellent sentence. The Smilodon/Thylacosmilus passage has vivid prose ("Place them side by side and you see the same animal, arrived at twice") that earns its length.

## 4. Evidence

The evidence is well-selected and well-layered. The CGEL verbless clause is the chapter's running example and it works: specific enough to be checkable, important enough to be consequential. The subject/phoneme/will trinity covers syntax, phonology, and diachrony without overlap. The Smilodon/Thylacosmilus convergence case is effective and pays forward to Ch 4's mechanism-seeking move. Two concerns. First, the treatment of structuralist anti-essentialism (lines 34--35) is thin relative to the claims it makes; a single sentence on Hjelmslev or Firth would substantiate the assertion about what "survived into practical work." Second, the chapter does not address the possibility that Huddleston and Pullum might simply accept the verbless-clause inconsistency as a principled trade-off (a "best overall analysis" rather than a symptom of failure). The chapter's argument is stronger if it acknowledges and then refutes this defence rather than treating the inconsistency as self-evidently damning.

## 5. Cross-chapter coherence

The chapter sets up Ch 3 cleanly (the closing paragraph names nominalism and gradience as the next targets) and Ch 4 (the biological parallel and "mechanism-seeking" frame are explicitly promissory). The standing-wave metaphor (line 193) is load-bearing for the rest of the book and appears again in Ch 5's dynamic-discreteness framework; the connection is implicit but clear. The term "stabiliser" does not appear in Ch 2, which is correct -- Ch 6 introduces it. The "blocked question" framing (SS2.6) is exactly what Ch 4 answers, and the handoff is well-executed. One concern flagged in the book-level report: Ch 1 and Ch 3 both have orphaned Parallel Architecture paragraphs, but Ch 2 does not mention Culicover and Jackendoff at all. If the Parallel Architecture thread is to be consolidated (probably in Ch 3), Ch 2's silence is fine. But if it remains in Ch 1, the reader may wonder why Ch 2 doesn't engage with it. The terminology distinction between "class" and "category" is introduced in SS2.2 (line 54: "I reserve *category* for natural kinds throughout") -- this is a crucial load-bearing commitment that persists through Ch 8's failure modes and Part III. It should be indexed.

## 6. House style issues

**En-dash vs. em-dash:** No em-dashes detected; en-dashes with `~--` are used consistently. Good.

**`\term{}` usage:** Mostly correct. However, several category/concept terms appear without `\term{}` where first introduced or where the distinction matters:
- Line 126: "the category is identified by a preponderance of properties" -- `\term{category}` would be appropriate here given the load-bearing distinction being drawn.
- Line 204: "Which criterion is correct?" uses `\emph{}` (via `\emph{Which criterion is correct?}`) for rhetorical emphasis, which is fine and distinct from `\term{}`.

**`\mention{}` usage:** Well-applied for linguistic forms throughout. One missed instance:
- Line 164: `\mention{-hood}` is correctly marked, but "a period of time" is a meaning gloss rendered in `\enquote{}` -- this is correct per style guide.

**`\enquote{}` usage:** Consistently applied for quotations. Correct.

**`\textit{}` vs. semantic macros:** Line 12 uses `\textit{CGEL}` for the title of a work. This recurs at lines 143, 149, 151, 155, 155, 289. The question is whether CGEL should have a dedicated command or remain as `\textit{}`. Since it is a work title, `\textit{}` is defensible, but six instances suggest a `\cgel` shorthand might be warranted. (Not strictly a house-style violation, but worth noting.)

**`\bigskip` as section separator:** Lines 27, 62, 74, 80, 170 use `\bigskip` as informal section breaks. The style guide does not explicitly prohibit this, but five instances in a single chapter is heavy. Consider whether some of these transitions could be handled with paragraph breaks alone or promoted to subsections.

**Table caption:** Lines 111--118, the caption for Table 2.1 mentions "definitional, distributional, diachronic, and operational criteria" but the table columns are "Definitional crispness," "Distributional coherence," and "Operationalisability" -- three columns, not four. The caption lists four criteria (including "diachronic") that the table doesn't visually represent. The caption should match the columns.

**Index entries:** The density of `\ixsq{}`, `\ixnq{}`, `\ixlq{}`, `\ixgq{}` entries is high and consistent, which is good. One potential issue: `\ixsq{essentialism}` appears dozens of times in a chapter entirely about essentialism; this will produce a long undifferentiated page range in the index. Consider using sub-entries (e.g., `\ixsq{essentialism!achievements}`, `\ixsq{essentialism!persistence}`) to make the index entry useful.

## 7. Specific recommendations

1. **Fix the Table 2.1 caption** (lines 111--118). The caption mentions four criteria (definitional, distributional, diachronic, operational) but the table has three columns. Either add a "Diachronic stability" column or remove "diachronic" from the caption text.

2. **Integrate or subsection the Aristotle clarification** (lines 29--38). The `\bigskip` + "A clarification is needed here about intellectual history" reads like an inserted aside. Either fold the Aristotle material into the preceding paragraphs with a transitional sentence, or give it a subsection heading (e.g., `\subsection{The target isn't Aristotle}`). The material is important -- it pre-empts the objection that the book is attacking a straw man -- but its current framing as an interruption weakens it.

3. **Acknowledge the principled-trade-off defence of CGEL.** The chapter treats the verbless-clause inconsistency as self-evidently problematic, but Huddleston and Pullum might argue it is a deliberate trade-off (accepting local criterion-switching for global descriptive coverage). A sentence in SS2.4 acknowledging this and explaining why it is still evidence of essentialism's limits would strengthen the argument.

4. **Substantiate the structuralism claim** (lines 34--35). Add one concrete example (Hjelmslev's glossematics, Firth's prosodic analysis, or Harris's distributional indeterminacy) to support the assertion that the relational metaphysics "didn't translate into tolerance for indeterminate membership." A parenthetical citation would suffice.

5. **Reduce `\bigskip` density.** Five `\bigskip` breaks in one chapter creates a choppy visual rhythm. The breaks at lines 62, 74, and 80 (within SS2.2) could be replaced by ordinary paragraph transitions. The break at line 170 (within SS2.5) separates the general diachronic claim from the `will` case study and could remain, but a transitional sentence would be smoother.

6. **Add sub-entries to the `essentialism` index.** The current `\ixsq{essentialism}` will produce a single index entry spanning almost every page of the chapter. Break into sub-entries keyed to sections: `essentialism!achievements`, `essentialism!diachronic problem`, `essentialism!persistence`, etc.

7. **Consider a `\cgel` macro.** `\textit{CGEL}` appears at least six times in the chapter and will recur throughout the book. A dedicated macro (`\newcommand{\cgel}{\textit{CGEL}}`) would simplify maintenance and ensure consistency.

8. **Sharpen the sociology section's payoff.** The "library's classification system would be disputed" line (end of the publication-norms paragraph, line 272) arrives after a long windup. Consider cutting one sentence from the setup (the Postal/Abney digression could be tightened) to bring the wit closer to the claim.

9. **Thread the "class" vs. "category" distinction forward.** The terminological commitment at line 54 ("I reserve *category* for natural kinds throughout") is a major decision that shapes the rest of the book (especially Ch 8's failure-mode diagnostics). Ensure it is indexed and consider a footnote cross-referencing Ch 8 where the distinction becomes load-bearing.

10. **Minor: line 12 underline macro.** `\uline{their hands above their heads}` and `\uline{no longer a minister}` -- verify these render correctly under the `ulem` package with `normalem` option. The use is correct, but `\uline` within `\mention{}` can produce formatting conflicts if the two overlap elsewhere in the book.

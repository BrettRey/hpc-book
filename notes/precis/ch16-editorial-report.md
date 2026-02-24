# Chapter 16 Editorial Report: What Changes

---

## 1. Argument

The chapter's argument is sound and appropriately scoped: it does what a final chapter should do by converting the book's theoretical apparatus into falsifiable commitments. The three-debts/gauntlet structure (show clustering, identify stabilisers, demonstrate projection, then predict and stress-test) is the right instrument for a closing chapter. The dual stress tests -- the essentialist's best case (mechanism-light projection) and the nominalist's best case (baseline parity) -- are genuinely well-constructed; they put the framework at risk from both sides of the debate the book opened in Chapters 1--3, which gives the ending structural symmetry with the beginning. One logical gap: the chapter asserts that the conditioned-vs-pooled comparison from Ch 15 is "the same test" applied across all rows of Table 16.1, but this flattens a genuine disanalogy. The conditioned model was developed for sociolinguistic variation (register, community); applying it to countability or lexical categories requires different conditioning variables (semantic domain, morphological context), and the chapter doesn't acknowledge that the "same test" is actually a family of tests with shared logic but different operationalisations.

## 2. Structure

The section ordering is mostly right. The progression from ontological framing (SS16.2) through synthesis ledger (SS16.3) to empirical predictions (SS16.4) to falsification conditions (SS16.5) to operationalisation (SS16.6) follows a natural deductive tightening. The new "Research agenda" section (SS16.7) sits well between "Operationalizing the gauntlet" and the conclusion: it collects the book's accumulated IOUs in one honest ledger, which is exactly what the book-level editorial report (item 6) recommended. The section earns its place. One structural concern: SS16.2 ("No level privilege, no level immunity") is three paragraphs of ontological positioning that overlap substantially with the conclusion (SS16.8), which re-states the Ladyman and Ross commitment and the scale-dependent ontology claim. The chapter would tighten if SS16.2's content were folded into the conclusion, letting the chapter move directly from the gauntlet figure into the synthesis ledger.

## 3. Prose

The voice is right for a closing chapter: clipped, declarative, deliberately austere. "A theory that survives every possible result explains nothing; if it can't lose, it can't win" (line 8) is one of the best opening lines in the book. The *data* conference-Q&A vignette (line 104) is vivid and instantly legible. The suitcase-zipper image in the conclusion (line 252) is effective precisely because it is domestic rather than technical. Where the prose drags: the operationalisation section (SS16.6, lines 200--226) reads like a methods preregistration rather than a book chapter; "hierarchical models for variance structure, changepoint or state-space methods for lag estimates, held-out log-loss on out-of-construction splits" (line 224) is a list that only a quantitative linguist would parse, and it risks losing the generalist reader the book has been cultivating. The sentence "The details belong in a preregistration, not a book chapter" (line 224) knows this but doesn't fix it -- it concedes the problem without solving it. Consider cutting the technical enumeration and letting the sentence stand alone.

## 4. Evidence

The *data* example is well-chosen and well-deployed: it is mid-shift, measurable, and familiar to any academic audience. But the chapter leans on it exclusively, and this creates a vulnerability the book-level report already flagged. No second case is developed at comparable resolution. A brief second pass through, say, the *fun* drift (from Ch 1 and Ch 5) or the *be like* quotative (from Ch 6) -- even at half the resolution of *data* -- would demonstrate that the gauntlet generalises rather than merely fitting one noun's trajectory. The synthesis ledger (Table 16.1) does useful bookkeeping but is backward-looking (summarising earlier chapters' commitments) rather than forward-looking (showing the gauntlet in action). The new Research Agenda section (SS16.7) partially addresses this by collecting the IOUs, but it remains a catalogue of debts rather than a demonstration of payment. The gauntlet table (Table 16.2) is the chapter's most operationally useful contribution.

## 5. Cross-chapter coherence

The new Research Agenda section (SS16.7) directly addresses the book-level report's concern (item 6) about accumulated promissory content: it collects seven open fronts with specificity. This is a significant improvement. Cross-references to earlier chapters are handled well: the *data* case threads through Ch 9 (countability), the conditioned-vs-pooled test through Ch 15, the zipper through Ch 13. One notable absence: Ch 8's failure-mode audit template (the seven-step instrument) is the direct ancestor of the gauntlet, but the chapter doesn't explicitly connect the two. A sentence in SS16.1 noting that the gauntlet extends the Ch 8 audit from single-case diagnosis to cross-domain falsification would close the loop. The chapter also doesn't pick up on Ch 13's discourse-level gap except in the Research Agenda -- the zipper metaphor is used repeatedly but the missing discourse tooth is never acknowledged in the main argument. The chapter's final line ("Words that won't hold still can still hold together -- until they don't") echoes the title of Ch 1 effectively, closing the frame.

## 6. House style issues

**En-dash/em-dash.** Line 3: `— James Ladyman` uses an em-dash. House style requires an en-dash with spaces for attributions. Should be `-- James Ladyman` (or use the `\epigraph` command's built-in formatting if it handles this). The epigraph macro likely handles the dash, but verify.

**\mention{} and \term{} usage.** Generally correct. Line 113 has `\term{meta-Occam\ixsq{meta-Occam}}` which is correct (introducing a technical concept). Line 115 uses `adjective\ixsq{adjective}` without `\term{}` or `\mention{}` -- this should be `\term{adjective}` in at least the first instance, since it is a category name being used in a technical sense. Similarly, line 115 has `category\ixsq{category}` bare where `\term{category}` would be appropriate in at least one occurrence. And 3 more instances of bare `category\ixsq{category}` in lines 169, 183, 188.

**Index entries in running text.** The chapter has extensive `\ixsq{}`, `\ixlq{}`, `\ixnq{}` indexing, which is fine. But several index entries appear to be attached to words that don't need semantic markup (e.g., `alignment\ixsq{alignment}` at line 256 without `\term{}`). The index commands are correctly placed, but where the indexed term is also being used technically, the semantic macro should wrap the visible text.

**Contractions.** The chapter uses contractions well and consistently: "can't," "don't," "isn't," "we're," "won't." No violations.

**Quotation marks.** `\enquote{}` is used correctly throughout (lines 104, 162, 167, 254, 258). No bare quotation marks.

**Paragraph length.** Most paragraphs are within the ~60-word target. The Research Agenda paragraphs (SS16.7) tend to run longer -- the countability paragraph (lines 233--234) is approximately 80 words, which is acceptable, but the pro-form gender paragraph (lines 239--240) runs to roughly 90 words. Neither is a violation of the 100-word guideline, but they are denser than the rest of the chapter.

**Bold/lists.** The Research Agenda section uses `\textsc{}` labels for each domain (Countability, Definiteness, etc.) as paragraph openers. This is a reasonable structural choice for a ledger-style section and doesn't violate the style guide's prohibition on bold labels, since small-caps topic markers are used elsewhere in the book for running threads.

## 7. Specific recommendations

1. **Add a second gauntlet case at sketch resolution.** The *fun* drift (introduced in Ch 1, developed in Ch 5) would take 300--500 words and would show the gauntlet operating on a different category boundary (noun-to-adjective rather than count-to-mass). Insert after the *data* operationalisation in SS16.6 or as a brief subsection before the Research Agenda. This is the single change most likely to strengthen the chapter.

2. **Trim SS16.2 ("No level privilege") and fold its content into the conclusion.** The Ladyman-and-Ross ontological commitment is stated in the epigraph (line 3), restated in SS16.2 (lines 111--112), and restated again in the conclusion (lines 256--257). Three statements of the same principle is two too many. Move the meta-Occam and comparative-concept paragraphs (lines 113--115) to the conclusion and cut SS16.2 entirely.

3. **Explicitly connect the gauntlet to Ch 8's audit template.** In SS16.1, after "Figure~\ref{fig:16:gauntlet} maps the evaluation pathway" (line 12), add a sentence: something like "The template extends the seven-step audit from Chapter 8 to the cross-domain level: what worked for diagnosing single categories now becomes a falsification instrument for the framework itself."

4. **Cut or compress the technical enumeration in SS16.6.** Lines 224--226 ("The machinery is straightforward: hierarchical models for variance structure...") can be reduced to "The statistical machinery -- variance decomposition, changepoint analysis, held-out prediction -- belongs in a preregistration, not a book chapter." This preserves the gesture without alienating non-quantitative readers.

5. **Fix the \term{} markup on bare category names.** Line 115: first instance of `adjective` should be `\term{adjective}`. Line 115: `category` as a technical term should get `\term{}` on at least one instance per paragraph where it is doing load-bearing theoretical work.

6. **Check the epigraph dash.** Line 3: verify whether `\epigraph` handles the attribution dash automatically. If the em-dash is manually inserted, replace with en-dash per house style.

7. **Consider whether the Research Agenda needs a brief framing coda.** The section's final paragraph ("That's seven open fronts...") is strong, but the transition to the conclusion is abrupt. A single bridging sentence -- e.g., "The gauntlet is the instrument; the agenda is the programme" -- would smooth the joint.

8. **Address the conditioned-vs-pooled disanalogy.** In SS16.3 (line 122), where the chapter claims all rows face "the same test," add a parenthetical or footnote acknowledging that the conditioning variables differ across domains (register and community for social stabilisation; semantic domain and morphological context for countability) while the inferential logic is shared.

---

*Report based on the full chapter text and cross-referenced against all 16 chapter precis, the book-level editorial report, and the house style guide.*

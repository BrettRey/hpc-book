# Chapter 13 Editorial Report: The Category Zipper

---

## 1. Argument

The chapter's central claim -- that the HPC diagnostic logic is scale-invariant and what changes across levels is the coupling regime -- is sound and does exactly what the book needs at this point. It converts four independent case studies into points on a single gradient, which is the architectural payoff Part III has been building toward. The argument earns its right to generalise by including negative cases and designed-to-fail controls, which is philosophically responsible and rhetorically effective. One weakness: the scale-invariance claim is asserted for discourse (Table 13.x, line 202) but never tested or even illustrated. An untested fifth tier that appears only in a table row weakens the claim to invariance rather than strengthening it. The chapter should either give discourse a brief subsection with at least one worked example, or explicitly scope the claim to four tiers and mark discourse as a predicted extension.

## 2. Structure

The controlled ascent (phonemes, words, grammar, constructions) is the right architecture, and the interposition of the negative-cases section between grammar and constructions is well judged -- it prevents the reader from feeling that the framework rubber-stamps everything. The stabiliser-weighting map (SS13.5) and the mediation gradient (SS13.6) both follow logically, but they feel like two codas rather than one resolution. SS13.6 in particular reads as a restatement of SS13.5 in Peircean vocabulary; the précis flags this and the book-level report echoes it. The question is whether SS13.6 does explanatory work that SS13.5 alone cannot. If it does (and the argument that the interpretant's *role* shifts is genuinely distinct from saying that *which stabilisers dominate* shifts), then the section needs a sharper opening sentence that names the added value. If it doesn't, fold SS13.6's key paragraph into the end of SS13.5 and save a section.

The final section, "The architecture of maintenance" (SS13.8), tries to do three things: restate the scale-invariance claim, introduce the "zone of maximum systematicity," and bridge to Ch 14 via the packaging-tightness metric. The packaging-tightness material (lines 249--253) feels like it belongs in the Ch 14 opening rather than here; it introduces a new empirical result and a new term (`packaging tightness`) that the chapter hasn't earned through its own argument.

## 3. Prose

The chapter's best writing is in SS13.4 (negative cases) and in the transitional paragraphs between tiers (lines 65--67, 94--96). The voice is confident without being bombastic: "A framework that never says no is no more than a vibe" (line 132) is exactly the right register. The zipper metaphor is well-deployed and not overworked.

Where the prose drags is in the constructions section (SS13.5, lines 150--181). The footnote density is the highest in the chapter (seven footnotes in 30 lines), and they carry methodological hedges that interrupt the argument's forward motion. The reader is asked to trust that Appendix material justifies the claims, but the main text doesn't tell a clean story between the hedges. The HistWords passage (lines 88--90) similarly tries to pack too much quantitative detail into continuous prose; the parenthetical about macro-F1 = 0.84 feels like a reporting obligation rather than a move in the argument.

The mediation gradient (SS13.6) is the chapter's weakest prose. Each paragraph opens with "At the [level] level" (lines 218, 220, 222, 224), creating a plodding four-beat repetition. The section could be substantially compressed -- the content of these four paragraphs is already implicit in Table 13.x and in the coupling-spectrum figure.

## 4. Evidence

The evidence is well-chosen at the extremes and thinner in the middle. The phoneme tier (PHOIBLE data, /y/ logistic model, pin/pen stress test) and the construction tier (ten-construction battery, ablation, designed-to-fail controls) are both impressively operationalized. The word tier (HistWords, go/went, Bybee's frequency-regularisation gradient) is persuasive. The grammar tier, however, is handled entirely by back-reference to Part III -- no new evidence is introduced. This means the chapter's own evidential centre of gravity sits at the endpoints of the gradient, not in the territory it claims is "most interesting and most contentious" (line 226). Even a single new observation about how a grammatical-category boundary behaves differently from a phoneme boundary under perturbation would ground the middle of the gradient in original evidence.

The Mohawk example (line 138) does useful work as a negative case but rests on a single word from Baker (1996: 40). A second example from a different polysynthetic family would strengthen the "heterogeneous routes" claim.

## 5. Cross-chapter coherence

The chapter fulfils its role in the book's arc well: it synthesises Part III and bridges to Part IV. The coupling continuum was introduced in SS8.6 (the "coupling coda"), and this chapter is the payoff. The section references to Ch 7 (SS7.3 triadic structure, SS7.5 field-relative projectibility) and Ch 8 (SS8.6 coupling, SS8.5 negative diagnosis) all resolve correctly.

The book-level report (SS5c) flags that the coupling coda in Ch 8 is "substantial enough to feel like a distinct theoretical contribution." Ch 13's dependence on it confirms that it is. If Ch 8's coda doesn't get a section heading or a more explicit framing, a reader who skimmed Ch 8's final pages will arrive at Ch 13 unprepared.

The discourse gap is a genuine cross-chapter problem. Ch 14 (grammaticality itself) focuses on the morphosyntactic level; Ch 15 (social stabilisation) addresses inter-speaker alignment but not discourse-level categories (speech acts, conversational structure). If discourse is in the table but nowhere in the text of Chs 13--16, the gap should be acknowledged explicitly.

The book-level report (SS6) notes that promissory content accumulates. Ch 13 adds: resultative subtype stratification, discourse-level evidence for the zipper, and the 25% downsampling prediction (line 234). These join a growing list of IOUs. The predictions section (SS13.7) would benefit from flagging which predictions are unique to this chapter and which are retrievals from earlier chapters.

## 6. House style issues

1. **`\textit{}` for linguistic data (line 138):** The Mohawk word `Washakotya'tawitsherahetkvhta'se` is wrapped in `\textit{}` rather than `\mention{}`. This is a linguistic form being cited; house style requires `\mention{}`.

2. **Backtick glosses (line 138):** The two inline glosses use raw backtick+single-quote pairs (`` `he made the thing...` `` and `` `he ruined her dress' ``). These are translation glosses, which is conventional in linguistic examples within `\gll`/`\glt` environments, but here they appear in running prose. Consider whether `\enquote{}` would be more consistent, or at least ensure the opening backtick and closing single-quote are balanced (the first gloss appears to open with a backtick but may not close with a matching apostrophe-quote).

3. **Bold labels in itemised lists (lines 51--55, 80--84, 158--162):** Three bullet lists use `\textbf{Form}:`, `\textbf{Object}:`, `\textbf{Interpretant}:` as labels. The style guide says "avoid bold labels in prose" and prefers narrative flow. These are structural labels recurring at each tier, so the repetition is motivated, but they should either be converted to prose transitions or flagged as an intentional exception.

4. **Publication title formatting (line 4):** `\textit{Harvard Gazette}` is correct for a publication title -- no issue.

5. **Table 13.1 uses `\term{Deitality}` (line 116):** Correct -- this is a technical term.

6. **Index markup density:** The chapter is heavily indexed (every occurrence of `object`, `interpretant`, `habit`, etc. carries `\ixsq{}`). This is not a style violation, but the reader-facing concern is whether the index will have entries so long as to be unhelpful. Worth a pass at index-edit time.

No em-dashes found. No raw double-quotes. No `\paragraph{}` headings. Contractions used throughout. `\enquote{}` used correctly for quotations. En-dashes with `~--` spacing are consistent.

## 7. Specific recommendations

1. **Address the discourse gap (high priority).** Either (a) add a brief subsection (SS13.4.5 or similar, 300--500 words) illustrating a discourse-level category through the HPC lens, even if only to show why discourse is harder to maintain as HPC, or (b) add a paragraph at the end of SS13.5 explicitly scoping the claim to four tiers and marking discourse as a predicted but untested extension. Remove the discourse row from Table 13.x if option (b) is chosen, or flag it with an asterisk and a note.

2. **Tighten or merge SS13.6 (mediation gradient).** The section currently restates SS13.5 in Peircean vocabulary without clearly adding explanatory content. Option A: add a single opening sentence naming what the Peircean framing buys that the stabiliser-weighting map alone cannot provide (if this exists -- the shift from "which stabilisers" to "the interpretant's role" is a real distinction, but it needs to be made explicit). Option B: compress SS13.6 to a single paragraph at the end of SS13.5 and cut the section heading.

3. **Fix the `\textit{}` on line 138.** Change `\textit{Washakotya'tawitsherahetkvhta'se}` to `\mention{Washakotya'tawitsherahetkvhta'se}`.

4. **Reduce footnote density in SS13.5 (lines 170--177).** Seven footnotes in 30 lines of text interrupt the argument. Consider moving the pre-registration details and the prevalence-threshold definition into the appendix and replacing the footnotes with a single footnote pointing there: "Methodological details, including pre-registration criteria, prevalence thresholds, and full ablation tables, are in Appendix X."

5. **Add one new piece of evidence for the grammar tier.** The grammar section (SS13.3) currently consists of a synthesis table and a paragraph of commentary. Even a small new observation -- how a specific grammatical-category boundary responds to a perturbation differently from a phoneme boundary or a construction boundary -- would ground the middle of the gradient in original evidence rather than pure back-reference.

6. **Move the packaging-tightness material (lines 249--253) to Chapter 14.** The $k = 4$ metric and the Left Branch Gap connection are a new empirical result that supports Ch 14's argument about grammaticality. In Ch 13's closing section, they arrive without sufficient setup and introduce a term (`packaging tightness`) the chapter hasn't earned. Replace with a transitional sentence that names the question Ch 14 will answer without pre-empting its evidence.

7. **Vary the paragraph openings in SS13.6.** The four-beat "At the [level] level" pattern (lines 218, 220, 222, 224) is mechanical. Vary the syntax: lead with the shift in the interpretant's role, not the tier label.

8. **Convert bold-label bullet lists to prose or add a justificatory note.** The three triadic-structure lists (phonemes, words, constructions) use `\textbf{}` labels, which the style guide discourages. If they are being retained as a deliberate structural parallel across tiers, add a brief LaTeX comment noting the design choice. Otherwise, convert to narrative paragraphs.

9. **Strengthen the polysynthesis negative case.** The Mohawk example from Baker (1996: 40) is a single data point. A second polysynthetic example from a different family (Chukchi is named but not illustrated) would make the "heterogeneous routes" argument more concrete.

10. **Flag which SS13.7 predictions are new.** The predictions section (lines 233--234) mixes predictions unique to this chapter with retrievals from earlier chapters (the /y/ analogy reprises Ch 13's own phoneme section; the resultative stratification reprises the negative-control result). A parenthetical note for each ("new to this chapter" vs. "reprising SS13.x") would help the reader track the book's growing ledger.

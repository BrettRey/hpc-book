# Chapter 6: The Stabilizers -- Editorial Report

---

## 1. Argument

The chapter's argument is sound and does exactly what the book needs at this point in the arc: it supplies the causal machinery that makes the HPC framework empirically testable rather than merely philosophical. The move from "categories are maintained" (asserted in Ch 4) to "here are the specific mechanisms, here is what happens when you remove one" is convincing. The two-case-study architecture -- quotatives maintained from above (social/functional), *whose* maintained from below (cognitive/discourse-structural) -- is well chosen to pre-empt the objection that the framework is "just sociolinguistics." One logical gap worth watching: the "mechanisms as categories, categories as mechanisms" self-application (lines 371--453) is theoretically elegant but the chapter's two defences against the regress objection (interventionism, anti-foundationalism) are stated with more confidence than they earn. The interventionist answer ("stop where causal leverage bites") works pragmatically but doesn't fully answer the metaphysical worry that the framework has no ground floor; the anti-foundationalist answer ("coherentist networks don't need one") is asserted rather than argued. A sceptical philosopher of science will push hardest here.

## 2. Structure

The chapter is well organized, moving from abstract framework (cluster, multi-scale typology, variation-as-activation) through extended case studies to robustness tests, theoretical commitments, and a refactoring-not-replacing coda. The section order is logical and earns its length. Two structural concerns. First, the four \subsubsection{}s under "How deep do mechanisms go?" (lines 335--453) push the nesting deeper than any other chapter in the book; "Causal depth," "Mereological structure," "What this means for explanation," and "Mechanisms as categories, categories as mechanisms" could be promoted to \subsection{} level without loss, since they do quite different work. Second, the final three sections -- "Degrees of projectibility" (548), "What this commits us to" (562), and "Refactoring, not replacing" (598) -- are each short and architecturally important, but they arrive after a very long quotative + *whose* block. The reader has been in case-study mode for ~350 lines and then gets three rapid-fire theoretical sections. Some pacing work -- even just a paragraph of transition between the *whose* case and the robustness-tests section -- would help the reader shift registers.

## 3. Prose

The prose is generally strong. The macrophage opening (line 9) earns the biological parallel efficiently; the "court transcript vs. biopic" line (184) is one of the book's best one-liners; the sourdough starter (379) and trail-in-the-woods (381) images are vivid and do real work. The closing paragraphs (620--626) land well -- the gradatio "Mechanisms don't just preserve categories; they constitute them" is exactly the right note.

Where it drags: the quotative case study is thorough but long. The five bold-labelled subsections of "The quotative cluster" (164--174) and the five bold-labelled subsections of "Quotative stabilizers" (182--258) give the section a textbook feel that sits oddly with the conversational voice elsewhere. The repetition of cross-linguistic caveats ("for Japanese and Turkish, the functional parallel is likely but awaits corpus confirmation" -- said three times in slightly different words at lines 166, 170, 172) could be consolidated. The *whose* case, by contrast, is tighter and more persuasive per word.

One tonal issue: the sentence at line 593 begins "it's silent on neural architecture" with a lowercase *it* after a full stop. This reads as a typo rather than a stylistic choice.

## 4. Evidence

The quotative evidence is excellent -- Tagliamonte and D'Arcy's panel data, Buchstaller's cross-linguistic synthesis, Golato on German *so*. The perturbation-prediction table (Table 2, line 280) is a genuine contribution. The *whose* case is deliberately flagged as attestation-based and promissory (line 461), which is honest, but the evidential weight placed on it -- as the case proving the framework is "not just sociolinguistics" -- is heavy for what amounts to a preprint's worth of attestations plus cross-linguistic examples that the author generated himself (footnote, line 504). The Japanese example in particular, marked as "the author's judgment, confirmed with native-speaker consultants," invokes exactly the kind of data the Source Grounding rule flags as needing verification. The German examples at lines 502--503 are similarly unattributed to a specific source. The Winckel et al. (2025) reference at line 487 is doing important corroborative work but arrives late and compressed.

The Fedorenko, Piantadosi, and Gibson (2024) dissociation argument (line 111) is well placed but the inferential move is fast: "The forcing function is specifically communicative" is a strong conclusion from a double dissociation that shows language and general reasoning are separable. That language has a dedicated network doesn't by itself prove the forcing function is communicative rather than, say, structural or representational. The chapter might acknowledge alternative readings.

## 5. Cross-chapter coherence

The chapter makes forward references to sec:7:mechanistic-alternative and sec:7:definitional-bet (lines 135, 527) and sec:7:generalising-lesson (line 174) -- sections in Chapter 7. These references have the form "As section X showed," which reads oddly when the referenced chapter comes *after* this one. The book-level report (item 2) notes that the chapter outline reversed Chs 6 and 7; if the current order is final (and it is better), these forward references need to be rewritten as genuine forward references ("as Chapter 7 will show") rather than backward-looking ones. The reference at line 135 ("As section 7.x showed, 90% of verbs strongly prefer one aspect") is particularly confusing because the reader hasn't encountered this data yet.

The definiteness thread at line 628 is well executed and connects cleanly to Ch 10's two-cluster architecture. The reference to Ch 8's failure modes (lines 367, 440, 525, 545) is appropriate; the particle contrast case (line 440) effectively previews Ch 8's diagnostic logic. The term "stabilizer" is introduced and defined here (line 29) and used consistently, but the chapter also uses "mechanism" freely throughout, sometimes interchangeably. The book-level report (item 9) flags this; the chapter would benefit from one more sentence in the definitional paragraph (line 29) clarifying when to prefer which term, since later chapters (especially Ch 7) will need the distinction to be stable.

The refactoring section (598--612) engages grammaticalization theory and prototype theory. Neither engagement is deep enough to pre-empt a specialist reader; in particular, the prototype theory paragraph (611) claims "the maintenance view predicts where stability should be robust ... and where it should fray," but this prediction has not been demonstrated within the chapter itself (it is demonstrated in Chs 9--10). A cross-reference would help.

## 6. House style issues

1. **Em-dash in epigraph attribution (line 7):** The source reads `{--- Adam Smith, \textit{...}}` with a Unicode em-dash character. House style requires en-dash with spaces (`~-- `), though epigraph attribution formatting may be governed by the \epigraph macro. Verify and fix if needed.

2. **\textit{} instead of semantic macro (line 7):** `\textit{Considerations Concerning the First Formation of Languages}` -- this is a book title. The house style uses `\textit{}` for titles in citations but normally titles in running text should be handled by the citation system or at minimum be consistent. Since this is inside an \epigraph, it is probably acceptable, but verify that the preamble doesn't define a `\worktitle{}` macro.

3. **\textit{} for figure caption (line 252):** `\textit{be like}` used instead of `\mention{be like}` in the caption of Figure 2. The caption reads "for quotative \textit{be like}" -- should be `\mention{be like}`.

4. **Bold labels in prose (lines 164, 166, 168, 170, 182, 184, 186, 188, 190, 479, 483, 489, 499, 525, 527, 529, 533, 535, 537):** The quotative cluster section and the stabilizers section use `\textbf{Label.}` for sub-points (e.g., `\textbf{Non-lexical content.}`, `\textbf{Processing economy.}`, `\textbf{1. Intervention and ablation.}`). The style guide explicitly says "Avoid bold labels in prose" and "Taxonomies and argument sequences should flow as narrative, not as itemized lists." This is a systematic violation -- 19 instances across three sections. The five quotative-cluster properties (lines 164--174), the five quotative stabilizers (lines 182--258), the three *whose* stabilizers plus cross-linguistic convergence (lines 479--509), and the six robustness tests (lines 525--537) all use this format. Recommendation: convert to prose with discourse markers ("First," "A second mechanism," etc.) per the style guide.

5. **Lowercase sentence start (line 593):** "it's silent on neural architecture" -- should be "It's silent on neural architecture." This is mid-sentence after a colon-less period.

6. **\emph{} used where \term{} may be appropriate (line 127):** `\emph{exposure-dependent stabilization}` and `\emph{population-wide stabilization}` -- these read as introduced technical terms. If they are meant as HPC-framework vocabulary, they should use `\term{}`. If they are merely emphatic, `\emph{}` is fine, but the chapter introduces them as a distinction ("That in turn distinguishes..."), which suggests terminological status. Review also: `\emph{within-speaker}` and `\emph{between-speaker}` at line 125 (likely fine as emphasis), and `\emph{prediction}` at line 461 (fine as emphasis).

7. **Bare asterisk for ungrammaticality (line 503):** `*\mention{Die Person, dessen du vergessen hast...}` uses a bare `*` rather than `\ungram{}` before the mention. The house style defines `\ungram{*sentence}` for this purpose.

8. **Backtick-style quotes in running text (lines 122, 137, 252):** Line 137 uses backtick-delimited words: `` `semantic' versus `syntactic' violations ``. These should use `\enquote{}` or single smart quotes via the quotation system. Same issue at line 122 (`\enquote{}` would be more consistent). And at line 252 the caption uses `\textit{be like}` where `\mention{}` is needed (already flagged above).

## 7. Specific recommendations

1. **Fix forward-reference tense (lines 135, 174, 467, 527).** References to Chapter 7 sections are written as "As section X showed" but Ch 7 follows Ch 6. Rewrite as forward references: "As Chapter 7 will show" or "Section X will demonstrate."

2. **Convert bold-label lists to prose (lines 164--174, 182--258, 479--509, 525--537).** This is the largest house-style violation. Rewrite the five quotative-cluster properties as a flowing paragraph with discourse markers; do the same for the five quotative stabilizers, the *whose* stabilizers, and the six robustness tests. The robustness-tests section (520--543) may retain its numbered format if reframed as a diagnostic checklist (the style guide permits enumerated lists for hypothesis/prediction lists), but the quotative sub-sections should flow.

3. **Consolidate cross-linguistic caveats in the quotative section.** The disclaimer "for Japanese/Turkish, this awaits corpus confirmation" appears at lines 166, 170, and 172 in slightly different phrasings. State it once, firmly, at the end of the cluster description (around line 172 where it already appears as a summary) and cut the per-property repetitions.

4. **Fix lowercase "it's" at line 593.** Capitalize to "It's" -- this is a new sentence.

5. **Replace \textit{be like} with \mention{be like} in Figure 2 caption (line 252).**

6. **Replace bare `*` with \ungram{} at line 503** for the German example.

7. **Replace backtick quotes at line 137** (`` `semantic' versus `syntactic' ``) with `\enquote{semantic}` and `\enquote{syntactic}`, or consider whether these need quoting at all (they may simply be attributing labels, in which case \term{} or \mention{} may be more appropriate).

8. **Sharpen the Fedorenko et al. inference (line 111).** Add a qualifying clause acknowledging that neural dissociation shows the language network is dedicated but doesn't alone establish that the forcing function is communicative (as opposed to structural/representational). Even one sentence would inoculate against a neurolinguist's objection.

9. **Consider promoting the four \subsubsection{}s under "How deep do mechanisms go?" (lines 335--453) to \subsection{} level.** They do heterogeneous work (causal decomposition, mereological decomposition, meta-theoretical implications, self-application of the framework) and the nesting is deeper than anywhere else in the book.

10. **Add a transition paragraph between the *whose* section's close (line 517) and the robustness-tests section (line 520).** The shift from case study to methodology is abrupt.

11. **Clarify the stabilizer/mechanism distinction (around line 29).** One more sentence specifying when to use which term would help downstream consistency, especially for Ch 7 which inherits both terms.

12. **Verify the Japanese *whose* example (line 504) against a published source or flag more prominently as author-generated.** The Source Grounding rule flags self-generated cross-linguistic data, especially for languages where the author is not a specialist. The footnote is honest but the example does substantial argumentative work.

---

*Report generated from a full read of chapter06.tex (628 lines), all 16 chapter precis, the book-level editorial report, and the house style guide.*

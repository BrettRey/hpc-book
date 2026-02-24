# Chapter 8: Failure Modes -- Editorial Report

---

## 1. Argument

The chapter's central argument is sound and structurally necessary: it turns the HPC framework into a falsifiable instrument by specifying what failure looks like. The two-diagnostic test (projectibility + homeostasis) is the book's key methodological contribution, and this is where it gets its sharpest formulation. The three failure modes (thin, fat, negative) are well-motivated and genuinely distinct. One gap: the chapter asserts that umbrella *adverb* fails the projectibility diagnostic ("train on manner adverbs; test on degree words") but never reports a quantitative result -- the claim rests on Ernst's distributional argumentation, not on the literal held-out procedure the chapter advertises. Polish aspect (Ch 7) remains the only worked numerical example of the projectibility test. This leaves the diagnostic looking more like a heuristic than the falsifiable procedure the framing promises. A second, smaller issue: the relationship between epistemic kinds and convenience classes is introduced via Khalidi but never fully distinguished from the book's own "class" terminology -- the reader could use a sentence clarifying whether all epistemic kinds are classes, whether some classes are epistemic kinds, or whether these are synonyms.

## 2. Structure

The chapter's organization is effective through Section 8.5 (negative classes). The inflation problem opens well, the two diagnostics are crisply stated, and the three case studies follow in a logical order (ascending severity: thin misses homeostasis; fat misses projectibility; negative misses both). The grain section (SS8.6) and the lexical-semantics subsection are well-placed as generalizations from the case studies. The audit template (SS8.7) is the right culmination. The coupling coda (SS8.8, "What kind of HPC?"), however, feels structurally dislocated: it introduces a substantial new theoretical commitment (the hard/loose/composite continuum) that is not about failure modes at all, but about variation *within* genuine HPCs. As the book-level report notes, Ch 13 builds its entire argument on this continuum; the material might deserve either its own short chapter or a more explicit framing as "the framework's last theoretical commitment before the case studies" rather than a section appended to a chapter about things going wrong. At minimum, a transition paragraph between SS8.7 and SS8.8 should acknowledge the shift in register from "how to diagnose failure" to "how to classify success."

## 3. Prose

The chapter's opening is among the best in the book -- "The danger of a good framework is that you start seeing it everywhere" is exactly the right tone, and the paper-clips line lands. The *otherwise* return (SS8.4.3) is the emotional payoff that Ch 1 set up, and it earns its length. The preposition-copying case study is clean and efficient. The voice is confident without being hectoring. Two places drag: the fat-clustering section front-loads a long paragraph on Sullivan and Craver (line 203) that reads more like a literature review than an argument -- the neuroscience parallel is interesting but could be halved without loss. The "note of sympathy for the original grammarians" paragraph (lines 237 ff.) is warm and appropriate but sits oddly after the decompose-the-wastebasket directive; it might land better *before* the directive, as setup rather than afterthought. One tonal issue: the coupling coda shifts into a more compressed, technical register (triadic terms, interpretant, habit) without the concrete-first approach that characterizes the rest of the chapter.

## 4. Evidence

The case studies are well-chosen and complementary: preposition copying/pruning for thin (low-frequency, no social indexing), adverb for fat (three subclasses, different mechanisms), non-finite clause for negative (four clause types, no positive cluster), and the Left Branch Condition as a second negative case (gap of abstinence). The *otherwise* discussion ties the fat-class diagnosis back to Ch 1's opening, which is architecturally satisfying. The heritage-language attrition example (Polinsky, line 72) is effective for the perturbation test. What is missing: the adverb case never gets the quantitative projectibility test it promises. The chapter says "Train on manner adverbs; test on degree words" (line 223) but then offers only distributional argumentation from Ernst. A sentence acknowledging that this is an informal application of the test, or pointing to where a literal held-out evaluation could be done, would prevent the reader from feeling the diagnostic is softer than advertised. The evidentiality discussion (lines 381--385) is rich but risks feeling like it belongs in a typology chapter rather than a failure-modes chapter; it might be better as a forward reference to Ch 16's gauntlet.

## 5. Cross-Chapter Coherence

The chapter delivers on Part II's promises cleanly: it picks up the two diagnostics from Chs 6 and 7, operationalizes them, and hands a reusable audit template to Part III. The definiteness thread at the end of SS8.7 correctly predicts the two-cluster diagnosis that Ch 10 confirms. The *otherwise* return pays off Ch 1's opening. The coupling continuum correctly previews Part III's deliberate weakening (countability tight, definiteness looser, lexical categories variable, gender narrow). Two issues. First, the chapter references "SS4.x" for the three failure modes preview but uses `\ref{sec:4:heterogeneity}` -- I cannot verify whether this label resolves correctly; if Ch 4 was restructured, this cross-reference may be stale. Second, the coupling coda uses "the triadic terms that Chapter 7 introduced" (line 455) without specifying what those terms are; a reader who skimmed Ch 7 may not remember that "interpretant" is the key concept. A brief parenthetical gloss would help. Third, the book-level report flags that Ch 6 and Ch 7 use "stabiliser" and "mechanism" somewhat interchangeably; this chapter inherits the ambiguity (e.g., line 66 uses "mechanism" where the chapter's own framing would suggest "stabilizer").

## 6. House Style Issues

**Dashes.** Line 27 uses an em-dash sequence: `\mention{weapon}---and, for those who have followed the debate,`. House style requires en-dashes with spaces (`~-- text ~--`), not em-dashes. This is the only em-dash instance.

**Capitalisation after colons in running text.** Lines 138--139: "it's a stable collection of animals. it's distinct from the fauna of Australia. It has a causal history (isolation). But \enquote{the fauna of Madagascar} isn't itself a species. it's an \emph{ecosystem}" -- three instances of sentence-initial "it's" without capitalisation ("it's a stable collection", "it's distinct from", "it's an \emph{ecosystem}"). These appear to be typos: sentences after full stops need initial capitals.

**Similarly at line 249:** "that's exactly why \term{adverb}" -- sentence-initial "that's" after a period needs capitalisation.

**Similarly at line 338:** "that's the fauna" -- same issue, uncapitalised sentence start.

**`\term{}` vs `\mention{}` consistency.** The chapter correctly uses `\mention{}` for linguistic forms cited as examples (*quickly*, *very*, *otherwise*) and `\term{}` for category labels (*adverb*, *thin*, *fat*). However, at line 207, bare asterisk-prefixed `*\mention{She ran very.}` appears without `\ungram{}` markup. House style requires `\ungram{}` for ungrammatical examples. The same issue appears at lines 215, 227 (twice), 228, and 273. That is 6 instances of bare `*` where `\ungram{}` should be used.

**Bare `\emph{}` where `\term{}` or `\mention{}` is needed.** Line 12: `\emph{seem}` -- this is emphasis, not mention or term, so `\emph{}` is correct here. Line 148: `\emph{material reinforcement}` (line 33) -- this introduces a semi-technical concept; `\term{}` would be more appropriate. Line 197: `\emph{construct validity}` -- same issue; this is a borrowed technical term being introduced and should use `\term{}`.

**Bulleted lists for argumentative content.** Lines 84--88, 177--182, 283--286, 298--303: the style guide discourages bulleted lists for argumentative sequences, preferring prose with transitions. The failure-mode summary (84--88) and the stabilizer audit (177--182) are borderline -- they function as quick-reference taxonomies rather than arguments -- but the preposition alternatives list (283--286) and the non-finite clause inventory (298--303) could easily be prose.

**Bold labels in lists.** Lines 85--87, 178--181, 213, 215, 217, 361, 363, 365: the style guide says "Avoid bold labels in prose." The failure-mode bullets and the methodological-implications subsections use `\textbf{}` labels. These are borderline (some function as mini-headings), but the three adverb-subclass paragraphs (lines 213--218) would read better as flowing prose with discourse markers ("First, manner adverbs... Second, degree words... Third, sentence adverbs...").

**Missing `\enquote{}`.** Line 37: `'Is this term legitimate?'` and `'What kind of work are we asking it to do?'` use backtick-style quotes rather than `\enquote{}`.

## 7. Specific Recommendations

1. **Fix the em-dash on line 27.** Replace `---` with `~--` (en-dash with non-breaking space and trailing space).

2. **Fix capitalisation errors.** Lines 138 (three instances of lowercase "it's" after full stops), 249 ("that's"), and 338 ("that's") all need initial capitals.

3. **Replace bare asterisks with `\ungram{}`.** Lines 207, 215, 227, 228, and 273 use `*` for ungrammaticality marking outside the `gb4e` example environment. Use `\ungram{}` or move these into proper `\ea`/`\z` environments.

4. **Add a transition paragraph between SS8.7 and SS8.8** acknowledging that the chapter shifts from diagnostic failure to coupling typology. One sentence suffices: something like "The audit asks whether a candidate passes the diagnostics. But genuine HPCs aren't all alike" (which is already there on line 450 but is inside SS8.8; pulling the register-shift acknowledgment into a brief bridge paragraph would smooth the reader's experience).

5. **Acknowledge the informal status of the adverb projectibility test.** At or near line 223, add a sentence noting that the "train on one subclass, test on another" procedure is being applied informally here, with the quantitative version demonstrated for Polish aspect in Ch 7. This prevents the reader from feeling the diagnostic is advertised as more rigorous than the evidence supports.

6. **Trim the Sullivan/Craver paragraph (line 203).** The neuroscience parallel is interesting but runs to ~120 words before returning to linguistics. Cut it to ~60 words: keep the construct-validity point and the communicative-pressure contrast; drop the "different labs use different paradigms" elaboration.

7. **Move the "sympathy for grammarians" paragraph (lines 237--238) before the decompose directive (line 235).** The emotional beat lands better as setup ("they weren't lazy; here's why the move was rational; but the maintenance view asks what we can learn from it") than as afterthought.

8. **Replace `\emph{material reinforcement}` (line 33) and `\emph{construct validity}` (line 203) with `\term{}`.** These are semi-technical terms being introduced.

9. **Replace backtick quotes on line 37 with `\enquote{}`.** Two instances: `'Is this term legitimate?'` and `'What kind of work are we asking it to do?'`

10. **Clarify the relationship between "epistemic kind" and "class."** Near line 27 or line 35, add a sentence: either "epistemic kinds are what we've been calling classes" or "classes are a broader notion; epistemic kinds are classes that serve a specific epistemic purpose." The current text introduces both without making the relationship explicit.

11. **Verify the cross-reference `\ref{sec:4:heterogeneity}` on line 16.** If Ch 4 has been restructured since this label was created, the reference may be stale.

12. **Consider whether the evidentiality discussion (lines 381--385) earns its length in this chapter.** It is well-written but functions more as a typological application than a failure-mode diagnosis. If space is tight, it could be shortened to a single paragraph with a forward reference to Ch 16.

13. **Add a parenthetical gloss for "interpretant" at its first appearance in SS8.8 (line 455).** Not all readers will have the Peircean apparatus fresh in mind by this point.

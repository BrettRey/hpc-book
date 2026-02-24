# Chapter 11: Editorial Report

*Lexical categories and their maintenance*

---

## 1. Argument

The chapter's central claim -- that word classes fall along a gradient of mechanism density, and that this gradient predicts cross-linguistic stability, acquisitional trajectory, and diachronic resilience -- is sound and well-earned by Part II's apparatus. The four-configuration typology (skeleton, plumage, wastebasket, braid) does genuine analytical work, and the noun/name opening reprises field-relative projectibility in a way that simultaneously teaches and advances the argument. Two argumentative gaps are worth flagging. First, the claim that "lexical category is itself an HPC with a small-count property" (lines 170--178) is sketched in a single paragraph but never tested; it does interesting theoretical work (explaining why the wastebasket persists) but reads as an aside when it deserves either a proper subsection or removal. Second, the chapter asserts that mechanism density predicts cross-linguistic stability but never directly confronts a language claimed to lack the noun-verb distinction with data -- the counterfactual (no frequency asymmetries, no processing cost, no acquisitional priority) is stated but not explored with a specific language, leaving the strongest challenge to the convergence story without an empirical answer.

## 2. Structure

The overall architecture -- introduction (noun/name as field-relative projectibility), skeleton (nouns and verbs), plumage (adjectives), wastebasket (adverbs), braid (pronouns/IRE/pro-forms), looking forward -- is clean and escalates in complexity in exactly the right way. The introduction is long (lines 6--56, about 1,500 words) but earns its length by doing three jobs: reopening the noun/name distinction, connecting to Ch 10's definiteness/deitality architecture, and previewing the four configurations with the Wallace epigraph. The `\bigskip` on line 39 marks the seam between the analytical setup and the roadmap, which works rhetorically as a breath but may look like a structural orphan in typeset output -- a `\medskip` or a simple paragraph break would be more conventional. The "Looking forward" section (lines 263--297) does solid bookkeeping (Table 11.2, the three predictions, the caveat about checkmarks installing joints) but spends its last two paragraphs essentially re-summarising the chapter's message (field-relative projectibility, name/noun one more time) rather than building new forward momentum toward Ch 12. The transition to gender (prediction three, line 291) is embedded in a list rather than given its own beat, which undersells the handoff.

## 3. Prose

The writing is among the best in the book. The opening two sentences ("A noun is a word that names a person, place, or thing. / This definition is wrong often enough to be interesting, and right often enough to be immortal.") are a hook that works for both linguists and non-specialists. The skeleton/plumage/wastebasket/braid metaphors are vivid and load-bearing without being decorative. The shark/dolphin convergence analogy (line 87) is well-deployed, and the "nouns and verbs are the grammatical skeleton" move earns the payoff it promises. The prose drags in two places: the mechanism-inventory bullet lists in the skeleton section (lines 75--81) and the adjective section (lines 114--118) are long and somewhat repetitive in cadence -- each bullet opens with a bold label, makes a claim, and gives an example, and by the fifth mechanism the reader is ready to move on. The wastebasket section has the sharpest voice in the chapter -- "Five words, five jobs, one label, doing no work whatsoever" (line 142) and "One thread is not a cable" (line 164) are exactly the register the book does best. The pronoun/braid section is architecturally impressive but occasionally dense; the passage from line 220 through 224 (the three-strand discourse argument) could use a concrete example to ground the abstraction.

## 4. Evidence

The evidence is well-chosen and well-stratified: Dixon's typological gradient for adjectives, the Swahili agreement data for morphological lock-in, Tomasello's verb islands for acquisition, the CGEL *more*/*much* misclassification for the wastebasket. The diachronic evidence in the pronoun section (demonstrative-stock /th/-cohort, interrogative /hw/-cohort, the Middle English grammaticalization of relative *who*) is genuinely illuminating and connects beautifully to Ch 10's deitality system. Two areas of thinness. First, the skeleton section's claim about convergent communicative pressure rests almost entirely on functional argumentation; there is no corpus data, no processing evidence, no cross-linguistic quantification comparable to what Chs 9 and 10 provide. The shark/dolphin analogy carries the intuition, but the chapter is lighter on evidence for its strongest claim (nouns and verbs as universal HPCs) than for its weaker ones (adjectives as thin, adverbs as fat). Second, the Mandarin and Swahili examples (lines 108, 117) are brief illustration rather than sustained analysis -- they do what they need to for a chapter that is deliberately cross-linguistic in survey mode, but a reviewer might want more engagement with the literature on flexible-root languages (e.g., Lushootseed, Tagalog) where the noun-verb distinction is most contested.

## 5. Cross-chapter coherence

The chapter connects backward fluently: the noun/name opening reprises Ch 7's field-relative projectibility; the skeleton section invokes Ch 6's stabilizers; the plumage section uses Ch 8's failure-mode diagnostics; the pronoun section ties to Ch 10's deitality system and Ch 12's gender. Forward connections are mostly handled through predictions rather than structural handoffs. The gender prediction (line 291) sets up Ch 12 directly, but the connection to Ch 13's zipper synthesis is thinner than it should be -- the chapter never explicitly positions its four configurations on Ch 8's coupling continuum (hard/loose/composite), even though the introduction promises this (line 55). The "lexical category as HPC" paragraph (lines 170--178) is an idea that Ch 13 could develop but currently doesn't connect to. One potential inconsistency: the chapter uses "class" and "category" with the terminological discipline established in the CLAUDE.md (category = genuine HPC, class = any grouping), but the summary table's column header (Table 11.2) uses "Manner adv." and "Adverb" without flagging that one is a category and the other a class -- the distinction is implicit in the checkmarks but could be made explicit.

## 6. House style issues

**`\textit{}` instead of semantic macros.** Lines 160, 162, 186, 200 use `\textit{CGEL}` (four instances). *CGEL* is a title and should be set with `\textit{}` for book titles, so this is correct. Line 254 uses `\textit{Menura novaehollandiae}` for a binomial, also correct.

**Epigraph dash.** Line 4: the attribution dash is a Unicode em-dash character (`---` equivalent). House style requires en-dashes with spaces for parentheticals, and epigraph attributions should follow the same convention. This should be `--` not `---` (or the Unicode em-dash). Check how other chapters handle epigraph attribution dashes for consistency.

**`\emph{}` used for emphasis.** Multiple instances (lines 13, 29, 53, 65, 67, 71, 76, 77, 79, 83, 110, 115, 117, 172, 178 -- approximately 15 instances). Most are genuine emphasis and `\emph{}` is appropriate. However, line 13 uses `\emph{how}` and `\emph{what}` where these are metalinguistic mentions that should arguably be `\mention{}`. Lines 76 (`\emph{token}`, `\emph{type}`), 115 (`\emph{attribution}`), and 172 (`\emph{inside}`): these are emphatic, not mentions, so `\emph{}` is fine.

**Uncontracted forms.** Five instances of uncontracted forms where contractions are preferred by house style: "do not" (line 63, in a formal-register passage about typological qualification -- arguably appropriate); "does not" (line 108 -- "A dedicated lexical category for doing it does not" -- rhythmic; contraction would weaken the cadence); "is not" (line 164); "cannot" (line 91); "does not" (line 117). Most of these serve rhetorical emphasis and may be intentional exceptions.

**`\bigskip` on line 39.** This is a raw spacing command rather than a structural element. If the intent is a section break within the introduction, a `\medskip` with a centered asterism or a simple `\par\noindent` after a blank line would be more conventional.

**Missing `\term{}` for first introduction of technical terms.** Line 210 introduces `\term{IRE words}` correctly. But line 87 introduces "skeleton" as a technical metaphor without `\term{}`; line 100 introduces "plumage" without `\term{}`; line 148 introduces "wastebasket" without `\term{}`. These function as the chapter's organizing vocabulary and appear in the summary. If they are intended as informal metaphors rather than technical terms, that is defensible, but the book-level editorial report treats them as diagnostic labels, suggesting they warrant `\term{}`.

**Line 200: `\mention{*is}`** -- The asterisk should use `\ungram{}` for consistency: `\ungram{\mention{is}}` or equivalent.

## 7. Specific recommendations

1. **Add a concrete language case to the skeleton section.** The claim that nouns and verbs are universal HPCs is the chapter's strongest and least evidenced. A paragraph engaging directly with a flexible-root language (Tagalog, Lushootseed, or Straits Salish) -- showing where the distributional traces predicted by the HPC account either appear or don't -- would substantially strengthen the section. This need not be long; the counterfactual on line 91 has already set up the framework.

2. **Promote or cut the "lexical category as HPC" paragraph (lines 170--178).** As written, this is a provocative aside that makes a substantial claim (the small-count property of lexical-category inventories is itself a maintained cluster) without testing it. Either give it a proper subsection with at least one prediction and one falsifier, or compress it to a footnote acknowledging the idea without developing it.

3. **Explicitly position the four configurations on the coupling continuum.** The introduction promises this (line 55: "Here that continuum earns its keep within a single level of description") but the chapter never maps skeleton/plumage/wastebasket/braid onto hard/loose/composite coupling with enough precision for the promise to feel kept. A paragraph or a column in Table 11.2 would suffice.

4. **Strengthen the forward transition to Ch 12.** The gender prediction (line 291) is currently the third item in a list. Give it its own closing paragraph after the list, making the Ch 12 handoff explicit: the pronoun section has shown that the pro-form inventory is maintained by discourse mechanisms; the question now is what happens when the gender system extends beyond pronouns into the entire pro-form inventory. This connects the braid directly to Ch 12's central claim.

5. **Tighten the mechanism-inventory bullet lists.** In the skeleton section (lines 75--81), the five mechanisms are well-explained but long. Consider compressing the discourse-frequency and semantic-recruitment bullets by 30--40%, since their points are simpler than the other three. The same applies to the adjective section's three bullets (lines 114--118), where the morphological-glue discussion runs to a full paragraph and could lose the Latin/Swahili doubling (one example would suffice since Swahili already appeared in the skeleton section).

6. **Fix the epigraph attribution dash** (line 4). Replace the Unicode em-dash with an en-dash (`--`) to match house style, or verify what convention other chapter epigraphs use and match it.

7. **Mark the skeleton/plumage/wastebasket labels with `\term{}` at first use** (lines 87, 100, 148) if they are intended as diagnostic shorthands that recur in the book's vocabulary. If they are purely informal, add a sentence in the "Looking forward" section disclaiming their technical status.

8. **Add one concrete example to the discourse-strand paragraph (lines 220--224).** The argument that discourse pressure "braids through both the lexical category and the operational category without being reducible to either" is abstract. A single worked example -- e.g., showing how *who* in a relative clause serves reference-tracking (discourse), gap-binding (operational), and case-marking (lexical) simultaneously in a single sentence -- would ground the architecture.

9. **Clarify the Table 11.2 column headers.** Make explicit that "Adverb" names a class (not a category) while the other columns name categories. A footnote or a label distinction (e.g., italicizing "Adverb" to mark its different status) would reinforce the terminological discipline the chapter has been teaching.

10. **Consider replacing `\bigskip` (line 39) with a subtler structural marker** -- either a simple paragraph break, a `\medskip`, or (if the intent is a visual separator) a centered asterism (`\astermark` or equivalent).

---

*Report based on full reading of chapter11.tex against all 16 chapter precis, the book-level editorial report, and the house style guide.*

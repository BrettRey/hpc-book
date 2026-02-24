# Chapter 4: Editorial Report

*"Categories without essences"*

---

## 1. Argument

The chapter's core argument is sound and well-paced: it earns the HPC commitment by building from biology (Boyd, Millikan) through a concrete mechanism sketch (acquisition, entrenchment, alignment, transmission, functional pressure) to practical payoffs and falsification conditions. The engagement with Khalidi's simple causal theory is the chapter's strongest philosophical move, because it shows the framework can absorb a principled weakening (not all kinds need homeostasis) without collapsing into vacuity. The Slater SPC material does necessary broadening. One gap: the chapter announces in the opening paragraph that the Parallel Architecture is a "natural ally" but never develops that alliance -- the PA shows up in a single sentence and then again as a simile in the payoffs section (l. 243, "function much like the interface rules in a PA framework"), without the reader being shown *how* the analogy cashes out. Either this thread needs a paragraph or it should be cut; as it stands, the PA looks like a dropped stitch from Ch 1 and Ch 3 where the same orphaning was flagged.

## 2. Structure

The chapter's organisation is mostly effective: it moves from framework (Boyd, Millikan) to mechanisms to philosophical objections to payoffs to precedents to heterogeneity to determinacy to Aristotle to commitments and falsification. Two structural decisions merit reconsideration. First, the "Sciences that made the shift" section (SS4.5) comes after the payoffs section, but its function is persuasive rather than argumentative -- it tells the reader "other fields did this and survived." That is motivational material better placed *before* the payoffs, or even folded into SS4.1 (species to categories) as a broadening gesture. Its current position interrupts the momentum from payoffs to the more theoretical heterogeneity, determinacy, and Aristotle sections. Second, the "Recovering Aristotle" section (SS4.8) feels like a philosophical grace note that could be shorter; the species-as-individuals paragraph (l. 354) adds a nuance that the book never uses again and could be trimmed.

## 3. Prose

The writing is mostly strong. The spinning-top metaphor is introduced cleanly and earns its keep across the chapter and the book. The honeycomb response to Ambridge ("Hexagons are real. So are nouns.") is the chapter's best line -- punchy, substantive, and structurally load-bearing. The refactoring metaphor in the payoffs section (l. 263) is effective. The prose drags in two places: the Slater SPC material (ll. 194--208) reads like a literature review rather than an argument -- the bullet list of stability routes could be integrated into the Khalidi response rather than standing as a separate passage. And the "What 'maintenance' commits us to" section (SS4.9) retreads ground from the chapter opening (the HPC commitment is restated almost verbatim from l. 18--22 at l. 362--364); the restatement should earn its place by adding something new, not just reminding.

## 4. Evidence

The evidence base is appropriate for an introductory framework chapter: the biology parallel is developed at the right depth, the sign language material is genuinely impressive, and the animacy/rubber-duck discussion (ll. 117--121) is memorable. However, as the precis noted, the sign language and infant-perception material is somewhat tangential to the chapter's primary job of introducing HPC for *grammatical* categories. The sign-language evidence (NSL, ABSL, Battison's constraints) runs for about 600 words and two figures; it could be compressed by half without losing the convergent-maintenance point. The infant-animacy discussion (ll. 117--121) is interesting but risks scope creep -- the chapter does not return to perceptual categories. The most conspicuous evidential gap is that no *grammatical* boundary case gets a worked HPC treatment in this chapter. *Fun*, *near*, and *cattle* are mentioned (payoffs section) but only as promissory references to Part III. A single worked paragraph -- showing how the named mechanisms converge on, say, *fun*'s trajectory -- would ground the framework concretely before asking the reader to wait four more chapters.

## 5. Cross-chapter coherence

The chapter does its forward-pointing job well: it sets up discreteness (Ch 5), projectibility (Ch 7), stabilisers (Ch 6), failure modes (Ch 8), and definiteness/deitality (Ch 10) with explicit cross-references. The definiteness thread at the end (l. 410--411) is clean. Two coherence issues. First, the "stabiliser" terminology is introduced here (l. 100) with a careful definition distinguishing the *functional role* from the *causal structure*, but Ch 6 (per its precis) uses "stabiliser" and "mechanism" somewhat interchangeably. The distinction drawn in this chapter needs to be enforced downstream, or the careful definition here will look like wasted effort. Second, the HPC slogan appears in compressed form here ("a category is a profile, stabilised by mechanisms, projectible relative to purposes," l. 245) but the full form in the CLAUDE.md notes adds "for a purpose." The wording should be consistent across all occurrences -- check Ch 3's introduction, Ch 7's development, and Ch 16's synthesis ledger.

## 6. House style issues

**Sentence-initial lowercase after period.** Several sentences begin with lowercase after what reads as a sentence break, likely artefacts of editing:
- l. 375: "that's why boundary cases aren't annoyances" -- should be "That's".
- l. 382: "it's whether the yardstick is \emph{responsive}" -- should be "It's".
- l. 384: "it's a claim that, despite heterogeneity" -- should be "It's".
- l. 393: "it's the point at which essentialism earns" -- should be "It's".
- l. 397: "that's the handoff." -- should be "That's".
- l. 408: "that's the kind of prediction" -- should be "That's".
(6 instances total.)

**Contraction "it's" where "its" is needed.** l. 129: "it's nearly impossible" -- correct contraction here, but read in context with l. 259 "what it's" (also correct). No actual error, but flag for proofread attention since the two forms appear close together in adjacent sections.

**Missing `\mention{}` or `\term{}`.** l. 259 uses bare `\enquote{really}` four times where the quotes are doing mention-work (citing a usage), not quoting someone. These should arguably be `\mention{really}` to match house style -- or kept as `\enquote{}` if the intent is to mark them as scare-quoted speech. The style guide says `\term{}` for concepts and `\mention{}` for forms; these are neither -- they are scare-quoted attributions. Current treatment is defensible but inconsistent with the pattern elsewhere in the book.

**`\mention{}` vs bare italics.** l. 90: `\term{Noun}` is used for the category name inside Ambridge's honeycomb discussion ("Noun, on this view, is the linguistic honeycomb"). This should be `\term{noun}` (lowercase) -- category names are not capitalised except at sentence-initial position per house style.

**Epigraph citation.** l. 8: The dash before "Pete Seeger" is an em-dash character. House style requires en-dash with spaces. Should be `~-- Pete Seeger`.

**Capitalisation in `\term{}`.** l. 90: `\term{Noun}` should be `\term{noun}`.

**Potential `\enquote{}` needed.** l. 236 uses bare `"mechanism"` with neutral double-quote characters. This should be `\enquote{mechanism}` (or already is, but verify the source matches -- the rendered line shows straight quotes, suggesting it may be an encoding issue or a missing macro).

**Index entries.** l. 26: `\ixnq{Boyd, Richard N.}\ixnq{Boyd, Richard}` -- Boyd appears with two different name forms. Consolidate to one canonical form across the book.

**`should've` and `could've`.** l. 28: "should've measurable signatures" -- this is a grammatical error. Should be "should have measurable signatures" or "should show measurable signatures." The contraction "should've" works as an auxiliary (*should've measured*) but not as a main verb here. Similar issue at l. 155: "could've survived" -- this one is fine grammatically. And l. 408 replicates the pattern correctly. Only l. 28 is wrong.

## 7. Specific recommendations

1. **Fix the six lowercase sentence-initial errors** (ll. 375, 382, 384, 393, 397, 408). These are outright typos.

2. **Fix "should've" at l. 28.** Replace with "should have" or "should show."

3. **Resolve the Parallel Architecture thread.** Either develop the PA alliance into a substantive paragraph (showing how interface rules in PA map onto stabiliser functions) or remove the two references (ll. 10, 243). The current state -- mentioned twice, developed zero times -- is the weakest version.

4. **Compress the sign-language material** (ll. 304--319) by ~40%. The convergent-maintenance point can be made with NSL alone; ABSL can be a one-sentence confirmation. The two figures (sonority and sign constraints) are both valuable, but the prose surrounding them is longer than needed.

5. **Move or absorb "Sciences that made the shift" (SS4.5).** Fold the biology paragraph into SS4.1 and the psychology paragraph into the opening (where prototype theory is already mentioned). The chemistry paragraph can be cut -- it makes a different point (structural reduction, not mechanism-maintenance) and weakens the analogy.

6. **Trim the Slater SPC bullet list** (ll. 196--202). Integrate the four stability routes into the Khalidi response as flowing prose rather than an itemised list -- the style guide discourages lists for argumentative sequences.

7. **Add one worked grammatical example.** A paragraph showing how the five named mechanisms converge on *fun*'s noun-to-adjective drift would ground the framework before Part III. The payoffs section (l. 251) already names *fun*; expand it from a gesture to a sketch.

8. **Cut or compress the species-as-individuals paragraph** (l. 354). The Ghiselin/Hull material is a philosophical nuance that the book never returns to; a footnote would suffice.

9. **Consolidate Boyd's index name** to one canonical form (either "Boyd, Richard" or "Boyd, Richard N." -- not both).

10. **Fix the epigraph dash** (l. 8) from em-dash to en-dash with spaces.

11. **Enforce the stabiliser/mechanism distinction downstream.** The careful definition at l. 100 distinguishes functional role (stabiliser) from causal structure (mechanism). Flag this for the Ch 6 editorial pass -- if the distinction is not maintained there, it undermines this chapter's careful setup.

12. **Verify HPC slogan wording consistency.** The compressed form at l. 245 should match the canonical form used in Ch 7 and Ch 16. Currently "projectible relative to purposes" vs. "projectible for a purpose" -- small but worth standardising.

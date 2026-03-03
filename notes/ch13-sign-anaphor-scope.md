# Ch 13: Sign Language Anaphor -- Scoping Notes

**Date:** 2026-03-03
**Status:** Decision made, chapter not yet drafted
**Decision:** Add as new Ch 13 (Option A). Current Ch 13 (The Category Zipper) moves to Ch 14. Part III becomes 6 chapters (9--14).

## Why this chapter

The current Part III tests HPC at different coupling tightnesses, but entirely within spoken/written language. A sign language case tests **modality independence** -- the claim that HPC architecture is substrate-neutral. This is the strongest possible stress test: completely different articulatory channel, same functional work.

## What makes sign language anaphor an HPC test case

### The two-cluster architecture
- **Semantic cluster:** referent identity, discourse prominence, animacy, role persistence
- **Formal cluster:** spatial loci, pointing direction, agreement verb directionality, eye gaze, body shift

These can decouple:
- Referent loses its locus (formal decay without semantic loss)
- Locus reused for new referent (formal continuity, semantic discontinuity)

### Mechanisms
- **Spatial working memory** constrains locus capacity (why only ~3-4 active loci)
- **Acquisition:** deaf children establish loci in a developmental sequence
- **Alignment:** interlocutors converge on shared spatial models
- **Role shift** as a maintenance strategy when loci decay

### Failure modes (perturbation responses)
- Locus decay over discourse distance
- Competition when too many referents active simultaneously
- Strategies to refresh: re-establishing, role shift, classifier predicates

### Cross-linguistic variation within sign languages
- ASL: heavy use of spatial loci + agreement verbs
- BSL: less spatial agreement, more body shift
- Village sign languages (Kata Kolok, Al-Sayyid Bedouin SL): reduced locus systems, different mechanism densities
- Mechanism density should predict clustering tightness -- same prediction the book makes for spoken languages

### What it tests that no other chapter tests
- **Modality independence:** coupling architecture isn't speech-specific
- **Substrate neutrality of mechanisms:** spatial working memory plays the role that morphological entrenchment plays in spoken language
- **The coupling spectrum extends:** sign language anaphor should slot into Ch 14's (formerly Ch 13's) stack at the "loose coupling" tier, with the same triadic structure

## Placement in Part III

The Part III design note says: "case studies ordered from tightest coupling to loosest." Sign language anaphor coupling is moderately tight (transparent mechanism, predictable failures, but narrow domain like gender). Should go after Ch 12 (gender) and before the stack (now Ch 14).

New Part III order:
- Ch 9: Countability (tight coupling, broad scope)
- Ch 10: Definiteness (loose coupling, budding)
- Ch 11: Lexical categories (cross-linguistic variation)
- Ch 12: Pro-form gender (tight coupling, narrow scope)
- **Ch 13: Sign language anaphor (modality independence)**
- Ch 14: The category zipper (synthesis/scale-invariance)

## Literature needed (source grounding -- read before writing)

### Essential
- Sandler, W. & Lillo-Martin, D. (2006). *Sign Language and Linguistic Universals.* Cambridge. -- The standard reference
- Schlenker, P. (2018). "Sign language semantics" -- Formal semantics of spatial reference
- Padden, C. (1988). *Interaction of Morphology and Syntax in ASL.* -- Agreement verbs and loci
- Cormier, K., Schembri, A., & Woll, B. (2013). "Pronouns and pointing in sign languages" -- Pronominal reference
- Meier, R. (2002). "Why different, why the same?" in *Modality and Structure in Signed and Spoken Languages* -- Modality effects

### Cross-linguistic / village sign languages
- De Vos, C. (2012). *Sign-Spatiality in Kata Kolok.* -- Reduced spatial system
- Sandler, W. et al. (2005). "The emergence of grammar: Systematic structure in a new language" -- ABSL
- Padden, C. et al. (2010). "The grammar of space in two new sign languages" -- ABSL + ISN

### Acquisition
- Lillo-Martin, D. & Meier, R. (2011). "On the linguistic status of 'agreement' in sign languages"
- Morgan, G. & Woll, B. (2002). *Directions in Sign Language Acquisition*

### HPC connection
- Check whether any existing work applies HPC or similar frameworks to sign language categories. If not, the chapter is genuinely novel.

## Chapter structure (preliminary)

1. Opening: the modality challenge (if HPC is right, it shouldn't matter whether the channel is oral-aural or manual-visual)
2. How anaphoric reference works in sign languages (loci, pointing, agreement verbs)
3. The two-cluster architecture: semantic referent tracking + formal spatial system
4. Mechanisms: spatial working memory, acquisition, alignment, role shift
5. Failure modes and perturbation: locus decay, competition, refresh strategies
6. Cross-linguistic variation: ASL vs BSL vs village sign languages
7. The HPC verdict: does the modality-independence claim hold?
8. Forward to Ch 14 (the stack): where sign language anaphor fits in the coupling spectrum

## What NOT to do

- Don't write from memory. Read the sign linguistics literature first.
- Don't treat sign languages as exotic curiosities. They're natural languages with their own structure.
- Don't assume ASL = all sign languages. Cross-linguistic variation is the point.
- Don't duplicate the general HPC apparatus (that's in Part II). Apply it.

## Downstream effects of adding this chapter

- Chapter numbering shifts: current Ch 13 → Ch 14, current Ch 14 → Ch 15, etc. through Ch 17 → Ch 18.
- All cross-references using `\ref{ch:the-category-zipper}` etc. should be label-based and survive renumbering.
- The chapter outline, PROJECT_STATUS.md, and CLAUDE.md chapter status sections need updating.
- Part III header in CHAPTER_OUTLINE.md: "5 chapters" → "6 chapters"
- The stack chapter (new Ch 14) summary table may need a row for sign language anaphor if it fits the coupling spectrum

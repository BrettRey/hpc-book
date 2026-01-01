# Jong-Bok Kim Correspondence - December 2025

**Context:** Brett sent Kim the definiteness/deitality chapter draft in October 2025, asking about SBCG/HPSG modeling of the two-cluster approach.

**Date:** December 27, 2025

---

## Summary of Kim's Feedback

### On Feature Geometry (Ch 10)

Kim endorses the two-cluster separation and proposes explicit feature structure:

```
SYN[DEITALITY [DEIXIS  ….
                DET-TYPE …
                HOSTING …]

SEM[DEFINITENESS [IDENT …
                   UNIQ ..
                   FAM .. ]
```

**Complication noted:** These features are relevant only at phrasal level, determined by context. E.g., "He is an Einstein" - the proper noun is converted to countable.

### On Constructional Constraints vs. Lexical Listing

Kim favors **construction-internal constraints**. Example: nominal + topic marking → definite (identifiable/familiar). The head noun alone cannot determine definiteness. Bare NP definiteness is context-determined.

### On Korean Evidence (Cross-Linguistic Predictions)

- Demonstratives do **not** compete with bare NPs + topic in Korean
- This implies familiarity/givenness (topic) differs from identifiability and uniqueness
- For article-less languages, only semantic/pragmatic features matter - your "deitality" would not matter syntactically
- **Prediction:** This is exactly what you'd expect from HPC analysis

### On Form-Meaning Pairings

Kim distinguishes SBCG from traditional CxG:
- Linguistic signs are form-meaning pairings
- Constructions *license* such signs
- **Every construction has a function** - could be semantic, pragmatic, or purely grammatical
- The a/an alternation is a **constructional constraint on PHONOLOGY** - not syntactic, not semantic

This aligns with your question about "semantically vacuous" constructions.

### On Grammaticality (Ch 14 Relevance)

**Key admission:**
> "The licensing-based theory, to my knowledge, has no clear distinction between well-formed ones and those with ? or ??, thus not clear about gradience. The grammar would accept all such, while not licensing * sentences."

This directly supports your HPC-gradience argument:
- Discrete licensing models fail to capture gradient acceptability
- The grammar licenses, but gradience is elsewhere
- This is exactly the gap your MMMG model addresses

---

## Full Email Thread

[Kim to Reynolds, Dec 27, 2025]

Brett,

Here go my thoughts on your draft and questions: I feel quite sorry for being slow for this, but I finally have time to sit on my desk.

As for definiteness, I agree that neither form nor meaning alone can have a clean characterization. You identified two key features, deitality (structural) and definiteness (semantic) and took these two as HPCs. Taking these two as property clusters seems to be a right direction, even could supported from Construction-based views. Seeing the grammar as a network system, we could assume that definiteness could inherit these properties including uniqueness and familiarity.

Below are my specific comments to your questions.

### Questions where your SBCG/HPSG perspective would help:

**1. Feature geometry.** Would you model deitality vs. definiteness as distinct, partially linked feature families (e.g., [DEIXIS]/[DET-TYPE]/[HOSTING] vs. [IDENT]/[UNIQ]/[FAM]) with constrained inheritance, or as a smaller set of features with construction-specific constraints? Any pitfalls you see in keeping the families partially independent yet interacting?

> At this point, I would have these as a set of features under SYNTAX and SEMANTICS.
>
> SYN[DEITALITY [DEIXIS  ….
>                DET-TYPE …
>                HOSTING …]
>
> SEM[DEFINITENSS [IDENT …
>                  UNIQ ..
>                  FAM .. ]
>
> A tricky part would be that these features would be relevant only on phrasal level expressions, determined by context. For instance, "He is an Einstein..", the proper noun is converted as a countable one.

**2. Constructional constraints vs. lexical listing.** For article-less languages, what's the best SBCG/HPSG treatment of demonstratives, genitives (-uy), topic marking, and numeral-classifier NPs as deital resources without building in definiteness? Would you favour construction-internal constraints over per-lexeme stipulations?

> I would favor construction-internal constraints. For instance, the combination of a nominal expression with the topic marking would be 'definite' (identifiable/familiar). The head noun or lexeme alone cannot determine its definiteness. The definiteness of a bare NP or nominal (with no article) is determined by context.

**3. Diagnostics and competition.** How would you encode competition among nearby constructions (demonstratives vs. genitives vs. bare NPs with topic) so that "deital" diagnostics cluster without collapsing distinct causal profiles? Are there clean ways to capture one-blocking and identificational hosting as constructional constraints?

> I am not sure if I understood this question clearly. Can you give me examples where these are competing against each other? In languages like Korean, for instance, demonstratives do not compete with bare NPs with topic, I think. This may imply that familiarity/given (topic) differs from identifiability and uniqueness. As for the classifiers, the associate NP and the numeral classifier share the countability and features like shape, function, and animacy. The definiteness has no roles here.

**4. Cross-linguistic predictions.** Which empirical cuts in Korean (and related languages) would best test the independence of the two clusters—e.g., effects of robust modifiers on article-like readings, limits on partitives with demonstratives/genitives, or distribution under topic/focus marking?

> Since such languages have no constructions limiting syntactically marked definite NPs, your deitality would not matter in these. Only the semantic/pragmatic features would matter, as in the topic construction. I think this is the kind of predictions we could get from your HPC.

**5. Diachrony in a constraint-based model.** Do you see a tractable way to represent slow center-of-gravity shifts (which properties become central vs. peripheral in the deital family) while keeping the grammar atemporal?

> As for Korean, I am not sure of its diachronical development. Your discussion of English surely makes sense to me.

---

### Additional Questions (from Brett's Nov 28 email):

You present the usual constructionist picture – a construction as a pairing of form and function/meaning – but the SBCG machinery you actually use is more general: typed FS constraints that may affect PHON/FORM/SYN and often leave SEM/CNTXT largely inherited. Some constructions (comparative correlatives, clefts, etc.) clearly introduce real semantic/pragmatic content, but others are mostly structural or morphophonological. Add to that the explicit decision to treat inflectional affixes as realizational processes rather than signs, and I find myself wondering how strongly you still want to hold on to the "form–meaning pairing" slogan.

So I'm curious:

**Do you think of "constructions are form–meaning pairings" as a strict claim about their ontology, or more as a useful heuristic for a family of constraint types that, in practice, often but not always link form and function?**

> I would take that form-meaning pairings are linguistic signs. In SBCG, linguistic knowledge is a set of such signs – lexical, phrasal, and clausal signs. Constructions are licensing such signs. In traditional CxG, I think these notions are not clearly distinguished. This is the main point of my form-function mapping book.

**How would you classify things like the a/an alternation? Is that, for you, purely morphological (outside the space of constructions), or a legitimate micro-construction whose non-inherited content is essentially formal (contextual PHON constraints) rather than semantic?**

> I think this is a constructional constraint given on the PHONLOGY string value. It cannot be a syntactic one. On the string a/an X, X could be any category: a good animal vs. an important point.

**More generally, are you comfortable saying that some constructions are "semantically vacuous" in the narrow sense (they just pass up SEM) but still count as constructions because they impose non-trivial formal constraints, or would you analyze those differently?**

> Ivan Sag suggests that there could be constructions with no meaning at all, while Adele Goldberg assumes that every construction has a certain meaning. I assume that every construction has a certain function – this function could have no semantic contribution, but just a pragmatic and grammatical function. This function could thus be a non at-issue meaning or pragmatic or functional one. To my knowledge, Fillmore also follows this direction.

**On grammaticality:**

> The licensing-based theory, to my knowledge, has no clear distinction between well-formed ones and those with ? or ??, thus not clear about gradience. The grammar would accept all such, while not licensing * sentences. As for the grammaticalization, this would then imply that the grammar would license all the diachronic developments.

---

## Action Items

- [ ] **Ch 10 (Definiteness)**: Kim's feature geometry endorses the two-cluster separation - consider adding a footnote or note acknowledging this SBCG formalization
- [ ] **Ch 10**: Korean evidence (no competition between demonstratives and bare NPs + topic) supports the HPC prediction that article-less languages don't need "deitality"
- [ ] **Ch 14 (Grammaticality)**: Kim's admission about licensing not capturing gradience is useful ammunition for the MMMG approach
- [ ] **Countability chapter**: Kim notes the "He is an Einstein" issue - context-determined countability at phrasal level
- [ ] Consider whether to cite Kim's SBCG book for the constructional constraint approach

---

## Transparent Free Relatives Collaboration (Dec 27)

Kim followed up proposing collaboration on transparent free relatives and "what":

> "Another thing -- one more thing I really want to work on more is 'transparent free relative clauses', which you could find from my form-function book. I have been wondering about various functions of 'what' in English from diachronic and synchronic perspectives. Somehow, the corresponding expression in Japanese (koto or no) and Korean (kes) is also really intriguing. It would be really great if we two can work on this topic together:-)"

**New project created:** `Transparent_free_relatives/`

**Cross-references:**
- `Independent_relative_whose/` - both involve non-standard relatives with internal/external structure interaction
- Kim's SYN[DEITALITY] / SEM[DEFINITENESS] distinction may apply to relative constructions
- "What" as lexical category puzzle connects to HPC book Ch 11

**Action items:**
- [x] Send Kim the whose draft (sent Dec 27)
- [x] Initial reply sent (Dec 27) - listed active collaborations, mentioned LLM workflow
- [ ] **Read Kim's feedback carefully** (both TFR chapter and definiteness comments)
- [ ] Incorporate Kim's insights into relevant projects (Ch 10, Ch 14, countability, grammaticality papers)
- [ ] **Reply substantively** - engage with his theoretical points, scope collaboration details

---

*Filed: December 27, 2025*

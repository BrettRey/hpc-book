# Chapter 13: Grammaticality Itself — Master Notes

**Last updated:** December 15, 2025

## Core Claim

Grammaticality = successful coupling at the obligatory compositional level.

The MMMG framework (Morphosyntactic-Meaning Model of Grammaticality) provides the formal apparatus:

```
G(u) = C^t(u) · K(u) · map
```

Where:
- `map` = 1 if M(u) successfully evokes μ(u), 0 otherwise
- `K(u)` = compatibility between morphosyntactic meaning and composite semantic meaning
- `C^t(u)` = community entrenchment at time t

**Key insight:** Only morphosyntax-meaning pairing failures trigger ungrammaticality. Phonology and discourse affect F(u) (subjective feeling), not G(u) (grammaticality proper).

---

## The Semantics-Morphosyntax Coupling

### Why This Interface Is Special

The coupling peaks at morphosyntax because of the convergence of:

1. **Compositional parallelism:** Form and meaning compose in structurally isomorphic ways
2. **Timescale alignment:** Both operate at phrase/clause level (~300-1000ms)
3. **Selection relations:** Constructions select for semantic properties, creating bidirectional inference
4. **Learnability:** Dense distributional evidence because patterns are obligatory
5. **Obligatoriness:** Must mark tense, number, definiteness — every utterance reinforces coupling
6. **Propositional semantics:** Truth-conditional meaning requires obligatory encoding

### The Architecture

| Level | Semantic Coupling | Why |
|-------|------------------|-----|
| Phonotactics | None | No semantic content |
| **Morphosyntax** | **Tight** | Obligatory + propositional |
| Prosody | Intermediate | Systematic but optional; pragmatic semantics |
| Discourse | Weak | Meaningful but defeasible |

### Core Claim

> **Propositional semantics requires obligatory morphosyntactic encoding because truth-conditional meaning must be compositionally recoverable.**

## Why Phonemes Don't Trigger Ungrammaticality

### The Arbitrariness Argument (Cratylus)

Phonemes can't clash with propositional meaning because they don't carry any. The sign is arbitrary.

> If someone who knows no Persian encounters *sib*, they have no way of deducing its meaning from the pronunciation /siːb/. The /s/ is entirely unhelpful. It is simply impossible to deduce from phonology alone that *sib* means 'apple' in Persian but 'goat' in Zoogocho Zapotec.

The Cratylean view (that phonemes are iconic — /s/ captures the sun's hissing radiance) fails immediately on cross-linguistic evidence. The association between a word's meaning and its pronunciation is **mostly arbitrary**.

**Exception:** Some phonemes are iconic. Winter et al. (2022) show that trilled /r/ evokes roughness cross-linguistically. But even this is limited: *creamy*, *murmur*, *serene* show the iconicity doesn't apply consistently, and it's restricted to sensory words.

### Phonetic Variability is Expected

We expect pronunciation to vary. The /æ/ in *can't* differs slightly from *hat* differs from *bag*. Your own /æ/ in *hat* differs each time you say it. Perceptual categories are broad — like watersheds, minor variations don't change the classification.

**Key insight:** We know phonemes have degrees of freedom, and we expect that freedom to be evident in what we hear. It's quite unlike form-meaning mismatches that lead to ungrammaticality.

### The *biopic* Example

> If one hears talk of a "bi-O-pic" about Robert Oppenheimer, one assumes the fault is in the stress pattern (BI-o-pic) and not the choice of words. Hearing "bi-O-pic" could lead to a moment of confusion, but never a feeling of ungrammaticality.

We can even reason toward an explanation: the speaker saw *biopic* in print and guessed by analogy with *myopic*. But the key is: **mispronunciation triggers identity/competence inference, not ungrammaticality**.

### Phonemes Carry Indexical Meaning

Phonemes don't carry *semantic* meaning, but they do carry *indexical* meaning:

- /kɑːnt/ means you haven't grown up in Canada; /kænt/ means you could have
- Parisian French speakers dropping word endings in 1400 signaled higher social status
- California men in early 2000s saying *pan* like *pen* indexed gay identity (Podesva 2011)
- Epenthetic /ɛ/ before *school*, *spoon*, *still* indexes Spanish L1

> What pronunciation means, what it signifies, more than anything else, is **identity**.

### The Asymmetry Explained

| Domain | Type of meaning | Deviation triggers... |
|--------|----------------|----------------------|
| Phonology | Indexical (identity) | Identity inference |
| Morphosyntax | Semantic (propositional) | Ungrammaticality |

We're "meaning-seeking animals" (Geertz), but we seek *different kinds* of meaning at different levels. Phonological deviation prompts: "Where are they from? What group do they belong to?" Morphosyntactic deviation prompts: "What are they trying to say? Is this even English?"

### Context Warps the Terrain

The watershed analogy suggests fixed terrain: rain falls, follows gravity, ends up in one basin or another. But for phonemes (and possibly grammatical categories), **context warps the terrain moment-to-moment**.

The same acoustic signal gets categorized as /æ/ or /ɛ/ depending on what preceded it, what word is expected, who's speaking. The basin boundaries shift with context. The boundary is **real but dynamic** — at any moment you perceive /æ/ or /e/, but the *location* of the boundary depends on local context.

**Implication for Ch 5:** The current basin metaphor emphasizes *diachronic* dynamics — how categories shift over time via mechanisms. But we should also acknowledge *synchronic* dynamics — how context shifts basin boundaries moment-to-moment.

For grammatical categories: a word ambiguous between noun and verb might be perceived as solidly noun-ish in one syntactic frame and verb-ish in another. *Fun* is more adjective-like in *that was very fun* than in *we had fun*. The terrain flexes with the constructions you're in.

**Metaphor upgrade:** Not a static watershed, but a terrain that flexes with context — like a rubber sheet being pushed and pulled by the forces of the immediate discourse.

---

## Information-Theoretic Framing

### Shannon: Mutual Information

Shannon asks: how much does knowing the form reduce uncertainty about the meaning, and vice versa?

| Level | Form → Meaning | Meaning → Form |
|-------|----------------|----------------|
| **Phoneme** | Low. Knowing /k/ tells you almost nothing about the concept. | Low. "Cat" doesn't determine /k/ (cf. French *chat*). |
| **Morpheme** | Medium. Knowing *-ed* tells you past tense. | Medium. Past tense predicts *-ed* (with exceptions). |
| **Construction** | High. *spray X with Y* strongly predicts location-object reading. | High. Holistic coverage reading predicts *with*-variant. |

The mesoscale paper's **Causal Primitive = Determinism + Specificity − 1** is essentially a bidirectional mutual information metric. Constructions win because they maximize mutual information in both directions.

**Phonemes fail** because they're like bits in a code — necessary for the message but don't carry semantically interpretable content. The information is in the arrangement, not the atoms.

### Kolmogorov: Complexity and Compression

Kolmogorov asks: what's the shortest program that generates the observed form-meaning pairs?

| Level | Kolmogorov Complexity | Why |
|-------|----------------------|-----|
| **Phonotactics** | Short program | FSG over phoneme sequences; no meaning to encode |
| **Morphosyntax** | Medium program | Each construction is a form-meaning pairing, but compositional — complex meanings from simpler ones |
| **Discourse** | Long program | Context dependence means mapping requires context specification |

**The Goldilocks zone for grammaticality:**
1. Program short enough to be learnable (compositional)
2. Mappings obligatory enough to be checkable (must mark tense, number, definiteness)

Phonology's program is short but contentless. Discourse's program is context-dependent and unmanageably long. Morphosyntax is where compositionality and obligatoriness intersect.

### Learnability = Low Complexity + High Mutual Information

Grammatical categories are learnable because they're the level where:
- **Kolmogorov complexity** is minimized (compositional structure compresses)
- **Mutual information** is maximized (obligatory form-meaning pairing)

This is why HPCs cluster most tightly at the morphosyntactic level — it's the information-theoretic sweet spot.

### CP is Effect-Space Relative (The Sharp Version)

The CE/CP framework explains why phonemes don't carry propositional meaning *in a structural way*:

**1. Propositional effects are massively many-to-many with phonemes**

Let E = the proposition expressed by an utterance. Intervene on a phoneme category C:
- The same phoneme occurs in utterances expressing indefinitely many propositions
- Any proposition is compatible with indefinitely many phoneme sequences (via paraphrase, lexical choice, register)

Therefore:
- H(E | C) stays huge → **low determinism**
- H(C | E) stays huge → **low specificity**
- **CP at phoneme scale, relative to propositional E, comes out low/negative**

This is exactly what the mesoscale paper showed: skeletons evaluated against the wrong distinctions produce negative CP.

**2. Phonemes are contrastive, not content-bearing**

Phonemes are good candidates for a CP peak if E = *lexical identity* (minimal-pair discrimination). That's what they're *for*: carving the acoustic stream into contrastive categories that constrain which wordform is signalled.

But propositions are downstream of choices at lexical/morphological/constructional scales. A phoneme affects propositional content only *indirectly* by differentiating wordforms — and often it doesn't (allophony). Its causal influence on propositions is:
- Highly context-dependent
- Non-local

**3. Duality of patterning as a scale-matching story**

The Hockett point (smallest reusable units carrying meaning → vast inventory, lost combinatorial efficiency) becomes: "Propositional E has its CP peak at larger units (lexemes/constructions), while smaller units are optimised for reliable transmission and discrimination."

The system's stable, high-CP mappings are simply not located at the phoneme scale when E is propositional.

**4. Phonemes CAN carry non-propositional information**

If E = speaker identity, stance, affect, social indexing, or register, fine phonetic detail can have a much tighter mapping — phones and prosody may show higher CP with respect to those effect spaces.

This is consistent with "not propositional": those effects aren't truth-conditional content, and they're the ones phonetic variables are plausibly tuned to constrain.

**Summary:** Phonemes don't "bear" propositional information because relative to a propositional effect space they're:
- Too low-level
- Too reusable
- Too indirect

...to sustain a high-CP, bidirectionally constraining mapping. The propositional peak lands at lexemes + constructions (the semantics-bearing mesoscale), not at phonemes.

### Discourse: The Same Logic, Higher Up

Discourse structures (topic chains, rhetorical relations) are **overgeneral** relative to propositions:
- H(E | C) high: many propositions fit the same discourse structure
- H(C | E) high: same content, many packaging options
- **CP for discourse, relative to propositional E, is low/negative**

But discourse may show *higher* CP relative to its own optimal effect space: **coherence, relevance, rhetorical effect**.

Additional problem: **defeasibility**. Context can override discourse patterns (*"She's smart, but she's smart"* = emphatic, not contradictory). The mappings are systematically more context-dependent.

### The Architecture Summary

| Level | Optimal Effect Space | Propositional CP |
|-------|---------------------|-----------------|
| Phonemes | Lexical identity | Low/negative |
| **Morphosyntax** | **Propositional content** | **High** |
| Discourse | Coherence/relevance | Low/negative |

**Grammaticality = propositional CP peak.** That's why only morphosyntactic violations trigger ungrammaticality.

### Connection to Categories (Tentative)

**Idea:** Categories are the infrastructure that makes high-CP morphosyntax possible.

Constructions operate on categories (agent, verb, theme). If categories were unstable or unpredictable, constructional CP would collapse. So high-CP propositional encoding *requires* stable, projectible categories.

The HPC mechanisms (acquisition, entrenchment, alignment, transmission) maintain the stability that high CP requires.

**Reformulation:** Grammatical categories are HPCs because they must be — high-CP encoding requires stable categories, and HPCs are how systems maintain stability without essences.

> **[NOTE: This connects CP → grammaticality → Ch 13. But the book's broader question is about linguistic categories in general: what qualifies, what doesn't, why it matters. The CP material is specifically about the grammaticality peak, not the general category question. The broader connection still needs development.]**

---

## Key Evidence: Turkish Vowel Harmony

The Turkish case provides a minimal pair demonstrating that phonology alone doesn't trigger ungrammaticality:

### Stem disharmony (lexical) → Grammatical
- *doktor* violates backness harmony
- But G(u) = 1 because no morphosyntactic feature is unrealized
- F(u) < 0 (sounds odd to some speakers)

### Suffix disharmony (morphosyntactic) → Ungrammatical
- **kitap-lar* (books, harmonic) vs. **kitap-ler* (ungrammatical)
- The suffix must copy [±back] from the stem
- Using wrong allomorph leaves feature unrealized → K(u) = 0 → G(u) = 0

**Key distinction:**
- Pure phonotactics → affects F(u) only
- Phonologically-conditioned allomorphy → affects G(u) because it realizes morphosyntactic features

---

## Edge Case: The "A Orange" Problem

### The puzzle
*A orange* feels ungrammatical, but the conditioning is purely phonological (avoid vowel clash). Doesn't this show phonology can trigger ungrammaticality?

### HPC answer: No — this is allomorphy, not phonotactics

The *a/an* alternation is **phonologically-conditioned allomorphy** within the indefinite article paradigm. When you say *a orange*, you've selected the wrong form of a morphosyntactic element.

**Parallel to Turkish:**
- *kitap-ler* → wrong allomorph of plural → K(u) = 0 → **ungrammatical**
- *a orange* → wrong allomorph of indefinite article → K(u) = 0 → **ungrammatical**

**French parallel:** *le hiver* → *l'hiver* (elision before vowel) — same mechanism

### HPC insight
This is what HPCs predict: **porous boundaries**. The core is form-meaning coherence, but phonological constraints matter when they interact with morphosyntactic selection. The phonology doesn't *create* grammaticality; it's *recruited into* the morphosyntactic system through allomorphy.

---

## Constructions as Mesoscale (CE 2.0)

The Causal Emergence framework provides quantitative support:

| Scale | Causal Primitive (CP) | Interpretation |
|-------|----------------------|----------------|
| Syntactic skeletons (micro) | −0.453 | Underspecified |
| **Constructions (meso)** | **+0.382** | Sharpest bidirectional constraints |
| Discourse functions (macro) | −0.207 | Overgeneral |

**Implication:** Constructions are where grammar lives — the scale with maximum form-meaning coupling. This supports the claim that grammaticality = successful pairing at the constructional level.

---

## The Reframing for the Book

### Current implicit framing
Semantic and morphosyntactic properties braid together to form grammatical HPCs.

### Revised framing
Semantic and morphosyntactic systems are **independent oscillators**. They align only when construction-mediated feedback creates **phase-locking**. The coupling, when it occurs, is what makes grammatical categories projectible.

**Cross-cutting is the base rate; alignment is the derived condition requiring specific mechanisms.**

---

## Open Questions

1. **Can we quantify coupling strength?** Mutual information between semantic and morphosyntactic properties; bidirectional conditional entropy.

2. **Do all grammatical HPCs decompose into semantic + morphosyntactic facets?** Test: find one that's purely formal or purely semantic but still projectible.

3. **What predicts grammaticalization targets?** Four filters: cognitive salience, discourse frequency, inferential utility, structural availability.

4. **Falsification condition:** If phonology alone (not allomorphy) caused feelings of ungrammaticality, that would seriously challenge the framework.

---

## Integration with Earlier Chapters

- **Ch 6 (Projectibility):** Expand volcano section — when do volcanoes go dormant? When can they re-ignite?
- **Ch 8 (Failure modes):** Flip the cross-cutting framing. Alignment is the puzzle, not misalignment.
- **Ch 9 (Countability):** The two-HPC architecture (individuation + count) is the paradigm case of coupling. (Already has forward ref to Ch 13.)
- **Ch 12 (The Stack):** Phonology lacks meaning; discourse lacks obligatoriness; morphosyntax has both. This is where the architecture argument from Ch 13 gets previewed.

---

## Better Metaphors

| Metaphor | Captures |
|----------|----------|
| Coupled oscillators | Independence + selective phase-locking |
| Lock and key | Fit is specific, defeasible, language-specific |
| Railway switching | Parallel tracks, discrete coupling sites (constructions) |
| Volcanic island with coral | Historical semantic origin + synchronic formal maintenance |

The "braided cables" metaphor implies tight uniform intertwining. These alternatives capture the selective, partial, defeasible nature of the coupling.

---

## Sources

- `literature/grammaticality-model.tex` — Full MMMG framework paper
- `literature/mesocale.tex` — CE 2.0 analysis of constructions
- `notes/semantic-morphosyntactic-coupling.md` — Multi-agent synthesis on coupling strength

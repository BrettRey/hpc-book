# Chapter 14 Grist: What Changes

## Overview

Chapter 14 is the book's closing statement on **consequences**—what shifts if you take the HPC view seriously. Current planned strands:

1. **Methodological consequences** (ABM, gradient judgments, corpus/experimental probes)
2. **Theoretical consequences** (gradience/discreteness dissolution)
3. **Typological consequences** (cross-linguistic rigor, assessing comparative concepts empirically)
4. **Disciplinary/institutional consequences** ← NEW: from linguistics-mereology project

---

## §14.4 (working title): Overlap as Principled—Disciplinary Structure

### Opening anecdote: Newton's mereological guardrail

Newton was concerned with whether his physical laws would make consistent predictions regardless of how a system was defined mereologically (in terms of parts and wholes). For a physical theory to be consistent, it shouldn't matter if you calculate the motion of a massive object (like a planet or a rock) by treating it as a single coherent "whole" or by treating it as a vast aggregate of tiny constituent particles. The predictions for the object's movement must be identical in both cases.

**The mereological check:** If you apply Newton's laws to the individual parts (the "mereological atoms") and then sum them up, you must arrive at the same result as when you apply Newton's laws to the composite object directly.

**The solution (Newton's Third Law):** As Barandes explains, this consistency is only mathematically possible if internal forces cancel out perfectly. If the forces that particles inside the object exert on each other did not cancel, the object could accelerate itself without any external influence just by the interaction of its parts. Newton's Third Law (for every action, there is an equal and opposite reaction) ensures that these internal forces inevitably sum to zero.

Consequently, mereology acted as a **theoretical guardrail**: it forced the inclusion of the Third Law to ensure the theory remained self-consistent when moving "up and down the mereological hierarchy" (from parts to wholes and back).

### The gap: No mereology of linguistics

Linguistics has no such guardrail. What it has instead:

- **Informal taxonomies**: phonetics → phonology → morphology → syntax → semantics → pragmatics (treated as a stack or tree)
- **Interface talk**: syntax-semantics interface, phonology-morphology interface, etc.—but treated as boundary problems to solve, not principled overlap
- **Institutional turf**: journals, departments, hiring lines carved up by subfield

But no one asks: *What does parthood mean for linguistics?* The discipline defaults to a tree-like picture that assumes:
- Disjointness (phonology and morphology don't overlap in substance)
- Single inheritance (a phenomenon belongs to one and only one subfield)
- Clean boundaries (interfaces are borders to police, not contact zones)

None of these hold. The mereology paper (cross-reference below) shows why.

### The HPC connection: Intensional mereology

Classical extensional mereology describes part-whole structure but doesn't ask *why* parts cohere. For natural kinds—biological species, grammatical categories, **disciplinary subfields**—we need a richer question: what makes something a *genuine* whole rather than an arbitrary collection?

Call this **intensional mereology**: the study of what makes parthood real rather than stipulated.

Newton's Third Law is the physics precedent. The analogous question for linguistics: **What makes a disciplinary fusion (experimental semantics, corpus pragmatics) a genuine whole rather than a label of convenience?**

The HPC framework provides the answer. A fusion persists not by accident but through **homeostatic mechanisms operating across lenses**:

- Methodological innovation (corpus tools) → changes what phenomena are tractable → changes theories → changes what counts as good methodology
- Theoretical commitment (Construction Grammar) → shapes what phenomena are recognised → shapes acceptable methods

The mechanisms are analogous to those maintaining grammatical clusters:
- **Entrenchment**: high-frequency research practices become expected
- **Acquisition**: new researchers learn the fusion as a package
- **Alignment**: collaboration enforces mutual expectations
- **Transmission**: grant/publication structures filter for learnable combinations

### Typed parthood (compressed version)

The full formal apparatus lives in the linguistics-mereology project (see cross-reference). The compressed version for Ch 14:

Instead of a single relation ≤, use a family:
- ≤ₚₕₑₙ (phenomena)
- ≤ₘₑₜₕ (methods)
- ≤ₜₕₑₒᵣᵧ (theoretical frameworks)
- ≤ᵢₙₛₜ (institutional communities)

Represent a subfield as a bundle: S = ⟨P, M, T⟩ (phenomena, methods, theory). Then:
- S₁ ≤ₚₕₑₙ S₂ iff P₁ ⊆ P₂
- S₁ ≤ₘₑₜₕ S₂ iff M₁ ⊆ M₂
- etc.

This explains why:
- "Psycholinguistics is part of linguistics" can be true methodologically and institutionally but not uniquely at the theoretical level
- Computational linguistics is method-heavy, cutting across many phenomenon-areas
- Construction Grammar is mainly a theory-part that can fuse with many P/M bundles
- Phonetics and phonology show P- and M-overlap (not containment)

### Consequences for practice

If overlap is principled (not noise), then:

1. **Peer review friction is predictable**: Method-heavy work is penalised in phenomenon-centred venues; hybrid fusions appear "impure" to single-lineage evaluators. This isn't failure—it's a structural effect of typed parthood.

2. **Cross-subfield debate has a logic**: Overlap(S₁, S₂) ≠ ∅ under at least one lens explains why debates recur (shared ground) while remaining unresolved (different lenses privileged).

3. **Interface problems are bidirectional**: The adjacency relation adj(x, y) isn't just "systematic interaction"—it's homeostatic. Each side helps maintain the other. Syntax-semantics interface phenomena persist because syntactic patterns cue semantic interpretations (comprehension) and semantic intentions license syntactic choices (production). The bidirectionality is constitutive.

4. **Venue/grant redesign**: If overlap is principled, evaluation structures should accommodate it. (Flag as speculative.)

---

## Cross-references

### 1. Linguistics-Mereology Project (meta-level)

**Path:** `/Users/brettreynolds/Documents/LLM-CLI-projects/linguistics-mereology/`

Key files:
- `main.tex` — Full paper with formal apparatus
- `CLAUDE.md` — Project summary
- `STATUS.md` — Current state and TODOs

The mereology project develops the **formal typed-parthood framework** in full. Ch 14 should use a compressed, prose-friendly version. The formal apparatus (typed ≤ relations, fusion ⊔, overlap, adjacency adj) can be:
- Left in the mereology paper for separate publication, or
- Included as a technical appendix if desired

### 2. English-Constructionary Project (object-level instantiation)

**Path:** `/Users/brettreynolds/Documents/LLM-CLI-projects/English-Constructionary/`

The Constructionary is a **concrete instantiation** of typed mereology at the object level—not disciplinary structure, but *language structure*. It demonstrates that **linguistic objects themselves** require the same non-tree, cross-cutting logic as the meta-level disciplinary map.

Key connection: `MEREOLOGY_NOTE.md` in that project documents the bidirectional relationship:

**What mereology offers the Constructionary:**
- Typed parthood validates treating constructions through multiple lenses (a plural-s construction is both a morphological part and a semantic part of the individuation system)
- Interfaces as adjacency, not containment: noun (syntax) vs. name (semantics) are adjacent kinds, not contained in each other
- Fusions: complex constructions bundle syntactic structure, semantic composition, and lexical constraints

**What the Constructionary offers mereology:**
- Empirical proof that the object-level isn't a tidy tree either
- Data to define *types* of adjacency: `implements` (form realizing meaning) vs. `related-to` (alternates within a system)
- Granularity demonstration: mereology must handle micro-parts (affixes) and macro-parts (whole grammars) in the same system

---

## Integration notes

- This section completes the "consequences" arc: methodological (ABM), theoretical (gradience), typological (cross-linguistic), **institutional/disciplinary** (mereology)
- The Newton anecdote provides a physics anchor parallel to Ch 5's phase-transition and Ch 7's biological-explanation framing
- Connects backward to Ch 7 (mechanisms) and Ch 8 (failure modes—disciplinary fusions can also fail: thin clustering = label without substance; fat clustering = wastebasket subfields)

---

## Status

- [ ] Draft section prose
- [ ] Decide: formal apparatus in appendix or defer to standalone paper?
- [ ] Add Barandes citation (source for Newton Third Law as mereological constraint)
- [ ] Check Simons 1987 and Cotnoir & Varzi 2021 citations (already in linguistics-mereology refs.bib)

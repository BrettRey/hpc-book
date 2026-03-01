# Prompt: Integrate Canudas-Grabolosa et al. (2026) into HPC Book

## Task

Read the paper at `literature/canudas-grabolosa2026linguisticModel.pdf` (symlinked from portfolio literature/), then find the best integration points in the book. Do NOT rewrite sections; identify specific locations (chapter, section, paragraph) where a citation or brief discussion should be added, and draft the insertions.

## The paper

Canudas-Grabolosa, I., Quam, M., Coppola, M., Snedeker, J., & Kocab, A. (2026). Is a linguistic model needed to build abstract event representations? *Cognition*, 271, 106474. doi:10.1016/j.cognition.2026.106474

**Design:** Nicaraguan homesigners (N=7; deaf adults with no access to an established sign language) and English-speaking 5-year-olds performed a nonverbal imitation task for generic two-participant events (e.g., DOG CHASING BIRD). Three demonstrations with unique exemplars, then participants replicate with new figurines.

**Key result:** Both groups correctly assigned agent and patient roles in two-participant events (children: 91%, homesigners: 89%, no group difference). Abstract relational event representations (role binding) emerge without exposure to transitive syntax or any external linguistic model.

**Important nuance:** The authors acknowledge that homesigners may have developed their own syntactic devices for encoding participant roles (Kocab et al. 2024; Coppola 2002), and that they are embedded in social environments rich in actions and artifacts. So "without language" doesn't mean "without structured experience." The result is also compatible with a weak version of the linguistic-construction hypothesis (internal systems may suffice, even if they're not conventional languages).

## Where it fits

The book already discusses Nicaraguan Sign Language emergence (Ch 4, §4.3) and Al-Sayyid Bedouin Sign Language (Ch 4), pre-linguistic cognitive grounding (Ch 12, on personhood), and the coupling spectrum from hard to composite (Ch 13). This paper adds a new dimension: evidence that *relational concepts* (not just object concepts or phonological structure) can be assembled pre-linguistically.

### Primary integration point: Chapter 4 (Categories without essences)

The existing NSL/ABSL discussion in §4.3 shows that *phonological* structure is constructed, not inherited. Canudas-Grabolosa extends this upward: *semantic* relational structure (agent/patient role binding) is also available without an external linguistic model. This strengthens the convergence argument: multiple levels of linguistic organization can emerge from non-linguistic mechanisms.

**What to add:** A brief paragraph or sentence near the NSL/ABSL discussion noting that the convergence pattern extends beyond phonology. Homesigners can represent generic two-participant events with correct role binding, suggesting that the agent/patient distinction is cognitively available prior to and independent of transitive syntax.

### Secondary integration point: Chapter 12 (Pro-form Gender)

The cognitive-grounding argument for personhood (the person/non-person distinction is pre-linguistic, tied to Theory of Mind) has a structural parallel in this paper: the agent/patient distinction is also pre-linguistic, supported by gestalt perception of agency and social interaction. Both are cases where grammar exploits a distinction already carved out by non-linguistic mechanisms.

**What to add:** A sentence in the cognitive-grounding subsection noting the parallel.

### Tertiary integration point: Chapter 13 (The category zipper)

The coupling spectrum moves from hard coupling (phonemes) through composite coupling (constructions). The homesigner finding is relevant to the "loose coupling" regime: the semantic cluster (agent/patient roles) exists independently, and grammar's job is to *couple* it with formal devices (case marking, word order, transitivity). Canudas-Grabolosa provides direct evidence that one side of the coupling can exist without the other.

**What to add:** A sentence in the loose-coupling discussion.

## Constraints

- The book is in polish phase. Additions should be minimal and surgical: a sentence or short paragraph, not a new subsection.
- Bib key: `canudas-grabolosa2026linguisticModel` (already in references-local.bib at portfolio root; will be merged via /push-bib)
- House style: `\term{}` for concepts, `\mention{}` for forms, `\textcite{}` narrative citations, `\citep{}` parenthetical. No em-dashes. En-dash with spaces for parenthetical asides.
- Source grounding: read the paper first. Quote specific results (89% vs 91%, no group difference). Do not paraphrase from this prompt alone.
- Do NOT over-integrate. Three small additions across three chapters is the right scope. The paper is supporting evidence for existing arguments, not a new argument.

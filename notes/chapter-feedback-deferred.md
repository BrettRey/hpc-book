# Deferred Chapter Feedback

Notes from the December 5, 2025 review-panel exercise. Items below were identified as valuable but better suited for chapters other than Chapter 4.

---

## Chapter 5 (Discrete from continuous)

- **Worked example threading mechanisms**: Add one compact case study that runs a single item (e.g., *fun*, *near*, or *otherwise*) through multiple mechanisms—showing how it's acquired, entrenched, aligned, and transmitted. The alignment micro-exchange is already there; consider extending.

---

## Chapter 8 (Failure modes)

- **Homeostasis test / diagnostic criteria**: Develop the minimal criterion for distinguishing homeostasis from mere multi-causal stability. Something like: "Homeostasis implies stabilising feedback that resists drift under perturbation. The diagnostic is whether the system returns toward the original configuration when perturbed, or merely settles into a new stable state."

- **Diverging population examples**: Add examples of speaker populations *diverging* rather than converging—cases where mechanisms are pulling subpopulations apart. Candidates: passive constructions, relative clauses with gaps in subject vs. object position, quantifier scope ambiguities.

---

## Chapter 10 (Word classes)

- **Cross-linguistic divergence**: The heterogeneity section from Chapter 4 could be extended here with examples of lexical-category systems maintained differently across languages (e.g., adjective-less languages, languages where property words pattern as nouns or verbs).

---

## Chapter 12 (Grammaticality itself)

- **Looping effect (Hacking)**: For standardised languages with writing and formal education, prescriptive intervention adds a feedback loop atop the basic mechanisms. This is historically contingent (most languages over most of history had no prescriptive overlay), not constitutive of category maintenance—but it's relevant for understanding grammaticality judgments in modern standard varieties.

- **Millikan's question**: Which causal-historical facts fix category membership? The "history wins" claim in Chapter 4 is stated but not fully grounded. The answer probably involves: history of acquisition (how the item was learned), history of use (what constructions it appears in), and history of coordination (which interlocutors it was aligned with). This belongs in the chapter on grammaticality itself.

- **Distinguish category reality from category sharpness**: Category reality is stabilised by mechanisms; category sharpness is an emergent effect that can vary by construction, register, and task. These can come apart.

---

## General / cross-cutting

- **Figures should show process, not just states** (Tufte): Wherever possible, figures should visualise dynamics—trajectories in feature space, before/after perturbation, diachronic movement—rather than static snapshots of stable states.

- **Gricean norm violations as category?** (Dec 14, 2025): Are Gricean norms HPC kinds? Key observation: Gricean violations are *often meaningful* (flouting generates implicatures), whereas grammatical violations are *rarely meaningful* (just errors). This asymmetry suggests different maintenance mechanisms — Gricean norms are maintained partly *because* their violation is interpretable. The system exploits violations rather than filtering them out. Potentially relevant for Part IV (scope extension beyond morphosyntax) or as a contrast case in Ch 8. No obvious home in current structure, but worth revisiting when drafting Part IV.

---

## Chapter 5 (Discrete from continuous) — deferred items

### Structural improvements

- **Move *fun* example earlier**: McCloskey suggests leading with concrete examples before the formalism. The *fun* analysis (currently §5.2.4) could motivate the machinery rather than illustrate machinery already presented.

- **Add worked toy example with schematic weights**: One fully worked case showing 3–5 dimensions, illustrative weights, and how a small change yields discrete reclassification at one scale while judgments remain gradient.

- **Add plain-language restatement after hyperreals**: Quarantine the mathematics for readers who want it; provide a clear non-technical summary for those who don't.

- **Designate one analogy as "main engine"**: Fahnestock suggests that phase-transition, basins, and hyperreals form a suite; explicitly label one as primary and others as supporting.

### Theoretical clarifications

- **Ontological status of basins** (Chater): Are basins in the world (community usage patterns), in the mind (speaker representations), or in the model (analyst's description)? The answer affects what counts as evidence.

- **What hyperreals add beyond interface + gradient-wellformedness** (Jackendoff): The novel prediction (hyperbolic variance with distance-to-boundary) is the answer, but should be made more explicit.

- **Critical phenomena signature** (Godfrey-Smith): Does discreteness emergence show the signature of phase transitions (scale-free correlations, power-law distributions, sensitivity near critical points)? Would strengthen the physics analogy if demonstrable.

- **Distinguish three cases in dual membership** (§5.2.4):
  1. Genuine dual category membership (item in overlapping basins)
  2. Construction-specific reanalysis (different category in different constructions)
  3. Polysemy with different category-realising senses

- **Add "what this predicts" paragraph**: Expectations about where borderline cases should cluster, how category shifts should look diachronically, why certain constructions should be more labile than others.

### Empirical grounding

- **Separate basin variance from measurement variance** (Dąbrowska): The framework predicts both sources of individual differences but doesn't explain which input dimensions produce which basin differences. Basin differences should be stable across tasks; measurement differences should vary.

- **Overlay empirical data on prediction figures** (Tufte): The judgment-variance prediction (hyperbolic relationship) needs data to test it. A prediction figure without data is a promissory note.

---

## Chapter 14 (What changes)

- **Agent-based modelling as methodological consequence**: If categories are maintained by interacting mechanisms, the natural methodological move is to simulate populations and test whether predicted basin dynamics emerge. ABM can probe:
  - Whether the five mechanisms produce discrete basin structure from continuous substrates
  - Whether boundary cases cluster where mechanisms compete (overlap at adj–prep, disjoint at noun–verb)
  - Convergence vs. homology: independent populations under similar vs. different functional constraints
  - Stability under perturbation (population size, learning noise, alignment strength)
  - Timescale interactions (entrenchment on utterance scales; transmission on generational)
  
  Key predecessors: Kirby's iterated-learning experiments (already cited in Ch 5), Steels' naming games, Baronchelli's consensus models, Griffiths & Kalish cultural-transmission simulations. The maintenance view gives these scattered models a unified theoretical home.
  
  Gap to flag: most ABM work tunes parameters ad hoc. The maintenance view offers a principled anchor—mechanisms should be operationalised from independent psycholinguistic/acquisitional evidence, not reverse-engineered from output.

# Gauntlet Reframing: Projection as Evaluand

**Date:** 2026-02-28
**Status:** Working notes from session. Local edits committed; architectural questions open.

---

## 1. The Projectibility Gap

**Problem diagnosed:** The book's prose defaults to two-legged descriptions of HPC ("maintained clusters") dropping the third constitutive leg: projectibility. Projectibility isn't a downstream bonus of maintenance -- it's baked into Boyd. A maintained cluster that doesn't project isn't an HPC.

**Local edits committed (4a87417):** ~20 passages across 8 chapters restored projectibility as constitutive. Ch16 synthesis ledger rewritten: header changed from "Mechanism commitment" to "What the cluster projects"; all 5 rows rewritten.

**Deeper question:** Are the local edits sufficient, or does the gauntlet need structural reframing?

**Resolution:** The chapter's architecture is mostly sound once the language is fixed. Three debts (including "demonstrate projection") gate entry to the gauntlet. The gauntlet then tests whether the maintenance account correctly predicts the *shape* of projection. One addition made: 2-3 sentences at the top of §16.2 making the inferential chain explicit:

> The three debts established that categories must project. The gauntlet asks whether the maintenance account correctly predicts *how* they project -- where projection holds, where it thins, and what degradation looks like when stabilisers weaken. Projection is the point; maintenance is the claimed explanation.

---

## 2. Prediction vs Description

**Key insight (Brett):** If a "prediction" just restates what the case studies already demonstrate, it's not a prediction -- it's a description of established facts. The gauntlet is toothless unless it predicts things that could fail on *new* data.

**The cross-frame transfer problem:** "Knowing a noun takes *a(n)* predicts *three*" is already demonstrated in ch9. Putting it in the gauntlet doesn't add risk.

**What's genuinely novel:** Predictions must go beyond the case studies. This led to dispatching agents with different disciplinary profiles and then to a more fundamental question: what questions does HPC let you *ask* that you couldn't ask before?

---

## 3. Diff-in-Diff: What HPC Opened in Other Fields

### Biology (species)

Before HPC: "What is the essence of a species?" vs "Species are just convenient labels."

New questions HPC opened:
- What *mechanisms* maintain species cohesion? (Gene flow, shared selection, developmental constraints.)
- Why does the species concept work better for some taxa than others? (Mechanism density varies.)
- What happens at speciation events? (Mechanisms decouple -- one cluster becomes two when gene flow breaks.)
- Why do hybrid zones have the structure they do? (Mechanisms weaken in a structured gradient.)

### Psychiatry (mental disorders)

Before HPC: DSM's necessary/sufficient criteria vs dimensional models. *Exactly our essentialism-vs-prototype impasse.*

New questions HPC opened:
- What maintains the symptom cluster? (Borsboom's network theory: symptoms causally sustain each other -- insomnia → fatigue → withdrawal → low mood → insomnia.)
- Which node is the *hub*? (Remove it and the cluster unravels. Intervene on it and the disorder remits.)
- Why do disorders show *comorbidity*? (Shared mechanisms -- anxiety and depression co-occur because their causal networks overlap.)
- Is depression categorical or dimensional? (Dissolved: categorical cluster with dimensional structure within the basin. Meehl's taxometric methods test this directly.)
- Is there a *general factor* of psychopathology (the p-factor)? (Some people have generally tighter symptom clustering.)

### Ecology (communities)

Before HPC: Clements's superorganism vs Gleason's accidental co-occurrence.

New questions HPC opened:
- What mechanisms hold a community together?
- What determines which communities co-exist in a landscape?
- What happens when you remove a keystone mechanism? (Structured cascade, not random disintegration.)

---

## 4. Questions HPC Opens for Linguistics (Not Yet Asked)

### From biology:

**The speciation question.** When does one category become two? And the reverse: when do two classes fuse into one HPC?

**IMPORTANT CORRECTION (Brett):** The definiteness/deitality case is NOT speciation-by-fission (one cluster splitting when a mechanism weakens). It's *budding*: definiteness (semantic cluster) existed first. A new mechanism emerged (grammaticalization of demonstrative → article), which *created* a second cluster (deitality) with its own maintenance regime. The formal system developed independent stabilisers and can now decouple from its parent. Not fission but budding. Not a broken connection but a new one.

**The hybrid zone question.** Boundary cases aren't just "hard to classify." They're regions where two adjacent categories' mechanisms both operate but neither dominates. What does the mechanism landscape look like there?

### From psychiatry:

**The network / hub-node question.** Which property in the cluster is the hub -- the one whose removal most destabilises the rest? For countability: is it individuation? Plural morphology? Determiner selection? The book describes coupling but doesn't ask which node is load-bearing. Testable asymmetry: intervene on the hub and the cluster unravels; intervene on a peripheral node and it holds.

**The comorbidity question.** Why do *categories* co-occur in grammars? Languages with robust count/mass tend to have articles. If countability and definiteness share a mechanism (referential anchoring), their co-occurrence isn't coincidental -- it's category-level comorbidity. Perturb the shared mechanism and both should weaken.

**The taxometric question.** Psychiatry developed specific statistical methods (MAXCOV, MAMBAC, L-Mode) to detect latent taxa vs continuous variation. These have never been applied to linguistic categories. Run taxometrics on countability judgments across a large speaker pool. If a latent taxon appears, sharp-boundary claim gets direct support. If not, Khalidi wins.

**The p-factor question.** Is there a general factor of *grammatical tightness* across speakers? Some speakers might have generally sharper categories across the board. If this factor exists, it suggests a speaker-level mechanism (general entrenchment strength, alignment sensitivity). If not, each category is maintained independently.

### From ecology:

**The community assembly question.** What determines which categories co-exist in a grammar? The mechanism-ecology framing predicts that grammars are assembled from available mechanisms, and the mechanism inventory constrains which categories can be sustained.

---

## 5. HPC and Grammaticalization: Genuinely New Questions

The budding insight (§4 above) opens specific questions for grammaticalization that traditional theory (Hopper & Traugott's clines) cannot ask:

### 5.1 Competitive exclusion

When two forms grammaticalize into the same functional niche (*will* / *going to*; *must* / *have to*), can they coexist as distinct categories? HPC predicts the answer depends on whether they recruit *distinct* mechanisms. Same mechanisms → one dies (competitive exclusion). Different mechanisms → they differentiate into distinct HPCs with different projection profiles. *Will* and *gonna* differentiated. The HPC question: can you predict which competitions result in differentiation vs death, based on mechanism overlap, *before the outcome is known*?

Grammaticalization theory can describe these outcomes. It can't predict them from mechanism landscape.

### 5.2 Phase transition vs cline

Grammaticalization theory assumes continuous clines. HPC predicts a phase transition: there should be a point where the new cluster acquires enough independent maintenance to project on its own. Before that point, the grammaticalizing form is a variant use -- knowing it's *the* doesn't predict anything beyond "demonstrative for identifiable referents." After that point, knowing it's an article predicts distributional behaviour, obligatoriness, phonological reduction, complementary distribution.

Testable: plot correlation between emergent properties over historical time. HPC predicts nonlinear increase (phase transition). Cline theory predicts linear increase. Genuine clash, not relabelling.

### 5.3 Mechanism parasitism

Grammaticalizing forms don't build maintenance from scratch. A demonstrative becoming an article plugs into existing structural maintenance (determiner position, NP structure). It only needs to develop its own semantic-formal coupling; distributional maintenance comes for free.

Predicts: grammaticalization should preferentially target positions where structural maintenance already exists. Traditional theory says "those are the grammatical slots" (circular). HPC gives a non-circular answer: maintenance is already there.

### 5.4 Co-grammaticalization from shared mechanisms

If two categories share maintenance mechanisms, emergence of one should facilitate emergence of the other. Article emergence creates maintenance infrastructure that a quantifier system can parasitize. Testable: do relevant categories co-emerge diachronically more than chance? If not, shared-mechanism story is wrong.

### 5.5 Hub-node in category genesis

In the emerging cluster, which property is the hub -- the one without which the cluster can't become self-sustaining? For deitality: obligatoriness? Phonological reduction? Complementary distribution? Which was constitutive of the new cluster's maintenance?

---

## 6. Curated Prediction Inventory (from agent consultation)

Five agents (psycholinguist, typologist, sociolinguist, computational linguist, philosopher of science) generated ~40 predictions. Triage below.

### A. Ordering predictions (theory predicts a specific untested sequence)

1. **Creole emergence recapitulates skeleton-first.** Noun/verb first, TMA before adjective class, gender/noun-class last or never. Testable against NSL, Tok Pisin. If gender crystallises before adjectives, ordering is wrong.

2. **Heritage attrition follows coupling tightness at matched frequency.** Not just "high-frequency holds." Tight coupling should predict resilience independently of frequency. Test: Turkish evidentials (-miş) should erode before past tense (-di). If they erode together, coupling tightness does no independent work.

3. **Developmental cluster tightening.** Children's diagnostics should become more *correlated* over time, not just more accurate. P(uses *a(n)* | uses plural) should increase from age 2-4. If diagnostics improve independently, coupling mechanism isn't operating in acquisition.

### B. Signature predictions (measurable patterns distinguishing HPC from alternatives)

4. **Variance spikes at boundaries, not continuous shading.** Boundary items should show elevated inter-speaker variance with intra-speaker sharpness. Each speaker categorical, but they disagree where boundary sits. If variance is uniform, Khalidi's fuzzy kinds win.

5. **Hierarchical models must outperform flat models.** If maintenance operates at multiple levels, hierarchical statistical models should show out-of-sample advantage for boundary cases. If flat models match, multi-timescale story is decorative.

6. **Conditioned distributions bimodal where pooled look gradient.** The ch15 claim operationalised. If conditioning never recovers bimodality, mixed-bin story is wrong.

### C. Negative predictions (theory predicts specific failures)

7. **Adverb and traditional "pronoun" should fail projection under matched methods.** Same cross-frame transfer test for noun, verb, adjective, adverb. If adverb projects as well as noun, wastebasket diagnosis is wrong.

8. **Negative classes shouldn't generalise.** Learning one non-finite type should provide no leverage for predicting another. Testable with AGL. If generalisation occurs, negative classes project.

### D. Cross-linguistic predictions

9. **Classifier hierarchy collapse.** Semantically transparent classifiers (Mandarin *tiáo* for long-thin) should show graded violations; semantically opaque classifiers (Dyirbal) should show categorical violations. If Mandarin shows no gradient, semantic coupling story is English-specific.

10. **Sprachbund effects realign category boundaries, not just spread features.** In contact zones, categories should converge faster than descent predicts. If contact spreads phonology/lexicon but leaves category boundaries genealogically determined, mechanism-ecology doesn't extend to contact.

11. **Tight coupling predicts cross-linguistic convergence; loose coupling predicts diversity.** Testable against WALS/Grambank: negative correlation between coupling strength and typological diversity.

### E. Processing / experimental predictions

12. **Cross-diagnostic priming tracks mechanism strength.** Priming from *three cats* should facilitate *a cat*; strength should correlate with age-of-acquisition coupling, not just co-occurrence. If priming is purely associative, mechanisms do no additional work.

13. **ERP dissociations between mechanism-maintained and merely frequent properties.** Adjective violations (mechanism-maintained) should show N400+P600; adverb violations (no mechanism) should show P600 only. If both pattern identically, brain doesn't track mechanism structure.

14. **Taxometric methods applied to linguistic categories.** MAXCOV/MAMBAC on countability judgments. If latent taxon appears, sharp-boundary supported. If continuous, Khalidi wins. Direct methodological import from psychiatry -- never been done in linguistics.

---

## 7. The Constructive Gap in the Gauntlet

The gauntlet is entirely about degradation -- what happens when maintenance weakens (fraying, drift, erosion). It never asks the constructive question: **what happens when new maintenance emerges?** How are categories born?

The deitality case is the template: grammaticalization creates a new mechanism, a new cluster forms around it, and eventually it develops enough independent maintenance to decouple from its parent. The gauntlet should have a constructive counterpart to its degradation predictions.

This connects to: competitive exclusion (§5.1), phase transition (§5.2), parasitism (§5.3), co-grammaticalization (§5.4).

---

## 8. What Still Needs Doing

1. **Ch16:** Add cross-frame transfer / projection as a positive prediction (logically prior to fraying/drift). Add constructive prediction (category genesis). Decide scope.
2. **Ch16:** Incorporate the diff-in-diff insights (taxometrics, hub-node, comorbidity, competitive exclusion). Decide which belong in the gauntlet chapter vs the research agenda section.
3. **Case study chapters (9-12):** Assess whether projection is demonstrated or merely asserted. If merely asserted, add brief passages showing the inferential step.
4. **Grammaticalization material:** Decide whether it belongs in ch16, in a separate section, or as a future-work pointer.
5. **The coupling spectrum (ch13):** Its cross-domain predictions (robustness ordering, perturbation cascades) aren't in the gauntlet. Add?

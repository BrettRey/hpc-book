# Psychiatry-to-Linguistics Analogues: Detailed Development

**Date:** 2026-02-28
**Context:** Developing specific linguistic analogues to the genuinely novel questions HPC theory opened in psychiatry (network analysis, comorbidity, taxometrics, p-factor, intervention logic).

---

## 1. Hub-Node Analysis

**Psychiatry:** In Borsboom's network theory of psychopathology, some symptoms are hubs whose removal collapses the cluster. Depression: insomnia is a hub -- it causally sustains fatigue, which sustains withdrawal, which sustains low mood, which perpetuates insomnia. Remove the hub (treat insomnia pharmacologically) and the cluster often remits. This is not just "most central symptom" -- it's the node whose removal breaks the causal feedback loop.

**Linguistic analogue:** Within a grammatical category, some properties are hubs whose removal would destabilize the cluster. The question isn't "which property is most prototypical" (that's just statistical centrality). It's "which property causally sustains the others such that its removal breaks the maintenance regime?"

### 1.1 Countability

**Candidate hub:** Individuation (conceptual unit-hood).

**Argument for:** The book's ch9 ABM shows individuation drives the whole system. If speakers lose the conceptual anchor (what counts as a unit), everything else should drift: plural morphology becomes inconsistent, determiner selection wavers, quantifier choice loses systematicity. The downstream properties (morphology, syntax) are maintained *because* individuation stabilises them.

**Argument against:** Maybe plural morphology is the hub. If productive plural formation breaks (becomes irregular, phonologically opaque), speakers might lose the explicit mark of countability, which then destabilizes determiner selection and quantifier choice. Individuation might survive (conceptually, speakers still track units) but the *cluster* as a grammatical category unravels because the overt mark vanishes.

**Test:** Artificial language learning with systematic perturbation. Three conditions:
- **Condition A:** Teach an artificial count/mass system with individuation cues (gestalt units in images) but irregular plural marking (no systematic suffix).
- **Condition B:** Teach systematic plural marking with no conceptual individuation cues (randomly assign nouns to count/mass).
- **Condition C:** Full system (individuation + systematic plurals).

Measure generalization to novel nouns after 48 hours. If Condition A shows stronger generalization than B, individuation is the hub. If B > A, morphology is the hub. If neither generalizes (only C does), the cluster requires both nodes -- no single hub, but a critical minimum coupling.

**Prediction from hub hypothesis:** Heritage speakers losing Turkish typically show morphological attrition first (evidentials, case suffixes). If countability *individuation* is the hub, count/mass determiner selection should remain stable even as plural morphology degrades. If *plural morphology* is the hub, determiner selection should degrade in lockstep with plural loss.

**Data check:** Turkish heritage speakers in Germany. Do they maintain *bir* (indefinite article, count-sensitive) after plural suffix regularization begins? If yes, individuation hub. If no, morphology hub.

### 1.2 Definiteness

**Candidate hub:** Familiarity assumption (the pragmatic presupposition that the referent is identifiable).

**Argument for:** Without familiarity, everything else falls apart. Form choice (*the* vs *a(n)*) tracks identifiability. Demonstratives and possessives parasitize it. If speakers lose the familiarity tracking, the cluster becomes inert -- forms are still used, but arbitrarily.

**Argument against:** Maybe the hub is *the* article itself (phonological reduction of demonstrative to unstressed grammatical marker). If the article didn't grammaticalize, English would still track familiarity (demonstratives do this in articleless languages like Polish), but there'd be no tight grammatical category. The cluster is maintained by the existence of a dedicated grammatical marker, not by the semantic function it encodes.

**Test:** Compare articleless languages with robust demonstrative systems (Russian, Latin, Classical Chinese) to languages with articles (English, Romance). Use cross-frame transfer: in articleless languages, knowing a noun takes proximal demonstrative should predict nothing about distal demonstrative choice (both can co-occur). In article languages, knowing *the* predicts *a(n)* complementarity.

**Prediction:** If familiarity is the hub, cross-frame transfer should work in both language types (semantic coupling exists even without articles). If the grammaticalized article is the hub, transfer should fail in articleless languages.

**Data:** Yanovich 2005 on Old Russian definiteness shows demonstrative system without grammaticalization. Check whether Old Russian speakers show systematic determiner-like distribution (hub = familiarity) or flexible demonstrative use (hub = grammaticalized form).

### 1.3 Lexical Categories (Adjectives)

**Candidate hub:** Predicativity (use in predicate position: *the cat is [ADJ]*).

**Argument for:** Predicativity is what makes adjectives *adjectives* rather than just modifiers. Many languages have prenominal modifiers (relative clauses, participles) but few have a distinct adjective class. The cluster forms when a set of words can predicate independently. If predicativity is lost (adjectives become frozen into noun-modifying only, like in Mandarin adjectives-without-copula), the category destabilizes.

**Argument against:** Maybe the hub is morphological agreement (adjectives inflect to match nouns). Romance languages: adjectives agree in gender/number. If agreement is lost, do adjectives remain a distinct category, or do they collapse into a general modifier class? English lost agreement but kept the category. So agreement isn't the hub. Predicativity might be.

**Test:** Comparative developmental study. In Romance L1 acquisition, children learn predicativity and agreement in parallel. If agreement is learned but predicativity isn't (adjectives used only attributively), does the category remain distinct? If predicativity develops but agreement lags (as in English), does the category form earlier?

**Prediction:** Languages with predicative-only adjectives (can't modify nouns directly) should show weaker category coherence than languages with both predicative and attributive use. Turkish adjectives: fully predicative, limited attributive morphology. Japanese adjectives: i-adjectives are predicative, na-adjectives are not. Compare projection strength.

**Data:** Backhouse 1984 on Japanese adjectives. If i-adjectives (predicative) show tighter cross-frame transfer than na-adjectives (attributive-only), predicativity is the hub.

### 1.4 Pro-form Gender

**Candidate hub:** Anaphoric dependency (the pronoun's interpretation depends on a linguistic antecedent, not just a perceptual scene).

**Argument for:** This is what makes pro-forms *linguistic* rather than just deictic. Demonstratives (*that cat*) don't need a linguistic antecedent; pronouns do. If anaphoric dependency is lost (pronouns used only deictically, pointing at perceptually present referents), the cluster degrades into demonstratives.

**Argument against:** Maybe morphological agreement (pronoun must match antecedent in gender/number) is the hub. If agreement breaks, anaphora becomes unreliable (which antecedent does *it* track?). The cluster destabilizes not because anaphora is lost, but because the formal mechanism linking pronoun to antecedent is degraded.

**Test:** Pronoun comprehension with ambiguous antecedents. Two conditions:
- **Anaphoric dependency test:** *The cat chased the dog. It was tired.* (two same-gender antecedents, no perceptual support)
- **Morphological agreement test:** *The cat chased the dog. She was tired.* (gender distinguishes antecedents)

If speakers lose agreement but maintain anaphora (default to recency or subject preference), anaphora is the hub. If they lose anaphora and fall back on deixis (pointing), agreement was the hub.

**Prediction:** Creole languages with reduced gender systems (Tok Pisin *em* is gender-neutral) should show robust anaphora but flexible agreement. If *em* resolves antecedents reliably, anaphora is the hub and agreement is peripheral. If anaphora degrades alongside gender loss, agreement is the hub.

**Data:** Tok Pisin corpus studies (Smith 2002). Does *em* show systematic antecedent resolution despite lack of gender marking? If yes, anaphora hub. If no, agreement hub.

### 1.5 Comparison Across Categories

The hub-node question reveals structure that centrality measures miss. For countability, morphology might be the hub (overt mark stabilizes the cluster). For definiteness, the hub might be the grammaticalized article. For adjectives, predicativity. For pro-forms, anaphoric dependency.

**Critical asymmetry:** Intervene on the hub and the cluster unravels. Intervene on a peripheral node and it repairs. Heritage Turkish speakers losing evidential morphology (-miş) show cascade: past tense becomes less systematic, aspect marking wavers. But losing locative case (-de) doesn't cascade -- other cases remain stable. Evidentials might be a hub; locative isn't.

**Research program:** Map the hub nodes for each category in the book's inventory (countability, definiteness, lexical categories, gender, operators). Test hub hypothesis with developmental data (which property learned last still destabilizes the whole cluster?), heritage attrition (which property lost first predicts cluster collapse?), and artificial language learning (which property's absence blocks generalization?).

---

## 2. Comorbidity (Category Co-Occurrence)

**Psychiatry:** Disorders co-occur because their causal networks overlap. Anxiety and depression are comorbid not because they're "similar" but because they share mechanisms: rumination, avoidance, sleep disruption. Perturb the shared mechanism and both disorders respond. If they didn't share mechanisms, comorbidity would be random co-occurrence.

**Linguistic analogue:** Grammatical categories co-occur in grammars because they share maintenance mechanisms. The co-occurrence isn't accidental; it's predicted by mechanism overlap. Perturb the shared mechanism and both categories should degrade.

### 2.1 Countability and Definiteness (Shared Mechanism: Referential Anchoring)

**Claim:** Languages with robust count/mass distinction tend to have articles. This isn't coincidental. Both categories are maintained by the same mechanism: referential anchoring (tracking identifiability of individual units).

**The mechanism:**
- **Countability:** Individuation requires conceptual anchors (what counts as *a cat* vs *cat* in general).
- **Definiteness:** *The* presupposes an identifiable referent; *a(n)* introduces a new unit.
- **Shared substrate:** Both require speakers to track whether a nominal picks out a discrete, identifiable individual.

**Prediction:** Languages with articles (English, Romance, Scandinavian) should show tighter count/mass distinction than articleless languages with the same cognitive resources (Russian, Polish, Latin). If the mechanism is shared, the categories should co-emerge diachronically.

**Test:** Historical corpus analysis. In Germanic and Romance, when did article systems grammaticalize, and when did count/mass become grammatically tight? If articles emerge first and countability tightness increases afterward, the causal arrow is: article emergence → strengthened referential anchoring → tighter countability.

**Data:**
- **Latin → Romance:** Latin had no articles; count/mass was loose (lexical, not grammatical). Romance developed articles (French *le/la*, Spanish *el/la*) from demonstratives. Did count/mass tighten afterward?
- **Old English → Middle English:** OE had weak article system (demonstrative-based); ME developed robust *the/a(n)*. Did quantifier restrictions tighten in ME?

**Counter-test (perturbation):** Heritage speakers losing article use. Does count/mass weaken in parallel?
- **Spanish heritage speakers in US:** Definite article often omitted in non-obligatory contexts (*me gusta Ø música* instead of *me gusta la música*). Prediction: quantifier choice should become less systematic (accepting *much books* where monolingual speakers reject it).

**Data needed:** Spanish heritage corpus (HABLA corpus, Miami-Dade). Compare quantifier violations in heritage speakers with reduced article use vs monolinguals.

### 2.2 Gender and Noun Classes (Shared Mechanism: Agreement Propagation)

**Claim:** Gender systems (Romance, Slavic) and noun class systems (Bantu, Algonquian) are typologically distinct but share a mechanism: morphological agreement propagates category membership across phrasal domains.

**The mechanism:**
- **Gender:** *la bella casa* -- gender on article and adjective agrees with noun.
- **Noun class:** Swahili *ki-kapu ki-kubwa ki-moja* (cl7-basket cl7-big cl7-one) -- class prefix on noun, adjective, numeral.
- **Shared substrate:** Agreement creates redundancy (the category is marked multiple times), which stabilizes the category against noise.

**Prediction:** Languages with agreement should show more stable gender/class systems diachronically than languages with gender but no agreement (e.g., English retains *he/she/it* in pronouns but lost adjectival gender). Agreement-rich systems should resist attrition longer.

**Test:** Romance vs Germanic gender retention. Romance (rich agreement) should maintain gender in heritage contexts better than German (weaker agreement).

**Data:**
- **Italian heritage speakers (Toronto, Montréal):** Gender retained robustly even in third generation (D'Alessandro 2015).
- **German heritage speakers (Pennsylvania Dutch, Texas German):** Gender system collapsed or reduced to two-way (Boas 2009).
- **Shared mechanism:** Agreement density. Italian marks gender on articles, adjectives, past participles, clitics. German marks it on articles and adjectives only.

**Perturbation test:** If agreement is the shared mechanism, artificially reducing agreement in an L2 learning task should destabilize both gender and noun-class systems equally. Teach Romance gender with no adjectival agreement (gender on article only). Does L2 learner acquisition degrade compared to full agreement condition?

### 2.3 Tense and Evidentiality (Shared Mechanism: Operator Stacking)

**Claim:** Languages with rich tense morphology (past/present/future) tend to have evidential or modal systems. Both are maintained by the same mechanism: layered functional structure (TMA hierarchy in generative terms; operator stacking in CGEL terms).

**The mechanism:**
- **Tense:** Marks event time relative to speech time.
- **Evidentiality:** Marks information source (direct witness, inference, hearsay).
- **Modal:** Marks epistemic stance (certainty, possibility).
- **Shared substrate:** All three are *scopal operators* stacking in a fixed hierarchy. Languages that develop one create structural scaffolding (positions in the clause spine) that other operators can parasitize.

**Prediction:** Evidentials should preferentially emerge in languages with rich tense systems, not in tenseless languages. Tense creates the structural maintenance (operator positions) that evidentials plug into.

**Test:** Typological survey (WALS). Do evidential systems co-occur with rich tense more than chance?

**Data (preliminary):**
- Turkish: rich tense (past/non-past) + evidential (-miş/-di distinction).
- Quechua: rich tense + evidential.
- Mandarin: minimal tense (aspect-based) + no grammatical evidential.
- Japanese: rich tense + no grammatical evidential (evidential meaning via sentence-final particles, not inflection).

Pattern unclear. But if shared mechanism is *inflectional morphology* (not just operator stacking), prediction sharpens: suffixing tense morphology should predict suffixing evidentials. Japanese uses particles, not suffixes.

**Perturbation test:** Heritage language attrition. If tense and evidential share mechanism, they should erode together. Turkish heritage speakers: tense simplification should predict evidential loss.

**Data:** Treffers-Daller & Mougeon 2005 on heritage Turkish. Evidential -miş often replaced by past -di. Does this co-occur with tense simplification (past/non-past distinction weakening)?

### 2.4 Implications for Typology

Comorbidity predicts non-random co-occurrence in typological databases. If HPC is right:

1. **Shared mechanisms predict positive correlation.** Languages with feature X should over-represent feature Y if X and Y share maintenance mechanisms.

2. **Independent mechanisms predict no correlation.** Gender and evidentiality share no obvious mechanism; they shouldn't correlate in WALS/Grambank.

3. **Competing mechanisms predict negative correlation.** If two features compete for the same structural resources, they should anti-correlate. (Example: maybe rich case and rich word order both signal grammatical relations; languages tend toward one or the other, not both maximally.)

**Testable:** Run logistic regression on Grambank. Predict presence of Feature Y from presence of Feature X, controlling for genealogical relatedness (phylogenetic regression). Significant positive coefficients = candidate shared mechanisms. Negative coefficients = competitive exclusion.

**Research program:** Build a "mechanism overlap matrix" for typological features. Where psychiatry asks "which disorders share causal networks?", typology asks "which categories share maintenance mechanisms?" The methodology is identical: comorbidity structure reveals mechanism structure.

---

## 3. Taxometrics (Detecting Latent Taxa)

**Psychiatry:** Paul Meehl developed taxometric methods to distinguish categorical taxa (depression is a discrete type) from continuous variation (depression is the low end of a dimension). Three methods:
- **MAXCOV (maximum covariance):** If a latent taxon exists, covariance between two indicators peaks at a specific cut-point on a third indicator.
- **MAMBAC (mean above minus below a cut):** Mean difference between groups above/below a sliding cut should show a peak if a taxon exists.
- **L-Mode (latent mode):** Factor score distributions should be bimodal if a taxon exists.

All three have been extensively validated in psychiatry (schizotypy shows taxonic structure; depression shows dimensional structure). They've *never been applied to linguistic categories*.

**Linguistic analogue:** Are grammatical categories discrete taxa or continuous dimensions? The book *assumes* discreteness (maintained clusters with sharp boundaries), but this has never been tested with methods designed to detect latent taxa.

### 3.1 What the Stimuli Would Look Like

**Countability example:** Collect judgments from 500 speakers on 100 nouns varying along the count-mass continuum:
- Clear count: *cat, book, idea*
- Clear mass: *water, sand, furniture*
- Boundary: *pasta, rice, stone, hair, cord*

For each noun, collect 5 indicators:
1. Acceptability of *much N* (1-7 scale)
2. Acceptability of *many N* (1-7 scale)
3. Acceptability of *three N* (1-7 scale)
4. Acceptability of bare plural *N are common* (1-7 scale)
5. Acceptability of *a/an N* (1-7 scale)

**MAXCOV analysis:** Use *much* as the indicator to stratify the sample. For speakers high vs low on *much* acceptance, compute covariance between *many* and *three*. If countability is a latent taxon, covariance should peak at the boundary between count/mass (where one taxon ends and the other begins).

**MAMBAC analysis:** Slide a cut along the *much* distribution. At each cut, compute mean *many* score for speakers above vs below the cut. If a taxon exists, the mean difference should peak at the boundary.

**L-Mode analysis:** Run factor analysis on the 5 indicators. Extract factor scores. If the distribution is bimodal, countability is taxonic. If unimodal, it's dimensional.

### 3.2 What a Positive Result (Latent Taxon) Would Mean

**For HPC theory:** Discreteness is real, not observer-imposed. The boundary between count and mass is maintained by mechanisms that create a genuine discontinuity in the property space. Categories are attractors, not arbitrary bins.

**For Khalidi's objection:** Khalidi claims grammars are fuzzy kinds (continuous variation, observer-dependent boundaries). A taxonic result refutes this. The boundary isn't fuzzy; it's sharp but variably located across speakers.

**For the book's §15 claim:** The book claims pooled distributions look continuous but conditioning on context recovers bimodality. Taxometrics is the direct test. If L-Mode shows bimodality, the claim is vindicated.

### 3.3 What a Negative Result (Continuous Variation) Would Mean

**For HPC theory:** Discreteness might be an illusion. The appearance of categories could be statistical artefact (clustering in a continuous space) rather than maintained kinds. This would require retreating to: HPC predicts *local* maxima (clusters), not global discontinuity.

**For Khalidi:** Vindication. Grammars are fuzzy kinds after all.

**For the book:** The account needs revision. If categories are continuous, maintenance mechanisms can't be creating sharp boundaries. They might be creating *density peaks* (regions of higher property co-occurrence) rather than discrete basins.

### 3.4 Which Categories Are Most Likely to Show Taxonic Structure?

**Prediction from coupling strength:**

1. **Strong candidates (tight coupling, expected taxonic):**
   - **Countability:** Individuation + plural + determiner tightly coupled.
   - **Pro-form gender:** Agreement + anaphoric dependency.
   - **Finite vs non-finite verbs:** Tense + agreement + clause type.

2. **Weak candidates (loose coupling, expected dimensional):**
   - **Adverbs:** No systematic morphology, no tight syntactic coupling. Should show continuous variation.
   - **Traditional "pronouns":** Wastebasket class. Should fail to show taxonic structure (mixture of several unrelated distributions).

3. **Intermediate (could go either way):**
   - **Adjectives:** Tight in Romance (agreement-based), loose in English (predicativity only).
   - **Definiteness:** Tight in English (grammaticalized article), loose in Russian (demonstrative-based).

**Test design:** Run taxometrics on all four categories (countability, adjectives, adverbs, pronouns) using parallel methods. If countability and adjectives show taxonic structure but adverbs and pronouns don't, coupling strength predicts taxonicity.

### 3.5 Why This Has Never Been Done

Taxometrics requires:
- Large sample sizes (n > 300 for reliable MAXCOV)
- Multiple continuous indicators per category (not just binary grammatical/ungrammatical)
- Sophisticated statistical methods (bootstrapping, simulation)

Linguistic judgment studies typically use 30-50 participants and binary judgments. Taxometrics requires scaling up. But it's feasible with modern crowdsourcing (Prolific, MTurk) and R packages (`RTaxometrics`, Ruscio & Ruscio 2004).

**Payoff:** Direct, quantitative answer to "are categories discrete or continuous?" Psychiatry settled analogous debates with these methods. Linguistics hasn't tried.

---

## 4. The p-Factor (General Grammatical Tightness)

**Psychiatry:** The p-factor (general psychopathology factor) is a latent dimension capturing individual differences in overall symptom clustering. Some people have generally tighter symptom networks across disorders; others have weaker clustering. The p-factor predicts severity, comorbidity, and treatment response better than specific diagnoses.

**Linguistic analogue:** Is there a general factor of *grammatical tightness* across speakers? Some speakers might have categorically sharp boundaries across the board (count/mass, definiteness, tense, gender all show low variance). Others might have generally looser categories (accept more boundary violations across domains).

### 4.1 What This Would Predict

**If the p-factor exists (general tightness):**

1. **Cross-category correlation:** Speakers with sharp count/mass boundaries should also have sharp definite/indefinite boundaries, sharp tense distinctions, etc. The tightness is speaker-level, not category-specific.

2. **Developmental trajectory:** Children who acquire one category early (tight boundaries by age 3) should acquire other categories early. General entrenchment mechanism operates across categories.

3. **Heritage attrition:** Speakers losing one category (e.g., evidentials in heritage Turkish) should show parallel weakening in other categories. General alignment sensitivity weakens.

4. **Social variation:** Prescriptivist speakers should show tighter boundaries across the board. Descriptivist/vernacular speakers should show looser boundaries. The difference is speaker-level mechanism strength, not category-specific knowledge.

**If the p-factor doesn't exist (category-specific tightness):**

1. **No cross-category correlation:** Sharp count/mass doesn't predict sharp definiteness. Each category is maintained independently.

2. **Domain-specific development:** Early noun mastery doesn't predict early verb mastery.

3. **Selective attrition:** Heritage speakers can lose evidentials while maintaining robust gender. No cascade.

4. **No general prescriptivism:** Speakers can be prescriptivist about one domain (split infinitives) while accepting variation in another (singular *they*).

### 4.2 How to Test This

**Study 1: Cross-category judgment battery**

Recruit 300 native English speakers. Collect acceptability judgments (1-7 scale) on boundary cases across 5 categories:

1. **Countability:** *much furniture / many furnitures / three furnitures*
2. **Definiteness:** *I went to Ø hospital / I went to the hospital* (U.S. vs U.K.)
3. **Tense:** *If I would have known... / If I had known...*
4. **Number agreement:** *The team are winning / The team is winning*
5. **Pronoun case:** *between you and I / between you and me*

Run factor analysis. If a general factor emerges (first eigenvalue >> second), there's a p-factor. If five independent factors emerge (one per category), no p-factor.

**Prediction from HPC theory:** If maintenance operates via speaker-level mechanisms (general entrenchment strength, general alignment sensitivity), p-factor should exist. If maintenance is category-specific (individuation for countability, familiarity for definiteness), no p-factor.

**Study 2: Developmental longitudinal**

Track 50 children from age 2-5. Measure category tightness at 6-month intervals across countability, definiteness, tense. Compute intra-child correlation: does early count/mass mastery predict early tense mastery?

If p-factor exists: yes, strong positive correlation.
If not: no correlation.

**Study 3: Heritage speaker attrition**

Sample 100 heritage Spanish speakers (U.S., second generation). Measure category tightness for:
- Gender (article-noun agreement)
- Subjunctive (mood distinctions)
- Preterite/imperfect (aspect)
- Ser/estar (copula choice)

Compute inter-category correlations. If speakers losing gender also lose subjunctive (cross-category correlation), p-factor exists. If attrition is category-specific (some speakers lose gender but maintain subjunctive), no p-factor.

**Data available:** HABLA corpus (Miami), Otheguy & Zentella 2012 on NYC Spanish. Re-analyze for cross-category correlations.

### 4.3 What Finding It (Or Not) Would Mean

**If p-factor exists:**

- Mechanism strength varies across speakers, not just across categories.
- Some speakers are generally "tighter" grammars (high entrenchment, high alignment sensitivity).
- This could be: genetic (individual differences in statistical learning), social (exposure to prescriptive norms), or cognitive (general executive function).
- Intervention implications: targeting general mechanisms (increasing input frequency, explicit instruction) should tighten categories across the board.

**If p-factor doesn't exist:**

- Maintenance is category-specific. Each HPC has its own mechanism ecology.
- Speaker variation is domain-specific (sharp in one area, loose in another).
- Intervention must be category-targeted (teaching count/mass won't improve tense).

**Theoretical importance:** The p-factor question reveals whether mechanisms operate at speaker-level or category-level. Psychiatry found a p-factor (general psychopathology); but that doesn't mean linguistics will. The HPC account is compatible with either outcome, but the answer determines the right level of explanation.

### 4.4 Analogy Breakdown

**Where the analogy might break:**

Psychopathology is largely *within-person* variation (how tightly coupled are this person's symptoms?). Grammar is partly social (community-level norms). The p-factor in grammar might be confounded by:

- **Register variation:** Same speaker has tight grammar in formal contexts, loose in casual. Not a p-factor but context-sensitivity.
- **Prescriptive ideology:** Speakers who've been taught rules show tightness in taught domains but not untaught. Apparent p-factor is actually education effect.

**Control:** Use implicit measures (reaction time, ERP) instead of explicit judgments. If p-factor appears in neural signatures (N400 amplitude for violations), it's not just ideological.

---

## 5. Intervention Logic (From Description to Perturbation)

**Psychiatry:** The field moved from "describe symptom clusters" (DSM-III through DSM-5) to "intervene on a causal node and observe the cascade." If insomnia is a hub in depression, treating insomnia should reduce other symptoms (fatigue, withdrawal, low mood). This is *mechanistic intervention*, not just symptom management. The success of the intervention validates the causal model.

**Linguistic analogue:** Move from "describe property clusters" to "perturb a mechanism and observe the cascade." If individuation maintains countability, weakening individuation should destabilize determiner selection, plural morphology, and quantifier choice. If the cluster doesn't degrade, individuation wasn't the mechanism.

### 5.1 What Counts as "Intervention" in Linguistics?

Clinical intervention (prescribe a drug, apply a therapy) has no direct linguistic analogue. But several experimental paradigms create controlled perturbations:

1. **Artificial language learning (AGL):** Teach a miniature grammar with mechanisms present or absent. Observe generalization.
2. **Priming:** Saturate speakers with atypical input (e.g., mass-quantifiers with count nouns). Measure whether the cluster destabilizes.
3. **Heritage attrition:** Natural experiment -- speakers lose input, mechanisms weaken, categories degrade. Observe which degrade together (shared mechanism) vs independently.
4. **Diachronic change:** Historical corpora show mechanism emergence/loss over time. Grammaticalization is intervention by cultural evolution.
5. **Cross-linguistic typology:** Compare languages with/without a mechanism. If mechanism M maintains category C, languages with M should have C; languages without M shouldn't.

None is a perfect analogue to clinical intervention (we can't "treat" a grammar). But all create controlled perturbations that test causal claims.

### 5.2 Intervention Study 1: AGL with Mechanism Ablation (Countability)

**Design:** Teach adults a miniature count/mass system over 3 days. Four conditions:

**Condition A (Full mechanism):**
- Individuation cues: nouns refer to discrete objects vs substances (visually presented).
- Plural morphology: systematic suffix (-ka for plural, -Ø for singular/mass).
- Determiner: count nouns take *ba*, mass nouns take *fe*.
- Training: 20 nouns (10 count, 10 mass), 200 trials.

**Condition B (No individuation):**
- Same morphology and syntax, but nouns randomly assigned to count/mass (no perceptual individuation cues).
- Tests whether morphology alone can maintain the category.

**Condition C (No morphology):**
- Individuation cues present, but no plural suffix (all nouns appear in same form).
- Determiner distinction remains (*ba* vs *fe*).
- Tests whether individuation + distributional cues suffice without overt morphology.

**Condition D (No determiner):**
- Individuation and morphology present, but no determiner system.
- Tests whether individuation + morphology suffice without distributional anchors.

**Test phase (day 4):** Novel nouns (20 new items). Participants choose determiner (*ba* vs *fe*) and produce plural if count. Measure generalization accuracy.

**Predictions from hub-node analysis:**

- If individuation is the hub: Condition A > B, and C should show partial success (individuation compensates for missing morphology).
- If morphology is the hub: Condition A > C, and B should fail completely (no generalization without morphology).
- If determiner distribution is the hub: Condition A > D, and D should fail.

**Psychiatric analogue:** Ablation studies in depression treatment. If you remove rumination (hub candidate) via Cognitive Behavioral Therapy, does the cluster remit? If you remove only fatigue (peripheral node) via stimulants, does the cluster persist?

### 5.3 Intervention Study 2: Priming-Induced Cluster Destabilization (Definiteness)

**Design:** Saturate speakers with non-canonical article use to test whether the cluster destabilizes.

**Phase 1 (Priming):** Participants read 100 sentences with articles used non-canonically:
- *I adopted a cat. Later, a cat was sleeping.* (indefinite for familiar referent, canonical = *the cat*)
- *The musician walked on stage.* (definite for new referent, canonical = *a musician*)

**Phase 2 (Test):** Acceptability judgments on new sentences. Does the priming weaken the definiteness boundary?

**Measure:**
- Acceptability of non-canonical *a(n)* for familiar referents.
- Acceptability of non-canonical *the* for new referents.
- Control: Sentences with demonstratives (*that cat*). If definiteness cluster degrades, demonstrative use might increase (compensatory).

**Prediction from HPC theory:**

- If definiteness is a maintained cluster, priming should *not* destabilize it (mechanisms resist perturbation). Temporary exposure to noise doesn't break entrenchment.
- If definiteness is just a statistical regularity (Khalidi's view), priming should weaken it (no maintenance mechanisms to resist).

**Psychiatric analogue:** Stress tests in remitted depression. Brief stress exposure shouldn't trigger relapse if maintenance mechanisms (CBT-taught coping, medication) are in place. If it does trigger relapse, mechanisms weren't fully operational.

### 5.4 Intervention Study 3: Heritage Attrition as Natural Experiment (Gender)

**Design:** Use heritage Spanish speakers as a natural perturbation experiment. Input reduction (limited Spanish exposure) weakens mechanisms. Observe which categories degrade together.

**Participants:** 100 heritage Spanish speakers (U.S., second generation). Compare to 50 monolinguals (Mexico City).

**Measures:**
1. Gender agreement (article-noun, adjective-noun)
2. Gender pronoun resolution (*lo/la* tracking antecedent)
3. Verb agreement (person/number)
4. Subjunctive mood (present/past)

**Analysis:** If gender and pronoun resolution share a mechanism (morphological agreement propagation), they should degrade together (positive correlation in error rates). If verb agreement shares the same mechanism, it should degrade in parallel. If subjunctive is maintained by a different mechanism (semantic: irrealis), it should degrade independently.

**Prediction:**
- Shared mechanism: ρ(gender errors, pronoun errors) > 0.7
- Independent mechanism: ρ(gender errors, subjunctive errors) ≈ 0

**Psychiatric analogue:** Comorbidity predicts intervention response. If anxiety and depression share mechanisms (rumination), treating one should improve both. If they're independent, treatment effects shouldn't transfer.

### 5.5 Intervention Study 4: Diachronic Grammaticalization (Definiteness → Deitality)

**Design:** Use historical corpora to observe category emergence as a natural intervention.

**Case:** Old English → Middle English. OE had weak article system (demonstrative-based: *se/sēo/þæt*). ME developed robust *the/a(n)*.

**Intervention:** Grammaticalization of demonstrative to article is the perturbation. Did it create a new HPC (deitality) or just strengthen existing definiteness?

**Measures (corpus-based):**
1. **Complementary distribution:** % of NPs with article. If *the* becomes obligatory, deitality is forming.
2. **Phonological reduction:** OE *þæt* → ME *the* (unstressed). Reduction signals grammaticalization.
3. **Cross-frame transfer:** Does knowing a noun takes *the* predict *a(n)* in ME? Test with distributional semantics (word embeddings).

**Timeline:**
- OE (pre-1100): Demonstrative system, no obligatory articles.
- Early ME (1100-1300): Transitional.
- Late ME (1300-1500): Robust article system.

**Prediction from budding hypothesis (§4 of gauntlet notes):**

- Phase transition, not cline. Correlation between article properties (obligatoriness, reduction, complementarity) should increase nonlinearly.
- Pre-transition: properties independent (demonstratives are flexible).
- Post-transition: properties tightly coupled (articles form HPC).

**Test:** Plot correlation strength over time. HPC predicts sigmoid curve (phase transition). Cline theory predicts linear increase.

**Psychiatric analogue:** Developmental psychopathology. When does a cluster of behaviours become a disorder? HPC predicts phase transition (subclinical → clinical discontinuity maintained by feedback loops). Dimensional models predict continuous severity increase.

### 5.6 Where the Analogy Breaks

**Psychiatry has clinical intervention (drugs, therapy).** Linguistics has no direct analogue. We can't "prescribe" a grammar change and observe effects.

**But:**
- AGL is analogous to controlled lab intervention.
- Heritage attrition is analogous to discontinuing treatment (stop input, mechanisms weaken).
- Grammaticalization is analogous to spontaneous remission or disorder emergence (natural history).

The psychiatric logic still applies: **validate the mechanism by perturbing it.** If the claimed mechanism is real, perturbation should produce predicted effects. If not, the mechanism is decorative (post-hoc description, not causal explanation).

---

## Summary and Research Agenda

The five psychiatry-to-linguistics analogues open concrete, testable questions that go beyond the book's current scope:

### Immediate Opportunities (Feasible Now)

1. **Taxometrics on countability:** Collect 500-speaker judgment data, run MAXCOV/MAMBAC/L-Mode. Direct test of discreteness claim. (6 months, ~$5K crowdsourcing cost.)

2. **Heritage attrition cross-category correlations:** Re-analyze existing corpora (HABLA, Otheguy) for p-factor and comorbidity. (3 months, no cost.)

3. **AGL mechanism ablation:** Four-condition countability study tests hub-node hypothesis. (1 year, standard lab study.)

### Medium-Term (Requires Corpus Development)

4. **Diachronic phase transition:** Old English → Middle English article emergence. Requires parsed historical corpora with distributional semantics. (1-2 years, computationally intensive.)

5. **Priming destabilization:** Definiteness perturbation via non-canonical input. Tests maintenance resilience. (6 months, standard psycholinguistics.)

### Long-Term (Multi-Site, Large-Scale)

6. **Cross-linguistic comorbidity:** Grambank + phylogenetic regression. Which categories co-occur due to shared mechanisms? (2-3 years, collaboration with typologists.)

7. **Developmental p-factor:** Longitudinal tracking of category emergence across domains. (5 years, expensive.)

### Where Analogies Break

- **No clinical intervention:** Linguistics lacks psychiatry's experimental control (can't "treat" a grammar).
- **Social vs individual:** Grammar is community-maintained; psychopathology is individual. Confounds p-factor interpretation.
- **Normativity:** Linguistic categories are partly ideological (prescriptivism); psychiatric categories aren't (no "correct" level of depression).

But the core logic transfers: **mechanisms are validated by perturbation.** Psychiatry went from description to intervention. Linguistics should follow.

---

**Recommendation for the book:** The gauntlet chapter (ch16) should include a "Future Directions" section explicitly importing these methods. Frame them as "questions HPC lets us ask that we couldn't ask before." This positions the book not as endpoint but as research programme opening.

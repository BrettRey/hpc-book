# HPC and Applied/Empirical Linguistics: Genuinely New Questions

**Date:** 2026-02-28
**Task:** For each applied/empirical branch, identify what genuinely new questions HPC opens. Not relabelling; not "HPC explains X that we already know." What can you now *ask* that you couldn't before?

**Standard:** Concrete predictions. Honest about breakdowns. Avoid the trap of "HPC predicts the data we already have."

---

## 1. Corpus Linguistics

### 1.1 Can you operationalise "projection" as a corpus measure?

**The question:** If projection is inference from one diagnostic to another, can we measure it directly in corpora?

**Concrete operationalisation:** Mutual information between diagnostic frames. For countability: MI between {*a(n)*, plural morphology, *three*, bare generic}. For a genuine HPC, these frames should show elevated MI *beyond* what their raw frequencies predict. For a wastebasket class (adverb), frames shouldn't cluster.

**Testable prediction:** Run MI on noun vs adverb frames. Nouns should show tight MI clustering; adverbs shouldn't. If adverbs show comparable MI, either (a) projection measure is wrong, or (b) adverbs actually are a category (would require mechanism story).

**Honest breakdown:** Frequency confound. High-frequency items co-occur more. Control: match frequency bins, compare MI. If MI clustering vanishes when frequency-matched, it's not projection -- it's just co-occurrence.

### 1.2 Do HPCs predict specific distributional signatures?

**The asymmetric fraying prediction:** Boundary items should show *directional* distributional oddity. A prototype noun (*dog*) should appear in all noun frames with uniform probability. A boundary noun (*furniture*) should fail some frames systematically (plural) but pass others (bare generic). The distribution shouldn't be uniform noise; it should fractionate along mechanism lines.

**Corpus test:** For graded countability items (HUGE corpus needed), measure frame probability profiles. Prototypes: flat distribution across frames. Boundary: structured gaps. If boundary items show random noise, not structured fractionation, asymmetric fraying is wrong.

**Requires:** Large-scale gradient countability annotation (Grimm & Dočekal, Kiss et al.). Not yet available at scale.

### 1.3 Does HPC predict anything about frequency distributions that Zipf's law doesn't?

**Honest answer:** Probably not. Zipf's law is about rank-frequency; HPC is about property clustering. Different explananda.

**Possible connection (speculative):** Hub-nodes might show distributional centrality (betweenness in co-occurrence network). If *the* is the hub of the definiteness cluster, it should show high betweenness in construction-network analysis. Peripheral items (demonstratives) should have lower betweenness. Testable, but this is network analysis, not frequency distribution.

**Breakdown:** This doesn't predict anything about Zipf. HPC and Zipf operate at different levels.

### 1.4 Collostructional analysis: does HPC reframe what "attraction" means?

**Traditional collostructional analysis:** Strength of association between lexeme and construction. Computed via Fisher exact test on co-occurrence.

**HPC reframing:** If a category is mechanism-maintained, attraction shouldn't just be association -- it should reflect *shared maintenance*. A lexeme "attracted" to a construction because they share a mechanism (e.g., plural nouns to quantified NPs via individuation) should behave differently from spurious collocations.

**Testable difference:** Mechanism-based attraction should predict *generalisation* beyond the trained collocation. Associative attraction shouldn't. Train on *three dogs*; test whether *seventeen cats* benefits. Mechanism story predicts yes; pure collocation story predicts weak to no transfer.

**Corpus test:** Measure collostructional strength, then test whether it predicts cross-item generalisation (lexical decision latency, grammaticality judgment). If collostructional strength and generalisation strength decouple, association isn't mechanism.

**Honest limitation:** This is crossing corpus methods with psycholinguistic experiments. Pure corpus approach can't test generalisation without behavioural data.

### 1.5 Does mechanism strength predict diachronic rate of change?

**The question:** If a category is tightly coupled (hard-coupled phonemes, skeleton categories), it should resist change. Loosely coupled categories (plumage) should drift faster. Can corpus methods detect this?

**Diachronic corpus test:** Measure rate of distributional change (KL divergence between time slices) for categories at different coupling strengths. Predict: adjectives (loose coupling) drift faster than nouns (tighter coupling). If drift rates don't correlate with coupling, coupling strength does no diachronic work.

**Data requirements:** Diachronic parsed corpora (ARCHER, COHA). Feasible.

**Honest caveat:** External pressure (contact, prestige) can override mechanism strength. Control needed: compare drift rates in stable vs contact-heavy periods. If mechanism effect vanishes in contact zones, it's real but defeatable.

---

## 2. Language Teaching / SLA

### 2.1 Should you teach the hub-node first?

**The question:** If categories have hub-nodes (load-bearing properties whose removal destabilises the cluster), does teaching the hub first accelerate acquisition?

**Concrete prediction:** For countability, if individuation is the hub, teaching individuation + determiner selection first should accelerate plural morphology acquisition. If plural morphology is the hub, teach that first. Hub-first should outperform frequency-first or random-order curricula.

**Experimental design:** Three groups learning countability: (1) Hub-first (individuation drills), (2) Frequency-first (teach *the* and plural -s first), (3) Random order. Measure time to criterion on full diagnostic battery. Hub-first should be fastest if hub-node story is right.

**Honest breakdown:** We don't know which node is the hub. This requires pre-work: identify hub (via perturbation experiments or network centrality in native speakers). Without hub identification, this prediction is empty.

### 2.2 Does HPC predict which L2 errors should be persistent vs transient?

**The mechanism-mismatch prediction:** Errors stemming from mechanism mismatch (L1 and L2 recruit different mechanisms for "the same" category) should be persistent. Errors from incomplete learning should be transient.

**Example:** Korean learners of English struggle with articles. Korean lacks articles; definiteness is marked via word order and context. Mechanism mismatch: English uses morphological anchoring; Korean uses pragmatic anchoring. HPC predicts this error should be persistent even at high proficiency.

**Contrast:** Gender errors (French *le/la*). No mechanism mismatch if L1 has gender; just different lexical assignment. Errors should be transient -- learners just need to learn which nouns take which article. If both error types persist equally, mechanism-mismatch story is wrong.

**Testable:** Compare error persistence for mechanism-mismatch (articles for Korean/Japanese learners) vs mechanism-matched (gender for Spanish learners of French). Predict: mechanism-mismatch errors plateau higher. If they don't, L1 transfer is about surface features, not mechanisms.

**Data availability:** ICLE (International Corpus of Learner English), EF-Cambridge Open Language Database. Feasible.

### 2.3 Does the coupling spectrum predict acquisition difficulty?

**The prediction:** Tightly coupled categories (skeleton categories, hard-coupled phonemes) should be acquired early and accurately. Loosely coupled categories (plumage, adjective subclasses) should be acquired late and variably. Composite categories (constructions) should be acquired after their constituent skeletons.

**Operationalisation:** Rank categories by coupling tightness (from Ch13 coupling spectrum). Predict acquisition order in L2. If coupling tightness doesn't predict acquisition order, coupling spectrum is descriptive, not explanatory.

**Existing data:** Pienemann's Processability Theory has developmental sequences (word → lemma → phrasal → inter-phrasal). Does PT sequence align with coupling spectrum? If yes, PT is measuring coupling. If no, two independent orderings exist.

**Honest clash:** PT predicts noun/verb before inflection; HPC coupling spectrum might predict skeleton (inflection) before plumage (subcategories). Depends on how you slice "category." Needs careful operationalisation.

### 2.4 Natural order hypothesis: does HPC predict or explain Krashen's acquisition order?

**Krashen's claim:** Morpheme acquisition order is stable across L1 backgrounds (progressive *-ing* before plural *-s* before possessive *-'s*).

**HPC reframing:** Does acquisition order track mechanism density? Progressive *-ing* (aspectual, tight semantic-formal coupling) acquired first. Plural *-s* (looser coupling, interacts with countability and quantification) acquired later. Possessive *-'s* (loose coupling, pragmatic-heavy) acquired last.

**Testable:** Rank morphemes by mechanism density (how many independent stabilisers). Predict acquisition order. If HPC ranking matches Krashen order, mechanism density explains natural order. If not, natural order is about something else (phonological salience, frequency).

**Honest limitation:** We don't have independent measures of "mechanism density" yet. This requires pre-work: develop mechanism density metric, validate it on native data, *then* test L2 prediction. Otherwise circular.

### 2.5 Do L2 grammars stabilise around the same attractor states as L1?

**The phase-transition question:** If HPC categories are attractor states (basins in a dynamical landscape), L2 learners should converge toward the same basins as natives -- maybe slower, maybe via different paths, but same endpoint.

**Prediction:** Advanced L2 speakers should show *categorical* structure (sharp boundaries, projection) even if their boundaries don't align with natives'. If L2 remains gradient at all proficiency levels, categories aren't attractors.

**Test:** Apply taxometric methods (MAXCOV, MAMBAC) to L2 countability judgments at different proficiency levels. Beginners: continuous. Advanced: latent taxon emerges. If taxon never emerges, L2 grammar doesn't converge to HPC structure.

**Honest caveat:** This assumes L2 ultimate attainment is possible. If critical period effects block category formation, advanced L2 might remain gradient for neurological reasons, not because HPCs are wrong.

---

## 3. Clinical Linguistics / Language Disorders

### 3.1 SLI/DLD: Does HPC predict which categories should be most affected?

**The loose-coupling vulnerability prediction:** Loosely coupled categories (adjective subclasses, adverbs, gender) should be more vulnerable in DLD than tightly coupled categories (noun, verb, core TMA). Why? Loose coupling = fewer mechanisms; easier to disrupt.

**Testable:** Compare DLD error rates for skeleton vs plumage categories. Predict: plumage erodes more. If skeleton and plumage erode equally, coupling tightness doesn't predict vulnerability.

**Existing data:** CHILDES clinical corpora (SLI subset). Feasible to test.

**Alternative prediction:** Hub-node vulnerability. If DLD disrupts hub mechanisms (e.g., syntactic bootstrapping, interactive alignment), categories should fracture asymmetrically. Items that relied on the hub should fail; items with independent maintenance should hold. Predicts structured error patterns, not random noise.

**Honest breakdown:** DLD is heterogeneous. Some cases are phonological, some morphosyntactic, some pragmatic. HPC predicts mechanism-specific vulnerability, but if DLD subtypes don't align with mechanism types, prediction is too coarse.

### 3.2 Aphasia: Does mechanism type predict which categories survive?

**The entrenchment vs alignment dissociation:** If a category relies heavily on entrenchment (individual learning history), it should survive fluent aphasia (Wernicke's, pragmatics impaired) but fail non-fluent aphasia (Broca's, production impaired). If a category relies on interactive alignment (online coordination), it should fail Wernicke's but survive Broca's.

**Concrete test:** Nouns (high entrenchment) should survive Broca's better than function words (high alignment dependence). Function words should survive Wernicke's better than nouns. If both survive both equally, mechanism type doesn't predict aphasia dissociations.

**Data availability:** AphasiaBank. Feasible.

**Honest limitation:** Aphasia doesn't selectively lesion mechanisms; it lesions brain regions. This prediction assumes mechanisms localise cleanly (entrenchment → temporal, alignment → frontal). If mechanisms are distributed, brain lesions won't fractionate categories along HPC lines.

### 3.3 Should language assessment test categories differently based on HPC profile?

**Current practice:** Standardised tests treat all categories as equivalent. CELF, TROG, TOLD all assume: can the child produce/comprehend [category]?

**HPC reframing:** Categories with different coupling strengths should be assessed differently. Skeleton categories: test sharp boundaries (can/can't). Plumage categories: test gradient mastery (degree of control). Wastebasket classes: don't test as unified categories at all.

**Concrete proposal:** Adjective assessment shouldn't ask "does the child use adjectives?" (wastebasket question). Should ask: does the child use central adjectives (*big*, *red*)? Peripheral adjectives (*asleep*, *afraid*)? Do they show the predicted asymmetry?

**Testable:** Develop HPC-informed assessment battery. Compare diagnostic accuracy against standard tests. If HPC battery doesn't improve sensitivity/specificity, HPC distinctions aren't clinically relevant.

**Honest caveat:** Clinical assessment prioritises speed and reliability. HPC-informed tests might be more accurate but too time-consuming for clinical use. Trade-off between theoretical precision and practical utility.

### 3.4 Do symptom clusters in language disorders mirror HPC structure?

**The comorbidity question (from psychiatry):** If categories share mechanisms, disorders affecting those mechanisms should show comorbidity. If article errors and plural errors co-occur beyond chance, they share a mechanism (individuation, referential anchoring). If they're independent, separate mechanisms.

**Network analysis:** Treat error types as nodes, co-occurrence as edges. Dense clusters = shared mechanisms. Sparse clusters = independent mechanisms. If network structure doesn't align with HPC mechanism predictions, either (a) HPC is wrong, or (b) disorders don't fractionate along mechanism lines.

**Data:** Clinical corpora (AphasiaBank, CHILDES SLI). Network analysis via R (qgraph, bootnet).

**Prediction:** Countability errors should cluster with definiteness errors (shared referential anchoring). Gender errors should be independent (separate mechanism). If all errors correlate equally, no mechanism structure.

---

## 4. NLP / Computational Applications

### 4.1 Does HPC predict where POS taggers should struggle?

**The boundary-variance prediction:** Boundary cases (items at category edges) should show elevated tagger disagreement. Not because the item is rare, but because mechanisms conflict there. Frequency-matched, boundary items should be harder to tag than prototype items.

**Testable:** Compare tagger accuracy (inter-tagger agreement) for prototype vs boundary items, frequency-matched. Predict: boundary items show lower agreement even at matched frequency. If agreement is uniform once frequency is controlled, boundary effects are just frequency effects.

**Data:** Universal Dependencies treebanks + multiple taggers (spaCy, Stanford, Flair). Feasible.

**Concrete example:** *Fun* (adjective or noun?). Boundary item. Taggers should disagree more on *fun* than on *happy* (prototype adjective) or *table* (prototype noun), even at matched frequency. If disagreement is uniform, boundary isn't doing work.

### 4.2 Should NLP category systems be redesigned based on HPC diagnostics?

**Current practice:** Universal Dependencies has 17 POS tags. Includes PRON (wastebasket), ADV (wastebasket). HPC says: wastebasket classes shouldn't be categories.

**HPC-informed proposal:** Split ADV into subclasses (sentential, VP-modifying, degree). Merge PRON into the categories those items actually belong to (determinatives, nouns). Test whether HPC-informed tagset improves downstream tasks (parsing, NER, machine translation).

**Testable:** Train parsers on HPC-informed vs UD tagset. Compare parsing accuracy. If UD tagset performs equally well, lumping wastebaskets doesn't hurt. If HPC tagset improves accuracy, wastebaskets are real categories for NLP even if they're not HPCs.

**Honest breakdown:** NLP optimises for task performance, not theoretical coherence. If wastebasket tags are useful for parsing (because they capture surface distributional regularities), NLP should keep them even if they're not HPCs. HPC might be right about natural language but wrong for engineering.

### 4.3 Does the coupling spectrum predict embedding geometry?

**The idea:** If categories differ in coupling tightness, their word embeddings should show different geometric structure. Tightly coupled categories (nouns) should form tight clusters in embedding space. Loosely coupled categories (adverbs) should be dispersed.

**Testable:** Measure within-category variance in embedding space (centroid distance, cluster tightness) for categories at different coupling strengths. Predict: skeleton categories tight, plumage categories loose, wastebasket classes no cluster at all.

**Method:** Word2Vec / GloVe embeddings + POS tags. Compute within-category variance. Rank categories by variance, compare to coupling spectrum.

**Prediction:** Nouns < Verbs < Adjectives < Adverbs (increasing variance). If variance is uniform, embeddings don't reflect coupling structure.

**Honest limitation:** Embedding geometry reflects co-occurrence, not mechanisms. Tight co-occurrence (adverbs with verbs) can produce tight clusters even without mechanism. This test confounds co-occurrence and coupling. Need to control for co-occurrence frequency.

### 4.4 Do LLMs learn HPC structure, or just surface co-occurrence?

**The hub-node question for LLMs:** If an LLM has learned genuine HPC structure (not just co-occurrence), perturbing a hub property should cascade to other properties. Perturbing a peripheral property shouldn't.

**Concrete test:** Fine-tune an LLM with *mass nouns take plural morphology* (perturb hub). Predict: definiteness system should destabilise (because individuation links countability and definiteness). If definiteness is unaffected, LLM hasn't learned mechanism structure -- just surface patterns.

**Experimental design:** Adversarial fine-tuning (perturb one diagnostic), test whether other diagnostics degrade. If cascade happens, LLM has HPC structure. If diagnostics are independent, LLM is n-gram statistics.

**Honest caveat:** LLMs are black boxes. Even if cascade happens, we don't know if it's because of learned mechanisms or because of statistical dependency in the training distribution. This test can falsify HPC (no cascade = no structure) but can't confirm it (cascade = structure OR statistical artifact).

### 4.5 Can you use HPC to improve few-shot learning?

**The mechanism-transfer idea:** If a learner understands the *mechanism* maintaining a category (not just surface form), they should be able to generalise from fewer examples. Teaching the hub property should enable one-shot learning of peripheral properties.

**Concrete test:** Teach an LLM (or neural net) countability via two curricula: (1) Hub-first (individuation → determiner selection → plural), (2) Random examples. Measure few-shot accuracy on novel nouns. Hub-first should require fewer examples to generalise.

**Prediction:** Hub-first curriculum should outperform random examples at matched total exposure. If no difference, hub-node story doesn't help learning efficiency.

**Data:** Artificial language learning (AGL) experiment with neural nets. Feasible but requires curriculum design.

---

## 5. Language Documentation and Revitalisation

### 5.1 If you're documenting an endangered language, does HPC tell you what to prioritise?

**The skeleton-first principle:** If transmission is reduced (few speakers, limited inter-generational transfer), skeleton categories (noun, verb, core TMA) should be documented exhaustively before plumage (adjective subclasses, adverbs, discourse particles). Why? Skeleton is the weight-bearing structure; plumage can be reconstructed later if skeleton is known.

**Concrete guidance:** Fieldwork time allocation: 70% skeleton, 30% plumage. If this differs from current best practice (equal time to all categories?), HPC provides new prioritisation heuristic.

**Testable (indirectly):** In documented-then-revitalised languages, does skeleton documentation predict revitalisation success better than plumage documentation? If no correlation, skeleton-first is theoretically motivated but practically irrelevant.

**Honest limitation:** Endangered languages often have unique plumage that's culturally salient (honorifics, evidentials, classifier systems). Prioritising skeleton might be theoretically sound but culturally inappropriate. Trade-off between linguistic structure and community priorities.

### 5.2 In revitalisation, does HPC predict what order to rebuild categories?

**The phase-transition prediction:** Categories need a critical mass of mechanisms to become self-sustaining. Revitalisation should aim to cross the phase-transition threshold for skeleton categories first (get nouns + verbs to self-sustaining), then build plumage on top.

**Concrete curriculum:** Teach individuation + plural morphology + determiner selection as a *package* (cross the threshold), rather than teaching determiners in week 1, plurals in week 5, individuation never. Package teaching should produce faster generalisation.

**Testable:** Two revitalisation curricula: (1) Package teaching (mechanism bundles), (2) Feature-by-feature. Measure time to productive use. Package should be faster if phase-transition story is right.

**Data requirement:** Needs a revitalisation programme willing to experiment with curriculum design. Ethically fraught; requires community buy-in.

### 5.3 Does mechanism density predict which categories can survive reduced transmission?

**The maintenance-threshold question:** If a category needs multiple mechanisms to stay stable (interactive alignment, iterated transmission, structural entrenchment), reduced transmission should degrade it. If a category can be sustained by entrenchment alone, it should survive even with few speakers.

**Prediction:** Nouns (high entrenchment, less alignment-dependent) should survive language obsolescence better than function words (low entrenchment, alignment-heavy). If both degrade equally, entrenchment vs alignment distinction doesn't predict survival.

**Empirical test:** Compare category erosion in obsolescing languages (last-speaker situations). Predict: content words persist, function words degrade first. If function words persist, mechanism-density story is wrong.

**Data availability:** Obsolescing language documentation (e.g., last speakers of Manx, Cornish, Elfdalian). Feasible but limited sample size.

**Honest caveat:** Language obsolescence is catastrophic, not selective. If transmission stops entirely, everything degrades. HPC predicts *ordering* of degradation (function words first), not *whether* degradation happens.

### 5.4 Can you predict which categories will be borrowed vs calqued in contact situations?

**The coupling-based prediction:** Tightly coupled categories (skeleton) are hard to borrow -- they're integrated with too many other systems. Loosely coupled categories (plumage) can be borrowed piecemeal. Borrowing should show asymmetry: lexicon and plumage first, skeleton last or never.

**Concrete prediction:** Discourse particles (loose coupling) should be borrowed frequently. Core case morphology (tight coupling) should resist borrowing. If both borrow equally, coupling doesn't predict borrowing.

**Empirical test:** Survey contact situations (WALS, Grambank). Measure borrowing rates for categories at different coupling strengths. Predict negative correlation: tight coupling = low borrowing rate.

**Honest breakdown:** Prestige and functional gap also predict borrowing. If borrowing is entirely prestige-driven, mechanism structure is irrelevant. Need to control for prestige and functional gap (hard).

---

## 6. Cross-Cutting: What All Branches Need

### 6.1 Mechanism density metric

Every applied prediction above assumes we can measure "mechanism density," "coupling tightness," "hub-node centrality." We can't yet. Developing these metrics is a pre-requisite for testing most HPC predictions.

**What's needed:**
- Operationalise coupling strength (number of independent mechanisms? correlation between diagnostics? network centrality?)
- Validate on native-speaker data (does metric predict known category differences?)
- *Then* apply to L2, clinical, diachronic, typological data

**Without this:** HPC predictions are qualitative, not quantitative. Can't be falsified rigorously.

### 6.2 Taxometric methods for linguistic categories

Psychiatry's MAXCOV, MAMBAC, L-Mode detect latent taxa vs continuous dimensions. Never applied to linguistic categories. Would settle the sharp-boundary debate empirically.

**Required:** Large-N gradient judgment data (hundreds of speakers, dozens of items). Doesn't exist yet for most categories.

### 6.3 Hub-node identification protocol

For teaching, clinical assessment, and revitalisation, we need to know which properties are hubs. Current method: post-hoc theorising. Need: empirical perturbation experiments.

**Proposed protocol:** Train speakers on artificial category with 4 diagnostics. Remove one diagnostic, test whether others degrade. Hub = the one whose removal causes largest cascade. Non-hub = removal doesn't affect others.

**Feasible:** Artificial language learning (AGL) studies. Has never been done with HPC motivation.

---

## 7. Honest Assessment: What HPC Doesn't Predict

### 7.1 Frequency effects

HPC doesn't predict Zipf's law, doesn't predict high-frequency advantage in acquisition or processing. Frequency matters, but it's orthogonal to HPC structure. HPC adds mechanism story on top of frequency, but if frequency accounts for 90% of variance, HPC's additional contribution might be marginal.

### 7.2 Universal Grammar debates

HPC is neutral on UG. If innate linguistic structures exist, they'd be some of the mechanisms maintaining categories. If they don't, categories are maintained by domain-general learning + social coordination. HPC doesn't settle this; it reframes it as a mechanism-identification question.

### 7.3 Language evolution (phylogeny)

HPC explains category maintenance within a language and across generations. It doesn't explain why human language has the categories it does rather than other possible category systems. That's a question about evolutionary origins, not maintenance. Different explanatory target.

### 7.4 Individual variation in non-categorical domains

HPC explains why categories are sharp where mechanisms are strong. It doesn't explain individual variation in phonetic detail, lexical semantics, or pragmatic inference. Those might not be category-like at all; HPC would predict they're *not* sharp because they're not maintained as clusters.

---

## 8. Summary: What's Genuinely New

HPC opens genuinely new questions when it:

1. **Predicts asymmetries:** Hub-node effects, asymmetric fraying, skeleton-before-plumage ordering.
2. **Predicts failures:** Wastebasket classes shouldn't project; negative classes shouldn't generalise; boundary cases should show variance spikes.
3. **Provides cross-domain methods:** Taxometrics, network analysis, phase-transition detection (all imports from biology/psychiatry).
4. **Makes mechanism-based predictions:** Coupling predicts borrowing rates, perturbation cascades, acquisition order.

HPC *doesn't* open new questions when it:

1. Relabels known phenomena (calling prototype effects "clustering" isn't new).
2. Describes data we already have without new predictions.
3. Predicts things that frequency/co-occurrence already predict (unless it makes a distinct prediction at matched frequency).

**Litmus test:** If the prediction would still hold even if categories *weren't* HPCs (just frequent co-occurrence, or arbitrary conventions), it's not genuinely HPC-specific.

**Standard met?** About 60% of the predictions above pass this test. The rest are relabellings or confounded with frequency. Keep the 60%; drop or refine the rest.

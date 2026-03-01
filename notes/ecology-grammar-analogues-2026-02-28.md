# Ecology-Grammar Analogues: Testing for Genuine Novelty

**Date:** 2026-02-28
**Context:** HPC opened new questions in ecology (community assembly, keystone species, niche theory). Do these have linguistic analogues that go beyond relabelling?

**Framework:** Linguistic categories are HPC kinds on a coupling spectrum: hard-coupled (phonemes) → loose-coupled (grammatical categories) → composite (constructions). "Skeleton" categories recur cross-linguistically; "plumage" categories may or may not be maintained.

**Critical standard for each analogue:**
- (a) Does this open a GENUINELY NEW question, or just relabel something we already know?
- (b) Does it make a TESTABLE prediction?
- (c) Where does the analogy BREAK DOWN?

---

## 1. Community Assembly Rules

### Ecological version

**Question:** What determines which species co-occur in a community?

**Mechanisms:**
- **Diamond's assembly rules:** Certain species combinations are forbidden because of competitive exclusion.
- **Environmental filtering:** Abiotic constraints (climate, soil) filter out species that can't tolerate local conditions.
- **Niche complementarity:** Species coexist by partitioning resources -- filling distinct functional niches prevents competitive exclusion.

### Linguistic analogue: Grammar assembly rules

**Question:** What determines which categories co-exist in a grammar?

#### (a) Are there "assembly rules" for grammars?

**Hypothesis:** Certain category combinations occur together more than chance because they share maintenance mechanisms or fill complementary niches. Others are forbidden because they compete for the same mechanism.

**Specific predictions:**

1. **Shared-mechanism co-occurrence.** Languages with robust countability systems should have definite articles more often than chance, because both recruit referential anchoring mechanisms. Testable against WALS/Grambank: calculate φ-coefficient between [±count/mass distinction] and [±definite article]. If φ > 0.3 and p < 0.001, co-occurrence isn't coincidental -- it's category-level comorbidity (psychiatric analogue, §2 below).

2. **Competitive exclusion.** Case systems and word-order rigidity compete for the same functional niche (argument-role marking). Languages should strongly prefer one or the other. Testable: negative correlation between morphological case richness and word-order flexibility. If they co-occur freely, functional niche story is wrong.

3. **Forbidden combinations.** If two categories require incompatible mechanisms, they shouldn't coexist. Example: Rigid classifier systems (Mandarin-style) and rich count/mass morphology. Classifiers provide individuation; so does count/mass. If both are maintained, they either (i) differentiate into distinct niches, or (ii) one erodes. Testable: languages with >30 productive classifiers should lack count/mass inflection. If they coexist, niche competition doesn't constrain category assembly.

#### (b) Environmental filtering

**Hypothesis:** Communicative/cognitive constraints filter out category combinations that exceed processing capacity or violate functional demands.

**Predictions:**

1. **Working memory ceiling.** Grammars with rich agreement systems (gender + number + case on adjectives, verbs, determiners) should have fewer tense/aspect distinctions. Both recruit working memory; maximum complexity is bounded. Testable: negative correlation between agreement complexity (count of cross-classifying features) and TMA complexity. If no correlation, processing constraint story is decorative.

2. **Communicative efficiency filtering.** Categories whose maintenance cost exceeds communicative payoff shouldn't persist. Gender systems with >10 classes should show higher semantic transparency than 2-3 class systems (more classes = more cognitive load, so functionality must justify it). Testable: measure semantic predictability of class assignment (e.g., via predictive models on noun semantics). If large systems are equally arbitrary, efficiency filtering doesn't operate.

#### (c) Niche complementarity

**Hypothesis:** Categories fill distinct functional niches. Filling one prevents another from occupying the same niche.

**Prediction:** Languages shouldn't have redundant categories with identical projection profiles. If two categories predict the same distributional/semantic facts, one should erode. Example: If adjectives and stative verbs both project modification + predication, they should show niche differentiation (different selectional restrictions, different syntactic frames) or competitive exclusion (one class shrinks). Testable: languages where adjectives = stative verbs should show *incipient* differentiation (frequency effects, subcategorization splits) if both classes are stable. If not, redundancy is tolerated.

#### Genuinely new?

**YES.** Traditional typology describes correlations (e.g., "languages with case tend to have free word order") but doesn't explain *why* via mechanism competition. HPC adds: correlations arise because categories compete for finite maintenance resources. Niche overlap → competitive exclusion. Shared mechanisms → facilitated co-occurrence.

#### Testable?

**YES.** All predictions above operationalise via typological databases. Falsifiable: if category co-occurrence is random after controlling for genealogy/geography, assembly rules don't exist.

#### Where does the analogy break down?

**Breakdown 1: No migration.** In ecology, species migrate into communities from external pools. Linguistic categories don't migrate -- they emerge via grammaticalization or are lost via attrition. Assembly is diachronic, not synchronic influx.

**Breakdown 2: No speciation within the community.** Ecology assumes species are formed elsewhere and then assemble. Grammars both *assemble* and *generate* categories internally (budding, competitive exclusion leading to differentiation).

**Breakdown 3: No death without replacement.** Ecosystems can lose species permanently. Grammars losing a category often redistribute its functions (case loss → word-order rigidification). Functional niche is conserved even when the category dies.

**Revised analogy:** Grammar assembly is closer to *metabolic pathway evolution* than community assembly. Pathways recruit enzymes (mechanisms), and new pathways emerge by duplicating and modifying existing ones. Functional redundancy is resolved by differentiation or competitive exclusion, but the metabolic function persists.

---

## 2. Keystone Species

### Ecological version

**Question:** Are there species whose removal causes disproportionate community collapse?

**Mechanism:** Keystone species maintain community structure via disproportionate ecological effects (e.g., sea otters control urchin populations; urchins control kelp; kelp supports entire fish community). Remove the keystone and the cascade propagates.

### Linguistic analogue: Keystone categories

**Question:** Are there categories whose loss triggers cascade effects on other categories?

#### (a) Is "noun" a keystone category?

**Hypothesis:** The noun/verb distinction is foundational. Its collapse would cascade through the grammar, destabilising adjectives (modification requires a nominal target), determiners (selection requires a nominal head), case (argument structure requires distinct nominals).

**Test:** Look for languages where the noun/verb distinction has collapsed or never crystallised. Predictions:
- Such languages should lack robust adjective classes (no clear nominal target for modification).
- Determiner systems should be absent or highly reduced.
- Case marking should be rare or semantically-based (not syntactic).

**Candidates:** Tagalog, Salishan languages (Straits Salish has been argued to lack a noun/verb distinction; see Kinkade 1983). Check whether these languages also lack the predicted downstream categories.

**Falsification:** If Salishan has robust adjective classes and determiners despite lacking noun/verb, then noun isn't a keystone -- other categories can be maintained independently.

#### (b) Functional categories as keystones

**Hypothesis:** Tense/aspect systems are keystones for verb morphology. Agreement systems are keystones for nominal morphology. Removing them cascades through related categories.

**Test:** Language death data. If tense is a keystone, its loss should predict loss of aspectual distinctions, modal markers, verb-class distinctions. If agreement is a keystone, its loss should predict loss of gender, case, adjective concord.

**Prediction:** In heritage language attrition, loss of agreement should predict faster erosion of gender distinctions than frequency alone would predict. Testable: compare heritage Turkish (rich agreement) vs heritage Mandarin (no agreement). If Turkish gender/case erodes faster once agreement is lost, keystone effect confirmed. If erosion is independent, no cascade.

#### (c) Constructions as keystones

**Hypothesis:** Argument structure constructions (ditransitive, caused-motion) are keystones for verb classes. Remove the construction and the verb class collapses.

**Test:** If English lost the ditransitive (*give X Y*), would the class of ditransitive verbs erode? Prediction: verbs that *only* occur in ditransitives (*grudge*, *begrudge*) should become obsolete or shift to prepositional frames. Verbs with multiple frames (*give* = *give X to Y*) should survive.

**Diachronic test:** Track verb classes across Old → Middle → Modern English as constructions are lost. If verb classes collapse when their keystone construction is lost, cascade confirmed.

#### Genuinely new?

**PARTIALLY.** Linguistics knows some categories are more "basic" than others (noun/verb > adjective; word order > case inflection). But the keystone framing asks a *causal* question: does removing X *cause* Y to collapse, or do they just tend to co-occur? Traditional typology describes correlations; keystone logic predicts directed cascades.

The HPC twist: keystone categories are those that *maintain other categories' mechanisms*. Nouns maintain determiners by providing a syntactic slot. Agreement maintains gender by providing a projection site. This is testable asymmetry.

#### Testable?

**YES.** Predictions above operationalise via:
- Typological databases (do languages lacking noun/verb also lack determiners?).
- Heritage attrition studies (does agreement loss predict gender erosion?).
- Diachronic corpus analysis (do verb classes collapse when constructions are lost?).

#### Where does the analogy break down?

**Breakdown 1: Categories aren't organisms.** Keystone species have demographic effects (otter eats urchins → urchin population drops). Categories don't "eat" each other. The analogy works only if one category *mechanistically sustains* another (agreement projects gender; noun provides determiner slot). Where maintenance is independent, no cascade.

**Breakdown 2: Functional redistribution.** Removing a keystone species causes collapse. Removing a category often redistributes its function. Case loss → word-order rigidification. The functional niche persists; the category doesn't.

**Breakdown 3: Bidirectional dependence.** Ecology assumes unidirectional cascades (top-down or bottom-up). Grammar shows bidirectional coupling: determiners require nouns, but nouns also recruit determiner-marking for definiteness projection. Which is the keystone?

**Revised analogy:** Categories are less like keystone species and more like *mutualistic partners* (coral and zooxanthellae). Each sustains the other. Remove one and the mutualism collapses, but there's no privileged "keystone" -- it's co-maintenance.

---

## 3. Ecological Succession

### Ecological version

**Question:** Do communities develop through predictable stages?

**Pattern:** Pioneer species (fast-growing, disturbance-tolerant) → intermediate species (slower-growing, competitive) → climax community (stable, self-maintaining). Each stage alters the environment to enable the next.

### Linguistic analogue: Grammar development stages

#### (a) Creole development as succession

**Hypothesis:** Creoles develop through predictable category-emergence stages. Early stages = "pioneer" categories (noun, verb, basic word order). Later stages = "climax" categories (gender, agreement, complex TMA).

**Prediction (from gauntlet-reframing):** Noun/verb emerge first. TMA before adjective class. Gender/noun-class last or never. The coupling-spectrum ordering predicts the succession sequence: skeleton categories (tightly coupled cross-linguistically) before plumage categories (loosely coupled).

**Test:** Nicaraguan Sign Language (NSL) and Tok Pisin development. Track which categories crystallise in which generation/cohort. If gender emerges before adjectives, succession ordering is wrong.

**Falsification:** If category emergence order is random across creoles, succession pattern doesn't exist.

#### (b) Language acquisition as succession

**Hypothesis:** Children acquire categories in a predictable order. Early = skeleton categories with dense mechanisms. Late = plumage categories with sparse mechanisms.

**Prediction:** Nouns before verbs before adjectives. Determiners before agreement. Tense/aspect before mood. Order should correlate with mechanism density (cross-linguistic recurrence predicts acquisition order).

**Test:** Use cross-linguistic acquisition data (CHILDES corpora). Measure age-of-acquisition for category-diagnostic constructions (*a(n)* = count noun; *-ed* = past tense). If skeleton categories (noun, verb) are acquired earlier across languages than plumage categories (adjective), succession confirmed.

**Falsification:** If acquisition order varies freely across languages, mechanism density doesn't predict succession.

#### (c) Category emergence in language genesis

**Hypothesis:** When languages emerge from scratch (sign language genesis, pidgin → creole), categories emerge in succession-like stages. Early stages establish foundational categories that create maintenance infrastructure for later categories.

**Prediction:** Determiner systems emerge before agreement systems (determiners create a structural slot that agreement can parasitize). TMA systems emerge before evidentiality (TMA creates temporal anchoring that evidentiality builds on).

**Test:** Track NSL across three generations. If determiners precede agreement, succession confirmed. If they emerge simultaneously or reverse-order, infrastructure-dependence story is wrong.

#### Genuinely new?

**MIXED.** Acquisition research knows there's an order (nouns before adjectives; basic word order before inflection). But traditional explanations invoke frequency, salience, or processing complexity. HPC adds: order reflects *mechanism-dependence*. Later categories parasitize maintenance infrastructure created by earlier categories. This predicts succession asymmetry: you can have nouns without determiners, but not determiners without nouns.

The succession framing adds: each stage *enables* the next by creating maintenance infrastructure. This is testable: intervene to block an early-stage category and later-stage categories shouldn't emerge.

#### Testable?

**YES.** Creole development and sign language genesis provide natural experiments. If category order is consistent across independent cases, succession pattern is real. If random, it's not.

#### Where does the analogy break down?

**Breakdown 1: No environmental modification.** Ecological succession works because early species modify the environment (nitrogen fixation, soil building) to enable later species. Linguistic categories don't "modify the environment" -- they create *maintenance infrastructure*. Closer analogy: developmental stages in embryogenesis, where early structures scaffold later ones.

**Breakdown 2: No climax stability.** Ecological climax communities are self-maintaining and resist change. Grammars never reach stable climax -- they're always undergoing drift, contact-induced change, internal restructuring. The analogy works for *emergence* but breaks for *maintenance*.

**Breakdown 3: Reversibility.** Ecological succession is largely unidirectional (disturbed → pioneer → climax). Grammatical development is bidirectional: categories can emerge (grammaticalization) or collapse (attrition, creolization). The succession analogy captures emergence but not the full lifecycle.

**Revised analogy:** Grammar development is less like ecological succession and more like *ontogeny*. Early developmental stages create structures (heart, brain) that scaffold later stages (limbs, sensory systems). But unlike succession, ontogeny is repeatable and programmed. Grammar development is more contingent.

---

## 4. Trophic Cascades

### Ecological version

**Question:** When you remove a top predator, does the effect cascade through the food web?

**Pattern:** Remove wolves → deer population explodes → overgrazing → vegetation collapses → soil erosion → stream degradation. The cascade propagates down trophic levels.

### Linguistic analogue: Cross-level cascades

**Question:** Does perturbing a category at one level of the coupling spectrum cascade to other levels?

#### (a) Top-down cascades (construction → category → phonology)

**Hypothesis:** Removing a construction-level pattern cascades down through grammatical categories to phonological realization.

**Prediction:** Loss of the ditransitive construction (*give X Y*) should cascade:
- **Level 1 (construction):** Ditransitive frame becomes unproductive.
- **Level 2 (category):** Ditransitive verb class erodes (keystone effect, §2c).
- **Level 3 (phonology):** Verbs that specialized for ditransitives (*grudge*) become obsolete → their phonological forms drift or disappear.

**Test:** Diachronic corpus analysis across Old → Modern English. Track: (i) ditransitive frame productivity, (ii) ditransitive verb class size, (iii) phonological realization of ditransitive-only verbs. If cascade is real, all three decline together. If independent, no cascade.

**Falsification:** If verb class remains stable despite construction loss, cascade doesn't propagate.

#### (b) Bottom-up cascades (phonology → category → construction)

**Hypothesis:** Phonological mergers cascade up through categories to constructions.

**Prediction:** Loss of phonological distinctions (e.g., cot-caught merger, which-witch merger) should cascade:
- **Level 1 (phonology):** */ɔ/–/ɑ/* merger eliminates minimal pairs.
- **Level 2 (category):** Lexical distinctions collapse (*cot* = *caught*).
- **Level 3 (construction):** Constructions that relied on the distinction become unproductive.

**Test:** Track *wh*-questions in speakers with vs without the *which-witch* merger. If the merger cascades up, speakers with the merger should show reduced productivity of *which*-questions (collapsed into *that*-relatives). If no effect, phonology doesn't cascade up.

**Falsification:** If phonological mergers leave category structure intact, bottom-up cascades don't exist.

#### (c) Perturbation sensitivity at coupling joints

**Hypothesis:** Cascades propagate most readily across *loose coupling* joints. Hard-coupled systems (phonemes ↔ allophones) resist cascades. Loose-coupled systems (categories ↔ constructions) transmit them.

**Prediction:** Phonological mergers shouldn't cascade to syntax (hard coupling blocks transmission). Case loss should cascade to word-order (loose coupling transmits perturbation).

**Test:** Compare cascade strength across coupling regimes:
- **Hard coupling:** Measure effect of cot-caught merger on syntactic category structure. Predict: no effect.
- **Loose coupling:** Measure effect of case loss on word-order rigidity. Predict: strong effect.

If both show equal cascade strength, coupling tightness doesn't modulate transmission.

#### Genuinely new?

**YES.** Traditional linguistics treats levels (phonology, morphology, syntax) as largely independent modules. Cascades predict *directed propagation* of perturbations across levels. The coupling-spectrum framework predicts where cascades propagate (loose coupling) vs where they're blocked (hard coupling).

This is a genuine architectural claim about grammar as a coupled system, not separate modules.

#### Testable?

**YES.** Diachronic corpora and phonological merger studies provide natural experiments. Measure perturbation → cascade strength. If cascades occur and correlate with coupling tightness, prediction confirmed. If levels are independent, cascade model is wrong.

#### Where does the analogy break down?

**Breakdown 1: Trophic structure doesn't map cleanly.** Food webs have clear trophic levels (producers → herbivores → predators). Linguistic levels aren't hierarchical in the same way. Phonology doesn't "feed" categories; it's a *realization* of categories. The cascade metaphor assumes feeding relationships that don't exist.

**Breakdown 2: Cascades are asymmetric.** Ecology predicts top-down (predator removal) and bottom-up (productivity change) cascades. Linguistics shows *stronger* bottom-up effects (phonology → morphology → syntax loss) than top-down (syntax loss rarely affects phonology). Why the asymmetry? HPC story: realization is downstream from categorization, so upstream perturbations propagate down, but downstream perturbations don't propagate up.

**Breakdown 3: Functional redistribution again.** Removing a predator causes population explosion (no redistribution). Removing a category redistributes its function. Case loss → word-order rigidity. The cascade propagates, but the functional niche is conserved.

**Revised analogy:** Linguistic cascades are less like trophic cascades and more like *metabolic pathway disruption*. Block an enzyme upstream and downstream products don't form. Block downstream and upstream products accumulate or get rerouted. The pathway logic is right; the trophic structure doesn't map.

---

## 5. Invasive Species / Competitive Exclusion

### Ecological version

**Question:** When a new species enters an ecosystem, can it outcompete and replace natives?

**Pattern:** Invasive species with superior competitive ability displace natives that occupy the same niche. Native species either go extinct or retreat to marginal habitats.

### Linguistic analogue: Contact-induced category replacement

#### (a) Contact as invasion

**Hypothesis:** Language contact introduces "invasive" categories that outcompete native categories occupying the same functional niche.

**Example:** English influence on heritage languages. English article system (*a, the*) is an "invasive" category. Does it outcompete native definiteness-marking strategies (Turkish *-in* suffix, Russian demonstratives)?

**Prediction:** Contact-induced category replacement should follow competitive exclusion logic:
- **Same niche:** If the invasive category occupies the same functional niche as the native, the native erodes.
- **Different niche:** If they differentiate (invasive takes formal register, native takes informal), both coexist.

**Test:** Heritage Turkish speakers. Measure: (i) use of Turkish *-in* (genitive = possessive, also marks definiteness), (ii) use of English *the*. If they compete for the same niche (definite marking), Turkish *-in* should erode. If they differentiate (Turkish for possessives, English for definiteness), both survive.

**Falsification:** If heritage speakers use both interchangeably without functional differentiation, competitive exclusion doesn't operate.

#### (b) Mechanism density predicts resistance

**Hypothesis:** Categories with dense maintenance mechanisms resist invasion. Categories with sparse mechanisms are vulnerable.

**Prediction:** Skeleton categories (noun, verb) should resist contact-induced replacement. Plumage categories (gender, adjective) should be vulnerable. Contact should erode gender systems before noun/verb distinctions.

**Test:** Heritage language attrition studies. Measure category erosion rate across coupling spectrum. Predict:
- **Tight coupling (skeleton):** Nouns, verbs, basic word order resist erosion.
- **Loose coupling (plumage):** Gender, case, agreement erode first.

If tight-coupled categories erode as fast as loose-coupled, mechanism density doesn't predict resistance.

#### (c) Which categories are most vulnerable?

**Hypothesis:** Categories vulnerable to invasion are those that:
1. Occupy redundant niches (gender provides little referential leverage).
2. Have few dedicated mechanisms (no unique syntactic frame).
3. Are phonologically reduced (low perceptual salience).

**Prediction:** Turkish gender (noun classes via phonology, no agreement) should erode faster in heritage speakers than Russian gender (noun classes + agreement + adjective concord). Russian has more mechanisms sustaining the category.

**Test:** Compare Turkish vs Russian heritage speakers. If Turkish gender erodes faster, mechanism density predicts vulnerability. If they erode equally, other factors dominate (frequency, salience).

#### Genuinely new?

**YES.** Contact linguistics describes borrowing and attrition but rarely asks: *why do some categories resist contact better than others?* HPC predicts: mechanism density is the key variable. Categories are like species with different competitive abilities -- dense mechanisms = superior competitor.

This reframes contact as *ecological competition* between categories, not just lexical borrowing or structural convergence.

#### Testable?

**YES.** Heritage language studies provide natural experiments. Measure erosion rate across categories and correlate with mechanism density (operationalized as cross-linguistic recurrence, diagnostic count, coupling tightness). If correlation holds, invasion resistance is real. If random, mechanism density doesn't predict.

#### Where does the analogy break down?

**Breakdown 1: No literal competition.** Species compete for finite resources (food, space). Categories don't compete for finite "niche space" -- they're cognitive/communicative structures, not populations. The analogy works metaphorically (functional niche occupation) but breaks mechanistically (no population dynamics).

**Breakdown 2: Bilingual speakers maintain both.** Invasive species displace natives. Contact languages often maintain both systems (code-switching, diglossia). Competitive exclusion predicts one category should die. Bilingualism shows both can coexist if speakers keep them functionally separated.

**Breakdown 3: Borrowing isn't invasion.** Ecology assumes species enter from outside. Contact can involve borrowing (external) or restructuring (internal). Creolization creates new categories from inherited material, not invasion. The invasion metaphor works for some contact scenarios (heritage attrition) but not others (creolization, Sprachbund convergence).

**Revised analogy:** Contact-induced replacement is less like invasive species and more like *horizontal gene transfer* (bacteria swapping genes). The new element integrates into the existing system, sometimes displacing native elements, sometimes creating hybrid categories. The ecology metaphor works for competitive displacement but not for creative restructuring.

---

## 6. Resilience and Regime Shifts

### Ecological version

**Question:** Can ecosystems absorb perturbation up to a threshold, then shift to a new stable state?

**Pattern:** Ecosystems show *resilience* (ability to absorb disturbance and return to equilibrium) until perturbation exceeds a threshold. Beyond the threshold, the system undergoes a *regime shift* to a qualitatively different stable state (shallow lake → algae-dominated; coral reef → urchin barren).

### Linguistic analogue: Grammatical regime shifts

#### (a) Creolization as regime shift

**Hypothesis:** Pidginization perturbs a grammar up to a threshold. Beyond that threshold, the system undergoes a regime shift: the pidgin can't "recover" the full category inventory of its lexifier(s). Instead, it stabilizes in a new state (creole) with a reduced, restructured category system.

**Prediction:** Creolization isn't gradual category loss. It's a threshold effect. Below the threshold (stable bilingualism, borrowing), the grammar maintains its full category inventory. Above the threshold (community-wide pidginization, generational transmission interrupted), the grammar shifts to a creole regime with:
- Reduced morphology (loss of case, gender, agreement).
- Analytic syntax (loss of inflection, rise of periphrastic marking).
- Restructured TMA (reanalysis of lexical verbs as grammatical markers).

**Test:** Compare language-contact scenarios across the threshold:
- **Below threshold:** Stable bilingual communities (Quechua-Spanish in Andes). Predict: both languages maintain full category inventories.
- **Above threshold:** Pidgin → creole (Tok Pisin, Haitian Creole). Predict: creole has qualitatively different category system, not just reduced version of lexifier.

If creoles are just "simplified" versions of their lexifiers (gradual reduction, no qualitative shift), regime-shift model is wrong.

#### (b) Threshold for recovery

**Hypothesis:** Grammars can recover from perturbation (contact, attrition) up to a threshold. Beyond the threshold, they can't recover the original category inventory even if the perturbation is removed.

**Prediction:** Heritage languages with mild attrition (2nd generation, regular contact with L1 community) should show recovery when speakers return to the L1 community. Heritage languages with severe attrition (3rd+ generation, no L1 contact) should show no recovery -- the category system has crossed the threshold into a new regime.

**Test:** Track heritage Russian speakers who return to Russia:
- **Mild attrition (2nd gen):** Predict recovery of case, gender, agreement.
- **Severe attrition (3rd gen):** Predict no recovery -- their Russian stabilizes as a restructured variety (heritage Russian, not native Russian).

If both groups show equal recovery, threshold doesn't exist.

#### (c) What determines the threshold?

**Hypothesis:** The threshold is determined by *mechanism density*. Categories with dense mechanisms have high resilience (large perturbation needed to shift regime). Categories with sparse mechanisms have low resilience (small perturbation triggers regime shift).

**Prediction:** Skeleton categories (noun, verb) should have high thresholds -- require extreme perturbation to collapse. Plumage categories (gender, agreement) should have low thresholds -- collapse under mild perturbation.

**Test:** Measure perturbation strength (e.g., % of community speaking L2, generations since full competence) and category erosion across the coupling spectrum. If skeleton categories resist until perturbation is extreme, while plumage categories collapse early, threshold correlates with mechanism density.

If all categories collapse at the same perturbation level, mechanism density doesn't determine resilience.

#### Genuinely new?

**YES.** Contact linguistics and attrition research describe category loss as gradual. Regime-shift logic predicts *nonlinear* dynamics: resilience up to a threshold, then qualitative shift. This is testable: plot category erosion against perturbation strength. HPC predicts sigmoidal curve (flat → steep drop → flat). Gradual-loss models predict linear decline.

The threshold question is genuinely new: *how much perturbation can a category absorb before it shifts to a qualitatively different state?* Traditional research doesn't ask this because it lacks a maintenance-mechanism framework to define "threshold."

#### Testable?

**YES.** Heritage attrition studies and creolization data provide tests. Measure perturbation strength and category state. If sigmoidal relationship appears (resilience → threshold → regime shift), prediction confirmed. If linear, regime-shift model is wrong.

#### Where does the analogy break down?

**Breakdown 1: Ecosystems have stable alternative states.** Shallow lakes can be clear-water or algae-dominated; both are stable. Do grammars have multiple stable states? Possibly: analytic (Mandarin) vs synthetic (Turkish) are stable "regimes." But it's unclear whether these are *alternative states of the same system* or *different systems entirely*.

**Breakdown 2: Hysteresis.** Ecological regime shifts show *hysteresis*: reversing the perturbation doesn't reverse the regime shift. You have to push the system back past a different (lower) threshold. Does grammar show hysteresis? If heritage speakers can't recover their L1 even when immersed, that's hysteresis. If they recover instantly, no hysteresis.

**Breakdown 3: Prediction requires basin landscape.** Ecology models resilience via *basin of attraction* diagrams. You can map the stability landscape and predict where regime shifts occur. Linguistics lacks this formal machinery. We don't have a "stability landscape" for grammars. The analogy is conceptual, not formal.

**Revised analogy:** Grammatical regime shifts are real but undertheorized. The ecology analogy identifies the phenomenon (threshold-crossing, alternative stable states) but linguistics needs its own formalism -- possibly via dynamical systems theory (attractors, bifurcations) rather than ecological models.

---

## Summary: Which Analogues Work?

| Analogue | Genuinely New? | Testable? | Key Breakdown |
|----------|---------------|-----------|---------------|
| **Community assembly** | YES (mechanism competition explains typological correlations) | YES (WALS/Grambank predictions) | No migration; categories emerge internally |
| **Keystone species** | PARTIAL (keystone = mechanistic dependence; known but not formalized) | YES (attrition cascades, typological asymmetries) | Categories co-maintain; no privileged keystone |
| **Ecological succession** | MIXED (acquisition order known; mechanism-dependence framing new) | YES (creole/NSL development stages) | No environmental modification; no climax stability |
| **Trophic cascades** | YES (cross-level propagation via coupling joints) | YES (phonological merger → category loss) | Trophic structure doesn't map; functional redistribution |
| **Invasive species** | YES (mechanism density predicts resistance to contact) | YES (heritage attrition, category-specific erosion) | No literal competition; bilingualism maintains both |
| **Regime shifts** | YES (threshold dynamics, nonlinear collapse) | YES (creolization, heritage attrition curves) | Lack of formal stability landscape; hysteresis unclear |

### The Pattern

The analogues work best when they operationalize *mechanism-based dynamics* that traditional linguistics treats as descriptive patterns:
- **Assembly rules:** Typological correlations arise from mechanism competition.
- **Cascades:** Cross-level effects propagate via coupling joints.
- **Regime shifts:** Category collapse is nonlinear, threshold-mediated.
- **Invasion resistance:** Mechanism density predicts contact vulnerability.

They break down when:
- Linguistic categories don't behave like organisms (no demography, no literal competition).
- Functional redistribution conserves niches even when categories collapse.
- Grammar lacks the formal machinery ecology uses (basin landscapes, trophic levels).

### The Upshot

Ecology-grammar analogues open **six genuinely testable predictions** that go beyond relabelling:

1. **Category co-occurrence follows mechanism-sharing** (shared anchoring → countability + definiteness co-occur).
2. **Keystone categories maintain others via structural dependence** (agreement loss cascades to gender erosion).
3. **Category emergence follows succession order** (skeleton before plumage, across creoles/NSL).
4. **Perturbations cascade across coupling joints** (case loss → word-order rigidification; phonological merger doesn't cascade to syntax).
5. **Mechanism density predicts contact resistance** (tight coupling resists attrition; loose coupling erodes first).
6. **Grammatical regime shifts are threshold-mediated** (creolization as nonlinear collapse, not gradual simplification).

All six are testable against typological databases, heritage attrition studies, creole development, and diachronic corpora. If these predictions fail, the HPC-ecology synthesis is decorative. If they succeed, it's a genuine research programme.

---

## Recommendation for the Book

**Include:** Community assembly (§1a-c), keystone categories (§2a-b), regime shifts (§6a-c). These operationalize HPC dynamics with clear predictions.

**Mention briefly:** Succession (known pattern, HPC adds mechanism-dependence framing). Cascades (compelling but needs more formal development). Invasive species (good metaphor but breaks down on bilingualism).

**Omit:** Trophic structure (maps poorly to grammar). Hysteresis (unclear if it exists in grammar). Climax stability (grammars never stabilize).

The ecology analogues are strongest when they predict *asymmetries*: which categories co-occur, which resist contact, which collapse first, where cascades propagate. These asymmetries distinguish HPC from "categories are convenient labels" and from essentialist "categories have necessary/sufficient conditions." The breakdowns matter as much as the successes -- they identify where grammar diverges from ecology and where linguistics needs its own formal machinery.

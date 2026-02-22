# Chapters 7 & 9 ABM Review Packet (2026-02-22)

## Scope
Review ABM-related sections in Chapter 7 and Chapter 9 after recent revisions.

## Chapter 7: ABM prose excerpt

   173	\subsection{Simulation interlude: The Volcanic Island}
   174	\label{sec:7:simulation-interlude}
   175	
   176	To make the mechanism/projectibility distinction concrete, we can use an \term{agent-based model} (ABM).\footnote{The Python scripts for the simulations in this book are available at \url{https://github.com/BrettRey/hpc-book/tree/main/code}.} ABMs are computational toy worlds where researchers specify simple rules for individual \enquote{agents}~-- how they interact, what they say, and how they learn from each other's outputs. By letting these artificial speakers loose to talk to each other over thousands of simulated interactions, we can observe what kinds of macroscopic structures (like grammatical categories) spontaneously emerge or stabilize from their local behavior.
   177	
   178	The role of the ABM here is illustrative rather than probative. It doesn't test the Polish data directly or calibrate to corpus frequencies. It asks a narrower question: if the mechanism story is right, does a minimal toy system generate the qualitative signature we claim?
   179	
   180	Consider a minimal ABM demonstrating this exact dynamic: a simple system in which a category label stays extensionally stable while its maintaining mechanisms change.
   181	
   182	Imagine a population of agents producing and learning a binary opposition (like perfective/imperfective) over a set of lexemes (the \enquote{island}).
   183	
   184	In Phase~1 (the active volcano), there is a global semantic regularity that is highly predictive of the category. As agents interact, they learn via simple prediction-error updates to rely on this semantic cue (internal weight $w$) to predict the correct form. Meanwhile, through repeated exposure, they also establish and tighten an item-specific boundary $\theta$ (the \enquote{coral} taking root).
   185	
   186	In Phase~2, the volcano goes dormant: the semantic signal is replaced by pure uncorrelated noise. It no longer predicts anything.
   187	
   188	If we track the agents' learning, the result gives a clear qualitative signature consistent with the maintenance view (Figure~\ref{fig:volcano_drift}).
   189	
   190	\begin{figure}[htpb]
   191	\centering
   192	\includegraphics[width=0.9\textwidth]{figures/volcano_drift_experiment.pdf}
   193	\caption{A minimal simulation of mechanistic drift. In Phase~1, the semantic mechanism is highly predictive. In Phase~2, the semantic cue goes dormant (becomes pure noise). As Panel~A shows, the observable \emph{semantic cue effect} collapses in Phase~2. The internal \emph{semantic coefficient} ($w$) weakens but remains positive as a residual vestige rather than vanishing. Meanwhile, as Panel~B shows, the extensional stability of the category (the boundary similarity to Phase~1) remains robust, maintained by the boundary parameters taking over the predictive work.}
   194	\label{fig:volcano_drift}
   195	\end{figure}
   196	
   197	As soon as the semantic signal becomes unreliable, the observable behaviour changes: the \emph{semantic cue effect}~-- the difference the cue makes to production probability~-- collapses. Yet the internal \emph{semantic coefficient} ($w$) doesn't vanish. In this model, once the cue is uncorrelated with outcomes, updates to $w$ become near-zero in expectation; $w$ relaxes downward somewhat, then plateaus as a residual vestige rather than being fully unlearned.
   198	
   199	Meanwhile, the category boundaries themselves~-- the extensional stability of the population's grammar (Panel B)~-- persist robustly. The population consensus remains sharp. When the original historical mechanism dies, the behaviour is sustained by a completely different set of contemporary stabilisers: the entrenched item-specific boundaries ($\theta$) that have shifted to absorb the predictive load.
   200	
   201	This computational sketch is consistent with the core methodological claim of the maintenance view: a category can remain extensionally real and predictively useful while the textbook \enquote{invariant meaning} story becomes causally inert. The semantic representation may genuinely exist in the cognitive system (as a historical fossil), but what projects synchronically is the cue structure and boundary entrenchment, not the historically inherited semantic story.

## Chapter 9: ABM prose excerpt

   271	\subsection{The unstable hybrids: Data}
   272	
   273	Then there is \mention{data}.
   274	
   275	On March 11, 2015, Minnesota legislators halted work on a license-plate reader bill to debate grammar. The bill text read \mention{the data are private}; Representative John Lesch insisted \mention{data} is singular. The committee voted; the motion passed unanimously; Lesch pumped his fist. The law was amended: \mention{data is}. Grammar rarely gets a roll-call vote, so it took the opportunity.
   276	
   277	Lesch won the vote, but he entered what usage expert Bryan Garner calls a \mention{skunked} term argument \citep{garner2016}. \mention{Data} is currently moving from the count basin (Latin plural of \mention{datum}) toward looser count packaging and, in some registers, toward mass construal (synonym for \mention{information}). In the transition, it exhibits the behavior of a system seeking a new equilibrium. Scientists say \mention{data are}. Tech CEOs say \mention{data is}. The cluster is reweighted, property by property. Historically the plural of \mention{datum}, it's shifting in everyday usage: \mention{this data is} and other singular-agreement patterns are now common, especially in informal and spoken registers. Corpus studies confirm that singular agreement with \mention{data} now predominates in most registers \citep{garner2016}.
   278	
   279	Why is \mention{data} drifting? Because its functional anchor is disappearing. \mention{Datum}~-- the singulative~-- has become archaic, confined to philosophy-of-science contexts and pedantic style guides. Without a robust singulative in active use, the tight-linkage properties have nothing to attach to. Speakers who need to refer to a single piece of information say \mention{data point}, not \mention{datum}. But \mention{data point} is a compound, not a singulative of \mention{data}. It doesn't anchor the count cluster the way \mention{officer} anchors \mention{police}.
   280	
   281	Result: \mention{data} drifts toward the loose end of the scale. Tight properties erode (\mention{three data} was always rare), while loose ones can remain robust for long periods. If the drift continues and further mechanisms align with it, fully mass packaging becomes possible~-- with expressions like \mention{data point} carrying precision where needed.
   282	
   283	This is the quasi-count pattern run in reverse. \mention{Cattle} is stable because \mention{cow} exists. \mention{Data} is drifting because \mention{datum} is dying.
   284	
   285	We can model this dynamic computationally to expose the expected drift signature (Figure~\ref{fig:data_drift}).\footnote{The Python scripts for the simulations in this book are available at \url{https://github.com/BrettRey/hpc-book/tree/main/code}.} This simulation is a didactic mechanism sketch, not calibrated empirical proof. Agents in the model are intentionally simple: each speaker stores a confidence score for how individuated a noun is, chooses packaging for basic communicative intents (one item, exact small quantity, vague many, existence, mass quantity), updates that confidence from what they hear, and is periodically replaced by new learners with weak priors who bootstrap from finite tutor exposure. In representative runs under this parameterization, \mention{a(n)} and \mention{three} decline substantially while \mention{many}/agreement stay near ceiling over the same window. The computational model therefore captures asymmetric fraying rather than immediate category collapse.
   286	
   287	\begin{figure}[htpb]
   288	\centering
   289	\includegraphics[width=1\textwidth]{figures/data_drift_experiment.png}
   290	\caption{Simulated data drift. Panel A tracks anchor erosion over phases: declining \mention{datum} availability, declining \mention{datum} individuation, and the associated shift in \mention{data} individuation. Panel B shows the corresponding constructional profile: tighter properties (\mention{a(n)}, low cardinals) weaken first, while looser properties (\mention{many}, agreement) remain comparatively robust over the same interval.}
   291	\label{fig:data_drift}
   292	\end{figure}
   293	
   294	%~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- --
   295	\section{Cross-linguistic parallels}
   296	\label{sec:9:cross-linguistic}

## Countability ABM code: status and assumptions

     1	#!/usr/bin/env python3
     2	"""
     3	Countability Agent-Based Model
     4	==============================
     5	
     6	A DIDACTIC MECHANISM SKETCH for Chapter 9 of "Words That Won't Hold Still."
     7	
     8	STATUS: This is an intuition pump, not evidence. It makes the two-cluster story
     9	and the implicational hierarchy visible by operationalizing the mechanisms as
    10	interacting update rules. It is NOT a calibrated simulation and should not be
    11	cited as empirical support for the theory.
    12	
    13	Core components:
    14	- Agents with lexicons containing individuation confidence per noun
    15	- Constructions as "locks" with tolerance thresholds (tight to loose)
    16	- Bidirectional inference: production and comprehension update beliefs
    17	- Multi-timescale maintenance: processing, acquisition, transmission
    18	- Institutional layer: prescriptive feedback from editors/teachers
    19	- Functional anchoring: singulative alternatives bleed regularization pressure
    20	
    21	The model demonstrates:
    22	1. Tight-before-loose erosion (data drift as datum dies)
    23	2. Functional anchoring as stabilizer (cattle stable with cow available)
    24	3. Why prescriptivism struggles (LEGO -> Legos despite corporate campaigns)
    25	
    26	STRESS TEST: The ablation experiment removes mechanisms and shows the pattern
    27	breaks, proving the results aren't automatic/tautological.
    28	
    29	Usage:
    30	    python countability_abm.py              # Run all experiments

## Countability ABM code: agent assumptions

   522	    def _sample_intent(self, noun: str, speaker: Agent) -> str:
   523	        """
   524	        Sample communicative intent conditioned on the noun's current profile.
   525	
   526	        High-individuation nouns are usually discussed in count-like contexts.
   527	        Lower-individuation nouns are more likely to occur in mass-quantity uses.
   528	        """
   529	        intents = ['singleton', 'exact_small', 'vague_many', 'existence', 'mass_quantity']
   530	
   531	        if noun not in speaker.lexicon:
   532	            return random.choice(intents)
   533	
   534	        ind = speaker.lexicon[noun].individuation
   535	        if ind >= 0.85:
   536	            weights = [0.38, 0.25, 0.22, 0.13, 0.02]
   537	        elif ind >= 0.65:
   538	            weights = [0.24, 0.20, 0.28, 0.18, 0.10]
   539	        elif ind >= 0.45:
   540	            weights = [0.12, 0.12, 0.30, 0.26, 0.20]
   541	        else:
   542	            weights = [0.05, 0.05, 0.20, 0.30, 0.40]
   543	
   544	        return random.choices(intents, weights=weights, k=1)[0]
   545	
   546	    def step(self, interactions_per_step: int = 50):
   547	        """
   548	        Run one time step of the simulation.
   549	
   550	        Each step:
   551	        1. Random pairs of agents interact
   552	        2. Speaker produces, hearer observes
   553	        3. Institutional agents may provide corrections
   554	        """
   555	        self.time_step += 1
   556	
   557	        for _ in range(interactions_per_step):
   558	            # Pick speaker and hearer
   559	            speaker, hearer = random.sample(self.agents, 2)
   560	
   561	            # Pick a noun to talk about (weighted by frequency)
   562	            noun = self._sample_noun_by_frequency()
   563	
   564	            # Pick a communicative intent conditioned by current noun profile.
   565	            intent = self._sample_intent(noun, speaker)
   566	

## Countability ABM code: drift protocol + ablation design

   757	def _run_data_drift_protocol(
   758	    world: World,
   759	    n_phases: int = 10,
   760	    steps_per_phase: int = 35,
   761	    interactions_per_step: int = 60,
   762	    turnover_rate: float = 0.04,
   763	    apply_datum_decay: bool = True
   764	) -> List[Dict[str, float]]:
   765	    """
   766	    Shared protocol for the data-drift experiment and its ablations.
   767	    """
   768	    phase_data: List[Dict[str, float]] = []
   769	
   770	    for phase in range(n_phases):
   771	        if apply_datum_decay:
   772	            for _ in range(4):
   773	                world.perturb_singulative_availability('datum', decay_rate=0.20)
   774	
   775	        world.run(n_steps=steps_per_phase, interactions_per_step=interactions_per_step)
   776	        if turnover_rate > 0:
   777	            world.generational_turnover(turnover_rate=turnover_rate)
   778	
   779	        data_profile = world.get_community_profile('data')
   780	        data_ind_mean = sum(a.lexicon['data'].individuation for a in world.agents) / len(world.agents)
   781	        datum_ind_mean = sum(a.lexicon['datum'].individuation for a in world.agents) / len(world.agents)
   782	        datum_frequency = world.noun_specs['datum'].frequency_weight
   783	
   784	        phase_data.append({
   785	            'phase': phase + 1,
   786	            'a(n)': data_profile['a(n)'],
   787	            'three': data_profile['three'],
   788	            'many': data_profile['many'],
   789	            'agreement': data_profile['agreement'],
   790	            'much': data_profile['much'],
   791	            'data_ind_mean': data_ind_mean,
   792	            'datum_ind_mean': datum_ind_mean,
   793	            'datum_frequency': datum_frequency,
   794	        })

  1048	def experiment_mechanism_ablation(seed: int = 42) -> Dict[str, World]:
  1049	    """
  1050	    STRESS TEST: Mechanism ablation to prove results aren't automatic.
  1051	
  1052	    This version compares drift trajectories under targeted mechanism removals.
  1053	    """
  1054	    print("\n" + "="*70)
  1055	    print("STRESS TEST: Mechanism Ablation")
  1056	    print("="*70)
  1057	    print("\nComparing drift trajectories under targeted ablations.")
  1058	    print("If the model were tautological, these manipulations would look the same.")
  1059	
  1060	    results = {}
  1061	
  1062	    # --- Baseline (all mechanisms on) ---
  1063	    print("\n" + "-"*50)
  1064	    print("BASELINE: Drift with anchor decay + learning + retrieval constraints")
  1065	    print("-"*50)
  1066	    world_baseline = World(n_agents=100, random_seed=seed, use_anchor_retrieval=True)
  1067	    _run_data_drift_protocol(world_baseline)
  1068	    baseline = world_baseline.get_community_profile('data')
  1069	    print(f"  data a(n): {baseline['a(n)']:.2%}, three: {baseline['three']:.2%}")
  1070	    print(f"  data many: {baseline['many']:.2%}, agreement: {baseline['agreement']:.2%}")
  1071	    results['baseline'] = world_baseline
  1072	
  1073	    # --- Ablation 1: Remove anchor-retrieval gating ---
  1074	    print("\n" + "-"*50)
  1075	    print("ABLATION 1: Disable anchor-retrieval constraints")
  1076	    print("-"*50)
  1077	    print("Singulative fallback remains available even as token frequency decays.")
  1078	    world_no_anchor_retrieval = World(
  1079	        n_agents=100,
  1080	        random_seed=seed,
  1081	        use_anchor_retrieval=False
  1082	    )
  1083	    _run_data_drift_protocol(world_no_anchor_retrieval)
  1084	    no_anchor_retrieval = world_no_anchor_retrieval.get_community_profile('data')
  1085	    print(f"  data a(n): {no_anchor_retrieval['a(n)']:.2%}, three: {no_anchor_retrieval['three']:.2%}")
  1086	    print(f"  data many: {no_anchor_retrieval['many']:.2%}, agreement: {no_anchor_retrieval['agreement']:.2%}")
  1087	    print("  Delta vs baseline:")
  1088	    print(f"    a(n): {no_anchor_retrieval['a(n)'] - baseline['a(n)']:+.2%}")
  1089	    print(f"    three: {no_anchor_retrieval['three'] - baseline['three']:+.2%}")
  1090	    results['no_anchor_retrieval'] = world_no_anchor_retrieval
  1091	
  1092	    # --- Ablation 2: Remove the anchor perturbation itself ---
  1093	    print("\n" + "-"*50)
  1094	    print("ABLATION 2: No datum decay")
  1095	    print("-"*50)
  1096	    print("The anchor remains available; drift should attenuate.")
  1097	    world_no_decay = World(n_agents=100, random_seed=seed, use_anchor_retrieval=True)
  1098	    _run_data_drift_protocol(world_no_decay, apply_datum_decay=False)
  1099	    no_decay = world_no_decay.get_community_profile('data')
  1100	    print(f"  data a(n): {no_decay['a(n)']:.2%}, three: {no_decay['three']:.2%}")
  1101	    print(f"  data many: {no_decay['many']:.2%}, agreement: {no_decay['agreement']:.2%}")
  1102	    print("  Delta vs baseline:")
  1103	    print(f"    a(n): {no_decay['a(n)'] - baseline['a(n)']:+.2%}")
  1104	    print(f"    three: {no_decay['three'] - baseline['three']:+.2%}")
  1105	    results['no_decay'] = world_no_decay
  1106	
  1107	    # --- Ablation 3: Remove bidirectional inference ---
  1108	    print("\n" + "-"*50)
  1109	    print("ABLATION 3: Disable learning (freeze lexicons)")
  1110	    print("-"*50)
  1111	    print("Without bidirectional inference, the system should be static.")
  1112	
  1113	    world_frozen = World(n_agents=100, random_seed=seed, use_anchor_retrieval=True)
  1114	
  1115	    # Freeze learning by setting rate to 0
  1116	    for agent in world_frozen.agents:
  1117	        agent.learning_rate = 0.0
  1118	
  1119	    initial_data = world_frozen.get_community_profile('data')
  1120	    _run_data_drift_protocol(world_frozen, turnover_rate=0.0)
  1121	    final_data = world_frozen.get_community_profile('data')
  1122	
  1123	    print(f"  data a(n): start={initial_data['a(n)']:.2%}, end={final_data['a(n)']:.2%}")
  1124	    print(f"  data three: start={initial_data['three']:.2%}, end={final_data['three']:.2%}")
  1125	    print(f"  Delta a(n): {final_data['a(n)'] - initial_data['a(n)']:+.2%}")
  1126	    print(f"  Delta three: {final_data['three'] - initial_data['three']:+.2%}")
  1127	
  1128	    results['frozen'] = world_frozen
  1129	
  1130	    print("\n" + "-"*50)
  1131	    print("ABLATION SUMMARY")
  1132	    print("-"*50)
  1133	    print("The ablations show that specific mechanisms produce specific effects:")
  1134	    print("  - Anchor retrieval constraints amplify tight-lock erosion")
  1135	    print("  - Without anchor decay, erosion attenuates")
  1136	    print("  - Without learning, drift is dramatically reduced")
  1137	    print("These checks make the mechanism dependencies explicit.")
  1138	    print("-"*50)

## Volcano ABM code assumptions

     1	#!/usr/bin/env python3
     2	"""
     3	Volcanic Island (Chapter 7) — semantic mechanism declines, category persists
     4	===========================================================================
     5	This is a didactic mechanism sketch: an intuition pump, not evidence.
     6	
     7	Core idea:
     8	- Agents learn a binary category boundary on a continuous cue x ("shape"/"distributional cue")
     9	- There is also a semantic cue s ∈ {+1,-1} that is informative pre-switch and uninformative post-switch
    10	- We track:
    11	    A) semantic cue effect and mean learned semantic weight w
    12	    B) persistence of the category: boundary similarity to the pre-switch mean, and consensus (sharpness)
    13	"""

    93	    else:
    94	        s = -y_sign
    95	    return x, s, y
    96	
    97	def simulate(n_agents: int = 200,
    98	             T: int = 24000,
    99	             t_switch: int = 12000,
   100	             x_mu_1: float = 0.0,
   101	             x_mu_2: float = 0.15,   # mild ecological shift after switch -> coherent boundary drift

## Current run snapshots (seed=42 unless noted)

Initial state of 'data':
  a(n): 35.00%
  three: 67.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.410)
  a(n): 31.00%
  three: 61.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.168)
  a(n): 25.00%
  three: 61.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.069)
  a(n): 22.00%
  three: 59.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.028)
  a(n): 21.00%
  three: 56.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.012)
  a(n): 16.00%
  three: 55.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.005)
  a(n): 16.00%
  three: 52.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.002)
  a(n): 14.00%
  three: 52.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.001)
  a(n): 13.00%
  three: 49.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.000)
--- Phase 10: datum availability declining ---
  a(n): 12.00%
  three: 43.00%
  many: 100.00%
  agreement: 100.00%
  (datum frequency: 0.000)
RESULT: Tight-before-loose erosion pattern:

BASELINE: Drift with anchor decay + learning + retrieval constraints
  data a(n): 12.00%, three: 43.00%
ABLATION 1: Disable anchor-retrieval constraints
  data a(n): 17.00%, three: 53.00%
  Delta vs baseline:
ABLATION 2: No datum decay
  data a(n): 14.00%, three: 50.00%
  Delta vs baseline:
ABLATION 3: Disable learning (freeze lexicons)
  data a(n): start=39.00%, end=39.00%
  data three: start=68.00%, end=69.00%
  Delta a(n): +0.00%
  Delta three: +1.00%
ABLATION SUMMARY
  - Anchor retrieval constraints amplify tight-lock erosion
  - Without anchor decay, erosion attenuates

'cattle' individuation: mean=0.541, std=0.049
'folks' individuation:  mean=0.830, std=0.099
  'three cattle' accepted by: 0.0% of agents
  'three folks' accepted by: 42.0% of agents
  'many cattle' accepted by: 76.0% of agents
  'many folks' accepted by: 100.0% of agents
RESULT:
  - 'three folks' is genuinely split across speakers

volcano at switch: sem_effect=0.274, w=0.106
volcano final: sem_effect_last10_mean=0.014, w_final=0.083
volcano persistence: boundary_sim_post_mean=0.990, consensus_post_mean=0.834

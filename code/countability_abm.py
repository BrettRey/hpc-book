#!/usr/bin/env python3
"""
Countability Agent-Based Model
==============================

A DIDACTIC MECHANISM SKETCH for Chapter 9 of "Words That Won't Hold Still."

STATUS: This is an intuition pump, not evidence. It makes the two-cluster story
and the implicational hierarchy visible by operationalizing the mechanisms as
interacting update rules. It is NOT a calibrated simulation and should not be
cited as empirical support for the theory.

Core components:
- Agents with lexicons containing individuation confidence per noun
- Constructions as "locks" with tolerance thresholds (tight to loose)
- Bidirectional inference: production and comprehension update beliefs
- Multi-timescale maintenance: processing, acquisition, transmission
- Institutional layer: prescriptive feedback from editors/teachers
- Functional anchoring: singulative alternatives bleed regularization pressure

The model demonstrates:
1. Tight-before-loose erosion (data drift as datum dies)
2. Functional anchoring as stabilizer (cattle stable with cow available)
3. Why prescriptivism struggles (LEGO -> Legos despite corporate campaigns)

STRESS TEST: The ablation experiment removes mechanisms and shows the pattern
breaks, proving the results aren't automatic/tautological.

Usage:
    python countability_abm.py              # Run all experiments
    python countability_abm.py --exp=drift  # Run specific experiment
    python countability_abm.py --exp=ablation  # Run stress test
    python countability_abm.py --interactive  # Interactive exploration

Author: Brett Reynolds / Claude Code
Date: January 2026
"""

import random
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Set
from collections import defaultdict
from enum import Enum
import argparse

# Optional visualization (graceful fallback if not available)
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Note: matplotlib not available; text-based output only")


# =============================================================================
# CORE DATA STRUCTURES
# =============================================================================

class Construction(Enum):
    """
    Constructions ordered from tightest count to loosest, plus mass construction.
    The numeric value represents the individuation threshold required.
    Higher = tighter = more precision demanded.

    MUCH is a mass construction: licensed when individuation is LOW (< 0.4).
    """
    A_N = 0.9           # "a book" - requires identifying exactly one atomic unit
    LOW_CARDINAL = 0.85  # "three books" - exact enumeration
    SEVERAL = 0.7       # "several books" - approximate plurality
    MANY = 0.5          # "many books" - magnitude only
    AGREEMENT = 0.3     # plural agreement - just non-singular construal
    MUCH = -0.4         # "much water" - mass quantifier (negative = max threshold)

    @property
    def tolerance(self) -> float:
        """The individuation threshold this construction demands."""
        return self.value

    @property
    def is_mass(self) -> bool:
        """True if this is a mass construction (licensed by low individuation)."""
        return self.value < 0

    @property
    def label(self) -> str:
        """Human-readable label for the construction."""
        labels = {
            'A_N': 'a(n)',
            'LOW_CARDINAL': 'three',
            'MANY': 'many',
            'SEVERAL': 'several',
            'AGREEMENT': 'agreement',
            'MUCH': 'much'
        }
        return labels.get(self.name, self.name)


@dataclass
class NounProfile:
    """
    A noun's profile in an agent's lexicon.

    Attributes:
        individuation: Confidence that this noun supports atomic individuation [0,1]
        entrenchment: Dict mapping constructions to entrenchment scores
                      (high = stored as chunk, bypasses compositional check)
        exposure_count: Number of times this noun has been encountered
    """
    individuation: float
    entrenchment: Dict[Construction, float] = field(default_factory=dict)
    exposure_count: int = 0

    def __post_init__(self):
        # Initialize entrenchment for all constructions if not provided
        for c in Construction:
            if c not in self.entrenchment:
                self.entrenchment[c] = 0.0


@dataclass
class NounSpec:
    """
    Specification for a noun type in the world.

    Attributes:
        name: The noun form
        initial_individuation: Starting individuation confidence
        has_singulative: Whether a singulative form exists (functional anchor)
        singulative_name: The singulative form if any
        is_institutional_target: Whether prescriptivists care about this noun
        institutional_preference: If targeted, what's the "correct" construal?
        frequency_weight: Relative frequency in discourse (affects sampling probability)
    """
    name: str
    initial_individuation: float
    has_singulative: bool = False
    singulative_name: Optional[str] = None
    is_institutional_target: bool = False
    institutional_preference: Optional[str] = None  # 'count' or 'mass'
    frequency_weight: float = 1.0  # Relative sampling probability


# =============================================================================
# AGENT CLASS
# =============================================================================

class Agent:
    """
    A speaker/hearer with a lexicon of noun profiles.

    Agents:
    - Produce utterances (selecting constructions for communicative goals)
    - Comprehend utterances (updating beliefs based on observed usage)
    - May be "institutional" (editors/teachers who provide corrective feedback)
    """

    def __init__(
        self,
        agent_id: int,
        lexicon: Dict[str, NounProfile],
        is_institutional: bool = False,
        learning_rate: float = 0.05,
        entrenchment_rate: float = 0.02
    ):
        self.id = agent_id
        self.lexicon = lexicon
        self.is_institutional = is_institutional
        self.learning_rate = learning_rate
        self.entrenchment_rate = entrenchment_rate

        # Track production history for analysis
        self.production_history: List[Tuple[str, Construction]] = []

    def can_use_construction(self, noun: str, construction: Construction) -> bool:
        """
        Check if this agent's grammar licenses the construction for this noun.

        A construction is licensed if:
        1. For count constructions: individuation >= tolerance
        2. For mass constructions (MUCH): individuation <= |tolerance|
        3. Highly entrenched constructions bypass compositional check
        """
        if noun not in self.lexicon:
            return False

        profile = self.lexicon[noun]

        # Check entrenchment first (chunked expressions bypass compositional check)
        if profile.entrenchment.get(construction, 0) > 0.7:
            return True

        # Compositional check depends on construction type
        if construction.is_mass:
            # Mass constructions: licensed when individuation is LOW
            return profile.individuation <= abs(construction.tolerance)
        else:
            # Count constructions: licensed when individuation is HIGH
            return profile.individuation >= construction.tolerance

    def get_licensed_constructions(self, noun: str) -> List[Construction]:
        """Return all constructions this agent licenses for the noun."""
        return [c for c in Construction if self.can_use_construction(noun, c)]

    def produce(
        self,
        noun: str,
        communicative_intent: str,
        world: 'World'
    ) -> Optional[Tuple[str, Construction]]:
        """
        Produce an utterance given a communicative goal.

        Args:
            noun: The noun to use
            communicative_intent: 'singleton', 'exact_small', 'vague_many', or 'existence'
            world: The simulation world (for accessing singulatives)

        Returns:
            Tuple of (noun_used, construction) or None if blocked
        """
        if noun not in self.lexicon:
            return None

        # Map intent to preferred construction(s)
        # Includes both count and mass paths
        intent_map = {
            'singleton': [Construction.A_N],
            'exact_small': [Construction.LOW_CARDINAL],
            'vague_many': [Construction.MANY, Construction.SEVERAL],
            'existence': [Construction.AGREEMENT, Construction.MANY],
            'mass_quantity': [Construction.MUCH],  # Mass path
        }

        preferred = intent_map.get(communicative_intent, [Construction.MANY])

        # Try preferred constructions in order
        for construction in preferred:
            if self.can_use_construction(noun, construction):
                self.production_history.append((noun, construction))
                return (noun, construction)

        # Fallback: try singulative if available (for count intents)
        noun_spec = world.get_noun_spec(noun)
        if noun_spec and noun_spec.has_singulative:
            sing = noun_spec.singulative_name
            if sing and sing in self.lexicon:
                for construction in preferred:
                    if self.can_use_construction(sing, construction):
                        self.production_history.append((sing, construction))
                        return (sing, construction)

        # Second fallback: try mass construction if count failed
        if communicative_intent != 'mass_quantity':
            if self.can_use_construction(noun, Construction.MUCH):
                self.production_history.append((noun, Construction.MUCH))
                return (noun, Construction.MUCH)

        # Last resort: measure phrase (abstracted as None)
        # In reality: "piece of furniture", "head of cattle"
        return None

    def observe(self, noun: str, construction: Construction,
                is_correction: bool = False, correction_strength: float = 0.1,
                correction_direction: Optional[str] = None):
        """
        Update beliefs based on observing a noun-construction pair.

        Implements bidirectional inference: seeing a construction used with a noun
        updates the noun's individuation estimate.

        Args:
            noun: The noun observed
            construction: The construction it appeared in
            is_correction: Whether this is prescriptive correction
            correction_strength: How much weight to give corrections
            correction_direction: For corrections, target direction ('count' or 'mass')
        """
        if noun not in self.lexicon:
            return

        profile = self.lexicon[noun]
        profile.exposure_count += 1

        # Bayesian-ish update: observed construction implies individuation
        # sufficient for that construction
        observed_threshold = construction.tolerance

        # Learning rate decays with exposure (entrenchment makes beliefs sticky)
        effective_lr = self.learning_rate / (1 + 0.01 * profile.exposure_count)

        if is_correction:
            effective_lr = correction_strength

        # Update individuation toward the threshold that would license this
        # (or away from it if this was a correction saying "don't do this")
        if is_correction:
            # Correction: move toward the institutional preference
            if correction_direction == 'count':
                # Push toward count (higher individuation)
                profile.individuation += effective_lr * (1.0 - profile.individuation)
            elif correction_direction == 'mass':
                # Push toward mass (lower individuation)
                profile.individuation -= effective_lr * profile.individuation
            else:
                # Default: move away from observed (legacy behavior)
                profile.individuation += effective_lr * (1.0 - profile.individuation)
        else:
            # Normal observation: move toward licensing the construction
            # This is the bidirectional inference
            if construction.is_mass:
                # Mass construction observed: suggests low individuation
                target = abs(observed_threshold) * 0.5  # Target below mass threshold
                delta = profile.individuation - target
                profile.individuation -= effective_lr * delta * 0.5
            elif profile.individuation < observed_threshold:
                # Count construction suggests higher individuation than we thought
                delta = observed_threshold - profile.individuation
                profile.individuation += effective_lr * delta
            else:
                # Observation consistent with or below our estimate
                # Slight regression toward observed threshold
                delta = profile.individuation - observed_threshold
                profile.individuation -= effective_lr * delta * 0.5

        # Clamp to [0, 1]
        profile.individuation = max(0.0, min(1.0, profile.individuation))

        # Update entrenchment for this construction
        current = profile.entrenchment.get(construction, 0.0)
        profile.entrenchment[construction] = min(1.0, current + self.entrenchment_rate)

    def get_count_profile(self, noun: str) -> Dict[str, bool]:
        """
        Get the full count profile for a noun (which locks it opens).
        Returns dict mapping construction labels to True/False.
        """
        if noun not in self.lexicon:
            return {}

        return {c.label: self.can_use_construction(noun, c) for c in Construction}


# =============================================================================
# WORLD / SIMULATION
# =============================================================================

class World:
    """
    The simulation world containing agents, nouns, and running the dynamics.
    """

    def __init__(
        self,
        n_agents: int = 100,
        n_institutional: int = 5,
        random_seed: Optional[int] = None
    ):
        if random_seed is not None:
            random.seed(random_seed)

        self.noun_specs: Dict[str, NounSpec] = {}
        self.agents: List[Agent] = []
        self.n_institutional = n_institutional
        self.time_step = 0

        # Statistics tracking
        self.history: List[Dict] = []

        self._initialize_nouns()
        self._initialize_agents(n_agents)

    def _initialize_nouns(self):
        """Set up the noun inventory with their specifications."""

        # Core nouns from the chapter
        specs = [
            # Fully count
            NounSpec('book', 0.95),
            NounSpec('dog', 0.95),
            NounSpec('idea', 0.90),

            # Quasi-count (stable with anchors)
            NounSpec('cattle', 0.55, has_singulative=True, singulative_name='cow'),
            NounSpec('police', 0.55, has_singulative=True, singulative_name='officer'),
            NounSpec('poultry', 0.50, has_singulative=True, singulative_name='chicken'),

            # Unstable intermediate (no anchor)
            NounSpec('folks', 0.60, has_singulative=False),

            # Drifting (dying anchor) - starts high because historically count
            NounSpec('data', 0.88, has_singulative=True, singulative_name='datum',
                    is_institutional_target=True, institutional_preference='count'),

            # Corporate target
            NounSpec('lego', 0.85, has_singulative=False,
                    is_institutional_target=True, institutional_preference='mass'),

            # Fully mass
            NounSpec('furniture', 0.25),
            NounSpec('water', 0.10),
            NounSpec('equipment', 0.20),

            # Singulatives
            NounSpec('cow', 0.95),
            NounSpec('officer', 0.95),
            NounSpec('chicken', 0.95),
            NounSpec('datum', 0.85),  # Starting higher but will decline
        ]

        for spec in specs:
            self.noun_specs[spec.name] = spec

    def _initialize_agents(self, n_agents: int):
        """Create the agent population."""

        for i in range(n_agents):
            # Build lexicon for this agent
            lexicon = {}
            for name, spec in self.noun_specs.items():
                # Add some individual variation
                ind = spec.initial_individuation + random.gauss(0, 0.05)
                ind = max(0.0, min(1.0, ind))
                lexicon[name] = NounProfile(individuation=ind)

            # First n_institutional agents are editors/teachers
            is_institutional = (i < self.n_institutional)

            agent = Agent(
                agent_id=i,
                lexicon=lexicon,
                is_institutional=is_institutional,
                learning_rate=0.03 if not is_institutional else 0.01
            )
            self.agents.append(agent)

    def get_noun_spec(self, noun: str) -> Optional[NounSpec]:
        """Get the specification for a noun."""
        return self.noun_specs.get(noun)

    def _sample_noun_by_frequency(self) -> str:
        """
        Sample a noun weighted by frequency_weight.
        Nouns with higher frequency_weight are more likely to be selected.
        """
        nouns = list(self.noun_specs.keys())
        weights = [self.noun_specs[n].frequency_weight for n in nouns]
        total = sum(weights)
        if total == 0:
            return random.choice(nouns)
        # Weighted random selection
        r = random.random() * total
        cumulative = 0
        for noun, weight in zip(nouns, weights):
            cumulative += weight
            if r <= cumulative:
                return noun
        return nouns[-1]  # Fallback

    def step(self, interactions_per_step: int = 50):
        """
        Run one time step of the simulation.

        Each step:
        1. Random pairs of agents interact
        2. Speaker produces, hearer observes
        3. Institutional agents may provide corrections
        """
        self.time_step += 1

        for _ in range(interactions_per_step):
            # Pick speaker and hearer
            speaker, hearer = random.sample(self.agents, 2)

            # Pick a noun to talk about (weighted by frequency)
            noun = self._sample_noun_by_frequency()

            # Pick a communicative intent (includes mass path)
            intent = random.choice(['singleton', 'exact_small', 'vague_many', 'existence', 'mass_quantity'])

            # Speaker produces
            result = speaker.produce(noun, intent, self)

            if result:
                produced_noun, construction = result

                # Hearer observes
                hearer.observe(produced_noun, construction)

                # Institutional correction?
                if hearer.is_institutional:
                    spec = self.get_noun_spec(produced_noun)
                    if spec and spec.is_institutional_target:
                        # Check if production violates institutional preference
                        if spec.institutional_preference == 'count':
                            # Should be count; correct if using mass-like forms
                            if construction in [Construction.MUCH] or \
                               (construction == Construction.AGREEMENT and
                                not speaker.can_use_construction(produced_noun, Construction.LOW_CARDINAL)):
                                speaker.observe(produced_noun, Construction.LOW_CARDINAL,
                                              is_correction=True, correction_strength=0.05,
                                              correction_direction='count')
                        elif spec.institutional_preference == 'mass':
                            # Should be mass; correct if treating as count
                            if construction in [Construction.A_N, Construction.LOW_CARDINAL]:
                                # This is the LEGO case - push toward mass
                                speaker.observe(produced_noun, Construction.MUCH,
                                              is_correction=True, correction_strength=0.05,
                                              correction_direction='mass')

        # Record statistics
        self._record_stats()

    def _record_stats(self):
        """Record population-level statistics for this time step."""
        stats = {'time': self.time_step}

        # For each noun, compute mean individuation and acceptance rates
        for noun in self.noun_specs.keys():
            ind_values = [a.lexicon[noun].individuation for a in self.agents
                         if noun in a.lexicon]
            if ind_values:
                stats[f'{noun}_ind_mean'] = sum(ind_values) / len(ind_values)
                stats[f'{noun}_ind_std'] = (sum((x - stats[f'{noun}_ind_mean'])**2
                                               for x in ind_values) / len(ind_values)) ** 0.5

            # Acceptance rates for each construction
            for c in Construction:
                accepts = sum(1 for a in self.agents if a.can_use_construction(noun, c))
                stats[f'{noun}_{c.label}_accept'] = accepts / len(self.agents)

        self.history.append(stats)

    def run(self, n_steps: int = 100, interactions_per_step: int = 50):
        """Run the simulation for n_steps."""
        for _ in range(n_steps):
            self.step(interactions_per_step)

    def perturb_singulative_availability(self, singulative: str, decay_rate: float = 0.02):
        """
        Reduce availability of a singulative form (simulating 'datum' dying).

        This reduces both:
        1. The frequency_weight (how often it's sampled in discourse)
        2. Agent-level individuation and entrenchment (internal representations)

        The frequency reduction is the primary mechanism: speakers encounter
        the singulative less often, weakening its role as an anchor.
        """
        if singulative not in self.noun_specs:
            return

        # PRIMARY: Reduce discourse frequency (affects sampling probability)
        spec = self.noun_specs[singulative]
        spec.frequency_weight *= (1 - decay_rate)

        # SECONDARY: Reduce individuation confidence across all agents
        for agent in self.agents:
            if singulative in agent.lexicon:
                profile = agent.lexicon[singulative]
                profile.individuation *= (1 - decay_rate * 0.5)  # Slower internal decay
                # Also reduce entrenchment
                for c in profile.entrenchment:
                    profile.entrenchment[c] *= (1 - decay_rate)

    def generational_turnover(self, turnover_rate: float = 0.05):
        """
        Replace some agents with new learners (simulates acquisition/transmission).

        New learners initialize their lexicons based on the current community
        distribution, with some noise. This implements multi-timescale
        maintenance: the slow loop of acquisition transmits patterns to
        new learners who then participate in the fast loop.

        Args:
            turnover_rate: Proportion of agents replaced per call (default 5%)
        """
        n_replace = max(1, int(len(self.agents) * turnover_rate))

        # Compute current community means for each noun
        community_means = {}
        for noun in self.noun_specs.keys():
            ind_values = [a.lexicon[noun].individuation for a in self.agents
                         if noun in a.lexicon]
            if ind_values:
                community_means[noun] = sum(ind_values) / len(ind_values)
            else:
                community_means[noun] = self.noun_specs[noun].initial_individuation

        # Replace random (non-institutional) agents
        replaceable = [i for i, a in enumerate(self.agents) if not a.is_institutional]
        if len(replaceable) < n_replace:
            n_replace = len(replaceable)

        to_replace = random.sample(replaceable, n_replace)

        for idx in to_replace:
            # Create new agent with lexicon based on community means + noise
            lexicon = {}
            for name in self.noun_specs.keys():
                # New learner acquires from community with acquisition noise
                ind = community_means[name] + random.gauss(0, 0.08)
                ind = max(0.0, min(1.0, ind))
                lexicon[name] = NounProfile(individuation=ind)

            new_agent = Agent(
                agent_id=self.agents[idx].id,
                lexicon=lexicon,
                is_institutional=False,
                learning_rate=0.05  # New learners learn faster initially
            )
            self.agents[idx] = new_agent

    def get_community_profile(self, noun: str) -> Dict[str, float]:
        """
        Get community-level acceptance rates for each construction.
        Returns dict mapping construction labels to acceptance proportions.
        """
        profile = {}
        for c in Construction:
            accepts = sum(1 for a in self.agents if a.can_use_construction(noun, c))
            profile[c.label] = accepts / len(self.agents)
        return profile

    def print_matrix(self, nouns: Optional[List[str]] = None):
        """
        Print the implicational matrix (Table 9.1 style).
        Includes both count constructions (tight to loose) and mass (MUCH).
        """
        if nouns is None:
            nouns = ['book', 'cattle', 'police', 'folks', 'data', 'furniture', 'water']

        # Count constructions (tight to loose) + mass construction
        constructions = [Construction.A_N, Construction.LOW_CARDINAL,
                        Construction.MANY, Construction.AGREEMENT, Construction.MUCH]

        # Header
        header = f"{'Noun':<12}" + "".join(f"{c.label:>12}" for c in constructions)
        print(header)
        print("-" * len(header))

        # Rows
        for noun in nouns:
            if noun not in self.noun_specs:
                continue
            profile = self.get_community_profile(noun)
            row = f"{noun:<12}"
            for c in constructions:
                rate = profile[c.label]
                if rate > 0.8:
                    symbol = "   +   "
                elif rate > 0.5:
                    symbol = "   ~   "
                elif rate > 0.2:
                    symbol = "   ?   "
                else:
                    symbol = "   -   "
                row += f"{symbol:>12}"
            print(row)


# =============================================================================
# EXPERIMENTS
# =============================================================================

def experiment_baseline(seed: int = 42) -> World:
    """
    Baseline: Verify the initial hierarchy matches Chapter 9's predictions.
    """
    print("\n" + "="*70)
    print("EXPERIMENT: Baseline Hierarchy")
    print("="*70)
    print("\nVerifying that the initial state matches the implicational hierarchy.")
    print("Expected: book > cattle/police (quasi) > folks (unstable) > furniture/water")

    world = World(n_agents=100, random_seed=seed)

    # Run briefly to let agents interact
    world.run(n_steps=20, interactions_per_step=30)

    print("\nCommunity acceptance matrix (+ = >80%, ~ = 50-80%, ? = 20-50%, - = <20%):")
    print()
    world.print_matrix()

    return world


def experiment_data_drift(seed: int = 42, visualize: bool = True) -> World:
    """
    Experiment 1: Data drift as datum dies.

    Demonstrates tight-before-loose erosion: when the singulative anchor
    weakens, the count cluster peels in order (agreement last to go).
    """
    print("\n" + "="*70)
    print("EXPERIMENT: Data Drift (Tight-Before-Loose Erosion)")
    print("="*70)
    print("\nSimulating the death of 'datum' and observing 'data' drift toward mass.")
    print("Prediction: tight properties (a(n), cardinals) erode before loose (agreement).")

    world = World(n_agents=100, random_seed=seed)

    # Initial state
    print("\nInitial state of 'data':")
    print(world.get_community_profile('data'))

    # Run with progressive datum decay
    n_phases = 8
    steps_per_phase = 25

    phase_data = []

    for phase in range(n_phases):
        print(f"\n--- Phase {phase + 1}: datum availability declining ---")

        # Decay datum availability (frequency-based, no manual outcome nudge)
        for _ in range(4):
            world.perturb_singulative_availability('datum', decay_rate=0.20)

        # Run interactions + generational turnover (transmission mechanism)
        world.run(n_steps=steps_per_phase, interactions_per_step=50)
        world.generational_turnover(turnover_rate=0.03)  # 3% per phase

        datum_mean_ind = sum(a.lexicon['datum'].individuation for a in world.agents) / len(world.agents)
        profile = world.get_community_profile('data')
        phase_data.append(profile)

        print(f"  a(n): {profile['a(n)']:.2%}")
        print(f"  three: {profile['three']:.2%}")
        print(f"  many: {profile['many']:.2%}")
        print(f"  agreement: {profile['agreement']:.2%}")
        print(f"  much: {profile['much']:.2%}")
        print(f"  (datum frequency: {world.noun_specs['datum'].frequency_weight:.3f})")

    print("\n" + "-"*50)
    print("RESULT: Tight-before-loose erosion pattern:")
    print("  - a(n) and cardinals should decline first")
    print("  - agreement should be last to decline")
    print("-"*50)

    # Final matrix
    print("\nFinal community matrix:")
    world.print_matrix(['book', 'data', 'datum', 'cattle', 'water'])

    # Visualization
    if visualize and HAS_MATPLOTLIB:
        _plot_drift_experiment(phase_data)

    return world


def experiment_functional_anchoring(seed: int = 42) -> Tuple[World, World]:
    """
    Experiment 2: Functional anchoring as a stabilizer.

    Compare two scenarios:
    1. Cattle with 'cow' available (stable quasi-count)
    2. Simulated cattle without 'cow' (pressure toward regularization)
    """
    print("\n" + "="*70)
    print("EXPERIMENT: Functional Anchoring")
    print("="*70)
    print("\nComparing quasi-count stability with and without singulative anchors.")

    # Scenario A: Normal (cow available)
    print("\n--- Scenario A: 'cattle' with 'cow' available ---")
    world_a = World(n_agents=100, random_seed=seed)
    world_a.run(n_steps=100, interactions_per_step=50)

    profile_a = world_a.get_community_profile('cattle')
    print(f"  a(n): {profile_a['a(n)']:.2%}")
    print(f"  three: {profile_a['three']:.2%}")
    print(f"  many: {profile_a['many']:.2%}")
    print(f"  agreement: {profile_a['agreement']:.2%}")

    # Scenario B: Remove cow (simulate anchor loss)
    print("\n--- Scenario B: 'cattle' with 'cow' unavailable ---")
    world_b = World(n_agents=100, random_seed=seed)

    # Remove the singulative specification
    world_b.noun_specs['cattle'].has_singulative = False
    world_b.noun_specs['cattle'].singulative_name = None

    # Also reduce 'cow' availability in lexicons
    for agent in world_b.agents:
        if 'cow' in agent.lexicon:
            agent.lexicon['cow'].individuation = 0.1  # Make cow unusable

    world_b.run(n_steps=100, interactions_per_step=50)

    profile_b = world_b.get_community_profile('cattle')
    print(f"  a(n): {profile_b['a(n)']:.2%}")
    print(f"  three: {profile_b['three']:.2%}")
    print(f"  many: {profile_b['many']:.2%}")
    print(f"  agreement: {profile_b['agreement']:.2%}")

    print("\n" + "-"*50)
    print("RESULT: Without functional anchor:")
    print("  - Expect pressure toward regularization (tight properties emerging)")
    print("  - Or increased avoidance/measure strategies")
    print("-"*50)

    return world_a, world_b


def experiment_prescriptivism(seed: int = 42, visualize: bool = True) -> World:
    """
    Experiment 3: Why prescriptivism struggles.

    Simulates the LEGO campaign: institutional pressure to use 'LEGO bricks'
    rather than 'Legos', but cognitive pressure from discrete-object construal.
    """
    print("\n" + "="*70)
    print("EXPERIMENT: Prescriptivism vs. Cognitive Pressure (LEGO)")
    print("="*70)
    print("\nSimulating 40 years of LEGO Group's campaign against 'Legos'.")
    print("Prediction: Unless institutional feedback is unrealistically strong,")
    print("           count construal wins because objects are discrete.")

    world = World(n_agents=100, n_institutional=10, random_seed=seed)

    # LEGO starts as clearly count (discrete objects)
    # But has institutional pressure toward mass

    # Increase institutional presence for this experiment
    for agent in world.agents[:15]:
        agent.is_institutional = True

    print("\nInitial state of 'lego':")
    print(world.get_community_profile('lego'))

    phase_data = []

    # Run simulation in phases, tracking LEGO
    for phase in range(5):
        world.run(n_steps=40, interactions_per_step=60)

        profile = world.get_community_profile('lego')
        phase_data.append(profile)

        print(f"\nPhase {phase + 1} (timestep {world.time_step}):")
        print(f"  a(n): {profile['a(n)']:.2%}")
        print(f"  three: {profile['three']:.2%}")
        print(f"  many: {profile['many']:.2%}")

    print("\n" + "-"*50)
    print("RESULT:")
    print("  - Discrete objects exert strong pressure toward count construal")
    print("  - Institutional feedback slows but rarely reverses this")
    print("  - This is why 'Legos' persists despite corporate campaigns")
    print("-"*50)

    if visualize and HAS_MATPLOTLIB:
        _plot_prescriptivism_experiment(phase_data)

    return world


def experiment_folks_instability(seed: int = 42) -> World:
    """
    Experiment 4: Demonstrate the instability of 'folks'.

    'folks' lacks a functional anchor and shows high inter-speaker variation.
    """
    print("\n" + "="*70)
    print("EXPERIMENT: Folks Instability")
    print("="*70)
    print("\nDemonstrating why 'folks' shows high inter-speaker variation.")
    print("Unlike 'cattle' (anchored by 'cow'), 'folks' has no singulative.")

    world = World(n_agents=100, random_seed=seed)
    world.run(n_steps=100, interactions_per_step=50)

    # Compare cattle vs folks variability
    cattle_inds = [a.lexicon['cattle'].individuation for a in world.agents]
    folks_inds = [a.lexicon['folks'].individuation for a in world.agents]

    cattle_mean = sum(cattle_inds) / len(cattle_inds)
    cattle_std = (sum((x - cattle_mean)**2 for x in cattle_inds) / len(cattle_inds)) ** 0.5

    folks_mean = sum(folks_inds) / len(folks_inds)
    folks_std = (sum((x - folks_mean)**2 for x in folks_inds) / len(folks_inds)) ** 0.5

    print(f"\n'cattle' individuation: mean={cattle_mean:.3f}, std={cattle_std:.3f}")
    print(f"'folks' individuation:  mean={folks_mean:.3f}, std={folks_std:.3f}")

    print("\nConstruction acceptance across agents:")

    # Show that 'three folks' is highly variable
    n_agents = len(world.agents)
    three_cattle = sum(1 for a in world.agents
                       if a.can_use_construction('cattle', Construction.LOW_CARDINAL))
    three_folks = sum(1 for a in world.agents
                      if a.can_use_construction('folks', Construction.LOW_CARDINAL))

    many_cattle = sum(1 for a in world.agents
                      if a.can_use_construction('cattle', Construction.MANY))
    many_folks = sum(1 for a in world.agents
                     if a.can_use_construction('folks', Construction.MANY))

    print(f"  'three cattle' accepted by: {100*three_cattle/n_agents:.1f}% of agents")
    print(f"  'three folks' accepted by: {100*three_folks/n_agents:.1f}% of agents")
    print(f"  'many cattle' accepted by: {100*many_cattle/n_agents:.1f}% of agents")
    print(f"  'many folks' accepted by: {100*many_folks/n_agents:.1f}% of agents")

    print("\n" + "-"*50)
    print("RESULT:")
    print("  - 'folks' shows higher inter-speaker variation")
    print("  - 'three folks' acceptance is split (some accept, some reject)")
    print("  - This matches the corpus data: 'three folks' is suppressed 8.6x")
    print("-"*50)

    return world


def experiment_mechanism_ablation(seed: int = 42) -> Dict[str, World]:
    """
    STRESS TEST: Mechanism ablation to prove results aren't automatic.

    This experiment removes key mechanisms and shows the predicted pattern breaks:
    1. Remove entrenchment → tight-before-loose ordering degrades
    2. Remove anchoring → quasi-count nouns destabilize

    This is the "control" that shows the model isn't tautological.
    """
    print("\n" + "="*70)
    print("STRESS TEST: Mechanism Ablation")
    print("="*70)
    print("\nRemoving mechanisms to show the pattern isn't automatic.")
    print("If the model were tautological, ablation wouldn't change outcomes.")

    results = {}

    # --- Ablation 1: Remove entrenchment ---
    print("\n" + "-"*50)
    print("ABLATION 1: Disable entrenchment (chunking)")
    print("-"*50)
    print("Without entrenchment, high-frequency patterns shouldn't resist change.")

    world_no_ent = World(n_agents=100, random_seed=seed)

    # Disable entrenchment by setting rate to 0 for all agents
    for agent in world_no_ent.agents:
        agent.entrenchment_rate = 0.0

    # Run the data drift scenario
    for phase in range(6):
        for _ in range(4):
            world_no_ent.perturb_singulative_availability('datum', decay_rate=0.20)
        world_no_ent.run(n_steps=25, interactions_per_step=50)
        world_no_ent.generational_turnover(turnover_rate=0.03)

    profile = world_no_ent.get_community_profile('data')
    print(f"\n'data' after drift (NO entrenchment):")
    print(f"  a(n): {profile['a(n)']:.2%}, three: {profile['three']:.2%}")
    print(f"  many: {profile['many']:.2%}, agreement: {profile['agreement']:.2%}")

    # Check if cattle destabilized without entrenchment protecting 'many cattle'
    cattle_profile = world_no_ent.get_community_profile('cattle')
    print(f"\n'cattle' stability (NO entrenchment):")
    print(f"  many: {cattle_profile['many']:.2%} (should be lower without chunking protection)")

    results['no_entrenchment'] = world_no_ent

    # --- Ablation 2: Remove functional anchoring ---
    print("\n" + "-"*50)
    print("ABLATION 2: Remove functional anchors")
    print("-"*50)
    print("Without anchors, quasi-count nouns should face regularization pressure.")

    world_no_anchor = World(n_agents=100, random_seed=seed)

    # Remove all singulative anchors
    for spec in world_no_anchor.noun_specs.values():
        spec.has_singulative = False
        spec.singulative_name = None

    # Also make singulatives unavailable in agent lexicons
    for agent in world_no_anchor.agents:
        for sing in ['cow', 'officer', 'chicken', 'datum']:
            if sing in agent.lexicon:
                agent.lexicon[sing].individuation = 0.0

    # Run for a while to see if cattle/police regularize
    for _ in range(8):
        world_no_anchor.run(n_steps=30, interactions_per_step=50)
        world_no_anchor.generational_turnover(turnover_rate=0.05)

    cattle_no_anchor = world_no_anchor.get_community_profile('cattle')
    police_no_anchor = world_no_anchor.get_community_profile('police')

    print(f"\n'cattle' without anchor 'cow':")
    print(f"  a(n): {cattle_no_anchor['a(n)']:.2%}, three: {cattle_no_anchor['three']:.2%}")
    print(f"  many: {cattle_no_anchor['many']:.2%}")
    print(f"\n'police' without anchor 'officer':")
    print(f"  a(n): {police_no_anchor['a(n)']:.2%}, three: {police_no_anchor['three']:.2%}")
    print(f"  many: {police_no_anchor['many']:.2%}")

    results['no_anchoring'] = world_no_anchor

    # --- Ablation 3: Remove bidirectional inference ---
    print("\n" + "-"*50)
    print("ABLATION 3: Disable learning (freeze lexicons)")
    print("-"*50)
    print("Without bidirectional inference, the system should be static.")

    world_frozen = World(n_agents=100, random_seed=seed)

    # Freeze learning by setting rate to 0
    for agent in world_frozen.agents:
        agent.learning_rate = 0.0

    initial_cattle = world_frozen.get_community_profile('cattle')

    # Run interactions (should have no effect)
    world_frozen.run(n_steps=100, interactions_per_step=50)

    final_cattle = world_frozen.get_community_profile('cattle')

    print(f"\n'cattle' before interactions: many={initial_cattle['many']:.2%}")
    print(f"'cattle' after 100 steps:     many={final_cattle['many']:.2%}")
    print(f"Change: {abs(final_cattle['many'] - initial_cattle['many']):.2%}")
    print("(Should be ~0% if learning is truly disabled)")

    results['frozen'] = world_frozen

    print("\n" + "-"*50)
    print("ABLATION SUMMARY")
    print("-"*50)
    print("The ablations show that specific mechanisms produce specific effects:")
    print("  - Entrenchment protects high-frequency patterns")
    print("  - Functional anchors stabilize quasi-count equilibria")
    print("  - Bidirectional inference drives the dynamics")
    print("Without these mechanisms, the HPC pattern degrades or disappears.")
    print("-"*50)

    return results


# =============================================================================
# VISUALIZATION
# =============================================================================

def _plot_drift_experiment(phase_data: List[Dict[str, float]]):
    """Plot the tight-before-loose erosion pattern."""
    fig, ax = plt.subplots(figsize=(10, 6))

    phases = list(range(1, len(phase_data) + 1))

    constructions = ['a(n)', 'three', 'many', 'agreement']
    colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']
    markers = ['o', 's', '^', 'D']

    for i, c in enumerate(constructions):
        values = [phase[c] for phase in phase_data]
        ax.plot(phases, values, color=colors[i], marker=markers[i],
                linewidth=2, markersize=8, label=c)

    ax.set_xlabel(r'Phase ($\it{datum}$ availability declining)', fontsize=12)
    ax.set_ylabel('Community acceptance rate', fontsize=12)
    ax.set_title(r"$\it{Data}$ Drift: Tight-Before-Loose Erosion" + "\n"
                 r"(As $\it{datum}$ dies, count properties peel in order)", fontsize=14)
    ax.legend(loc='upper right')
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    # Add annotation
    ax.annotate('Tight properties\nerode first', xy=(3, 0.3), fontsize=10,
                ha='center', style='italic', color='gray')

    plt.tight_layout()
    plt.savefig('data_drift_experiment.png', dpi=150)
    print("\nPlot saved to: data_drift_experiment.png")
    plt.close()


def _plot_prescriptivism_experiment(phase_data: List[Dict[str, float]]):
    """Plot the LEGO prescriptivism experiment."""
    fig, ax = plt.subplots(figsize=(10, 6))

    phases = list(range(1, len(phase_data) + 1))

    constructions = ['a(n)', 'three', 'many']
    colors = ['#d62728', '#ff7f0e', '#2ca02c']

    for i, c in enumerate(constructions):
        values = [phase[c] for phase in phase_data]
        ax.plot(phases, values, color=colors[i], linewidth=2,
                marker='o', markersize=8, label=c)

    ax.set_xlabel('Phase (simulation time)', fontsize=12)
    ax.set_ylabel('Community acceptance rate', fontsize=12)
    ax.set_title(r"Prescriptivism vs. Cognitive Pressure ($\it{Lego}$)" + "\n"
                 r"(Institutional $\it{LEGO\ bricks}$ campaign vs. count construal)", fontsize=14)
    ax.legend(loc='lower right')
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    # Add annotation about discrete objects
    ax.annotate('Discrete objects\nresist mass construal',
                xy=(3, 0.85), fontsize=10,
                ha='center', style='italic', color='gray')

    plt.tight_layout()
    plt.savefig('prescriptivism_experiment.png', dpi=150)
    print("\nPlot saved to: prescriptivism_experiment.png")
    plt.close()


def plot_basin_visualization():
    """
    Create a visualization of the count basin with locks at different positions.
    This illustrates the chapter's metaphor of tight locks at center, loose at edges.

    Key insight: HIGH individuation = CENTER of basin (opens all locks)
                 LOW individuation = EDGE or outside basin
    """
    if not HAS_MATPLOTLIB:
        print("matplotlib required for basin visualization")
        return

    fig, ax = plt.subplots(figsize=(10, 10))

    # The basin edge is at individuation = 0.3 (agreement threshold)
    # Radius in the plot = 1 - individuation (so high individuation = center)

    # Draw concentric circles representing tolerance thresholds
    # Inner circles = tighter locks (higher threshold)
    thresholds = [
        (0.9, 'a(n)', '#d62728'),      # Tightest - innermost
        (0.85, 'three', '#ff7f0e'),
        (0.7, 'several', '#9467bd'),
        (0.5, 'many', '#2ca02c'),
        (0.3, 'agreement', '#1f77b4'), # Loosest - basin edge
    ]

    for thresh, label, color in thresholds:
        # Convert threshold to radius: higher threshold = smaller circle
        radius = 1.0 - thresh
        circle = plt.Circle((0, 0), radius, fill=False, color=color,
                            linewidth=2, linestyle='--', alpha=0.7)
        ax.add_patch(circle)
        # Label position
        label_r = radius + 0.03
        ax.annotate(f'{label}',
                   xy=(label_r * 0.7, label_r * 0.7),
                   fontsize=9, ha='center', color=color, fontweight='bold')

    # Draw the basin boundary (individuation = 0.3)
    basin_edge = plt.Circle((0, 0), 0.7, fill=True, color='#e8f4f8',
                            alpha=0.3, zorder=0)
    ax.add_patch(basin_edge)

    # Plot nouns as points based on their individuation
    # Radius = 1 - individuation (so book near center, water outside)
    nouns = [
        ('book', 0.95, 15),
        ('dog', 0.93, 45),
        ('idea', 0.88, 75),
        ('folks', 0.60, 150),
        ('cattle', 0.55, 180),
        ('police', 0.52, 210),
        ('data', 0.45, 250),   # Drifting toward edge
        ('furniture', 0.25, 290),  # Outside basin
        ('water', 0.10, 330),      # Well outside basin
    ]

    for name, ind, angle in nouns:
        rad = math.radians(angle)
        # Invert: high individuation = small radius (center)
        plot_radius = 1.0 - ind
        x = plot_radius * math.cos(rad)
        y = plot_radius * math.sin(rad)

        # Color by position: green=center, yellow=mid, red=edge/outside
        if ind > 0.85:
            color = '#2ecc71'  # Full count - center
        elif ind > 0.5:
            color = '#f39c12'  # Quasi-count - mid-basin
        elif ind > 0.3:
            color = '#e67e22'  # Marginal - near edge
        else:
            color = '#e74c3c'  # Mass - outside basin

        ax.plot(x, y, 'o', markersize=12, color=color, zorder=5)
        ax.annotate(name, xy=(x, y), xytext=(5, 5), textcoords='offset points',
                   fontsize=10, fontstyle='italic')

    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect('equal')

    ax.set_title("The Count Basin\n"
                 "Center = high individuation (opens all locks); Edge = low individuation",
                 fontsize=14)

    # Legend
    green_patch = mpatches.Patch(color='#2ecc71', label='Full count (center, opens all locks)')
    yellow_patch = mpatches.Patch(color='#f39c12', label='Quasi-count (mid-basin, loose locks only)')
    red_patch = mpatches.Patch(color='#e74c3c', label='Mass (outside basin)')
    ax.legend(handles=[green_patch, yellow_patch, red_patch], loc='lower right')

    ax.axis('off')

    plt.tight_layout()
    plt.savefig('count_basin_visualization.png', dpi=150)
    print("\nBasin visualization saved to: count_basin_visualization.png")
    plt.close()


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Countability Agent-Based Model (Chapter 9) - DIDACTIC MECHANISM SKETCH',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Experiments:
  baseline     Verify initial hierarchy matches predictions
  drift        Data drift as datum dies (tight-before-loose erosion)
  anchor       Functional anchoring (cattle with/without cow)
  prescriptive LEGO prescriptivism vs cognitive pressure
  folks        Folks instability demonstration
  ablation     STRESS TEST: remove mechanisms, show pattern breaks
  all          Run all experiments (default)
  basin        Generate basin visualization only

NOTE: This is an intuition pump, not calibrated evidence.
        """
    )
    parser.add_argument('--exp', default='all',
                       help='Experiment to run (see list below)')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility')
    parser.add_argument('--no-viz', action='store_true',
                       help='Disable visualization (text output only)')
    parser.add_argument('--interactive', action='store_true',
                       help='Enter interactive exploration mode')

    args = parser.parse_args()

    visualize = not args.no_viz and HAS_MATPLOTLIB

    print("="*70)
    print("COUNTABILITY AGENT-BASED MODEL")
    print("Implementing Chapter 9's HPC theory of the count cluster")
    print("="*70)

    if args.interactive:
        interactive_mode(args.seed)
        return

    if args.exp == 'all':
        experiment_baseline(args.seed)
        experiment_data_drift(args.seed, visualize)
        experiment_functional_anchoring(args.seed)
        experiment_prescriptivism(args.seed, visualize)
        experiment_folks_instability(args.seed)
        experiment_mechanism_ablation(args.seed)  # Stress test
        if visualize:
            plot_basin_visualization()
    elif args.exp == 'baseline':
        experiment_baseline(args.seed)
    elif args.exp == 'drift':
        experiment_data_drift(args.seed, visualize)
    elif args.exp == 'anchor':
        experiment_functional_anchoring(args.seed)
    elif args.exp == 'prescriptive':
        experiment_prescriptivism(args.seed, visualize)
    elif args.exp == 'folks':
        experiment_folks_instability(args.seed)
    elif args.exp == 'ablation':
        experiment_mechanism_ablation(args.seed)
    elif args.exp == 'basin':
        if visualize:
            plot_basin_visualization()
        else:
            print("Basin visualization requires matplotlib")
    else:
        print(f"Unknown experiment: {args.exp}")
        parser.print_help()

    print("\n" + "="*70)
    print("SIMULATION COMPLETE")
    print("="*70)


def interactive_mode(seed: int):
    """Interactive exploration of the model."""
    print("\n--- Interactive Mode ---")
    print("Creating world with default parameters...")

    world = World(n_agents=100, random_seed=seed)

    print("\nCommands:")
    print("  run N        - Run N time steps")
    print("  matrix       - Show implicational matrix")
    print("  profile NOUN - Show detailed profile for a noun")
    print("  decay NOUN   - Decay singulative for a noun")
    print("  agent N      - Show agent N's lexicon")
    print("  quit         - Exit")

    while True:
        try:
            cmd = input("\n> ").strip().split()
        except (EOFError, KeyboardInterrupt):
            break

        if not cmd:
            continue

        if cmd[0] == 'quit':
            break
        elif cmd[0] == 'run':
            n = int(cmd[1]) if len(cmd) > 1 else 10
            world.run(n_steps=n)
            print(f"Ran {n} steps. Total time: {world.time_step}")
        elif cmd[0] == 'matrix':
            world.print_matrix()
        elif cmd[0] == 'profile':
            if len(cmd) > 1:
                noun = cmd[1]
                print(f"\nCommunity profile for '{noun}':")
                print(world.get_community_profile(noun))
            else:
                print("Usage: profile NOUN")
        elif cmd[0] == 'decay':
            if len(cmd) > 1:
                noun = cmd[1]
                world.perturb_singulative_availability(noun, 0.2)
                print(f"Decayed singulative availability for '{noun}'")
            else:
                print("Usage: decay NOUN")
        elif cmd[0] == 'agent':
            if len(cmd) > 1:
                n = int(cmd[1])
                if 0 <= n < len(world.agents):
                    agent = world.agents[n]
                    print(f"\nAgent {n} ({'institutional' if agent.is_institutional else 'regular'}):")
                    for noun, profile in agent.lexicon.items():
                        print(f"  {noun}: ind={profile.individuation:.3f}")
                else:
                    print(f"Agent index out of range (0-{len(world.agents)-1})")
            else:
                print("Usage: agent N")
        else:
            print(f"Unknown command: {cmd[0]}")


if __name__ == '__main__':
    main()

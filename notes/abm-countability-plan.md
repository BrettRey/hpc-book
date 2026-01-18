# Agent-Based Modeling Notes for Chapter 9 (Countability)

**Date:** 2026-01-17  
**Status:** Planning — to be implemented

---

## Why Countability is the Best ABM Target

1. **Discretized moving parts**: Stabilizers (bidirectional inference, acquisition/overgeneralization, entrenchment/chunking, institutional norms, functional anchoring) already located on different timescales → operationalizable as interacting update rules.

2. **Easy outcome measures**: Count cluster as vector of "lock outcomes" (a(n), low numerals, many, agreement) → community-level implicational profile over time → maps to triangular matrix already in chapter.

3. **Natural perturbations**: Remove singulative anchor (datum dying), introduce prescriptive pressure (LEGO, data is), alter frequency/genre exposure (folks) → show system settling/sliding between equilibria.

4. **Pedagogical arc**: Shows full HPC story: covariance → maintenance → stability vs drift → intermediate equilibria (quasi-count) → directional failure modes (tight-before-loose).

---

## Minimal ABM Ingredients

### Agents
- Speakers/hearers with lexicons for small noun set (book, cattle, police, furniture, data, folks)
- Latent variable per noun per agent: "individuation confidence" (continuous) + optional "constructional entrenchment" score

### Constructions as Locks
- a(n), three, many, agreement
- Each has tolerance threshold on individuation parameter (tightest to loosest)

### Production
- Agent with communicative intention (singleton vs small exact vs vague many) chooses least-cost licensed frame
- If no frame licensed → measure/unit strategy (piece of furniture, data point) or alternative lexeme (cow/officer as anchors)

### Comprehension/Learning
- Update individuation confidence based on observation
- Bayesian updating or simple reinforcement rule

### Institutional Layer (optional)
- Minority of "editors/teachers" penalize outputs (data are vs data is)
- Alter perceived costs, not meaning directly

---

## Demonstrations

1. **Tight-before-loose erosion**: Reduce exposure to datum → agreement shifts first ("this data is"); exact numerals remain rare

2. **Functional anchoring**: cattle/police stable if cow/officer available; remove anchor → regularization pressure

3. **Why prescriptivism struggles**: Cognitively cheap count packaging (LEGO bricks → *three Legos*) wins unless institutional feedback unrealistically strong

---

## Insertion Point

- **Best fit**: §9 "Multi-timescale maintenance" — ABM as explicit integration of fast loop (processing), slow loop (acquisition), community loop (norms/transmission)
- **Alternative**: "Diachronic signatures" — generative sanity check showing stabilizers sufficient for self-completion (pea) and drift (data)

---

## Why Other Chapters are Harder

- **Ch 10 (Definiteness)**: Needs discourse models, hearer-modeling, constructional inventories for weak definites — heavier minimum viable model
- **Ch 11 (Lexical categories)**: Good for Kirby-style iterated learning, but abstract or balloons into grammar induction
- **Ch 13 (Zipper)**: Better for *talking about* ABM methodologically; concrete exemplar points back to Countability

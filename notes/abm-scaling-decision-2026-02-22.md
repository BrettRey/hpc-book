# ABM scaling decision (2026-02-22)

## Question
Should Chapter 7 and Chapter 9 ABMs be scaled from hundreds of agents to hundreds of thousands (e.g., 500,000)?

## Benchmarks run in this repo

### Volcano ABM (`code/volcano_abm.py`)
- `n_agents=200`, `T=24000`: ~0.61s
- `n_agents=2000`, `T=24000`: ~3.01s
- `n_agents=10000`, `T=24000`: ~12.66s
- `n_agents=100000`, `T=24000`: ~119.31s

Key dynamic: this model updates one random learner per interaction. With fixed `T`, expected updates per agent are `T/N`.

- At `N=200`, `T=24000`: ~120 updates/agent
- At `N=500000`, `T=24000`: ~0.048 updates/agent

So pushing `N` up by orders of magnitude without increasing `T` mostly under-trains agents. To preserve comparability at `N=500000`, `T` would need to be around `60,000,000` to keep ~120 updates/agent.

### Countability ABM (`code/countability_abm.py`)
Full drift protocol benchmark with interaction budget scaled as `interactions_per_step = 0.6 * N`:
- `N=100`: ~1.20s
- `N=1000`: ~12.16s
- `N=5000`: ~75.45s

Additional memory check:
- `N=20000` (short run): ~8.88s, peak RSS around ~226 MiB.

Extrapolation: `N=500000` with scaled interactions is feasible only at high runtime/memory cost and is not a good default for quick chapter iteration.

## Decision
Use **moderate N + multi-seed summaries**, not extreme N.

- Volcano: low-thousands is fine for stronger smoothing, with seed sweeps for uncertainty.
- Countability: `N=1000–5000` with interaction budget scaled to N, plus seed sensitivity (`--exp=sensitivity`).

## Why this is methodologically better
- Larger N only reduces Monte Carlo noise.
- Main uncertainty in these ABMs is structural/modeling assumptions, not sampling error alone.
- Multi-seed summaries directly address trajectory fragility and avoid over-reading single seeded runs.

## Implementation changes made
- Added runtime controls so interaction budget scales with N by default.
- Added/extended sensitivity workflows and manifests to report distributional behavior across seeds.
- Added chapter prose clarifying why we avoid extreme N with fixed interaction horizon.

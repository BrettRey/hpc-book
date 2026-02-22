## Strengths

- The epistemic-status discipline is unusually explicit and consistent. Both models label themselves as didactic mechanism sketches, not empirical tests (`code/volcano_abm.py:5`, `code/countability_abm.py:8`), and the chapters repeat that caveat in plain prose (`chapters/chapter07.tex:178`, `chapters/chapter09.tex:285`).
- The prose for non-modelers is strong. The Chapter 7 “controlled cartoon” framing and two-parameter explanation (`w` and `\theta`) is clear without hiding formal structure (`chapters/chapter07.tex:176`, `chapters/chapter07.tex:180`). Chapter 9 similarly gives an accessible assumptions walk-through (`chapters/chapter09.tex:287`).
- Mechanism-to-observable mapping is concrete. You specify what is measured and why (semantic effect vs. weight; boundary similarity vs. consensus) (`chapters/chapter07.tex:184`), which is exactly what transparent ABM reporting should do.
- Countability includes meaningful stress testing and multi-timescale dynamics (turnover plus learning), not just a single toy run (`code/countability_abm.py:652`, `code/countability_abm.py:1048`).

## Major Concerns

- Sensitivity analysis is still underpowered relative to the claims. Reporting is largely single-run and seed-centric (“current runs”), while key outcomes show nontrivial seed dependence in ablations. In my quick sweep, drift outcomes for tight constructions varied materially across seeds, and ablation effect direction was not stable for all manipulations. That means mechanism dependence is plausible, but not yet robustly quantified.
- Ceiling effects blunt inferential force. In repeated drift runs, loose properties (`many`, agreement) sat at or near 100% throughout, making “asymmetric fraying” partly a design consequence rather than a hard test. This links to threshold choices and intent weights (`code/countability_abm.py:117`, `code/countability_abm.py:535`).
- Volcano ABM lacks parallel ablation rigor. It demonstrates a signature, but there is no explicit no-switch control, no boundary-learning knockout, and no sensitivity grid over cue reliability/shift magnitude (`code/volcano_abm.py:97`). So it is a strong plausibility probe, not yet a strong mechanism-isolation exercise.
- Some measurements are parameterized in ways that need stronger justification. Boundary similarity uses a fixed normalization constant (`1.5`) (`code/volcano_abm.py:173`), and the post-switch ecological shift is hard-coded (`x_mu_2=0.15`) (`code/volcano_abm.py:101`). These are defensible choices, but currently under-motivated for readers.
- Interpretation discipline is mostly good, but occasionally drifts into broad exclusion claims (“No version of feature-bundle theory predicts this order”) that exceed what these ABMs can adjudicate (`chapters/chapter09.tex:368`).

## Minor Concerns

- Reproducibility artifacts are not fully audit-friendly: figures are saved, but run manifests (seed, params, commit hash, environment) are not exported (`code/countability_abm.py:90`, `code/volcano_abm.py:252`).
- Default seeds differ across models (`7` vs `42`), which can confuse readers about which run produced chapter figures (`code/volcano_abm.py:256`, `code/countability_abm.py:1347`).
- Chapter prose could expose one compact parameter table for non-modelers (thresholds, learning rates, turnover), rather than leaving those assumptions mostly in code.

## Priority Fixes (top 5)

1. Add multi-seed batch reporting (minimum: 100 seeds) with means and uncertainty bands for the headline metrics; report effect sizes for each ablation, not only one trajectory.
2. Build a Volcano ablation suite mirroring Chapter 9 rigor: no-switch control, freeze-`\theta`, freeze-`w`, and reliability sweeps; then report which qualitative signatures survive.
3. Add a concise “assumptions and parameters” table to Chapter 7/9 prose, mapped to code constants, with one-sentence rationale per choice.
4. Reduce ceiling dependence by widening intent/threshold sensitivity tests and reporting when loose properties leave ceiling; otherwise state clearly that those dimensions are not currently discriminative.
5. Implement a reproducibility manifest written on each run (JSON/CSV): seed, parameter set, git commit, timestamp, and summary metrics, and cite that file in captions.
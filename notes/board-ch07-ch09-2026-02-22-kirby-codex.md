## Strengths
- The epistemic-status framing is unusually responsible: both prose and code repeatedly mark these ABMs as didactic mechanism sketches, not calibrated evidence (`chapters/chapter07.tex:178`, `chapters/chapter09.tex:285`, `code/countability_abm.py:8`).
- Chapter 9 gives ABM newcomers a usable entry point by stating state variables, update events, and turnover shortcut explicitly (`chapters/chapter09.tex:287`).
- The countability model includes targeted ablations rather than only “happy-path” runs, which is the right methodological instinct (`code/countability_abm.py:1048`).
- The Chapter 7 model cleanly operationalizes one key hypothesis: cue reweighting can change while category-level behavior persists (`chapters/chapter07.tex:180`, `code/volcano_abm.py:97`).

## Major Concerns
- From an iterated-learning perspective, `generational_turnover` is not acquisition: new agents are initialized from community means plus Gaussian noise, with full lexicons preloaded (`code/countability_abm.py:671`, `code/countability_abm.py:692`). That is mean-field resampling, not transmission through a learning bottleneck.
- The “tight-before-loose” outcome is partly built in structurally. Construction thresholds are hard-coded in order (`code/countability_abm.py:117`), and communicative intents are themselves conditioned on current individuation (`code/countability_abm.py:522`). That feedback loop makes the hierarchy likely even before any rich social dynamics.
- The transmission story is currently stronger in prose than in demonstrated effect size. In quick multi-seed checks, the drift signature persists without turnover, and turnover shifts are modest relative to seed variance. So claims about generational turnover doing heavy explanatory work should be softened unless a dedicated turnover ablation is reported.
- The Chapter 7 “ABM” is really many independent learners sampling from an external generator, not agents learning from each other (`code/volcano_abm.py:132`). Also, boundary persistence uses a normalized/clipped distance with an arbitrary scale factor (`code/volcano_abm.py:173`), which weakens interpretability of “stability remains high.”

## Minor Concerns
- Anchor death is strongly exogenous: four 20% decays per phase (`code/countability_abm.py:772`), plus direct decay of internal representations (`code/countability_abm.py:643`). That intervention is useful, but should be labelled as a forced perturbation schedule.
- Reproducibility metadata is inconsistent in the packet: it says seed 42 unless noted, but the reported volcano numbers match seed 7 (the script default) (`notes/ch7-ch9-abm-review-packet-2026-02-22.md:366`, `code/volcano_abm.py:256`).
- For non-ABM readers, assumptions are mostly clear, but limits on external validity would benefit from one explicit “cannot show” sentence in each chapter interlude.

## Priority Fixes (top 5)
1. In `chapters/chapter09.tex:287`, replace “approximate transmission” wording with: “Operationally, turnover here is mean-field replacement (new agents initialized near population means), not child-style learning from sparse input.”
2. Refactor `code/countability_abm.py:652` so new learners sample finite utterances from a few tutors and learn via `observe`, instead of direct mean initialization. That makes acquisition/transmission claims methodologically defensible.
3. Add an explicit turnover ablation in `experiment_mechanism_ablation` (`code/countability_abm.py:1048`): compare `turnover_rate=0` vs `>0` with learning kept on, and report effect sizes/intervals, not only single-seed deltas.
4. In `code/volcano_abm.py:169`, replace current boundary similarity with agreement on a fixed probe set between pre-switch and post-switch category assignments; remove arbitrary `1.5` normalization.
5. Add one sentence in `chapters/chapter07.tex:197` and `chapters/chapter09.tex:300`: “These models test mechanism plausibility under specified assumptions; they do not estimate real historical trajectories or population parameters.”
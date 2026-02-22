**Strengths**
The chapter has a strong organizing claim and repeats it consistently: grammaticality as a maintained form-value coupling (`chapters/chapter14.tex`, “The HPC claim”). The best part is the explicit separation of signal and target: “acceptability’s what the detector reports; grammaticality’s the category” (`chapters/chapter14.tex:45`). That is the right move if you want a scientifically serious theory rather than armchair intuitionism.

The illusion section is also well chosen: garden paths and comparative illusions are exactly the cases that force a detector-vs-oracle distinction (`chapters/chapter14.tex`, “Grammaticality illusions”). I also like the negative-space discipline (“what doesn’t count”), which prevents the theory from swallowing every kind of linguistic discomfort. Finally, you include a scoped falsifier in the definiteness thread (`chapters/chapter14.tex:299-300`), which is a publishability-positive move.

**Major Concerns**
1. The mechanism is still under-specified at the computational level. “The detector’s Bayesian” (`chapters/chapter14.tex:43`) is a promissory note unless you define likelihood, prior, and update dynamics over constructions. Right now, this reads as mechanistic rhetoric plus metaphor (“zipper,” “immune system,” “spinning top”), not yet a model.

2. The phenomenology section is disciplined in tone, but the sign/object/interpretant mapping (“jolt, block, correction”) is not independently validated (`chapters/chapter14.tex`, “Three registers”). A skeptic will say this is post-hoc relabeling unless each register has separable behavioral/processing signatures.

3. Some empirical claims are too strong relative to evidence status. “No amount of exposure” and “persists across tasks, speakers, and presentation modes” for LBE (`chapters/chapter14.tex:240`) need narrower wording or direct meta-analytic backing. “~3-sigma absence” (`chapters/chapter14.tex:248`) is especially vulnerable unless you provide corpus model details. Heavy reliance on `reynolds2026lbe` (unpublished) will trigger immediate skepticism.

4. Acceptability vs grammaticality remains partly circular in the current framing. If entrenchment both constitutes grammaticality and calibrates the detector (`chapters/chapter14.tex:49`), then what observational pattern could show detector error rather than grammar change? You need identifiability conditions.

5. First thing skeptical specialists will reject: “syntax owns it” (`chapters/chapter14.tex:172`) and the dual-role claim (“maintainer and maintained”) unless you formalize levels of explanation to avoid category/mechanism collapse.

**Priority Fixes**
1. Add a compact formal model box: latent grammaticality state \(G\), detector output \(D\), inputs from structure, surprisal, and exposure history.
2. Replace absolute empirical claims with calibrated ones (“in available studies,” “in English varieties tested so far”).
3. Mark speculative links (schema drift, LBE unsatiatability mechanism) explicitly as hypotheses, not established results.
4. Operationalize “structural meaning” with annotation targets (dependency role, clause type, argument mapping) so it is testable.
5. State one clear discriminative prediction against a pure processing/surprisal account and one against relevance-theoretic inferential accounts.

**Decisive Tests**
1. Pre-registered model comparison on acceptability judgments: mixed-effects prediction from (a) structural well-formedness annotations, (b) LM surprisal, (c) parsing difficulty metrics, (d) interaction terms. Your theory should win by adding structural-coupling features beyond surprisal.
2. Dissociation benchmark: items crossing grammaticality and processing load (grammatical/high-load garden paths vs ungrammatical/low-load local violations). If detector architecture is right, these quadrants should produce specific error asymmetries.
3. Satiation longitudinal experiment with hierarchical Bayesian learning models: compare constraints predicted to drift vs resist drift. Fit competing update rules (frequency-only vs competition-based “conspicuous absence”).
4. Probe-based LM test: extract whether models encode “structural meaning” variables (argument structure, clause type) independently of token probabilities; then test whether human judgments track probe confidence or raw surprisal.
5. Community calibration test: train/adapt LMs on register/dialect-specific corpora and predict cohort-structured judgment shifts. If no cohort-structured shift appears where entrenchment differs, core maintenance claims are in trouble.
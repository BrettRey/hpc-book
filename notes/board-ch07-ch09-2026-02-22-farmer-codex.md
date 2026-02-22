## Strengths
You are doing several things right for an illustrative ABM program. Epistemic-status labeling is explicit and repeated in both prose and code (`chapters/chapter07.tex:178`, `chapters/chapter09.tex:285`, `code/countability_abm.py:8`, `code/volcano_abm.py:5`). That is rare, and it materially reduces misuse risk. You also give non-ABM readers an accessible mechanism sketch (`chapters/chapter09.tex:287`) and, in Chapter 7, you cleanly separate observables from interpretation (`chapters/chapter07.tex:193`, `chapters/chapter07.tex:195`). Finally, you have a real ablation scaffold rather than just a narrative figure (`code/countability_abm.py:1048`), which is the correct instinct if you want causal-mechanism credibility rather than decorative simulation.

## Major Concerns
The core risk is that some outcomes are strongly “baked in” by construction, then narrated as discovered. In `code/countability_abm.py`, threshold geometry (`Construction`), intent-weight schedules (`code/countability_abm.py:535`), noun priors (`code/countability_abm.py:445`), and explicit anchor decay (`code/countability_abm.py:773`) all point in the same direction. That does not invalidate the model, but it narrows what it can claim: mechanism plausibility, not evidential adjudication.

Second, ablation claims are too strong relative to stability. The code language “prove results aren’t automatic” and “specific mechanisms produce specific effects” (`code/countability_abm.py:1050`, `code/countability_abm.py:1133`) overstates what appears to be seed-sensitive behavior. In a quick 20-seed sweep, the sign of key deltas flipped frequently (for example, no-anchor vs baseline on `three` was positive only 8/20 seeds). That is not failure; it is uncertainty, and it should be reported as such.

Third, some headline signatures are saturated, not discriminating. In the same sweep, `many` and `agreement` for `data` stayed at 1.00 across seeds after drift runs. If a metric is pinned at ceiling, it cannot do explanatory work; it mostly reflects model architecture.

Fourth, measured-vs-inferred language is still inconsistent across artifacts. Chapter 7 is mostly disciplined, but the packet still uses overreach phrasing like “stark mathematical demonstration” and “proof of concept for the core methodological claim” (`notes/ch7-ch9-abm-review-packet-2026-02-22.md:188`, `notes/ch7-ch9-abm-review-packet-2026-02-22.md:201`). That should be harmonized downward.

Fifth, the volcano model has hidden normalization choices that can look innocuous but matter: post-switch ecological shift (`code/volcano_abm.py:101`) and similarity scaling constant (`code/volcano_abm.py:173`). For non-ABM readers, these are effectively free parameters unless surfaced explicitly.

## Minor Concerns
There is no uncertainty reporting (intervals, seed ensembles, or effect-size distributions) in chapter prose tied to the figures (`chapters/chapter09.tex:291`, `chapters/chapter07.tex:193`). There is also no explicit “null” or rival toy mechanism to benchmark interpretive uniqueness. If two alternative micro-rules yield similar macro-signatures, the current narrative should say so. Finally, the review packet appears partly out of sync with revised chapter language; that creates avoidable epistemic drift between internal and public-facing claims.

## Priority Fixes (top 5)
1. Replace deterministic-seeming claims with ensemble language in text and captions.  
Edit `chapters/chapter09.tex:291` to: “In representative runs under this parameterization, tight properties often decline earlier than loose properties.”

2. Add a one-page “assumption ledger” (exogenous knobs vs endogenous outcomes) for Chapter 9.  
Reference exact knobs from `code/countability_abm.py:535`, `code/countability_abm.py:773`, `code/countability_abm.py:445`.

3. Downgrade overstrong packet phrasing to mechanism-illustration phrasing.  
Revise `notes/ch7-ch9-abm-review-packet-2026-02-22.md:188` and `notes/ch7-ch9-abm-review-packet-2026-02-22.md:201` to “illustrates” and “is consistent with,” not “demonstrates/provides proof.”

4. Report seed-ensemble effect ranges for each ablation before interpretation.  
Add summary output near `code/countability_abm.py:1048` (median delta, IQR, sign consistency).

5. Add one null model per chapter ABM to test narrative uniqueness.  
For Chapter 7 (`code/volcano_abm.py:97`), randomize or remove lexeme boundaries; for Chapter 9 (`code/countability_abm.py:757`), decouple intent sampling from current individuation and compare signatures.
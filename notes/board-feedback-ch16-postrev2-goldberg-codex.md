1. Overall verdict: **Improved but still missing core work**.

2. Strengths:
- The Ch15→Ch16 handoff now cleanly converts claim into risk: `No conditioning gain, no maintenance claim` and immediate gauntlet framing (`chapters/chapter15.tex:217`, `chapters/chapter15.tex:219`, `chapters/chapter16.tex:12`).
- Table-role separation is now explicit, which fixes prior conceptual blur between synthesis and testing (`chapters/chapter16.tex:70`, `chapters/chapter16.tex:71`).
- Falsifier adjudication is tighter: pre-fixed proxy family and threshold-scope caveat reduce post hoc escape routes (`chapters/chapter16.tex:126`, `chapters/chapter16.tex:165`, `chapters/chapter16.tex:166`).

3. Concerns:
- The “one inferential lane” over-centers `P(Form|D,R,C)` across domains; that is strong on social conditioning, weaker on construction-internal predictors central to learning/generalization (`chapters/chapter16.tex:46`, `chapters/chapter16.tex:77`).
- The running case is still effectively one lexical ecosystem (`data`), so constructional transfer claims are under-tested (`chapters/chapter16.tex:16`, `chapters/chapter16.tex:142`).
- The 5% rule is still contestable because predictive metric/split protocol is not nailed down in-text (`chapters/chapter16.tex:165`).

4. One concrete next edit (smallest high-leverage change):
- After `chapters/chapter16.tex:165`, add one sentence that defines the gain metric and split type as **out-of-construction** (not random-token) generalization, e.g. held-out log-loss reduction on unseen construction families.
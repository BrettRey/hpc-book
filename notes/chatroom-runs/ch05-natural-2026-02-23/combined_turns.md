### [R1-T00] Moderator
Moderator: We are running a natural comedy writers' room pass. Talk like humans, not forms. The only hard job is coverage: Pass T must get through the whole chapter top-to-bottom.
Coverage plan for Pass T:
- R1-T01 Parker: chapters/chapter05.tex:1-62
- R1-T02 Ephron: chapters/chapter05.tex:63-124
- R1-T03 Twain: chapters/chapter05.tex:125-186
- R1-T04 Seinfeld: chapters/chapter05.tex:187-248
- R1-T05 Adams: chapters/chapter05.tex:249-310
- R1-T06 Wilde: chapters/chapter05.tex:311-372
- R1-T07 Wodehouse: chapters/chapter05.tex:373-434
Candidate line(s):
1) n/a
2) n/a
Vote (optional): n/a

### [R1-T01] Parker
Parker: If we’re doing a clean top-to-bottom pass, this opening needs to hit thesis sooner. The personal setup is lively, but four beats of origin story before the puzzle makes the argument feel delayed. Keep the date and the Pullum/Nefdt spark, then pivot hard into the problem statement so the chapter starts doing work by line 25. The good news is the core logic is already there: scale explains tolerance, mechanism explains boundary stability. I’d just trim jargon pileup so “dynamic discreteness” is the one flag the reader carries into the formal section.
Pitches:
- `chapters/chapter05.tex:25` Add: “This chapter’s claim is simple: linguistic categories can be behaviorally discrete while materially continuous, because social-cognitive mechanisms stabilize boundaries at usable scales.”
- `chapters/chapter05.tex:59` Replace with: “Relative Tolerance: A change preserves category membership when it is negligible relative to the current scale; the same absolute change may flip membership near a boundary.”
Vote: n/a

### [R1-T02] Ephron
Ephron: I’m with Parker on carrying one clean flag into the math, and this section is where that flag either earns trust or gets buried. Right now line 66 sounds a bit defensive (“not a philosophical aside”) when it could sound confident and testable. The skip-path box is great social design for mixed readers, but the three bullets should mirror the same diction used later so skimmers don’t feel they switched books. In the formalization, the logic is strong; what needs polish is reader footing at the handoff from infinitesimals to prediction, so the stakes stay empirical rather than metaphysical. There’s also a small prose stumble at line 121 (“what it’s”), and the epistemicism contrast at 123 wants one clarifying sentence so the difference lands as more than a name-check. Tune those beats and the section reads rigorous and hospitable at the same time.
Pitches:
- `chapters/chapter05.tex:66` Replace with: “The next section does empirical work, not detour: it predicts that judgment variance should track distance to boundary in a specific functional form, and that signature should vanish if the hyperreal model is wrong.”
- `chapters/chapter05.tex:124` Add: “Where epistemicism ties unknowability to limits of discrimination, this model ties it to scale-relative access to a sharp cutoff that is precise in theory but not finitely specifiable in practice.”
Vote: n/a

### [R1-T03] Twain
Twain: Parker and Ephron are both right that this chapter is strongest when it sounds like it can be wrong, not just right in theory. In this stretch, line 127 gets a little triumphal before the evidence lands, so I’d phrase it as a prediction claim instead of a verdict. The Khalidi contrast is useful, but “fuzzy realism doesn’t” reads too absolute unless we specify the behavioral pattern it misses. The metric section is the other place to tighten: good substance, too much throat-clearing. Say plainly that we don’t need one sacred metric, just local agreement on what counts as “small,” then move on. That keeps the math grounded and avoids the seminar-tone pileup.

Pitches:
- `chapters/chapter05.tex:127` Replace with: “On this view, the formalism earns its keep by predicting where boundaries drift and where judgment variance spikes under perturbation, rather than merely positing an inaccessible cutoff.”
- `chapters/chapter05.tex:161` Replace with: “We do not need one uniquely correct metric; we need metrics that locally agree on what counts as a tiny perturbation near the boundary, because that shared local structure is what Relative Tolerance requires.”
Vote: n/a

### [R1-T04] Seinfeld
Seinfeld: Ephron's footing note and Twain's "sound like it can be wrong" both bite here, because this stretch repeats the claim so often it starts sounding ceremonial instead of empirical. The evidentiality example is excellent, then we hit that giant metric sentence and suddenly we are assembling furniture without the picture on the box. One clean prediction in plain English right after the example would keep the reader from wandering. The "two stories" paragraph works once, but by line 240 we have heard geometry versus mechanism four times, and each repeat loses force. I would compress the slogans and let each mechanism carry a distinct observable job: acquisition sets initial clustering, entrenchment steepens cores, alignment repairs local drift, transmission filters variants. The `very fun` / `a lot of fun` beat is gold because it sounds like people talking, not a committee memo.
Pitches:
- `chapters/chapter05.tex:194` Add: “Empirical prediction: in English, speakers should preserve evidential distinctions in inference and paraphrase tasks, but fail to show stable morphosyntactic clustering on evidential diagnostics, because no grammatical evidential basin is maintained.”
- `chapters/chapter05.tex:230` Replace with: “The basin model locates stability in feature space; homeostatic mechanisms explain how interaction and learning keep items near those attractors over time without redefining the boundary.”
Vote: chapters/chapter05.tex:127

### [R1-T05] Adams
Adams: Twain’s “make it falsifiable” note is exactly the right pressure here: the `fun` section already has multiple diagnostics, so frame it as convergent measurement, not just a historical story. Seinfeld’s furniture warning also bites at line 304, where the reader is asked to carry the diachrony-to-synchrony transition without a handle. Add one explicit design sentence that says we are testing two boundary regimes: drift toward a basin versus stable residence at the boundary. The absurd-but-clarifying model is orbital mechanics: `fun` is spiraling into a new orbit, reciprocals are parked at a Lagrange point between pronoun and determiner pulls. If you say that plainly, “three diagnostics” lands as method rather than teaser.
Pitches:
- `chapters/chapter05.tex:304` Replace with: “The contrast now becomes testable: \mention{fun} models diachronic movement toward a category boundary, while reciprocals let us test whether a form can remain synchronically stable at that boundary without ongoing directional drift.”
- `chapters/chapter05.tex:308` Replace with: “The goal is not to force a binary label from isolated tests, but to measure opposing pronoun-like and determinative-like pulls and ask whether intermediate placement is a stable grammatical state.”
Vote: chapters/chapter05.tex:230

### [R1-T06] Wilde
Wilde: Seinfeld’s “furniture without the picture” problem is still lurking here: the argument dazzles, then briefly forgets to hand us the wrench. Adams’s orbital image is useful precisely because it implies instrumentation; if reciprocals are parked at the Lagrange point, variance is how we detect the parking brake. The diagnostics in 311–317 are excellent, but the significance caveat should distinguish statistical volatility from ontological instability in one clean stroke. Then the gradient section should stop half a beat earlier in philosophy and start one beat earlier in falsification. Right now the model reads true; it should read risked. Give the reader one sentence that says exactly what would kill the claim, and the whole section gains spine.
Pitches:
- `chapters/chapter05.tex:319` Replace with: “Inferential strength varies with the comparison set, but the structural result does not: across specifications, reciprocals remain between pronoun and determinative anchors, so the wobble is statistical, not ontological.”
- `chapters/chapter05.tex:366` Add: “A direct falsifier follows: if independently boundary-near items do not show greater within-item judgment variance than boundary-far items after controls for frequency and participant effects, the two-layer model fails.”
Vote: chapters/chapter05.tex:304


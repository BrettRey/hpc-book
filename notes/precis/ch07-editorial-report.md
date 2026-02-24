# Chapter 7: Editorial Report

*Deep read of `chapters/chapter07.tex` against the style guide, the ch07 precis, and the full book arc.*

---

## 1. Argument

The chapter's central argument -- that projectibility is what mechanisms are *for*, not a bonus they happen to produce -- is sound and necessary for the book. The subordination of profile and mechanism to projectibility is the chapter's sharpest philosophical move, and the Polish aspect case study gives it genuine teeth: a category that is descriptively real yet definitionally unprojectible is exactly the worked demonstration Part II needs. The volcanic-island metaphor carries real explanatory weight and does structural work in later chapters (Ch 9 on *data*, Ch 10 on definiteness/deitality, Ch 11 on adjective plumage). The Peircean section (7.5, "What projection is") successfully grounds projectibility in the would-be/interpretant apparatus without making Peirce ornamental; the dissolution of Goodman's circularity via mechanisms sustaining habits rather than habits bootstrapping themselves is the chapter's strongest philosophical contribution. One gap: the transition from the Polish case to the generalising examples (causative alternation, syncretism, BERT grammatical relations) at lines 210--218 is too compressed -- three independent empirical programmes are given a paragraph each, and the reader can't assess whether the "mechanism projects; definition doesn't" claim applies uniformly or only to specific kinds of mismatch.

## 2. Structure

The chapter's organisation is largely effective: failure case (NPI), slogan unpacking, worked example (Polish), mechanistic reinterpretation, Peirce, field-relative projectibility, epistemic payoff. Two structural issues stand out. First, the "Unpacking the framework" subsection (lines 42--63) sits under no section heading -- it is a `\subsection` directly under the chapter opener. Since the chapter otherwise uses `\section` for its major divisions, this subsection floats oddly; it would read better promoted to a `\section` or folded into the introduction. Second, the "Generalising the lesson" section (lines 202--218) performs two distinct jobs: it summarises the Polish case and then supplies three independent cross-linguistic/cross-domain parallels. These parallels deserve more development or should be flagged as a rapid survey. The current pacing -- a careful 150-line treatment of Polish followed by three paragraphs of generalisation -- creates an evidential lopsidedness. The Part III preview (lines 335--350) is well-placed and concise but repeats information the reader will get in the "Looking forward" closing paragraphs (lines 462--467); one of the two could be trimmed.

## 3. Prose

The writing is at its best in the opening pages (the Tagomi epigraph, the pedicab inference, the slogan unveiling) and in the volcanic-island extended metaphor -- these passages have the book's characteristic combination of plainness and precision. The Peirce section (lines 221--246) is well-controlled: quotations are integrated into the argument rather than displayed as decoration, and the "men and words reciprocally educate each other" passage lands with real force. The prose drags in two places. The "What the framework offers" section (lines 430--449) reads like a grant narrative: five numbered benefits, each following the pattern "The maintenance view says X. This matters because Y." The tone shifts from argumentative to promotional. The parenthetical at lines 97--99, beginning "(A moderate reader might object...)", is valuable content but is typeset as a single-sentence parenthetical that runs to 60 words; it would read better as its own paragraph. The simulation interlude (lines 173--199) is carefully hedged but the hedging itself becomes repetitive -- "illustrative rather than probative," "doesn't by itself establish," "the warrant is limited" all say the same thing.

## 4. Evidence

The Polish aspect case (Divjak, Wisniewski, and Milin) is well-chosen and well-handled -- the three-model comparison is clearly explained, the asymmetry between imperfective and perfective prediction is highlighted effectively, and the gap-filling validation adds a second evidential layer. The ABM simulation is appropriately flagged as didactic, and the 20-seed sensitivity run (line 199) provides minimal but adequate robustness evidence. The field-relative projectibility cases are mixed in quality. The tomato case (lines 257--265) is pedagogically excellent but philosophically lightweight -- it's a standard illustration that does not advance the argument beyond what the abstract statement already established. The proper nouns/proper names case (lines 270--294) is strong and linguistically specific. The constituency/dependency case (lines 296--309) is genuinely illuminating. The colour non-grammaticalisation case (lines 311--332, drawing on Prasertsom, Smith, and Culbertson) is the section's best evidence -- it provides a *negative* prediction (colour should grammaticalise but doesn't) and an experimental confirmation. The degrees-of-projectibility subsection (lines 412--427) marshals three independent experimental findings (Favier and Huettig, Sassenhagen et al., Graziano-King and Cairns) efficiently and persuasively.

## 5. Cross-chapter coherence

The chapter fulfils its promissory obligations from Ch 6 (which promised that Ch 7 would show what mechanisms are *for*) and sets up Ch 8 (failure modes) cleanly. The definiteness thread at lines 469--470 is well-integrated and specific. The Part III preview (lines 335--350) accurately foreshadows Chs 9--12. One terminology concern: the chapter uses "stabiliser" and "mechanism" with apparent interchangeability (e.g., lines 16, 49, 234--238), despite Ch 6 having introduced "stabiliser" as a terminological choice. The book-level editorial report flags this; Ch 7 is one of the places where the slippage is most visible. The Peirce section (lines 221--246) establishes would-be, interpretant, and habit as load-bearing terms; these are picked up in Chs 9--14. The non-reductive position (line 238: "mechanisms sustain habits, but habits aren't reducible to mechanisms") is a commitment that Ch 14's phenomenology section depends on -- it is clearly stated here, which is good. The NPI example at the chapter's opening (lines 39--40) reappears in the Peirce section (line 234) as the negative case for mediation vs. correlation; this callback is effective. Missing connection: the chapter does not reference Ch 5's basin-of-attraction geometry, despite the fact that "degrees of projectibility" (lines 412--427) maps naturally onto distance-from-basin-centre. A single sentence connecting variance-at-periphery to the basin model would strengthen the cross-chapter fabric.

## 6. House style issues

1. **Missing `\mention{}` on linguistic forms.** Line 122: `\mention{\ipa{robić}}` and `\mention{\ipa{zrobić}}` are correctly marked, but the backtick-quoted glosses (`do', `accomplish') use raw single quotes rather than `\enquote{}`. Same pattern at line 124 (`swim', `swim across', `complete the crossing'). And at line 123 where the translation of `\mention{\ipa{pływać}}` uses a bare backtick-tick pair. These should use semantic quotation marks. Approximately 6 more instances in the chapter follow this pattern (lines 88, 161, 381, 421).

2. **Backtick-tick quotation marks.** Line 123: `` `swim' `` uses TeX-style backtick-tick quotation. The house style requires `\enquote{}`. This occurs throughout interlinear-style glosses in the chapter -- approximately 8 instances total.

3. **Bold in prose.** Lines 47, 49, 53: `\textbf{Profile}`, `\textbf{Stabilized by mechanisms}`, `\textbf{Projectible relative to purposes}` use bold labels in running prose. The style guide says "Avoid bold labels in prose. Taxonomies and argument sequences should flow as narrative, not as itemized lists." These could be converted to `\term{}` or worked into flowing prose with ordinal transitions.

4. **Bold in enumerated items.** Lines 58--60 use `\textbf{}` inside `\enumerate{}` items. Lines 357--363 repeat this pattern ("Cluster check," "Homeostasis check," "Projectibility check"). Lines 435, 439, 441, 443, 445, 447 use the same pattern for the five-benefit enumeration. The style guide permits enumeration for hypothesis/prediction lists, but bold labels within them are discouraged.

5. **`\bigskip` as section transition.** Line 451 uses `\bigskip` to separate the "What the framework offers" subsection from the chapter's closing paragraphs. This is a layout hack; the transition should be handled by a subsection heading, a scene break command, or simply a new paragraph.

6. **Orphaned subsection.** Lines 42--63: `\subsection{Unpacking the framework}` appears immediately under the chapter opener with no parent `\section{}`. This may be intentional (treating the introduction as implicit), but it is the only subsection in the chapter without a parent section.

7. **Index entry consistency.** The chapter indexes `\ixsq{kind}` in several places (e.g., lines 39, 170, 385, 406, 459) but uses "kind" in the text despite the CLAUDE.md instruction that the book uses "category" throughout and avoids "kind." The index entries track the text's usage, so if "kind" is retained in text, the index entries are correct -- but the terminological preference should be checked.

8. **Sentence-initial numeral.** Line 199: "20-seed sensitivity run" -- if this ever begins a sentence, it should be written out, but here it doesn't. No issue.

9. **`\term{}` vs `\mention{}` distinction.** Lines 270--271: `\term{proper noun}` and `\term{proper name}` are correctly marked as technical concepts. Line 292: `\mention{Brett}` is correctly marked as a mentioned form. Good.

10. **En-dash in closing line.** Line 464: "The next chapter asks: how do we know when we don't have a kind" -- the colon after "asks" introduces a question without a capital letter; this is fine stylistically but note that the question is not set off with `\enquote{}` or italics. This is a judgment call, not a violation.

## 7. Specific recommendations

1. **Promote or restructure the orphaned subsection.** Either promote "Unpacking the framework" (line 42) to `\section{}` or fold it into the chapter introduction above. The current structure has a subsection with no parent section, which creates a formatting anomaly in the PDF.

2. **Develop the generalising examples.** The three cross-linguistic parallels at lines 210--218 (causative alternation, syncretism, BERT grammatical relations) are doing significant argumentative work -- they're the chapter's main evidence that the Polish pattern generalises. Each currently gets one paragraph. Either expand each to 2--3 paragraphs with enough detail that the reader can assess the claim, or explicitly frame them as a rapid survey and flag Ch 11 as the place where the word-class case is developed fully.

3. **Connect degrees-of-projectibility to Ch 5's basin geometry.** Add a sentence in the "Degrees of projectibility" subsection (around line 423) linking variance-at-periphery to the basin-of-attraction model from Ch 5. Something like: "This is the variance signature that Chapter 5's basin geometry predicts: judgments diverge as items approach the ridgeline between basins."

4. **Trim the "What the framework offers" section.** The five-benefit enumeration (lines 435--449) could be compressed from five paragraphs to three without losing content. Benefits 1 (legitimises mechanistic work) and 2 (cross-camp coherence) make the same point from different angles; benefits 4 (realism without essentialism) and 5 (origin vs. maintenance) are strong and should stay. Benefit 3 (reorients methodology) is valid but stated more effectively in the closing paragraphs (lines 452--459). Cutting or merging would restore the chapter's argumentative pace.

5. **Enforce stabiliser/mechanism terminology.** Do a pass to decide where "mechanism" is the right word (generic causal processes) and where "stabiliser" is (the specific HPC-maintaining processes introduced in Ch 6). The chapter currently uses them near-interchangeably, which undercuts the terminological choice Ch 6 made.

6. **Replace bold labels in the slogan-unpacking section.** Convert the three `\textbf{}` labels at lines 47, 49, 53 to `\term{}` or to prose transitions ("The first component, the profile, is what you observe..."). Same for the bold labels inside enumerated lists at lines 58--60 and 357--363.

7. **Fix backtick-tick quotation marks.** Replace all `` `gloss' `` patterns (lines 122--124, 161, 381, 421, and approximately 6 others) with `\enquote{gloss}` per house style.

8. **Replace `\bigskip` at line 451.** Use a subsection heading, a `\medskip` if a visual break is truly needed, or simply transition with a new paragraph.

9. **Trim duplicate Part III preview material.** The Part III preview subsection (lines 335--350) and the closing forward-looking paragraphs (lines 462--467) cover the same ground. Either cut the latter to a single sentence or remove the preview subsection and let the closing do the work.

10. **Reconsider "kind" vs "category" in text.** Lines 39, 170, 385, 406, 459 all use "kind" in running text. The CLAUDE.md says the book uses "category" throughout. Check whether these are deliberate exceptions (e.g., in phrases like "natural kind" where the philosophical term is intended) or inadvertent lapses. Where the intended sense is the book's own theoretical concept, prefer "category."

# Term Consistency Audit (2026-02-22 06:32:47)

## Scope
- Glossary source: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/glossary.tex`
- Glossary entries parsed: 196
- TeX files scanned: 28
- Issues found: 149
- Decisions file: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/reports/term-audit-decisions-from-code.csv`

## Decision Options
- `keep`: accept the observed form as-is.
- `replace_with_canonical`: replace with the glossary canonical term.
- `replace_custom`: provide your own replacement in `custom_replacement`.
- `scope`: choose `this_occurrence` or `all_same_observed_form`.

## Issue Counts
- `alias_used`: 2
- `normalized_variant`: 62
- `unknown_term`: 84
- `unknown_term_with_suggestion`: 1

## Findings

### T0001 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter02.tex:54`
- Observed: `classes`
- Canonical: `class`
- Suggested replacement: `class`
- Default action: `replace_with_canonical`
- Context: ... e difficulty and move on, rarely to question whether adjective and preposition were the right kinds of kind. \section{Where essentialism works} \label{sec:2:where-essentialism-works} Essentialism is unimpeachable when \term{[[classes]]} are constructed (I reserve \term{category} for natural kinds throughout). Stipulative definitions are the clearest case. A bachelor is an unmarried adult male because we define it so. Membership is determinate because ...
- Review in decisions CSV row `T0001`: `keep` | `replace_with_canonical` | `replace_custom`

### T0002 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter02.tex:66`
- Observed: `natural number`
- Default action: `keep`
- Context: ... igskip But there's a disanalogy, and it matters. In mathematics, you stipulate the category and discover its properties. In linguistics, you are trying to discover the category. The direction reverses. When you define \term{[[natural number]]}, you aren't hypothesising that something out there satisfies your definition. When you define \term{clause}, you are. Mathematical existence is logical consistency; natural-kind existence is causal-historical. A categor ...
- Review in decisions CSV row `T0002`: `keep` | `replace_with_canonical` | `replace_custom`

### T0003 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter02.tex:66`
- Observed: `clause`
- Default action: `keep`
- Context: ... rties. In linguistics, you are trying to discover the category. The direction reverses. When you define \term{natural number}, you aren't hypothesising that something out there satisfies your definition. When you define \term{[[clause]]}, you are. Mathematical existence is logical consistency; natural-kind existence is causal-historical. A category that's logically coherent might carve nothing in natural language. The bootstrapping problem makes this c ...
- Review in decisions CSV row `T0003`: `keep` | `replace_with_canonical` | `replace_custom`

### T0004 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter02.tex:257`
- Observed: `Species`
- Canonical: `species`
- Suggested replacement: `species`
- Default action: `replace_with_canonical`
- Context: ... maintain this population as a cohesive unit over time?} The answer varies: gene flow, shared selection pressures, developmental constraints, mate recognition systems. Different mechanisms predominate in different cases. \term{[[Species]]} names not a single kind defined by a single essence but a cluster of populations maintained~-- flexibly~-- by overlapping mechanisms. This shift~-- from definition-seeking to mechanism-seeking~-- is what made boundary ...
- Review in decisions CSV row `T0004`: `keep` | `replace_with_canonical` | `replace_custom`

### T0005 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter03.tex:74`
- Observed: `homeostatic property cluster`
- Default action: `keep`
- Context: ... rom philosophy of biology. Species aren't defined by essences; they're maintained by mechanisms (reproduction, selection, development) that keep certain properties clustering together \citep{boyd1991}. Boyd called these \term{[[homeostatic property cluster]]} kinds. The clustering is real (it supports induction) but dynamic (it requires ongoing maintenance). Remove the mechanisms and the cluster dissolves, like a spinning top that falls when the spin stops. Peirce tells you ...
- Review in decisions CSV row `T0005`: `keep` | `replace_with_canonical` | `replace_custom`

### T0006 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter03.tex:173`
- Observed: `schema`
- Default action: `keep`
- Context: ... snapshot of the system. The present account adds what he set aside: the mechanisms that maintain the system across time. A parallel comes from complexity science: \textcite{gellmann1994} calls such relational structures \term{[[schema]]}s~-- compressed internal models that encode regularities and enable prediction. In complex adaptive systems, a schema isn't a copy of the world but a coarse-grained encoding of its history, refined through feedback \auto ...
- Review in decisions CSV row `T0006`: `keep` | `replace_with_canonical` | `replace_custom`

### T0007 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter04.tex:88`
- Observed: `Mechanism`
- Canonical: `mechanism`
- Suggested replacement: `mechanism`
- Default action: `replace_with_canonical`
- Context: ... t the same style of explanation works: mechanism-based, historical, non-essentialist. What maintains the clustering matters more than what defines the category. \section{What mechanisms mean} \label{sec:4:mechanisms} \term{[[Mechanism]]} is doing a lot of work here, so I should say briefly what I mean. By \term{mechanism} I mean an empirically tractable process with a characteristic signature under perturbation: change the inputs in a targeted way, and ...
- Review in decisions CSV row `T0007`: `keep` | `replace_with_canonical` | `replace_custom`

### T0008 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter04.tex:90`
- Observed: `Noun`
- Canonical: `noun`
- Suggested replacement: `noun`
- Default action: `replace_with_canonical`
- Context: ... resented in the mind. His analogy is the honeycomb: hexagonal structure is a real feature of beehives, but no bee represents hexagons. The structure emerges from the local behaviours of many bees following simple rules. \term{[[Noun]]}, on this view, is the linguistic honeycomb~-- real enough to describe, but not internally represented. The analogy is useful but the conclusion doesn't follow. What makes the honeycomb real isn't that bees lack hexagon ...
- Review in decisions CSV row `T0008`: `keep` | `replace_with_canonical` | `replace_custom`

### T0009 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter04.tex:121`
- Observed: `living thing`
- Default action: `keep`
- Context: ... ubber duck is inanimate by any ontological criterion, but its curvature, part structure, and face-like configuration place it in the animal-appearance cluster. The category tracked by these neural representations isn't \term{[[living thing]]}; it's a cluster of statistical properties that happen to co-occur because animate beings share production constraints. This is exactly what an HPC account predicts. What gets called \enquote{animacy} at the neural level ...
- Review in decisions CSV row `T0009`: `keep` | `replace_with_canonical` | `replace_custom`

### T0010 - alias_used
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter04.tex:140`
- Observed: `interactive alignment`
- Canonical: `alignment`
- Suggested replacement: `alignment`
- Default action: `replace_with_canonical`
- Context: ... lignment} Speakers accommodate to each other. In conversation, interlocutors converge on lexical choices, syntactic structures, even phonetic details \citep{pickering2004,garrod2009}. This is \ixs{[[interactive alignment]]}\term{interactive alignment}: the tendency to match your speech to your interlocutor's. Alignment maintains categories by enforcing community-wide coherence. If I use \mention{adult} as a verb and you accommodate, we've both reinforced the verb us ...
- Review in decisions CSV row `T0010`: `keep` | `replace_with_canonical` | `replace_custom`

### T0011 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter04.tex:218`
- Observed: `HPC kind`
- Default action: `keep`
- Context: ... tained clusters that support scoped induction. That's enough for the epistemic work categories are supposed to do. If philosophers want to reserve \enquote{natural kind} for more fundamental entities, fine~-- call these \term{[[HPC kind]]}s and move on. A second objection targets the mechanisms themselves. \citet{onishi2022} press the question: what counts as a homeostatic mechanism? If the answer is \enquote{whatever keeps the properties clustered}, the ...
- Review in decisions CSV row `T0011`: `keep` | `replace_with_canonical` | `replace_custom`

### T0012 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:29`
- Observed: `Stabilizer`
- Canonical: `stabilizer`
- Suggested replacement: `stabilizer`
- Default action: `replace_with_canonical`
- Context: ... thways, social indexing, transmission dynamics~-- but the constraint is the same: the term is elastic enough to span cognitive and social scales, yet not so elastic that any correlation gets to call itself mechanistic. \term{[[Stabilizer]]} is a related term. Where \enquote{mechanism} emphasizes causal structure, \enquote{stabilizer} emphasizes the functional role \parencite{illari2012}~-- what keeps the cluster clustered. A stabilizer is a mechanism insof ...
- Review in decisions CSV row `T0012`: `keep` | `replace_with_canonical` | `replace_custom`

### T0013 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:115`
- Observed: `Analogy`
- Canonical: `analogy`
- Suggested replacement: `analogy`
- Default action: `replace_with_canonical`
- Context: ... ng on information structure). If the framework earns explanatory traction for both, it's not just sociolinguistics with a new label. Several mechanisms deserve mention even if they don't receive full case studies here. \term{[[Analogy]]} extends established patterns to new cases by perceived similarity~-- it's how children produce \mention{goed} and how adults accept novel compounds. \term{Standardization} operates through institutions: schools, style g ...
- Review in decisions CSV row `T0013`: `keep` | `replace_with_canonical` | `replace_custom`

### T0014 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:115`
- Observed: `Standardization`
- Canonical: `standardization`
- Suggested replacement: `standardization`
- Default action: `replace_with_canonical`
- Context: ... tion even if they don't receive full case studies here. \term{Analogy} extends established patterns to new cases by perceived similarity~-- it's how children produce \mention{goed} and how adults accept novel compounds. \term{[[Standardization]]} operates through institutions: schools, style guides, dictionaries, corpus-annotation schemes. These codify and enforce norms, creating explicit feedback loops that natural transmission lacks. \term{Indexicality} links ...
- Review in decisions CSV row `T0014`: `keep` | `replace_with_canonical` | `replace_custom`

### T0015 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:115`
- Observed: `Indexicality`
- Canonical: `indexicality`
- Suggested replacement: `indexicality`
- Default action: `replace_with_canonical`
- Context: ... ds. \term{Standardization} operates through institutions: schools, style guides, dictionaries, corpus-annotation schemes. These codify and enforce norms, creating explicit feedback loops that natural transmission lacks. \term{[[Indexicality]]} links linguistic forms to social meaning: a choice of variant signals group membership, registers attitude, or marks formality. The social stakes make the choice salient and its patterning consequential, reinforcing cat ...
- Review in decisions CSV row `T0015`: `keep` | `replace_with_canonical` | `replace_custom`

### T0016 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:115`
- Observed: `Error and repair`
- Canonical: `error and repair`
- Suggested replacement: `error and repair`
- Default action: `replace_with_canonical`
- Context: ... oup membership, registers attitude, or marks formality. The social stakes make the choice salient and its patterning consequential, reinforcing category boundaries beyond what communicative function alone would produce. \term{[[Error and repair]]} maintains structure through on-line correction~-- speakers monitor output, catch deviations, and adjust mid-utterance. This creates real-time negative feedback that keeps production within the category's basin. Finally, ...
- Review in decisions CSV row `T0016`: `keep` | `replace_with_canonical` | `replace_custom`

### T0017 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:375`
- Observed: `Processing economy`
- Canonical: `processing economy`
- Suggested replacement: `processing economy`
- Default action: `replace_with_canonical`
- Context: ... tible clusters stabilized by further mechanisms, then mechanisms are categories. This claim is a theoretical consequence of the framework rather than an independent empirical finding~-- but it has testable implications. \term{[[Processing economy]]} is a category~-- it bundles properties (reduced forms, high frequency, resistance to analogical pressure) that cluster reliably because of underlying neural and memory constraints. \term{Social indexing} is a category~- ...
- Review in decisions CSV row `T0017`: `keep` | `replace_with_canonical` | `replace_custom`

### T0018 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:375`
- Observed: `Social indexing`
- Canonical: `social indexing`
- Suggested replacement: `social indexing`
- Default action: `replace_with_canonical`
- Context: ... mplications. \term{Processing economy} is a category~-- it bundles properties (reduced forms, high frequency, resistance to analogical pressure) that cluster reliably because of underlying neural and memory constraints. \term{[[Social indexing]]} is a category~-- it bundles properties (youth association, in-group marking, register restriction) maintained by identity construction and network dynamics. The mechanisms we invoke to explain quotative stability are th ...
- Review in decisions CSV row `T0018`: `keep` | `replace_with_canonical` | `replace_custom`

### T0019 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:440`
- Observed: `Particle`
- Canonical: `particle`
- Suggested replacement: `particle`
- Default action: `replace_with_canonical`
- Context: ... used in much typological and pedagogical work as a wastebasket for uninflected words that don't fit elsewhere: \mention{up} in \mention{look up}, \mention{to} in infinitives, \mention{not}, sentence-final \mention{eh}. \term{[[Particle]]} is the \enquote{Other} box on a survey: it records leftovers; it doesn't identify a kind. Does this cluster survive a maintenance audit? The properties don't co-occur reliably: \mention{up} takes complements; infinitiva ...
- Review in decisions CSV row `T0019`: `keep` | `replace_with_canonical` | `replace_custom`

### T0020 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:442`
- Observed: `narrative discourse structure`
- Default action: `keep`
- Context: ... lysis isn't analogy-by-enthusiasm~-- it identifies genuine stabilization that \term{particle} lacks. The quotative category is also a mechanism in the larger kinds that contain it. Quotatives are part of what maintains \term{[[narrative discourse structure]]}~-- they enable the vivid re-enactment that makes storytelling work. They are part of what maintains \term{youth register}~-- the forms that index adolescent identity and solidarity. They are part of what maintains \term ...
- Review in decisions CSV row `T0020`: `keep` | `replace_with_canonical` | `replace_custom`

### T0021 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:442`
- Observed: `youth register`
- Default action: `keep`
- Context: ... chanism in the larger kinds that contain it. Quotatives are part of what maintains \term{narrative discourse structure}~-- they enable the vivid re-enactment that makes storytelling work. They are part of what maintains \term{[[youth register]]}~-- the forms that index adolescent identity and solidarity. They are part of what maintains \term{informal speech} as a recognizable variety~-- the cluster of features that signals casualness, immediacy, peer context. A ...
- Review in decisions CSV row `T0021`: `keep` | `replace_with_canonical` | `replace_custom`

### T0022 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:442`
- Observed: `informal speech`
- Default action: `keep`
- Context: ... ture}~-- they enable the vivid re-enactment that makes storytelling work. They are part of what maintains \term{youth register}~-- the forms that index adolescent identity and solidarity. They are part of what maintains \term{[[informal speech]]} as a recognizable variety~-- the cluster of features that signals casualness, immediacy, peer context. And again, the stabilization is reciprocal: narrative structure provides the discourse ecology in which quotatives f ...
- Review in decisions CSV row `T0022`: `keep` | `replace_with_canonical` | `replace_custom`

### T0023 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter06.tex:567`
- Observed: `macrophage`
- Default action: `keep`
- Context: ... ting to be discovered like chemical elements. I'm claiming that they are stably discoverable because mechanisms make them reliable targets of inquiry. The category \term{noun} is real in the same sense that the category \term{[[macrophage]]} is real: not because there is an essence that defines it, but because mechanisms of production and transmission~-- genetic, developmental, and functional for macrophages; cognitive, social, and transmission-level for no ...
- Review in decisions CSV row `T0023`: `keep` | `replace_with_canonical` | `replace_custom`

### T0024 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:207`
- Observed: `Aspect`
- Canonical: `aspect`
- Suggested replacement: `aspect`
- Default action: `replace_with_canonical`
- Context: ... ble once you attend to the distributional structure~-- lexical bias, tense context, morphological cues~-- rather than the semantic essence. This separation reveals that the category and the mechanism need not coincide. \term{[[Aspect]]} is a useful label picking out a real pattern, but the psychological reality of that pattern may be a network of cue--outcome associations, not a represented binary. The mechanism lives below the category; the projectibi ...
- Review in decisions CSV row `T0024`: `keep` | `replace_with_canonical` | `replace_custom`

### T0025 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:272`
- Observed: `proper names`
- Canonical: `proper name`
- Suggested replacement: `proper name`
- Default action: `replace_with_canonical`
- Context: ... oses. \subsection{Proper nouns and [[proper names]]} \label{sec:7:proper-nouns-names} Linguistics has its own tomatoes. Consider the distinction between \term{proper noun} and \term{proper name}. A semanticist works with \term{proper names}: expressions that refer directly to individuals without descriptive content, that are rigid designators (picking out the same individual across possible worlds), and that create referential opacity (\enquote{Lois believ ...
- Review in decisions CSV row `T0025`: `keep` | `replace_with_canonical` | `replace_custom`

### T0026 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:274`
- Observed: `proper nouns`
- Canonical: `proper noun`
- Suggested replacement: `proper noun`
- Default action: `replace_with_canonical`
- Context: ... These properties cluster because of the cognitive and communicative functions names serve: tracking individuals across contexts requires stable reference without shifting descriptive content. A syntactician works with \term{[[proper nouns]]}: words that head nominal projections, resist articles in certain languages, trigger particular agreement patterns, and fill argument slots. These properties cluster because of distributional pressures: words that behave ...
- Review in decisions CSV row `T0026`: `keep` | `replace_with_canonical` | `replace_custom`

### T0027 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:299`
- Observed: `constituent`
- Default action: `keep`
- Context: ... subsection{Constituency and dependency} \label{sec:7:constituency-dependency} The same logic applies to rival syntactic formalisms. Phrase-structure grammars, like \textit{CGEL}'s, represent sentences as hierarchies of \term{[[constituent]]}s~-- noun phrases, verb phrases, clauses nested inside each other. Dependency grammars, like \citeauthor{gibson2025}'s (\citeyear{gibson2025}), represent sentences as networks of \term{dependency relation}s~-- subject-of ...
- Review in decisions CSV row `T0027`: `keep` | `replace_with_canonical` | `replace_custom`

### T0028 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:299`
- Observed: `dependency relation`
- Default action: `keep`
- Context: ... nces as hierarchies of \term{constituent}s~-- noun phrases, verb phrases, clauses nested inside each other. Dependency grammars, like \citeauthor{gibson2025}'s (\citeyear{gibson2025}), represent sentences as networks of \term{[[dependency relation]]}s~-- subject-of, object-of, modifier-of~-- linking words directly without intermediate phrasal nodes. The rivalry is old, but the maintenance view dissolves the \enquote{which is \emph{real}?} framing. Both formalisms t ...
- Review in decisions CSV row `T0028`: `keep` | `replace_with_canonical` | `replace_custom`

### T0029 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:309`
- Observed: `poetic naturalism`
- Default action: `keep`
- Context: ... s sentence hard?} needs dependency. Neither formalism is epiphenomenal; each tracks mechanisms relevant to its questions. The debate is dissolved, not decided. This fits naturally with what \textcite{carroll2016} calls \term{[[poetic naturalism]]}: a sparse naturalistic metaphysics paired with a permission structure for higher-level vocabularies. Poetic naturalism tells you when it's licit to treat a vocabulary as tracking something real~-- when the description c ...
- Review in decisions CSV row `T0029`: `keep` | `replace_with_canonical` | `replace_custom`

### T0030 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:332`
- Observed: `Proper name`
- Canonical: `proper name`
- Suggested replacement: `proper name`
- Default action: `replace_with_canonical`
- Context: ... esn't project for grammatical inferences. The same extension~-- red things, warm-coloured things~-- supports robust categorisation in one domain and fails to support it in another. This extends the proper-name pattern. \term{[[Proper name]]} projects for semantic purposes; \term{proper noun} projects for syntactic purposes. \term{Warm-coloured} projects for ecological purposes; nothing projects it for grammatical purposes~-- so nothing grammaticalises. The ...
- Review in decisions CSV row `T0030`: `keep` | `replace_with_canonical` | `replace_custom`

### T0031 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:332`
- Observed: `Warm-coloured`
- Default action: `keep`
- Context: ... ports robust categorisation in one domain and fails to support it in another. This extends the proper-name pattern. \term{Proper name} projects for semantic purposes; \term{proper noun} projects for syntactic purposes. \term{[[Warm-coloured]]} projects for ecological purposes; nothing projects it for grammatical purposes~-- so nothing grammaticalises. The framework doesn't multiply categories recklessly; it asks what cluster of properties is maintained by wha ...
- Review in decisions CSV row `T0031`: `keep` | `replace_with_canonical` | `replace_custom`

### T0032 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:342`
- Observed: `Definiteness`
- Canonical: `definiteness`
- Suggested replacement: `definiteness`
- Default action: `replace_with_canonical`
- Context: ... ers are maintained by different mechanisms and project for different analytical purposes. Chapter~\ref{ch:definiteness-and-deitality} shows that definiteness and deitality are distinct HPCs with overlapping extensions. \term{[[Definiteness]]}~-- identifiability, uniqueness, familiarity~-- projects for semantic purposes. \term{Deitality}~-- the morphosyntactic properties that pattern with definite articles~-- projects for syntactic purposes. The literature's ...
- Review in decisions CSV row `T0032`: `keep` | `replace_with_canonical` | `replace_custom`

### T0033 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:342`
- Observed: `Deitality`
- Canonical: `deitality`
- Suggested replacement: `deitality`
- Default action: `replace_with_canonical`
- Context: ... \ref{ch:definiteness-and-deitality} shows that definiteness and deitality are distinct HPCs with overlapping extensions. \term{Definiteness}~-- identifiability, uniqueness, familiarity~-- projects for semantic purposes. \term{[[Deitality]]}~-- the morphosyntactic properties that pattern with definite articles~-- projects for syntactic purposes. The literature's confusion about \enquote{weak definites} and \enquote{generic definites} arises from treating th ...
- Review in decisions CSV row `T0033`: `keep` | `replace_with_canonical` | `replace_custom`

### T0034 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:387`
- Observed: `Green`
- Default action: `keep`
- Context: ... rcle. A habit isn't self-grounding; it's sustained by something. The stream's habit of flowing in a particular channel persists not because it has flowed there before but because water, gravity, and geology maintain it. \term{[[Green]]} is projectible not because it has been projected (Goodman's bootstrap) but because mechanisms sustain the would-be: chromium traces interact with light in stable ways; a visual system tuned by selection detects the refl ...
- Review in decisions CSV row `T0034`: `keep` | `replace_with_canonical` | `replace_custom`

### T0035 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter07.tex:389`
- Observed: `Noun`
- Canonical: `noun`
- Suggested replacement: `noun`
- Default action: `replace_with_canonical`
- Context: ... s that would make them switch from green to blue at time $t$. Projectibility tracks mechanism, not predicational habit. Goodman saw the habit but not what sustains it. For linguistic categories, the same logic applies. \term{[[Noun]]} is projectible because mechanisms like acquisition, entrenchment, and functional pressure keep nominal properties clustering together. A pseudo-category like \mention{nerboun} (noun if acquired before age 5, verb otherw ...
- Review in decisions CSV row `T0035`: `keep` | `replace_with_canonical` | `replace_custom`

### T0036 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:136`
- Observed: `English Morphosyntax`
- Default action: `keep`
- Context: ... \subsection{The grain question} One more trap before the case studies: the problem of grain. Even when we have genuine HPCs, we often group them into larger systems labelled \enquote{Grammar} or \enquote{Language.} Is \term{[[English Morphosyntax]]} an HPC kind? The temptation is to say yes. It's stable, it's learned, it's maintained. But this is the \term{Madagascar fallacy}. Biological species are the paradigmatic HPC kinds. \textit{Lemur catta} (the ring-tailed ...
- Review in decisions CSV row `T0036`: `keep` | `replace_with_canonical` | `replace_custom`

### T0037 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:140`
- Observed: `English`
- Default action: `keep`
- Context: ... he components~-- constructions, lexemes, phoneme contrasts, sometimes families or paradigms~-- not the grammar as a whole. The failure modes below apply at that level: we ask whether \term{adverb} is a kind, not whether \term{[[English]]} is. Section~\ref{sec:8:grain} returns to this question; for now, the point is that grain matters. A category can be too thin, too fat, too negative~-- or simply at the wrong level of analysis. \section{Thin clustering ...
- Review in decisions CSV row `T0037`: `keep` | `replace_with_canonical` | `replace_custom`

### T0038 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:148`
- Observed: `thin`
- Default action: `keep`
- Context: ... tters. A category can be too [[thin]], too fat, too negative~-- or simply at the wrong level of analysis. \section{Thin clustering: The smoke ring} \label{sec:8:thin} The first pattern is the class that barely exists. A \term{thin} class is one where the signal exists~-- speakers recognize it, linguists name it~-- but the property cluster is ghostly. There is no robust homeostatic loop maintaining it. It's a \enquote{smoke ring}: it has structure, ...
- Review in decisions CSV row `T0038`: `keep` | `replace_with_canonical` | `replace_custom`

### T0039 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:197`
- Observed: `fat`
- Default action: `keep`
- Context: ... s. We have a label without a kind. \section{Fat clustering: The wastebasket} \label{sec:8:[[fat]]} The second pattern is the opposite of thinness: not too little mechanism, but too many pulling in different directions. A \term{fat} class is a label that lumps distinct causal clusters into a single bin. The analyst treats them as one~-- usually for \enquote{wastebasket} reasons, where the class is defined residually: \enquote{everything that isn't ...
- Review in decisions CSV row `T0039`: `keep` | `replace_with_canonical` | `replace_custom`

### T0040 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:205`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... re robust than their neuroscientific counterparts~-- but the fat-class failure mode remains a live possibility wherever the label's institutional momentum outpaces its mechanistic grounding. \subsection{Case study: The \term{[[Adverb]]}} Try this: \mention{She ran quickly.} Now try: *\mention{She ran very.} \mention{Very} has never gone jogging. Both \mention{quickly} and \mention{very} are adverbs~-- the same part of speech, according to every gramma ...
- Review in decisions CSV row `T0040`: `keep` | `replace_with_canonical` | `replace_custom`

### T0041 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:209`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... ly} and \mention{very} are adverbs~-- the same part of speech, according to every grammar textbook. Yet one sentence is grammatical and the other isn't. What went wrong? The answer reveals everything about fat classes. \term{[[Adverb]]} doesn't name a natural kind; it names a filing cabinet where grammarians store everything that modifies but isn't an adjective. The items in the drawer have almost nothing in common~-- and when we try to generalise acro ...
- Review in decisions CSV row `T0041`: `keep` | `replace_with_canonical` | `replace_custom`

### T0042 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:233`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... rything. If you need every word to belong to exactly one part of speech, and you've already defined noun, verb, adjective, preposition, determiner, and conjunction, then \enquote{everything left over} must go somewhere. \term{[[Adverb]]} is that somewhere. The label groups items that are \enquote{close} only in the analyst's filing system. In terms of the mechanisms that maintain them, manner adverbs and degree words are far apart. The label is a conven ...
- Review in decisions CSV row `T0042`: `keep` | `replace_with_canonical` | `replace_custom`

### T0043 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:235`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... In terms of the mechanisms that maintain them, manner adverbs and degree words are far apart. The label is a convenience, not a kind. The maintenance view gives clear guidance when you diagnose a fat class: decompose. \term{[[Adverb]]} isn't an HPC. But the genuine clusters lurking inside it~-- the cluster around \mention{quickly}, the cluster around \mention{very}, the cluster around \mention{thus}, each maintained by its own braid of mechanisms~-- m ...
- Review in decisions CSV row `T0043`: `keep` | `replace_with_canonical` | `replace_custom`

### T0044 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:251`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... each for the category with the weakest positive profile: the one defined largely by exclusion, the one designed to mop up words that are neither nominal, verbal, adjectival, nor prepositional in their most typical uses. \term{[[Adverb]]} is, in this sense, the grammar's \enquote{default box} for items that refuse a clean fit. Seen this way, \mention{otherwise} isn't a quirky edge case that embarrasses an otherwise sound taxonomy. it's a demonstration c ...
- Review in decisions CSV row `T0044`: `keep` | `replace_with_canonical` | `replace_custom`

### T0045 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:260`
- Observed: `negative`
- Default action: `keep`
- Context: ... basket category makes when you ask it to behave like a kind. \section{Negative classes: The complement class} \label{sec:8:[[negative]]} The third pattern is the most categorical: the category defined by what it isn't. A \term{negative} class is a complement class: \enquote{everything that isn't X.} In set theory, complements are well-behaved~-- the complement of a set is precisely defined. In causal mechanism terms, they're incoherent. There is no suc ...
- Review in decisions CSV row `T0045`: `keep` | `replace_with_canonical` | `replace_custom`

### T0046 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:279`
- Observed: `negative class`
- Default action: `keep`
- Context: ... ibiting extraction from the left branch of an NP. But look for the mechanism. Is there a \enquote{Left Branch Guard} in the parser? A specific genetic instruction? The HPC view suggests a different diagnosis: this is a \term{[[negative class]]}~-- a gap of abstinence. English speakers don't have a rule against (\ref{ex:lbe-b}); they simply have a massive prior probability of zero for it because they never encounter it. Why is the gap so stable? \textcite{reyn ...
- Review in decisions CSV row `T0046`: `keep` | `replace_with_canonical` | `replace_custom`

### T0047 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:281`
- Observed: `competitor strategies`
- Default action: `keep`
- Context: ... rule against (\ref{ex:lbe-b}); they simply have a massive prior probability of zero for it because they never encounter it. Why is the gap so stable? \textcite{reynolds2026lbe} argues it's maintained by the density of \term{[[competitor strategies]]} (what we might call \enquote{workarounds}).\footnote{The Python scripts for the analyses in this book are available at \url{https://github.com/BrettRey/hpc-book/tree/main/code}.} If you want to question a possessor, you ...
- Review in decisions CSV row `T0047`: `keep` | `replace_with_canonical` | `replace_custom`

### T0048 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:329`
- Observed: `participial adjunct`
- Default action: `keep`
- Context: ... ans recognizing that the term is a taxonomic convenience, not a natural kind. The genuine HPCs are the specific constructions: \term{infinitival complement}, \term{perfect construction}, \term{progressive construction}, \term{[[participial adjunct]]}. Each has its own cluster, its own mechanisms, its own projectibility. The umbrella term names a residual class, not a causal unity. \section{The grain of analysis} \label{sec:8:grain} The grain question previewed in ...
- Review in decisions CSV row `T0048`: `keep` | `replace_with_canonical` | `replace_custom`

### T0049 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:363`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... set aside. Thin patterns don't need theoretical treatment because they lack the causal structure that would make treatment meaningful. Document them, but don't reify them. \textbf{When you diagnose fatness:} Decompose. \term{[[Adverb]]} isn't a kind; the clusters inside it~-- around \mention{quickly}, around \mention{very}, around \mention{thus}~-- might be, each maintained by its own mechanism braid. The genuine HPCs are lurking inside the wastebasket ...
- Review in decisions CSV row `T0049`: `keep` | `replace_with_canonical` | `replace_custom`

### T0050 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:371`
- Observed: `Subject`
- Canonical: `subject`
- Suggested replacement: `subject`
- Default action: `replace_with_canonical`
- Context: ... ually have mechanisms to maintain them. The negative label organizes your files; it doesn't track causal structure. \subsection{For typology} The framework reframes cross-linguistic comparison. We stop asking whether \term{[[Subject]]} is a universal category~-- a question that invites endless definitional dispute. Instead, we ask: is the category \term{Subject} in Language $L$ maintained by the same mechanisms as in Language $M$? Usually, the answer ...
- Review in decisions CSV row `T0050`: `keep` | `replace_with_canonical` | `replace_custom`

### T0051 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:371`
- Observed: `Subject`
- Canonical: `subject`
- Suggested replacement: `subject`
- Default action: `replace_with_canonical`
- Context: ... For typology} The framework reframes cross-linguistic comparison. We stop asking whether \term{[[Subject]]} is a universal category~-- a question that invites endless definitional dispute. Instead, we ask: is the category \term{Subject} in Language $L$ maintained by the same mechanisms as in Language $M$? Usually, the answer is no. English subjects are maintained by agreement morphology, fixed word order, and nominative case marking. Tagalog \enquote{ ...
- Review in decisions CSV row `T0051`: `keep` | `replace_with_canonical` | `replace_custom`

### T0052 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:377`
- Observed: `descriptive categories`
- Default action: `keep`
- Context: ... f the kind, and to test cross-linguistic identity, you need to show shared mechanisms, not just shared features. \citet{haspelmath2010} makes a related point with his distinction between \term{comparative concept}s and \term{[[descriptive categories]]}. Comparative concepts are analyst's tools~-- definitions constructed for cross-linguistic comparison. Descriptive categories are language-specific~-- the actual clusters maintained in particular speech communities. The ...
- Review in decisions CSV row `T0052`: `keep` | `replace_with_canonical` | `replace_custom`

### T0053 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter08.tex:379`
- Observed: `naturalised`
- Default action: `keep`
- Context: ... -- but only if they pass the diagnostics in that particular language. Cross-linguistic \enquote{sameness} is a claim about convergent mechanisms, not shared essence. That said, some \term{comparative concept}s may earn \term{[[naturalised]]} status when independent languages converge on similar patterns through similar mechanisms~-- the way camera eyes evolved independently in vertebrates and cephalopods. Naturalization is defeasible: it requires explicit m ...
- Review in decisions CSV row `T0053`: `keep` | `replace_with_canonical` | `replace_custom`

### T0054 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:55`
- Observed: `edge detection`
- Default action: `keep`
- Context: ... er} Descriptively, the cluster looks like a set of logical entailments. Explanatorily, it's maintained by perceptual and cognitive mechanisms that operate across modalities~-- and, strikingly, across species. Consider \term{[[edge detection]]}. Visual object perception depends on detecting boundaries. The visual cortex uses orientation-selective cells, Gabor-like filters, and mid-level grouping principles to extract edges from the visual field. These edges ar ...
- Review in decisions CSV row `T0054`: `keep` | `replace_with_canonical` | `replace_custom`

### T0055 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:55`
- Observed: `object files`
- Default action: `keep`
- Context: ... tation-selective cells, Gabor-like filters, and mid-level grouping principles to extract edges from the visual field. These edges are then grouped into coherent object representations~-- what \citet{kahneman1992} called \term{[[object files]]}: temporary episodic representations that bind features to locations and track objects across time. But edge detection isn't vision-specific. Blind echolocators produce tongue clicks and interpret the returning echoes t ...
- Review in decisions CSV row `T0055`: `keep` | `replace_with_canonical` | `replace_custom`

### T0056 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:63`
- Observed: `core knowledge`
- Default action: `keep`
- Context: ... ns, making it a plausible semantic anchor for grammatical reinforcement. And so, such mechanisms are ancient. \citet{spelke2007} argues\footnote{Or should that be \mention{argue}?} that human infants are equipped with \term{[[core knowledge]]} systems for objects~-- systems that operate from the first months of life. Infants as young as four months perceive objects as cohesive (parts move together), bounded (edges mark identity), and continuous (objects persi ...
- Review in decisions CSV row `T0056`: `keep` | `replace_with_canonical` | `replace_custom`

### T0057 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:65`
- Observed: `Cross-modal integration`
- Default action: `keep`
- Context: ... occlusion). These are the same properties that define the individuation cluster in adult conceptual systems. The mechanisms that maintain individuation aren't learned from scratch; they're built on an early foundation. \term{[[Cross-modal integration]]} reinforces the pattern. Object individuation isn't locked to a single sensory channel. When you set a cup down and see and hear it alighting, you don't perceive thre entities~-- one tactile, one visual, one auditory. Yo ...
- Review in decisions CSV row `T0057`: `keep` | `replace_with_canonical` | `replace_custom`

### T0058 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:129`
- Observed: `processing`
- Default action: `keep`
- Context: ... Make sure this cashes out in Ch~13 or is removed.} \subsection{Multi-timescale maintenance} The bidirectional inference mechanism operates at multiple timescales, each reinforcing the others. At the fast timescale of \term{[[processing]]} (milliseconds), every time a speaker produces or comprehends a count frame, the form--meaning link is activated. \mention{Three dogs} primes the expectation of individuation; individuation primes the expectation of coun ...
- Review in decisions CSV row `T0058`: `keep` | `replace_with_canonical` | `replace_custom`

### T0059 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:129`
- Observed: `error signals`
- Default action: `keep`
- Context: ... . \mention{Three dogs} primes the expectation of individuation; individuation primes the expectation of count morphosyntax. Mismatches~-- \ungram\mention{three furnitures}, say~-- incur processing costs. These costs are \term{[[error signals]]} (Chapter~\ref{ch:stabilizers}): they scream that the coupling has been violated, providing the negative feedback that keeps the basin's edges steep. They feel wrong because they violate entrenched expectations. At the ...
- Review in decisions CSV row `T0059`: `keep` | `replace_with_canonical` | `replace_custom`

### T0060 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:184`
- Observed: `Singular forms`
- Default action: `keep`
- Context: ... ng a noun that reverses the pattern~-- tight without loose~-- would challenge the account. The empirical record, as far as I can determine, contains no such case. Here's the hierarchy, ordered from tightest to loosest. \term{[[Singular forms]]} and \mention{a(n)} are the strictest, requiring the identification of exactly one atomic unit. \term{Low cardinals} like \mention{three} and \mention{five} are similarly precise, requiring exact enumeration. Relaxing th ...
- Review in decisions CSV row `T0060`: `keep` | `replace_with_canonical` | `replace_custom`

### T0061 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:184`
- Observed: `Low cardinals`
- Default action: `keep`
- Context: ... ar as I can determine, contains no such case. Here's the hierarchy, ordered from tightest to loosest. \term{Singular forms} and \mention{a(n)} are the strictest, requiring the identification of exactly one atomic unit. \term{[[Low cardinals]]} like \mention{three} and \mention{five} are similarly precise, requiring exact enumeration. Relaxing the tolerance slightly, \mention{several} requires multiple units but permits approximate quantity. \term{Distributive ...
- Review in decisions CSV row `T0061`: `keep` | `replace_with_canonical` | `replace_custom`

### T0062 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:184`
- Observed: `Distributives`
- Default action: `keep`
- Context: ... erm{Low cardinals} like \mention{three} and \mention{five} are similarly precise, requiring exact enumeration. Relaxing the tolerance slightly, \mention{several} requires multiple units but permits approximate quantity. \term{[[Distributives]]} like \mention{each} require discreteness but not enumeration. Further down, \mention{many} and \mention{few} require only relative magnitude assessment. \term{High round numerals} often function as approximate measures ...
- Review in decisions CSV row `T0062`: `keep` | `replace_with_canonical` | `replace_custom`

### T0063 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:184`
- Observed: `High round numerals`
- Default action: `keep`
- Context: ... tiple units but permits approximate quantity. \term{Distributives} like \mention{each} require discreteness but not enumeration. Further down, \mention{many} and \mention{few} require only relative magnitude assessment. \term{[[High round numerals]]} often function as approximate measures rather than exact counts. Finally, \term{plural agreement} is the most permissive, requiring only a non-singular construal. A noun that loses \mention{several} will already have l ...
- Review in decisions CSV row `T0063`: `keep` | `replace_with_canonical` | `replace_custom`

### T0064 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:184`
- Observed: `plural agreement`
- Default action: `keep`
- Context: ... teness but not enumeration. Further down, \mention{many} and \mention{few} require only relative magnitude assessment. \term{High round numerals} often function as approximate measures rather than exact counts. Finally, \term{[[plural agreement]]} is the most permissive, requiring only a non-singular construal. A noun that loses \mention{several} will already have lost \mention{a(n)} and low cardinals. A noun that retains only plural agreement will have lost eve ...
- Review in decisions CSV row `T0064`: `keep` | `replace_with_canonical` | `replace_custom`

### T0065 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:351`
- Observed: `Bidirectional inference`
- Canonical: `bidirectional inference`
- Suggested replacement: `bidirectional inference`
- Default action: `replace_with_canonical`
- Context: ... erion asks: is the clustering maintained by causal mechanisms, or is it merely a surface pattern that might scatter under perturbation? We've identified the mechanisms: We have identified five interlocking mechanisms. \term{[[Bidirectional inference]]} couples morphosyntax to individuation through a shared semantic variable. \term{Acquisition} transmits this coupling as a unit, as children overgeneralise from one property to the others. \term{Entrenchment} preserves h ...
- Review in decisions CSV row `T0065`: `keep` | `replace_with_canonical` | `replace_custom`

### T0066 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:351`
- Observed: `Acquisition`
- Canonical: `acquisition`
- Suggested replacement: `acquisition`
- Default action: `replace_with_canonical`
- Context: ... ht scatter under perturbation? We've identified the mechanisms: We have identified five interlocking mechanisms. \term{Bidirectional inference} couples morphosyntax to individuation through a shared semantic variable. \term{[[Acquisition]]} transmits this coupling as a unit, as children overgeneralise from one property to the others. \term{Entrenchment} preserves high-frequency patterns as chunks. \term{Institutional norms} stabilize the distribution at th ...
- Review in decisions CSV row `T0066`: `keep` | `replace_with_canonical` | `replace_custom`

### T0067 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:351`
- Observed: `Entrenchment`
- Canonical: `entrenchment`
- Suggested replacement: `entrenchment`
- Default action: `replace_with_canonical`
- Context: ... \term{Bidirectional inference} couples morphosyntax to individuation through a shared semantic variable. \term{Acquisition} transmits this coupling as a unit, as children overgeneralise from one property to the others. \term{[[Entrenchment]]} preserves high-frequency patterns as chunks. \term{Institutional norms} stabilize the distribution at the community level. Finally, \term{functional anchoring} bleeds pressure from intermediate cases like \mention{cattl ...
- Review in decisions CSV row `T0067`: `keep` | `replace_with_canonical` | `replace_custom`

### T0068 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:351`
- Observed: `Institutional norms`
- Default action: `keep`
- Context: ... tion through a shared semantic variable. \term{Acquisition} transmits this coupling as a unit, as children overgeneralise from one property to the others. \term{Entrenchment} preserves high-frequency patterns as chunks. \term{[[Institutional norms]]} stabilize the distribution at the community level. Finally, \term{functional anchoring} bleeds pressure from intermediate cases like \mention{cattle}, allowing them to persist without regularising. This is robust homeo ...
- Review in decisions CSV row `T0068`: `keep` | `replace_with_canonical` | `replace_custom`

### T0069 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:383`
- Observed: `ablation by perturbation`
- Default action: `keep`
- Context: ... ely on natural experiments: languages that \enquote{perturb} the system by packaging the relevant cues differently (see \textcite{doetjes2012} for a typological overview). These cross-linguistic comparisons function as \term{[[ablation by perturbation]]}. Languages don't typically delete a mechanism entirely; they reallocate or reweight it. A caution is required: real cross-linguistic work is messy. Unlike a controlled lab ablation, comparing languages involves multiple ...
- Review in decisions CSV row `T0069`: `keep` | `replace_with_canonical` | `replace_custom`

### T0070 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:393`
- Observed: `collective`
- Default action: `keep`
- Context: ... s count syntax. Welsh offers the evidence. For a large class of nouns~-- specifically those denoting things that naturally occur in groups (animals, vegetables, small objects)~-- the morphologically simple base form is \term{[[collective]]} (conceptually plural). To refer to a single unit, speakers must add a \term{singulative} suffix. For example, \mention{\textit{adar}} means `birds' (collective); \mention{\textit{aderyn}} means `a bird' (singulative). ...
- Review in decisions CSV row `T0070`: `keep` | `replace_with_canonical` | `replace_custom`

### T0071 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:403`
- Observed: `reallocation`
- Default action: `keep`
- Context: ... argumental use. What happens if we remove this reinforcement? The prediction is that the count cluster should either disperse or naturally dissolve, or the functional load should shift to a new location. One outcome is \term{[[reallocation]]}, as seen in Mandarin Chinese. Mandarin lacks obligatory noun number inflection. Without the constant \mention{book}/\mention{books} pulse trained by morphology, the inference engine builds the cluster differently. The f ...
- Review in decisions CSV row `T0071`: `keep` | `replace_with_canonical` | `replace_custom`

### T0072 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:405`
- Observed: `weakening`
- Default action: `keep`
- Context: ... general} classifiers (like \mention{\textit{gè}}) tolerate vague individuation, while specific classifiers demand precise shape properties. The mechanism remains, but the locus of coupling has moved. Another outcome is \term{[[weakening]]}, as argued for Halkomelem (Salish). \textcite{wiltschko2008} argues that in this language, plural marking isn't a functional head but an optional modifier. Speakers can say \mention{three boy} or \mention{three boys} wi ...
- Review in decisions CSV row `T0072`: `keep` | `replace_with_canonical` | `replace_custom`

### T0073 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:407`
- Observed: `null case`
- Default action: `keep`
- Context: ... komelem makes the decision optional. The prediction here is lower projectibility: without the obligatory morphological pulse, the \enquote{count} category should be less cohesive~-- and it's. A third possibility is the \term{[[null case]]}. Some languages are claimed to lack both obligatory number and obligatory classifiers (e.g., Yoruba, Indonesian). These act as the control group. A pure-mechanism view makes a risky prediction: in the absence of \textit ...
- Review in decisions CSV row `T0073`: `keep` | `replace_with_canonical` | `replace_custom`

### T0074 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:407`
- Observed: `transnumeral`
- Default action: `keep`
- Context: ... (e.g., Yoruba, Indonesian). These act as the control group. A pure-mechanism view makes a risky prediction: in the absence of \textit{any} reinforcing mechanism, there should be no rigid count/mass HPC. Nouns should be \term{[[transnumeral]]} (neutral), and semantic boundaries shouldn't predict grammatical behaviour. If these languages turned out to have a rigid, English-style count cluster without the mechanism, the HPC account would be falsified. The disc ...
- Review in decisions CSV row `T0074`: `keep` | `replace_with_canonical` | `replace_custom`

### T0075 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter09.tex:419`
- Observed: `negative projectibility`
- Default action: `keep`
- Context: ... ed. The result is a reordered hierarchy. Because the \enquote{tight} property (numerals) no longer demands high-precision atomic individuation, it becomes \enquote{looser} than it's in English. The failure mode here is \term{[[negative projectibility]]}: the inference \enquote{Accepts Numerals $\to$ Is Atomic Object} becomes unreliable. The disconfirmation condition is simple: if Yudja speakers processed \enquote{three blood} as strictly atomic (coercing it to \enquot ...
- Review in decisions CSV row `T0075`: `keep` | `replace_with_canonical` | `replace_custom`

### T0076 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:58`
- Observed: `deitality cluster`
- Default action: `keep`
- Context: ... he capacity to be picked up by a pronoun~-- is a downstream discourse affordance, not a core property. On the morphosyntactic side sits what I'll call the \term{form cluster}~-- or, in terminology we'll earn later, the \term{[[deitality cluster]]}. These are the grammatical properties that travel together in English determiners: resistance to existential \mention{there} under neutral prosody, eligibility as the complement of partitive \mention{of}, and suitabilit ...
- Review in decisions CSV row `T0076`: `keep` | `replace_with_canonical` | `replace_custom`

### T0077 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:361`
- Observed: `proper nouns`
- Canonical: `proper noun`
- Suggested replacement: `proper noun`
- Default action: `replace_with_canonical`
- Context: ... proper function (signalling identifiability of an individual) isn't performed; what persists is the form-cluster profile and the slot for domain specification. \subsection{Proper names} Proper names (as distinct from \term{[[proper nouns]]}, Chapter~\ref{ch:lexical-categories}) look like a failure of marking in English. \mention{Kim} and \mention{London} are semantically definite~-- they identify unique, familiar referents~-- but they typically lack form-c ...
- Review in decisions CSV row `T0077`: `keep` | `replace_with_canonical` | `replace_custom`

### T0078 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:363`
- Observed: `indexical anchoring`
- Default action: `keep`
- Context: ... naphoric recoverability) without the form-cluster properties. They don't resist existential pivots: \mention{There's a Kim here to see you} is natural. They don't license partitives in the standard way. Or rather, their \term{[[indexical anchoring]]} (Chapter~\ref{ch:stabilizers}) is achieved directly through the label, rendering the deital pointer redundant. The clusters have decoupled in the opposite direction from weak definites. Where weak definites have form w ...
- Review in decisions CSV row `T0078`: `keep` | `replace_with_canonical` | `replace_custom`

### T0079 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:388`
- Observed: `dissociated`
- Default action: `keep`
- Context: ... , it can be topicalized, it can be presupposed. The form cluster supports induction too: knowing a determiner is form-cluster lets you predict structural behaviour across contexts. Most importantly, the predictions are \term{[[dissociated]]}. You can know a noun phrase's form-cluster status without knowing its definiteness status~-- and the predictions you make will differ. Weak definites are form-cluster but not definiteness-cluster; proper names are defin ...
- Review in decisions CSV row `T0079`: `keep` | `replace_with_canonical` | `replace_custom`

### T0080 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:419`
- Observed: `deital`
- Default action: `keep`
- Context: ... term{[[deital]]ity} as a diagnostic remedy. The term derives from the deictic origins of the cluster: demonstratives grammaticalize into articles, and the distributional profile reflects that deictic source. A determiner is \term{deital} if it shows the form-cluster properties; it's \term{definite} if it contributes definiteness-cluster semantics. The term is ugly~-- methodologically ugly. If it sounds like a minor villain in a low-budget sci-fi, that' ...
- Review in decisions CSV row `T0080`: `keep` | `replace_with_canonical` | `replace_custom`

### T0081 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:419`
- Observed: `definite`
- Default action: `keep`
- Context: ... m the deictic origins of the cluster: demonstratives grammaticalize into articles, and the distributional profile reflects that deictic source. A determiner is \term{deital} if it shows the form-cluster properties; it's \term{[[definite]]} if it contributes definiteness-cluster semantics. The term is ugly~-- methodologically ugly. If it sounds like a minor villain in a low-budget sci-fi, that's partly the point. Its unfamiliarity forces a break with the ...
- Review in decisions CSV row `T0081`: `keep` | `replace_with_canonical` | `replace_custom`

### T0082 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter10.tex:434`
- Observed: `architecture`
- Default action: `keep`
- Context: ... he specific determiners~-- is English-specific. It reflects the grammaticalization history of English demonstratives, the selectional restrictions of English constructions, the conventions of English discourse. But the \term{[[architecture]]} generalizes \citep{lyons1999}. Languages with demonstrative-derived articles (French \mention{le}, German \mention{der}, Greek \mention{o}) show similar clusters: partitive restrictions, information-structural constrain ...
- Review in decisions CSV row `T0082`: `keep` | `replace_with_canonical` | `replace_custom`

### T0083 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:46`
- Observed: `Noun`
- Canonical: `noun`
- Suggested replacement: `noun`
- Default action: `replace_with_canonical`
- Context: ... ions that keep recurring across the linguistic hierarchy, each with its own diagnostic signature: \begin{itemize} \item \textbf{Robust categories} where multiple mechanisms converge on a thick, projectible cluster. \term{[[Noun]]} and \term{verb} are the paradigm cases~-- the skeletal categories that recur across languages because the discourse tasks they serve (reference and predication) demand them. \item \textbf{Thin classes} where the clu ...
- Review in decisions CSV row `T0083`: `keep` | `replace_with_canonical` | `replace_custom`

### T0084 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:47`
- Observed: `Adjective`
- Canonical: `adjective`
- Suggested replacement: `adjective`
- Default action: `replace_with_canonical`
- Context: ... recur across languages because the discourse tasks they serve (reference and predication) demand them. \item \textbf{Thin classes} where the clustering is real but the mechanisms are fewer and less tightly coupled. \term{[[Adjective]]} is the pivotal example: a category in English, with genuine distributional coherence, but one that varies dramatically across languages in its independence and scope~-- a category in some languages, absent in others. ...
- Review in decisions CSV row `T0084`: `keep` | `replace_with_canonical` | `replace_custom`

### T0085 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:48`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... but one that varies dramatically across languages in its independence and scope~-- a category in some languages, absent in others. \item \textbf{Fat labels} where a single term obscures multiple unrelated clusters. \term{[[Adverb]]} is the classic case~-- what Quirk called \enquote{the dustbin of the parts of speech}, a class with excellent storage capacity and terrible explanatory power~-- a perfectly good drawer, provided you don't mistake it for ...
- Review in decisions CSV row `T0085`: `keep` | `replace_with_canonical` | `replace_custom`

### T0086 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:48`
- Observed: `pronoun`
- Default action: `keep`
- Context: ... irk called \enquote{the dustbin of the parts of speech}, a class with excellent storage capacity and terrible explanatory power~-- a perfectly good drawer, provided you don't mistake it for a theory. And the traditional \term{[[pronoun]]} turns out to be another: a surface-distribution class that masks at least three distinct convergent-evolution stories. \end{itemize} The Wallace epigraph at the head of this chapter is the key. The resemblance of one a ...
- Review in decisions CSV row `T0086`: `keep` | `replace_with_canonical` | `replace_custom`

### T0087 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:87`
- Observed: `skeleton`
- Default action: `keep`
- Context: ... s the signature of a robust HPC~-- not a single causal thread but a cable of independent strands, each sufficient to maintain some clustering, collectively sufficient to maintain it all. The metaphor I want here is the \term{[[skeleton]]}. \citet{zimmer2015} observed that sharks and dolphins look strikingly alike~-- streamlined bodies, dorsal fins, tapered snouts~-- despite having diverged hundreds of millions of years ago. The resemblance isn't ancestry ...
- Review in decisions CSV row `T0087`: `keep` | `replace_with_canonical` | `replace_custom`

### T0088 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:108`
- Observed: `property-concept`
- Default action: `keep`
- Context: ... like Swahili manage with a small closed set of true adjectives and route most property concepts through relative-clause constructions: `a door which is red' rather than `a red door' \citep[e.g.,][]{schadeberg1992}. The \term{[[property-concept]]} role~-- attributing size, age, colour, value to a referent~-- exists in every language. A dedicated lexical category for doing it does not. Dixon's survey makes a further point that matters for the HPC framework. Even ...
- Review in decisions CSV row `T0088`: `keep` | `replace_with_canonical` | `replace_custom`

### T0089 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter11.tex:128`
- Observed: `thin`
- Default action: `keep`
- Context: ... ; the centre holds. That's the [[thin]]-class signature: shared mechanisms at the core, loosening at the margins. A fat class, by contrast, has no shared mechanisms at all~-- only a shared filing convention. This is what a \term{thin} HPC looks like. The clustering is real~-- in English, knowing that something is an adjective lets you predict a great deal of its syntactic behaviour. But the mechanisms maintaining the cluster are fewer and less tightl ...
- Review in decisions CSV row `T0089`: `keep` | `replace_with_canonical` | `replace_custom`

### T0090 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:68`
- Observed: `personal`
- Default action: `keep`
- Context: ... erarchy} %--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- The English pro-form gender system is hierarchically organized (Figure~\ref{fig:12:hierarchy}). At the top level, the distinction is between \term{[[personal]]} and \term{non-personal}. Within personal, there's a further split between \term{epicene} (unmarked for sex) and \term{sexual} (masculine/feminine). Within non-personal, productive subtypes include \term{locative} and \t ...
- Review in decisions CSV row `T0090`: `keep` | `replace_with_canonical` | `replace_custom`

### T0091 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:68`
- Observed: `non-personal`
- Default action: `keep`
- Context: ... - --- --- --- --- --- --- --- --- --- --- --- --- --- --- The English pro-form gender system is hierarchically organized (Figure~\ref{fig:12:hierarchy}). At the top level, the distinction is between \term{personal} and \term{[[non-personal]]}. Within personal, there's a further split between \term{epicene} (unmarked for sex) and \term{sexual} (masculine/feminine). Within non-personal, productive subtypes include \term{locative} and \term{temporal}. \begin{f ...
- Review in decisions CSV row `T0091`: `keep` | `replace_with_canonical` | `replace_custom`

### T0092 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:68`
- Observed: `sexual`
- Default action: `keep`
- Context: ... lly organized (Figure~\ref{fig:12:hierarchy}). At the top level, the distinction is between \term{personal} and \term{non-personal}. Within personal, there's a further split between \term{epicene} (unmarked for sex) and \term{[[sexual]]} (masculine/feminine). Within non-personal, productive subtypes include \term{locative} and \term{temporal}. \begin{figure}[htbp] \centering \begin{tikzpicture}[ level distance=1.2cm, sibling distance=3.5cm, every ...
- Review in decisions CSV row `T0092`: `keep` | `replace_with_canonical` | `replace_custom`

### T0093 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:68`
- Observed: `locative`
- Default action: `keep`
- Context: ... etween \term{personal} and \term{non-personal}. Within personal, there's a further split between \term{epicene} (unmarked for sex) and \term{sexual} (masculine/feminine). Within non-personal, productive subtypes include \term{[[locative]]} and \term{temporal}. \begin{figure}[htbp] \centering \begin{tikzpicture}[ level distance=1.2cm, sibling distance=3.5cm, every node/.style={font=\small\scshape}, edge from parent/.style={draw, thick}, level 1/ ...
- Review in decisions CSV row `T0093`: `keep` | `replace_with_canonical` | `replace_custom`

### T0094 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:68`
- Observed: `temporal`
- Default action: `keep`
- Context: ... l} and \term{non-personal}. Within personal, there's a further split between \term{epicene} (unmarked for sex) and \term{sexual} (masculine/feminine). Within non-personal, productive subtypes include \term{locative} and \term{[[temporal]]}. \begin{figure}[htbp] \centering \begin{tikzpicture}[ level distance=1.2cm, sibling distance=3.5cm, every node/.style={font=\small\scshape}, edge from parent/.style={draw, thick}, level 1/.style={sibling dist ...
- Review in decisions CSV row `T0094`: `keep` | `replace_with_canonical` | `replace_custom`

### T0095 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:253`
- Observed: `chain-internal coherence`
- Default action: `keep`
- Context: ... fully acceptable~-- coherent personal and non-personal chains. Examples (\ref{ex:12:dog-chain-c}) and (\ref{ex:12:dog-chain-d}) are degraded~-- the chain starts in one gender and shifts to another mid-sentence. This is \term{[[chain-internal coherence]]}. The constraint isn't absolute~-- discourse can independently reclassify a designatum (personification, stance shift)~-- but absent such cues, speakers prefer consistency within a reference chain. Attested mixed chains ...
- Review in decisions CSV row `T0095`: `keep` | `replace_with_canonical` | `replace_custom`

### T0096 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:266`
- Observed: `default construal`
- Default action: `keep`
- Context: ... ster~-- Theory of Mind operates on them as a package~-- and that the clustering is cognitively basic and socially consequential. Two kinds of personhood construal should be distinguished. In most cases, personhood is a \term{[[default construal]]}: \mention{the doctor} evokes a person without the speaker doing anything special. In others, personhood is \term{locally imposed}: \mention{Who's a good boy?} addressed to a dog requires active construal work. The maint ...
- Review in decisions CSV row `T0096`: `keep` | `replace_with_canonical` | `replace_custom`

### T0097 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:266`
- Observed: `locally imposed`
- Default action: `keep`
- Context: ... o kinds of personhood construal should be distinguished. In most cases, personhood is a \term{default construal}: \mention{the doctor} evokes a person without the speaker doing anything special. In others, personhood is \term{[[locally imposed]]}: \mention{Who's a good boy?} addressed to a dog requires active construal work. The maintenance story tracks both. Defaults are entrenched through ordinary usage; local impositions require discourse cues and carry inter ...
- Review in decisions CSV row `T0097`: `keep` | `replace_with_canonical` | `replace_custom`

### T0098 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:270`
- Observed: `designatum-driven inference`
- Default action: `keep`
- Context: ... nated slots for personal and non-personal reference. (Pro-form is a semantic grouping; what I'm tracking here is its \emph{realization}~-- the specific forms and where they're licensed.) The two clusters are coupled by \term{[[designatum-driven inference]]}. When speakers produce a pro-form, they signal how they're construing the referent. When hearers process a pro-form, they infer the construal. Form cues construal; construal constrains form. This coupling is the categor ...
- Review in decisions CSV row `T0098`: `keep` | `replace_with_canonical` | `replace_custom`

### T0099 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:279`
- Observed: `Cognitive grounding`
- Default action: `keep`
- Context: ... entrenchment, alignment, transmission. That list was explicitly incomplete; no theory of linguistic kinds can enumerate every stabilizing force. For pro-form gender, at least three domain-specific channels are visible. \term{[[Cognitive grounding]]} explains why acquisition succeeds. As noted above (§\ref{sec:12:coupling-subsec}), the person/non-person boundary is mapped onto a pre-existing conceptual distinction that infants acquire before language begins \autocit ...
- Review in decisions CSV row `T0099`: `keep` | `replace_with_canonical` | `replace_custom`

### T0100 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:281`
- Observed: `Semantic transparency`
- Canonical: `semantic transparency`
- Suggested replacement: `semantic transparency`
- Default action: `replace_with_canonical`
- Context: ... t. The empirical footprint: children should produce personal pro-forms for robots and animals that pass Theory-of-Mind tests, and non-personal pro-forms for entities that fail them, even before they can articulate why. \term{[[Semantic transparency]]} explains why transmission preserves the coupling. The mapping from personhood to pro-form is largely predictable: if you know a referent is construed as a person, you can predict the pro-form inventory it will take. Com ...
- Review in decisions CSV row `T0100`: `keep` | `replace_with_canonical` | `replace_custom`

### T0101 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:281`
- Observed: `learnability filtering`
- Default action: `keep`
- Context: ... such mismatches: the \mention{who}/\mention{which} alternation tracks personhood with high fidelity. This transparency means the system can be reconstructed from limited input~-- what Chapter~\ref{ch:stabilizers} called \term{[[learnability filtering]]}. Children acquiring English don't produce the persistent paradigmatic gender-agreement errors characteristic of antecedent-gender languages, though direct acquisition studies of the \mention{who}/\mention{which} contras ...
- Review in decisions CSV row `T0101`: `keep` | `replace_with_canonical` | `replace_custom`

### T0102 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:283`
- Observed: `Alignment and repair`
- Default action: `keep`
- Context: ... he empirical footprint: novel entities (AI assistants, fictional creatures) should be rapidly and consistently assigned pro-forms once their personhood status is pragmatically established, without explicit instruction. \term{[[Alignment and repair]]} explains why the coupling is enforced in real time. Consider a constructed repair: \begin{quote} A: \mention{The new surgeon started today. Is he any good?}\\ B: \mention{\emph{She}. Dr. Patel's a woman.} \end{quote} ...
- Review in decisions CSV row `T0102`: `keep` | `replace_with_canonical` | `replace_custom`

### T0103 - alias_used
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:290`
- Observed: `interactive alignment`
- Canonical: `alignment`
- Suggested replacement: `alignment`
- Default action: `replace_with_canonical`
- Context: ... ult; misgendering someone with \mention{he} when \mention{she} is appropriate triggers conversational repair \autocite{mcconnell-ginet2014}. This repair pressure operates through what Chapter~\ref{ch:stabilizers} called \term{[[interactive alignment]]}: interlocutors converge on shared construals, and deviations are corrected. The social stakes amplify the mechanism~-- gender isn't just about communication; it's about recognition. The pressure can also work in revers ...
- Review in decisions CSV row `T0103`: `keep` | `replace_with_canonical` | `replace_custom`

### T0104 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:307`
- Observed: `chain coherence`
- Default action: `keep`
- Context: ... ersonal construal, even when the referent is non-human. \mention{The dog who bit me} doesn't just filter for dogs already construed as persons; it \emph{invites} that construal. This is coupling, not selection. Second, \term{[[chain coherence]]}. If gender were just local presupposition, mixed chains (\mention{who... it}) should be as acceptable as any other presupposition shift within discourse. They aren't. The dispreference for mixed chains is a \emph{system ...
- Review in decisions CSV row `T0104`: `keep` | `replace_with_canonical` | `replace_custom`

### T0105 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:309`
- Observed: `boundary cases tracking the same dimension`
- Default action: `keep`
- Context: ... system-level} constraint~-- it tracks construal stability across the chain, not just satisfaction of local presuppositions. That's the signature of a maintained coupling, not a collection of independent filters. Third, \term{[[boundary cases tracking the same dimension]]}. The boundary cases~-- pets, collectives, infants, robots~-- don't scatter randomly. They cluster along the personhood dimension. If each pro-form had independent presuppositional content, we would expect idiosyncratic ...
- Review in decisions CSV row `T0105`: `keep` | `replace_with_canonical` | `replace_custom`

### T0106 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:323`
- Observed: `designatum-driven`
- Default action: `keep`
- Context: ... ffer not just in their inventories but in \emph{what maintains them}. The contrast between English and French illustrates the extremes; German sits between \autocite{corbett1991,audring2009}. English pro-form gender is \term{[[designatum-driven]]}: the form tracks how the speaker construes the referent. The metonymy example in §\ref{sec:12:designatum} showed this~-- \mention{the French fries... she} is possible because the pro-form follows the conceptualized cust ...
- Review in decisions CSV row `T0106`: `keep` | `replace_with_canonical` | `replace_custom`

### T0107 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:325`
- Observed: `antecedent-driven`
- Default action: `keep`
- Context: ... the pro-form follows the conceptualized customer, not the grammatical antecedent. The system is maintained by a live semantic link: form and meaning travel together because the coupling is transparent. French gender is \term{[[antecedent-driven]]}: the pro-form tracks the grammatical gender of the antecedent NP, regardless of the referent's properties. The same metonymy fails: \ea[*]{\label{ex:12:french-fries}\gll \mention{Les} \mention{frites} \mention{attenden ...
- Review in decisions CSV row `T0107`: `keep` | `replace_with_canonical` | `replace_custom`

### T0108 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:332`
- Observed: `pure entrenchment`
- Default action: `keep`
- Context: ... rence]} \z \noindent The speaker can't use masculine \mention{il} to track a male customer if the antecedent \mention{les frites} is grammatically feminine. The form-meaning link is dead: French gender is maintained by \term{[[pure entrenchment]]}~-- item-by-item memorization of arbitrary noun-class assignments, reinforced by NP-internal concord. German is the hybrid. Nouns carry grammatical gender (\mention{der Tisch} `the table', masculine; \mention{die Lampe} ...
- Review in decisions CSV row `T0108`: `keep` | `replace_with_canonical` | `replace_custom`

### T0109 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:343`
- Observed: `maintenance spectrum`
- Default action: `keep`
- Context: ... rent's natural gender, not the noun's grammatical class. German gender is maintained by \emph{two mechanisms in tension}: entrenchment of noun-class assignment, and semantic override in pronominal anaphora. This is the \term{[[maintenance spectrum]]}. At one end, English: semantically transparent, designatum-driven, clustering held together by a live conceptual distinction. At the other end, French: semantically arbitrary, antecedent-driven, clustering held together ...
- Review in decisions CSV row `T0109`: `keep` | `replace_with_canonical` | `replace_custom`

### T0110 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:354`
- Observed: `scope`
- Default action: `keep`
- Context: ... sex-based contrasts. The personhood partition may be cognitively more basic than the particular morphosyntactic systems that realize it. What's distinctive about English isn't the personhood distinction itself but its \term{[[scope]]}. Because English lacks NP-internal gender agreement, the designatum-driven pathway is unconstrained by formal concord. Speakers can shift a referent's construal without generating agreement violations. The \mention{who} ...
- Review in decisions CSV row `T0110`: `keep` | `replace_with_canonical` | `replace_custom`

### T0111 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:435`
- Observed: `constructionally conditioned`
- Default action: `keep`
- Context: ... lippage~-- one driven not by properties of the designatum but by the syntactic construction in which the pro-form appears. In fused determiner-head function, demonstratives aren't simply gender-neutral. Their gender is \term{[[constructionally conditioned]]}: \ea[*]{\label{ex:12:demo-pers-blocked}\mention{She chatted with that.} \hfill [personal blocked]} \z \ea[*]{\label{ex:12:demo-spec}\mention{This is Yoko.} / \mention{This is an acorn.} \hfill [specificational \mention ...
- Review in decisions CSV row `T0111`: `keep` | `replace_with_canonical` | `replace_custom`

### T0112 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter12.tex:448`
- Observed: `constructional support`
- Default action: `keep`
- Context: ... is constructional interference with the gender coupling. The same lexeme~-- \mention{that} as a fused head~-- behaves as non-personal in one syntactic frame and as gender-neutral in another. The stabilizing mechanism is \term{[[constructional support]]}: certain syntactic environments carry licensing conditions that override the default constraint. This parallels the lexeme-specific anchoring discussed above: relative \mention{which} with a full NP antecedent can licen ...
- Review in decisions CSV row `T0112`: `keep` | `replace_with_canonical` | `replace_custom`

### T0113 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter13.tex:46`
- Observed: `opaque coupling`
- Default action: `keep`
- Context: ... ast. At the word level, form merely points. The form \mention{went} is past by convention, not by decomposable form~-- the connection is brute memory. The system does not explain \mention{went}; it remembers it. This is \term{[[opaque coupling]]}. The triadic structure at the word level: \begin{itemize} \item \textbf{Form}: orthographic/phonological shape~-- \mention{went}, \mention{go}, \mention{dog}. \item \textbf{Object}: conventional pairing~-- pas ...
- Review in decisions CSV row `T0113`: `keep` | `replace_with_canonical` | `replace_custom`

### T0114 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter13.tex:86`
- Observed: `Deitality`
- Canonical: `deitality`
- Suggested replacement: `deitality`
- Default action: `replace_with_canonical`
- Context: ... ers retain the core but lose the margins. & Independent drift (e.g., \mention{a furniture}), semantic pressure propagating to form (\mention{pease} $\rightarrow$ \mention{pea}). \\ Definiteness & Loose (Cross-cutting) & \term{[[Deitality]]} forms one cluster; identifiability another. They overlap extensively but not exhaustively. & Form without semantics (weak definites); semantics without form (proper names). \\ Lexical Categories & Variable & Noun and ve ...
- Review in decisions CSV row `T0114`: `keep` | `replace_with_canonical` | `replace_custom`

### T0115 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter13.tex:104`
- Observed: `conditioning effect`
- Default action: `keep`
- Context: ... lavour: passive constructions, nominalizations, hedges like \mention{it has been argued}. The features cluster; experienced readers identify academic prose instantly. But this clustering isn't a homeostatic kind; it's a \term{[[conditioning effect]]} (see Chapter~\ref{ch:social-stabilization}). The \enquote{Academic} cluster is just the output of situational reweighting. Put the same researcher in front of a grant panel, a blog audience, and a conference poster, and ...
- Review in decisions CSV row `T0115`: `keep` | `replace_with_canonical` | `replace_custom`

### T0116 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter13.tex:221`
- Observed: `packaging tightness`
- Default action: `keep`
- Context: ... cues, are there domains where the bundle is so tight that separation is systematically resisted? One place to look is inside the nominal domain. We can measure this tightness. \textcite{reynolds2026lbe} quantifies the \term{[[packaging tightness]]} of the determiner--head relationship in English~-- the link that the Left Branch Gap (§\ref{sec:8:negative}) fails to break. Using a dependency-locality metric, he finds that determiners and their heads exhibit a packag ...
- Review in decisions CSV row `T0116`: `keep` | `replace_with_canonical` | `replace_custom`

### T0117 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:76`
- Observed: `balance`
- Default action: `keep`
- Context: ... pain, a dedicated alarm channel. Instead, the phenomenology of grammaticality is a bundle of metacognitive readouts that track the success of the coupling mechanism. These readouts look less like appetites and more like \term{[[balance]]} and \term{perception}. \subsection{Balance: The silent baseline} The primary analogue is \term{balance} or proprioception. Most of the time, balance is phenomenologically silent. When you walk down the street, you don ...
- Review in decisions CSV row `T0117`: `keep` | `replace_with_canonical` | `replace_custom`

### T0118 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:76`
- Observed: `perception`
- Default action: `keep`
- Context: ... larm channel. Instead, the phenomenology of grammaticality is a bundle of metacognitive readouts that track the success of the coupling mechanism. These readouts look less like appetites and more like \term{balance} and \term{[[perception]]}. \subsection{Balance: The silent baseline} The primary analogue is \term{balance} or proprioception. Most of the time, balance is phenomenologically silent. When you walk down the street, you don't feel \enquote{balan ...
- Review in decisions CSV row `T0118`: `keep` | `replace_with_canonical` | `replace_custom`

### T0119 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:80`
- Observed: `balance`
- Default action: `keep`
- Context: ... readouts that track the success of the coupling mechanism. These readouts look less like appetites and more like \term{[[balance]]} and \term{perception}. \subsection{Balance: The silent baseline} The primary analogue is \term{balance} or proprioception. Most of the time, balance is phenomenologically silent. When you walk down the street, you don't feel \enquote{balanced}; you just experience the world and your movement through it. The coupling work ...
- Review in decisions CSV row `T0119`: `keep` | `replace_with_canonical` | `replace_custom`

### T0120 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:88`
- Observed: `vision`
- Default action: `keep`
- Context: ... or is even articulated \parencite{nozari2011is}. The feeling of ungrammaticality is the system trying to keep itself upright. \subsection{Vision: Illusion and good-enough processing} If balance describes the baseline, \term{[[vision]]} describes the failure modes. Vision delivers structured objects, not raw sense data; we are aware of the output, not the intermediate computations. And like vision, grammatical processing is subject to systematic illusi ...
- Review in decisions CSV row `T0120`: `keep` | `replace_with_canonical` | `replace_custom`

### T0121 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:128`
- Observed: `grammaticality illusions`
- Canonical: `grammaticality illusion`
- Suggested replacement: `grammaticality illusion`
- Default action: `replace_with_canonical`
- Context: ... correspond to the triadic structure of sign, object, and interpretant. \section{Grammaticality illusions} \label{sec:14:illusions} The strongest evidence that the feeling is dissociable from the structure comes from \term{[[grammaticality illusions]]}~-- cases where the detector misfires. \subsection{Feels ungrammatical, is grammatical} The classic case is the garden-path sentence: \ea[]{\label{ex:14:garden-path} \mention{The horse raced past the barn fell.}} \z ...
- Review in decisions CSV row `T0121`: `keep` | `replace_with_canonical` | `replace_custom`

### T0122 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:194`
- Observed: `Declarative`
- Canonical: `declarative`
- Suggested replacement: `declarative`
- Default action: `replace_with_canonical`
- Context: ... plus affected recipient. The \term{passive} (\mention{was eaten}) demotes the agent. Break the construction's slot-filling requirements and the zipper won't close. At the clause-type level, value's illocutionary force. \term{[[Declarative]]} structure signals assertion; \term{interrogative} structure signals question; \term{imperative} structure signals command. Mismatch the structure and the force~-- use rising intonation on a declarative to fake a questio ...
- Review in decisions CSV row `T0122`: `keep` | `replace_with_canonical` | `replace_custom`

### T0123 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:204`
- Observed: `Appropriateness`
- Canonical: `appropriateness`
- Suggested replacement: `appropriateness`
- Default action: `replace_with_canonical`
- Context: ... {Grammaticality as a species of appropriateness} This grain-specific view suggests a larger picture. Grammaticality isn't sui generis; it's a \emph{species} of appropriateness, narrowed to the morphosyntactic channel. \term{[[Appropriateness]]} in general is the coupling between a form and \emph{all} the values it signals: structural meaning, social indexicality, register stance, identity marking. Grammaticality is what you get when you restrict attention to o ...
- Review in decisions CSV row `T0123`: `keep` | `replace_with_canonical` | `replace_custom`

### T0124 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:266`
- Observed: `Syntactic satiation`
- Canonical: `syntactic satiation`
- Suggested replacement: `syntactic satiation`
- Default action: `replace_with_canonical`
- Context: ... f the feeling of ungrammaticality's a noisy detector~-- not an oracle~-- then laboratory studies should reveal its characteristic failure modes. Three bodies of evidence confirm this prediction. \subsection{Satiation} \term{[[Syntactic satiation]]}'s the finding that repeated exposure to a marginally acceptable sentence can improve its perceived acceptability \parencite{snyder2000grammaticality}. But the effect's selective. Some constraints are susceptible to freq ...
- Review in decisions CSV row `T0124`: `keep` | `replace_with_canonical` | `replace_custom`

### T0125 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter14.tex:290`
- Observed: `garden-path sentences`
- Canonical: `garden-path sentence`
- Suggested replacement: `garden-path sentence`
- Default action: `replace_with_canonical`
- Context: ... hibits \term{selective fallibility}: it's exquisitely sensitive to some constraints and systematically vulnerable to others. The pattern reveals something about the architecture of the feeling, not just noise. Consider \term{[[garden-path sentences]]}. When readers encounter a grammatical sentence that's initially misparsed, they produce high unacceptability ratings at the point of reanalysis, even though the sentence's well-formed. The feeling of ungrammaticality fi ...
- Review in decisions CSV row `T0125`: `keep` | `replace_with_canonical` | `replace_custom`

### T0126 - unknown_term_with_suggestion
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:39`
- Observed: `grammatical`
- Canonical: `ungrammatical`
- Suggested replacement: `ungrammatical`
- Alternatives: `ungrammatical`, `grammaticality`
- Default action: `replace_with_canonical`
- Context: ... cuments its distribution across North American varieties: stable, predictable, and [[grammatical]]ized in specific discourse contexts.\footnote{See \url{https://ygdp.yale.edu/phenomena/double-is} for an overview.} So is it \term{grammatical}? The question is ill-posed because it treats \mention{English} as a single, flat population. If you pool all speakers and all contexts into one bucket, the double copula looks like a blurred edge~-- a 10\% probability ...
- Review in decisions CSV row `T0126`: `keep` | `replace_with_canonical` | `replace_custom`

### T0127 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:45`
- Observed: `cultural attractors`
- Canonical: `cultural attractor`
- Suggested replacement: `cultural attractor`
- Default action: `replace_with_canonical`
- Context: ... use the same social mechanisms keep regenerating them. The social variable isn't an external \mention{influence} on the grammar; it is a parameter of the grammar itself. \citet{sperber1996} calls such stable equilibria \term{[[cultural attractors]]}. The puzzle he addresses is this: if each transmission of a cultural item (a story, a pronunciation, a grammatical pattern) involves imperfect imitation or deliberate modification, why doesn't the item drift beyond reco ...
- Review in decisions CSV row `T0127`: `keep` | `replace_with_canonical` | `replace_custom`

### T0128 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:82`
- Observed: `Dialect`
- Canonical: `dialect`
- Suggested replacement: `dialect`
- Default action: `replace_with_canonical`
- Context: ... ) They don't have labels on the bolts. They have to infer the source. This inference isn't magic; it relies on three distinct mechanisms of social stabilization. In the technical literature, these often go by the names \term{[[Dialect]]}, \term{Register}, and \term{Discourse Community}. In the HPC framework, we can see them for what they are: stabilizer mechanisms that protect the cluster from drift. This mirrors \citet{khalidi2015three}'s taxonomy of s ...
- Review in decisions CSV row `T0128`: `keep` | `replace_with_canonical` | `replace_custom`

### T0129 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:82`
- Observed: `Register`
- Canonical: `register`
- Suggested replacement: `register`
- Default action: `replace_with_canonical`
- Context: ... e labels on the bolts. They have to infer the source. This inference isn't magic; it relies on three distinct mechanisms of social stabilization. In the technical literature, these often go by the names \term{Dialect}, \term{[[Register]]}, and \term{Discourse Community}. In the HPC framework, we can see them for what they are: stabilizer mechanisms that protect the cluster from drift. This mirrors \citet{khalidi2015three}'s taxonomy of social kinds, spec ...
- Review in decisions CSV row `T0129`: `keep` | `replace_with_canonical` | `replace_custom`

### T0130 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:82`
- Observed: `Discourse Community`
- Canonical: `discourse community`
- Suggested replacement: `discourse community`
- Default action: `replace_with_canonical`
- Context: ... . They have to infer the source. This inference isn't magic; it relies on three distinct mechanisms of social stabilization. In the technical literature, these often go by the names \term{Dialect}, \term{Register}, and \term{[[Discourse Community]]}. In the HPC framework, we can see them for what they are: stabilizer mechanisms that protect the cluster from drift. This mirrors \citet{khalidi2015three}'s taxonomy of social kinds, specifically his second kind: kinds ...
- Review in decisions CSV row `T0130`: `keep` | `replace_with_canonical` | `replace_custom`

### T0131 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:95`
- Observed: `maintained kinds`
- Canonical: `maintained kind`
- Suggested replacement: `maintained kind`
- Default action: `replace_with_canonical`
- Context: ... ething unrecognizable across generations? The standard sociolinguistic answer invokes geography, social networks, and identity. But these are descriptions, not mechanisms. Mechanisms are what HPC provides: dialects are \term{[[maintained kinds]]}. They cohere because transmission within communities, alignment during interaction, and identity-marking pressures keep regenerating the cluster. The dialect boundary isn't where the rules change; it's where the \emph{m ...
- Review in decisions CSV row `T0131`: `keep` | `replace_with_canonical` | `replace_custom`

### T0132 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:139`
- Observed: `slurs`
- Canonical: `slur`
- Suggested replacement: `slur`
- Default action: `replace_with_canonical`
- Context: ... Factory B}. This source attribution allows English to host massive internal diversity without losing its structural coherence. The clusters stay tight because we keep the bins separate effectively. Nunberg's history of \term{[[slurs]]} shows how such boundaries can be socially enforced into existence: the noun \mention{slur} as a label for derogative words only becomes widespread in Anglophone public discourse in the 1960s, tied to a changing civic-mo ...
- Review in decisions CSV row `T0132`: `keep` | `replace_with_canonical` | `replace_custom`

### T0133 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:141`
- Observed: `looping kinds`
- Canonical: `looping kind`
- Suggested replacement: `looping kind`
- Default action: `replace_with_canonical`
- Context: ... encodes stance. That is source attribution at the lexical level, and it makes the category real by making it policed by the community. \citep{nunberg2016slurs} This is closely related to what \citet{hacking1999} calls \term{[[looping kinds]]}. Hacking observed that when people are classified in a certain way~-- diagnosed with a disorder, labeled as a type~-- the classification loops back to affect how they behave, how others treat them, and even how they sel ...
- Review in decisions CSV row `T0133`: `keep` | `replace_with_canonical` | `replace_custom`

### T0134 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:158`
- Observed: `com-sits`
- Canonical: `com-sit`
- Suggested replacement: `com-sit`
- Default action: `replace_with_canonical`
- Context: ... n analytical convenience for linguists; it is the ground truth of acquisition. \citet{wiese2023} argues that children don't begin by learning languages like German or Turkish. They learn \term{Communicative Situations} (\term{[[com-sits]]}). In Wiese's \mention{free-range language} framework, the primary unit of acquisition is the com-sit: interactions with specific people (\eg\ \mention{talking to Dad}) in specific contexts (\eg\ \mention{breakfast tabl ...
- Review in decisions CSV row `T0134`: `keep` | `replace_with_canonical` | `replace_custom`

### T0135 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:166`
- Observed: `conditioned systems`
- Canonical: `conditioned system`
- Suggested replacement: `conditioned system`
- Default action: `replace_with_canonical`
- Context: ... English}. Because acquisition is com-sit dependent, we arrive directly at a core methodological conclusion of the maintenance view: there is no privileged scale of analysis. If the cognitive machinery is built to track \term{[[conditioned systems]]}, it tracks them at any scale where they stabilize~-- whether that's a dyadic routine between siblings, a specialised internet subculture, or a formal register shared by millions. The mechanisms of homeostasis are scale- ...
- Review in decisions CSV row `T0135`: `keep` | `replace_with_canonical` | `replace_custom`

### T0136 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:196`
- Observed: `Comparative concept`
- Canonical: `comparative concept`
- Suggested replacement: `comparative concept`
- Default action: `replace_with_canonical`
- Context: ... a definition that covers every construction in English without exception, then \textsc{subject} doesn't exist. But they were wrong to conclude that the only alternative is stipulation. To Haspelmath, we can now say: \term{[[Comparative concept]]}s aren't merely yardsticks we invent. They are \term{basin recognition}. When we find that the concept \textsc{adjective} is useful for describing unrelated languages, it isn't because we have forced the data into a box, ...
- Review in decisions CSV row `T0136`: `keep` | `replace_with_canonical` | `replace_custom`

### T0137 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:198`
- Observed: `Construction`
- Canonical: `construction`
- Suggested replacement: `construction`
- Default action: `replace_with_canonical`
- Context: ... re part of what makes those attractors cross-linguistically recurrent. The \enquote{comparative concept} tracks an attractor in the design space that is maintained by the community's action needs. To Croft, we can say: \term{[[Construction]]}s are indeed the primary units of form-meaning pairing, but they aren't islands. They are braided together by economy and alignment. \textsc{subject} is real in English not because it's a Platonic essence instantiated in ...
- Review in decisions CSV row `T0137`: `keep` | `replace_with_canonical` | `replace_custom`

### T0138 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:200`
- Observed: `discourse communities`
- Canonical: `discourse community`
- Suggested replacement: `discourse community`
- Default action: `replace_with_canonical`
- Context: ... r. To both, we can say: The complexity of sociolinguistic variation isn't evidence against categories, but evidence of \term{mixture}. Speakers don't condition on a single homogeneous grammar but on latent variables~-- \term{[[discourse communities]]} and \term{registers}~-- that shift the parameters. The fact that \mention{I done it} is grammatical in one community and ungrammatical in another doesn't mean the category \textsc{Perfect} is a fiction; it means it's pa ...
- Review in decisions CSV row `T0138`: `keep` | `replace_with_canonical` | `replace_custom`

### T0139 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:200`
- Observed: `registers`
- Canonical: `register`
- Suggested replacement: `register`
- Default action: `replace_with_canonical`
- Context: ... lexity of sociolinguistic variation isn't evidence against categories, but evidence of \term{mixture}. Speakers don't condition on a single homogeneous grammar but on latent variables~-- \term{discourse communities} and \term{[[registers]]}~-- that shift the parameters. The fact that \mention{I done it} is grammatical in one community and ungrammatical in another doesn't mean the category \textsc{Perfect} is a fiction; it means it's parameterised by a cond ...
- Review in decisions CSV row `T0139`: `keep` | `replace_with_canonical` | `replace_custom`

### T0140 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:202`
- Observed: `maintained kinds`
- Canonical: `maintained kind`
- Suggested replacement: `maintained kind`
- Default action: `replace_with_canonical`
- Context: ... rdination, terms needn't track pre-existing essences; similarity is defined in payoff space, so the properties that count as natural are those relevant to the community's action needs. That is exactly the space in which \term{[[maintained kinds]]} live. The nominalist is right that categories lack essences. What the nominalist declines to explain is why certain essenceless categories support induction, resist perturbation, and recur across unrelated languages. T ...
- Review in decisions CSV row `T0140`: `keep` | `replace_with_canonical` | `replace_custom`

### T0141 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/chapters/chapter15.tex:206`
- Observed: `real generals`
- Canonical: `real general`
- Suggested replacement: `real general`
- Default action: `replace_with_canonical`
- Context: ... e habits that keep \textsc{noun} stable across English speakers aren't conventions we could abolish by fiat; they're embedded in acquisition, production, and the inferential economy of communication. Peirce called these \term{[[real generals]]}~-- laws of habit that exist not in particular tokens but in the regularity of their effects. That's what HPC categories are: generals stabilized by causal work, sustaining would-bes that earn their reality by the infere ...
- Review in decisions CSV row `T0141`: `keep` | `replace_with_canonical` | `replace_custom`

### T0142 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:17`
- Observed: `definite article`
- Default action: `keep`
- Context: ... finitions leak everywhere. Consider \mention{action}: it names a kind of thing, but it's an \enquote{action word}, which is supposed to be a verb. Consider \mention{the} in \enquote{I took the bus}. \mention{The} is the \term{[[definite article]]}, but it doesn't identify a specific bus. Every rule has \enquote{exceptions} that aren't exceptions~-- they're evidence. \textbf{The nominalist temptation} swings the other way. If definitions fail, maybe categories ar ...
- Review in decisions CSV row `T0142`: `keep` | `replace_with_canonical` | `replace_custom`

### T0143 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:45`
- Observed: `Noun`
- Canonical: `noun`
- Suggested replacement: `noun`
- Default action: `replace_with_canonical`
- Context: ... \term{noun}?} we ask \enquote{What keeps \term{noun} stable?} The answer is a story about mechanisms, not a dictionary entry. \bigskip Once you learn to see maintained clusters, you might start seeing them everywhere. \term{[[Noun]]}? Maintained. \term{Verb}? Maintained. \term{Subject}? \term{Voice}? \term{Non-finite}? Everything looks like a spinning top. This is the inflation problem. Not every stable pattern is a genuine kind. Some patterns are ...
- Review in decisions CSV row `T0143`: `keep` | `replace_with_canonical` | `replace_custom`

### T0144 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:45`
- Observed: `Verb`
- Canonical: `verb`
- Suggested replacement: `verb`
- Default action: `replace_with_canonical`
- Context: ... uote{What keeps \term{noun} stable?} The answer is a story about mechanisms, not a dictionary entry. \bigskip Once you learn to see maintained clusters, you might start seeing them everywhere. \term{Noun}? Maintained. \term{[[Verb]]}? Maintained. \term{Subject}? \term{Voice}? \term{Non-finite}? Everything looks like a spinning top. This is the inflation problem. Not every stable pattern is a genuine kind. Some patterns are just accidents; some labe ...
- Review in decisions CSV row `T0144`: `keep` | `replace_with_canonical` | `replace_custom`

### T0145 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:45`
- Observed: `Subject`
- Canonical: `subject`
- Suggested replacement: `subject`
- Default action: `replace_with_canonical`
- Context: ... n} stable?} The answer is a story about mechanisms, not a dictionary entry. \bigskip Once you learn to see maintained clusters, you might start seeing them everywhere. \term{Noun}? Maintained. \term{Verb}? Maintained. \term{[[Subject]]}? \term{Voice}? \term{Non-finite}? Everything looks like a spinning top. This is the inflation problem. Not every stable pattern is a genuine kind. Some patterns are just accidents; some labels are just filing conventio ...
- Review in decisions CSV row `T0145`: `keep` | `replace_with_canonical` | `replace_custom`

### T0146 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:45`
- Observed: `Voice`
- Canonical: `voice`
- Suggested replacement: `voice`
- Default action: `replace_with_canonical`
- Context: ... answer is a story about mechanisms, not a dictionary entry. \bigskip Once you learn to see maintained clusters, you might start seeing them everywhere. \term{Noun}? Maintained. \term{Verb}? Maintained. \term{Subject}? \term{[[Voice]]}? \term{Non-finite}? Everything looks like a spinning top. This is the inflation problem. Not every stable pattern is a genuine kind. Some patterns are just accidents; some labels are just filing conventions. When a fra ...
- Review in decisions CSV row `T0146`: `keep` | `replace_with_canonical` | `replace_custom`

### T0147 - unknown_term
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:45`
- Observed: `Non-finite`
- Default action: `keep`
- Context: ... ory about mechanisms, not a dictionary entry. \bigskip Once you learn to see maintained clusters, you might start seeing them everywhere. \term{Noun}? Maintained. \term{Verb}? Maintained. \term{Subject}? \term{Voice}? \term{[[Non-finite]]}? Everything looks like a spinning top. This is the inflation problem. Not every stable pattern is a genuine kind. Some patterns are just accidents; some labels are just filing conventions. When a framework can explain ...
- Review in decisions CSV row `T0147`: `keep` | `replace_with_canonical` | `replace_custom`

### T0148 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:58`
- Observed: `Adverb`
- Canonical: `adverb`
- Suggested replacement: `adverb`
- Default action: `replace_with_canonical`
- Context: ... group marking it as identity. If English lost it tomorrow, nothing would restore it. It's a smoke ring~-- real for a moment, but not maintained. \item \textbf{Fat categories} lump distinct clusters under one label. \term{[[Adverb]]} is the paradigm case~-- the \enquote{dustbin of the parts of speech,} a category with excellent storage capacity and terrible explanatory power. It groups manner adverbs like \mention{quickly} (which follow verbs), degr ...
- Review in decisions CSV row `T0148`: `keep` | `replace_with_canonical` | `replace_custom`

### T0149 - normalized_variant
- Location: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/HPC book/frontmatter/precis.tex:59`
- Observed: `Non-finite clause`
- Canonical: `non-finite clause`
- Suggested replacement: `non-finite clause`
- Default action: `replace_with_canonical`
- Context: ... ng \mention{quickly} tells you nothing about where \mention{very} can appear~-- the label creates an illusion of unity where there's only a filing decision. \item \textbf{Negative categories} are defined by absence. \term{[[Non-finite clause]]} groups infinitivals, gerunds, and past participles~-- not because they share something, but because they all lack tense inflection. This is a family portrait taken in silhouette: the shared trait is what you can't see. ...
- Review in decisions CSV row `T0149`: `keep` | `replace_with_canonical` | `replace_custom`

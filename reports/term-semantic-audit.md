# Semantic Term Consistency Audit (2026-02-22 08:39:41)

## Scope
- Glossary source: `glossary.tex`
- TeX files scanned: 28
- Glossary-backed term occurrences analyzed: 335
- Distinct glossary terms observed: 179
- Minimum occurrences per term for outlier detection: 3
- Max flags per term: 2
- Flagged semantic-drift suspects: 12
- Decisions CSV: `reports/term-semantic-audit-decisions.csv`

## Interpretation
- This report only audits terms that already map to glossary entries.
- Flags are outlier candidates, not automatic errors.
- Use the walkthrough to mark each as `keep` or propose revision.

## Findings

### S0001 - `adverb`
- Location: `chapters/chapter08.tex:99`
- Observed form: `adverb`
- Similarity to glossary definition: `0.088`
- Similarity to this term's usage cluster: `0.152`
- Combined outlier score: `0.133`
- Glossary definition excerpt: A traditional residual category for modifiers that are not adjectives. Maintained by multiple unrelated mechanisms across subtypes. Fails projectibility across manner, degree, and sentence adverbs. A paradigmatic fat class; the remedy is decomposition. fat class.
- Context: ... extbf{Projectibility} & \textbf{Homeostasis} & \textbf{Example} \\ \midrule Thin & Fail (insufficient clustering) & Fail (no stabilizers) & Preposition doubling \\ Fat & Fail (subclass divergence) & Partial (subgroup mechanisms) & Umbrella \term{[[adverb]]} \\ Negative & Fail (no positive cluster) & Fail (defined by absence) & \term{non-finite clause} \\ \bottomrule \end{tabular} \end{table} \begin{figure}[t] \centering \begin{tikzpicture}[ box/.style={rectangle, draw, minimum width=5cm, ...
- Review in decisions CSV row `S0001` (recommended default: `keep` unless clearly inconsistent).

### S0002 - `adverb`
- Location: `chapters/chapter08.tex:140`
- Observed form: `adverb`
- Similarity to glossary definition: `0.070`
- Similarity to this term's usage cluster: `0.175`
- Combined outlier score: `0.143`
- Glossary definition excerpt: A traditional residual category for modifiers that are not adjectives. Maintained by multiple unrelated mechanisms across subtypes. Fails projectibility across manner, degree, and sentence adverbs. A paradigmatic fat class; the remedy is decomposition. fat class.
- Context: ... ogical history. Language is an ecosystem. The HPCs are the components~-- constructions, lexemes, phoneme contrasts, sometimes families or paradigms~-- not the grammar as a whole. The failure modes below apply at that level: we ask whether \term{[[adverb]]} is a kind, not whether \term{English} is. Section~\ref{sec:8:grain} returns to this question; for now, the point is that grain matters. A category can be too thin, too fat, too negative~-- or simply at the wrong level of analysis. \secti ...
- Review in decisions CSV row `S0002` (recommended default: `keep` unless clearly inconsistent).

### S0003 - `aspect`
- Location: `chapters/chapter07.tex:143`
- Observed form: `aspect`
- Similarity to glossary definition: `0.044`
- Similarity to this term's usage cluster: `0.248`
- Combined outlier score: `0.187`
- Glossary definition excerpt: A grammatical category describing how events are temporally and structurally construed. Maintained by distributional cue structures and morphological marking. Projectible patterns may diverge from textbook semantic definitions. A comparative concept whose language-specific mechanisms can drift. projectibility, mechanistic drift.
- Context: ... {sec:7:labels-mechanisms} Here's where the story takes a surprising turn. \citet{divjak2025learnability} found that the best model~-- the one that most closely matches native-speaker preferences~-- is the one that doesn't use the category \term{[[aspect]]} at all. The lemma-concrete model~-- the one that treats each verb individually, without abstracting to aspect~-- predicts human behaviour better than the aspect-aware models. The statistical evidence is overwhelming: the probability that ...
- Review in decisions CSV row `S0003` (recommended default: `keep` unless clearly inconsistent).

### S0004 - `count cluster`
- Location: `chapters/chapter09.tex:86`
- Observed form: `count cluster`
- Similarity to glossary definition: `0.228`
- Similarity to this term's usage cluster: `0.131`
- Combined outlier score: `0.160`
- Glossary definition excerpt: The morphosyntactic properties that travel together in English count nouns (plural, cardinals, many / few , agreement). Maintained by acquisition and entrenchment in count frames, plus alignment in discourse. Implicational hierarchy: tight properties imply loose ones. Coupled to individuation by bidirectional inference. individuation cluster, bidirectional inference, functional anchoring.
- Context: ... ndifferentiated substance; it lacks a plural form (outside special interpretations); it rejects cardinals (*\mention{two waters}) and takes mass quantifiers (\mention{much}, \mention{less}); and it triggers singular agreement. This is the \term{[[count cluster]]}: the set of formal properties that normally travel together. When you hear a word has a plural form, you can predict it will take \mention{many} and reject \mention{much}. You can predict it will refer to something conceptualized as an ind ...
- Review in decisions CSV row `S0004` (recommended default: `keep` unless clearly inconsistent).

### S0005 - `mechanism`
- Location: `chapters/chapter14.tex:250`
- Observed form: `mechanism`
- Similarity to glossary definition: `0.023`
- Similarity to this term's usage cluster: `0.104`
- Combined outlier score: `0.080`
- Glossary definition excerpt: Entities and activities organized in such a way that they are responsible for a phenomenon. Mechanisms include acquisition, alignment, entrenchment, and transmission. Identified by perturbation: weaken the process and the cluster frays. Adopts the consensus definition of . stabilizer, homeostasis, perturbation sensitivity.
- Context: ... ~-- the maintained coupling between morphosyntactic form and structural meaning. It sustains a would-be (one form--value pairing lets you predict others) and it's homeostatic (the feeling of ungrammaticality stabilizes the coupling). As a \term{[[mechanism]]}, it's a stabilizer for other HPCs. The category \term{noun}'s maintained partly because nounhood's grammatical~-- because using a word in a noun slot, with noun morphology, in noun constructions, triggers no mismatch signal. Grammaticality ...
- Review in decisions CSV row `S0005` (recommended default: `keep` unless clearly inconsistent).

### S0006 - `mechanism`
- Location: `chapters/chapter09.tex:18`
- Observed form: `mechanism`
- Similarity to glossary definition: `0.029`
- Similarity to this term's usage cluster: `0.153`
- Combined outlier score: `0.116`
- Glossary definition excerpt: Entities and activities organized in such a way that they are responsible for a phenomenon. Mechanisms include acquisition, alignment, entrenchment, and transmission. Identified by perturbation: weaken the process and the cluster frays. Adopts the consensus definition of . stabilizer, homeostasis, perturbation sensitivity.
- Context: ... t hard: unlike phoneme contrasts, where form directly realizes contrastive value with minimal slippage, the count system tolerates drift, and the pattern of that drift is where the [[mechanism]] story lives. (A note: Throughout Part III, I use \term{mechanism} and \term{stabilizer} to refer to causal structures and their functional roles respectively \parencite{illari2012}.) %~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- ~-- -- \section{One word, two categories} \label{sec:9:two-c ...
- Review in decisions CSV row `S0006` (recommended default: `keep` unless clearly inconsistent).

### S0007 - `noun`
- Location: `chapters/chapter04.tex:129`
- Observed form: `noun`
- Similarity to glossary definition: `0.024`
- Similarity to this term's usage cluster: `0.180`
- Combined outlier score: `0.133`
- Glossary definition excerpt: A lexical category associated with nominals and argument structure. Maintained by distributional cues, morphology, and acquisition biases. Cliquish stability across multiple diagnostics (determiners, number, agreement). Cross-linguistic comparability requires mechanism mapping. verb, subject, copied kind.
- Context: ... y, without conscious categorisation. They are the bedrock of the category, the items that every speaker agrees on, the deep-basin anchors around which less frequent items cluster. Change the behaviour of \mention{thing} and you change what \term{[[noun]]} means. This is vanishingly unlikely. \mention{Thing} is so entrenched that changing it's nearly impossible~-- it would require shifting the habits of every English speaker simultaneously. The skewed distribution isn't incidental~-- it's f ...
- Review in decisions CSV row `S0007` (recommended default: `keep` unless clearly inconsistent).

### S0008 - `noun`
- Location: `chapters/chapter08.tex:10`
- Observed form: `noun`
- Similarity to glossary definition: `0.021`
- Similarity to this term's usage cluster: `0.184`
- Combined outlier score: `0.135`
- Glossary definition excerpt: A lexical category associated with nominals and argument structure. Maintained by distributional cues, morphology, and acquisition biases. Cliquish stability across multiple diagnostics (determiners, number, agreement). Cross-linguistic comparability requires mechanism mapping. verb, subject, copied kind.
- Context: ... art seeing it everywhere. Once you learn to spot homeostatic property clusters~-- once you see how feedback loops can maintain stable patterns without essences~-- it becomes tempting to diagnose homeostasis in every corner of the grammar. \term{[[noun]]}? HPC. \term{subject}? HPC. \term{voice}? HPC. \term{non-finite clause}? Surely an HPC too. The world fills up with spinning tops. Soon even the paper clips look homeostatic. Words that won't hold still~-- that's one failure mode. Words th ...
- Review in decisions CSV row `S0008` (recommended default: `keep` unless clearly inconsistent).

### S0009 - `particle`
- Location: `chapters/chapter06.tex:440`
- Observed form: `particle`
- Similarity to glossary definition: `0.109`
- Similarity to this term's usage cluster: `0.111`
- Combined outlier score: `0.111`
- Glossary definition excerpt: A residual lexical class for small function-like items that resist cleaner category assignments in a language-specific grammar. Often maintained by construction-specific distributions and lexical idiosyncrasy rather than a single unified profile. Typically weak projectibility outside narrow constructional contexts. Frequently a descriptive class rather than a mechanism-backed category. class, category, construction.
- Context: ... sm makes the category projectible. Chapter~\ref{ch:failure-modes} develops such failure modes systematically; here, the contrast case shows that the quotative analysis isn't analogy-by-enthusiasm~-- it identifies genuine stabilization that \term{[[particle]]} lacks. The quotative category is also a mechanism in the larger kinds that contain it. Quotatives are part of what maintains \term{narrative discourse structure}~-- they enable the vivid re-enactment that makes storytelling work. They are ...
- Review in decisions CSV row `S0009` (recommended default: `keep` unless clearly inconsistent).

### S0010 - `proper name`
- Location: `chapters/chapter07.tex:332`
- Observed form: `Proper name`
- Similarity to glossary definition: `0.154`
- Similarity to this term's usage cluster: `0.327`
- Combined outlier score: `0.275`
- Glossary definition excerpt: A semantic category of expressions that directly refer to individuals. Maintained by discourse tracking and stable reference to individuals. Rigid designation and referential opacity effects. Cross-cuts the syntactic category of proper nouns. proper noun, definiteness cluster, field-relative projectibility.
- Context: ... nt because colour doesn't project for grammatical inferences. The same extension~-- red things, warm-coloured things~-- supports robust categorisation in one domain and fails to support it in another. This extends the proper-name pattern. \term{[[Proper name]]} projects for semantic purposes; \term{proper noun} projects for syntactic purposes. \term{Warm-coloured} projects for ecological purposes; nothing projects it for grammatical purposes~-- so nothing grammaticalises. The framework doesn't mu ...
- Review in decisions CSV row `S0010` (recommended default: `keep` unless clearly inconsistent).

### S0011 - `register`
- Location: `chapters/chapter15.tex:200`
- Observed form: `registers`
- Similarity to glossary definition: `0.022`
- Similarity to this term's usage cluster: `0.077`
- Combined outlier score: `0.061`
- Glossary definition excerpt: A situation-linked variety ( variety according to use ) realized as reweighting of linguistic options. Maintained by gatekeeping, genre expectations, and recurrent context-specific feedback. Systematic shifts in lexical/syntactic distributions across activity types. Chapter 15 treats register as a mode switch rather than a separate grammar. field, tenor, mode, dialect.
- Context: ... we can say: The complexity of sociolinguistic variation isn't evidence against categories, but evidence of \term{mixture}. Speakers don't condition on a single homogeneous grammar but on latent variables~-- \term{discourse communities} and \term{[[registers]]}~-- that shift the parameters. The fact that \mention{I done it} is grammatical in one community and ungrammatical in another doesn't mean the category \textsc{Perfect} is a fiction; it means it's parameterised by a conditioning structure. ...
- Review in decisions CSV row `S0011` (recommended default: `keep` unless clearly inconsistent).

### S0012 - `subject`
- Location: `chapters/chapter08.tex:10`
- Observed form: `subject`
- Similarity to glossary definition: `0.000`
- Similarity to this term's usage cluster: `0.143`
- Combined outlier score: `0.100`
- Glossary definition excerpt: A syntactic function cluster defined by converging behavioural and coding properties. Agreement, word order, case marking, and discourse roles. Convergence of multiple diagnostics rather than a single definition. Cross-linguistic identity is not guaranteed. comparative concept, category.
- Context: ... ywhere. Once you learn to spot homeostatic property clusters~-- once you see how feedback loops can maintain stable patterns without essences~-- it becomes tempting to diagnose homeostasis in every corner of the grammar. \term{noun}? HPC. \term{[[subject]]}? HPC. \term{voice}? HPC. \term{non-finite clause}? Surely an HPC too. The world fills up with spinning tops. Soon even the paper clips look homeostatic. Words that won't hold still~-- that's one failure mode. Words that \emph{seem} to hol ...
- Review in decisions CSV row `S0012` (recommended default: `keep` unless clearly inconsistent).

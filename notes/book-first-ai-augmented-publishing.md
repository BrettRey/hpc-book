# Book-first, AI-augmented publishing

## Working model

The right target object for this book is not "the book as a chatbot" and not "the book as a LoRA."

It is a layered publication:

1. Canonical reading editions: PDF plus EPUB/HTML.
2. Canonical listening edition: TTS/T2V audiobook, ideally in Brett's verified cloned voice.
3. Source-grounded AI adjunct: chat/search/tutor over the manuscript.
4. Optional generated derivatives: FAQ, study guide, teaching materials, chapter summaries, concept maps.

The book remains primary. The AI layer is an adjunct.

## What Tyler Cowen actually did

Cowen's GOAT model was narrower than a bespoke "AI-native book app":

- a conventional manuscript, written by the author
- a normal web/PDF reading path
- a chatbot companion layered over the text
- chapter-level prompting and AI-assisted interaction as an extra interface, not the only interface

That is the closer analogue here.

## Why not "the book as a LoRA"

A LoRA is a behavior/style layer on top of a base model. It is not a trustworthy representation of a specific book.

Problems:

- weak citation discipline
- hard to preserve chapter/section anchoring
- retraining required after substantive revision
- easy contamination from base-model prior knowledge
- bad fit for "what exactly does the book say here?"

Use retrieval for the book's contents. Use fine-tuning/LoRA only, if at all, for house voice, answer discipline, and local deployment.

Best hybrid if needed later:

- cleaned book chunks as the knowledge base
- retrieval over those chunks
- optional LoRA on an open model for style and answer policy

## Current practical state of the art

For a real public release in 2026, the strongest pattern is:

`LaTeX manuscript -> PDF + EPUB/HTML + audiobook + source-grounded companion`

not:

`LaTeX manuscript -> fine-tuned model that vaguely "knows" the book`

This means:

- book-first publishing
- AI-first discovery and teaching aids
- grounded answers with citations
- multiple modalities from one manuscript source

## Recommended v1 path

The lowest-friction prototype is probably NotebookLM.

Why:

- source-grounded by design
- citations back to uploaded sources
- easy chapter-by-chapter testing
- useful derivative outputs (FAQ/study-guide/audio-style overviews)
- low engineering overhead

Limits:

- less control over UI and branding
- platform dependence
- public sharing friction compared with a custom site

NotebookLM should be treated as a prototype and evaluation environment, not necessarily the final public home.

## Recommended final public form

If the AI layer proves valuable, the best final object is likely a custom site with:

- online reading edition
- embedded or linked PDF
- audiobook player
- chapter navigation
- source-grounded chat
- preset modes such as "summarize," "teach," "object," "trace this concept," and "show where this is defined"

The chat should always behave like a companion to the book, not a replacement for the book.

## Repo implications

The key engineering task is not model training. It is source normalization.

This repository is already in a strong starting state:

- chapterized LaTeX source
- glossary
- bibliography
- stable compiled PDF

Needed next step:

Build an export pipeline from LaTeX to clean chapter text with metadata.

Desired outputs:

- one cleaned file per chapter
- section/subsection boundaries preserved
- labels and cross-references resolved or retained as metadata
- glossary terms available as structured context
- figures, examples, and bibliography pointers retained where useful

Suggested target formats:

- Markdown for human inspection
- JSON/JSONL for retrieval/indexing

## Minimal architecture

1. Export each chapter from LaTeX into cleaned Markdown/JSON.
2. Attach metadata: chapter title, section, labels, citations, figure/example ids.
3. Load into NotebookLM for quick evaluation.
4. If the interaction quality is strong, build a custom retrieval-backed site.
5. Keep the PDF, EPUB/HTML, and audiobook as the primary publication objects.

## Decision rule

Default recommendation:

- do not treat the book itself as a LoRA
- do not make chat the primary publishing form
- do publish the book in normal reading/listening formats
- do build a grounded AI adjunct over the manuscript
- do prototype in NotebookLM before funding a custom artifact/site

## Possible next concrete tasks

1. Create a LaTeX-to-Markdown/JSON export script for chapter files.
2. Define a chunking scheme that respects chapter and section boundaries.
3. Prepare a NotebookLM-ready source bundle.
4. Evaluate answer quality on a fixed set of representative questions.
5. Decide whether the public release needs a custom site or whether a hosted companion is sufficient.

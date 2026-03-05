# Chapter 13 fact check (2026-03-03)

Scope: audited all chapter-specific quantitative claims and direct quotations in `chapters/chapter13-sign-anaphor.tex` against PDFs in `literature/` (using page-marked `pdftotext` dumps in `/tmp/ch13_factcheck`).

## Summary
- Checked claims: 33
- Fully supported: 27
- Needed wording/citation tightening: 6
- Unsupported after revision: 0

## Claims audited

| Ch.13 location | Claim (short) | Source check | Result | Action |
|---|---|---|---|---|
| §13.1 | one proposition every 1–2s in both modalities | `sandler-lillomartin2006-ch01`, p.3 text includes this and “modality independent upper limit” | Verified | none |
| §13.1 | “modality independent upper limit” | same source, p.3 | Verified | none |
| §13.1 | signed/spoken share core structural properties | `meier2002-modality-structure-sample`, ch.1 pp.2–5 (shared properties list; signed/spoken as natural languages) | Verified (paraphrase-level) | none |
| §13.2 | no clear upper bound; 7-locus ASL example | `schlenker2017`, p.4 | Verified | none |
| §13.2 | practical active-load claim tied to Steinbach p.2 | `steinbach-onea2016`, p.2 states “2–3 recursive steps” (not “2–4 referents”) | Needed fix | revised to “two to three recursive spatial splits” |
| §13.2 | 789/25,000 ambiguous BSL pointing tokens | `cormier2013`, p.235 | Verified | none |
| §13.2 | “cannot be characterised exclusively…” quote | `cormier2013`, p.244 | Verified | none |
| §13.2 | object agreement obligatory / subject optional | `sandler-lillomartin2006-ch03`, p.30 | Verified | none |
| §13.2 | cross-ling phonetic constraints (ASL/DGS/Auslan/JSL) | same source, pp.38+ | Verified | none |
| §13.2 | transfer structures up to 70% in narratives | `garcia2020`, p.6 | Verified | none |
| §13.2 | maintenance/reintro 76–95% | `garcia2020`, p.8 summary of prior corpus results | Verified | none |
| §13.2 | “the more prominent…, the less explicit…” quote | `steinbach-onea2016`, p.10 | Verified | none |
| §13.3 | loci as “formal index” quote | `schlenker2017`, p.10 | Verified | none |
| §13.3 | four readings under same locus with `only one` | `kuhn2016`, pp.14–15 | Verified | none |
| §13.3 | “strong loci-as-variables hypothesis has been falsified” quote | `kuhn2016`, p.18 | Verified | none |
| §13.3 | midpoint pointing for disjunctive sums | `kuhn2022`, p.15 | Verified | none |
| §13.3 | same locus can index multiple individuals | `kuhn2022` (via `kuhn2016` result), p.6 | Verified | none |
| §13.3 | “loci must be mediated by a featural layer” | `kuhn2022`, p.1 framing + p.6 analysis | Verified | none |
| §13.4 | DGS predicates RI=.70 vs M=.49; gesture no effect | `perniss-ozyurek2015`, pp.15–16 | Verified | none |
| §13.4 | “must carry the full load…” quote | same source, p.19 | Verified | none |
| §13.4 | BSL child data (0%, 90%, 70%; persistent non-manual deficits) | `morgan2002`, pp.16–19 | Verified | none |
| §13.4 | “developmental problem…” quote | `morgan2002`, p.18 | Verified | none |
| §13.4 | NSL shared-reference increase 0.63→0.88 | `senghas2001`, p.5 | Verified | none |
| §13.4 | NSL gen2 consistent directional layout | `senghas1997`, pp.9–10 | Verified | none |
| §13.4 | “body is a central reference point…” quote | `padden-etal2010`, p.19 | Verified | none |
| §13.5 | empty R-locus → presupposition failure | `steinbach-onea2016`, p.6 | Verified | none |
| §13.5 | classifier handshape persistence across predicate chains | `sandler-lillomartin2006-ch05`, pp.91–92 | Verified | none |
| §13.5 | Kata Kolok context-poor settings: list-buoy/anaphoric increase | `devos2012`, p.259 | Verified | none |
| §13.6 | ISL: Z=25%, X=42%, near-75% agreement, two double-agreement tokens in older groups | `padden-etal2010`, pp.14–18 | Verified | none |
| §13.6 | Kata Kolok: ~1 in 6 pointing; 3/839 spatially modified transitives; “exophoric reference predominates” | `devos2012`, pp.44, 152–153, 259 | Verified | none |
| §13.6 | ABSL: “avoided … entirely” with 47% single-argument | `sandler-etal2005`, p.6 shows frequent, not total avoidance | Needed fix | changed to “frequently avoided” |
| §13.6 | homesign: six children, 41–62% deictics, 2-sign semantic ordering | `goldinmeadow1977`, pp.2–4 | Verified | none |
| §13.2 | “highly discriminating for singular discourse referents” with `sandler2006:26` | page-local support not robust in available chapter extracts | Needed fix | replaced with a non-comparative, source-safe phrasing |
| §13.6/table | “no agreement system” in homesign row/prose | source does not directly state this term; inference only | Needed fix | softened to “no evidence of productive agreement morphology” |
| Table 13.1 | ISL tracking evidence “role shift support” | `padden2010` is not a role-shift study | Needed fix | changed to source-grounded tracking/localisation wording |
| Table 13.1 | ABSL tracking “role shift” label | `sandler2005` evidence is word order/prosody/clause sequencing | Needed fix | adjusted row wording |
| §13.6 + Table 13.1 | ASL tight-coupling line cited to `schlenker2018:10–11` | direct evidence for binding/crossover clearer in `schlenker2017` | Needed fix | retargeted citation to `schlenker2017:4–5, 10` |

## Revised text in chapter
Applied in `chapters/chapter13-sign-anaphor.tex`:
- Replaced Steinbach-based “two to four at a time” with source-accurate “two to three recursive spatial splits”.
- Replaced ABSL “avoided … entirely” with “frequently avoided”.
- Softened homesign agreement claim to evidence-based wording.
- Tightened table row descriptions for BSL/ISL/ABSL/Homesign to match cited evidence more directly.
- Removed an over-strong Sandler-backed singular-reference claim and replaced it with source-safe wording.
- Retargeted one ASL binding/locus citation from `schlenker2018` to the directly supporting `schlenker2017` pages.

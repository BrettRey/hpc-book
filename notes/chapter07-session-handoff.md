# Chapter 7 Restructure: Status and Next Steps

**Last updated:** 2025-12-08T22:30

---

## Current State

**COMPLETE:** Chapter 7 is a polished worked-case chapter demonstrating the maintenance view through two case studies (quotatives, filler-gap/*whose*). All major structural and clarity fixes have been implemented.

---

## Session Summary (2025-12-08, evening)

### Major accomplishments:

1. **Margin-note audit (first half)**
   - Fixed LaTeX double-backslash error (colloquialisation section)
   - Reduced "categories all the way down" redundancy
   - Added Aikhenvald 2004 for Eurasian evidentiality zone
   - Changed Tagliamonte textcite to autocite (redundancy fix)
   - Fixed "cognitive architecture" → "conditions" (Chater slippage)
   - Changed "memory retrieval" → "dependency tracking"

2. **Scale transitions made explicit**
   - Line 143: "co-location plus time produces the network density"
   - Line 145: "distal factors shape network structure, which shapes input frequency, which shapes entrenchment"
   - Line 215: Explained why cross-linguistic convergence isn't mysterious
   - Line 295: "mechanisms at different scales — cognitive, interactional, institutional — interact"

3. **Sharpened key definitions**
   - "Convergent maintenance: independent forms, stabilised by the same mechanisms, producing the same category architecture"
   - Glossed "shallower basin" = fewer stabilisers
   - Glossed "exercises" = providing input that keeps processing routine facilitated
   - Added "fashion cycle = a decade or two"

4. **Immunology analogy threaded through**
   - Added callback in §5.5: "A cell type maintains the signalling environment that maintains the cell type; a construction maintains the processing mechanism that maintains the construction"

5. **Margin-note audit (second half)**
   - Added Ide 2005 for Japanese/Korean honorific elaboration
   - Hedged German/Japanese cross-linguistic claims as "reported"
   - Trimmed §5.5 reciprocity redundancy
   - Added "adverb" as concrete wastebasket example

6. **Bridge paragraph for *whose* case**
   - Explicitly connects filler-gap → constraint profile → cross-ling → reciprocal
   - Makes "labels aren't mechanisms" point concrete

### Commits this session:
```
29a17e5 BRIDGE: Added 'labels aren't mechanisms' paragraph to whose case
0f1b8ce FIXES: 5 margin-note issues (second half)
cab59d6 ANALOGY: Immunology callback + basin clarification
f784bc3 FIXES: Top 5 second-half flaws
8e1cd0e SHARPEN: Define 'convergent maintenance' explicitly
39cbde7 BRIDGES: Made scale transitions explicit
5caec42 FIXES: Top 5 margin-note issues
7ac509e STRUCTURE: Acknowledge biology parallel is heuristic, not template
12f2d29 CHATER + EXPANSION: Fix storage language, expand activation states
de5555c STRUCTURE: Five quick fixes to Chapter 7
```

---

## Current chapter structure:

1. **Roadmap** (added this session)
2. The cluster (macrophage → nouns)
3. Stabilisers at multiple scales (biology → linguistics mapping)
4. Variation as activation states (*fast* example added this session)
5. **One case in depth: quotatives**
   - The cluster
   - Stabilisers (5 named)
   - How deep do mechanisms go? (causal depth, mereological structure, mechanisms as categories)
   - Why the same profile across languages?
   - The wider ecology: colloquialisation
   - Variation and activation
   - What if a mechanism were absent? (ablation test)
   - A contrast: evidentiality (Turkish vs Japanese)
6. **A second case: filler-gap and *whose***
   - The filler-gap mechanism
   - Independent relative *whose*: a gap that isn't
   - Stabilisers at multiple scales
   - Why the same constraints across languages?
   - **Bridge paragraph** (new this session)
   - Reciprocal maintenance
7. How to test whether a mechanism is real
8. Degrees of projectibility
9. What this commits us to
10. Refactoring, not replacing
11. The most telling facts (bridge to failure modes)

---

## Remaining issues (minor):

1. **Undefined references** to unwritten chapters (ch:word-classes, ch:what-changes, ch:failure-modes, etc.)
2. **Japanese glyphs** (って) — font doesn't have them; consider romanisation or font switch
3. **sec:4:payoffs** undefined — needs label in Chapter 4

---

## For next session:

1. **Add missing labels** (sec:2:where-essentialism-works, sec:4:payoffs, ch:kinds-without-essences, ch:failure-modes, ch:word-classes, ch:what-changes)
2. **Consider figure** for quotatives (S-curve of adoption, or cross-linguistic timeline)
3. **Continue to Chapter 8** (failure modes)
4. **Optional**: Fix Japanese glyph issue (romanise as "tte" or use font with CJK support)

---

## Bibliography additions this session:

- `aikhenvald2004` — Evidentiality (Oxford UP)
- `ide2005` — Japanese honorifics (John Benjamins)

---

## Branch status:

- **Branch:** `restructure-part-1`
- **Last commit:** `29a17e5`
- **PDF:** Compiled successfully with xelatex (45 pages)
- **Remote:** Pushed to origin

# Session Log: December 5, 2025 — Chapter 4 Review

**Branch**: `restructure-part-1`
**Pages**: 101
**Last commit**: `48b518f` (pushed to GitHub)

## Summary

Comprehensive review and polish of Chapter 4 ("Kinds without essences"), ensuring consistency with Chapter 5 and the stack.tex paper.

## Major Changes

### Content additions:
- Full chapter expansion (~245 lines, 10 sections)
- Stewart Brand epigraph on maintenance
- Spinning top analogy for dynamic stability
- Sign language phonology section (BSL, JSL, ISL, Kata Kolok, ISN)
- Figures: `4.sonority.png`, `4.hands.png` (with captions and refs)
- Parallel mechanisms table (biology vs linguistics)

### Citations added:
- Piantadosi 2024, Kallini et al 2024 (LLM distributional learning)
- Sandler 2006, Brentari 1998 (sign language phonology)
- Battison 1978, Senghas 2004/2005, Emmorey 2002, Marsaja 2008 (sign language)
- Boyd 1991/1999, Millikan 2017, Machamer 2000, Craver 2007
- Mayr 1959/1982, Rosch 1973/1978, Ohala 1990, Wilson 1999

### Terminology fixes:
- `\term{}` → `\mention{}` for word examples (fun, near, will, noun, etc.)
- "determiner" → "determinative" (lexical category, ~50 items)
- "HPC view" → "maintenance view" (3 places)
- "thin/thick" → "thin/fat/negative" per stack.tex
- "fuzzy boundaries" → "gradient structure near the boundaries"

### Stylistic improvements:
- Pivot paragraph: "without essences → with mechanisms"
- Softened noun-verb universality claim
- Replaced Pluto/planet → Larus ring species example
- Self-aware "feature not a bug" cliché
- "Extravagant toolkit" justification for Ch5 machinery
- Removed: "must" (2), contrastive "yet" (2), "need to" (1)

### Removals:
- All ISBN fields from references.bib (9)
- References stub section from chapter end
- Duplicate BibTeX entries

## Open items for future sessions:

1. **Biber warnings**: Duplicate entries (tomasello2003, bybee2010, chomsky1957, etc.) — need cleanup
2. **Chapter refs**: Forward refs to unwritten chapters (ch:failure-modes, ch:definiteness, etc.)
3. **Spinning top**: Orphan metaphor — could callback in Ch5 or leave as-is
4. **Chapter 5 polish**: Continue from where left off (advisory board items)

## Files modified:
- `chapters/chapter04.tex` (extensive)
- `references.bib` (~30 new entries, 9 ISBNs removed, duplicates fixed)
- `notes/book-slogans.md` (terminology section added)
- `.house-style/preamble.tex` (epigraph package)

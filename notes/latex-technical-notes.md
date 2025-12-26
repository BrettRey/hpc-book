# LaTeX Technical Notes

## Glossary Small Caps Issue (2025-12-26)

**Problem:** Glossary headwords were not rendering in small caps despite multiple attempts (`\glsnamefont`, category attributes, custom styles).

**Root Cause:** EBGaramond lacks a bold small caps font shape (`b/sc`). The `altlist` glossary style renders entry names inside `\item[]` which applies bold weight. When `\textsc{}` is applied, LaTeX silently falls back to bold (`b/n`) because the `b/sc` shape doesn't exist.

**Log evidence:**
```
LaTeX Font Warning: Font shape `TU/EBGaramond(0)/b/sc' undefined
(Font)              using `TU/EBGaramond(0)/b/n' instead on input line 5.
```

**Solution:** Switch to medium weight before applying small caps:
```latex
\AtBeginDocument{%
  \renewcommand*{\glossentryname}[1]{{\mdseries\textsc{\glsentryname{#1}}}}%
}
```

**Location:** `.house-style/preamble.tex` (lines 263–266)

**Lesson:** When `\textsc{}` appears to fail silently, check font shape warnings in the log. The font may lack the combined shape (e.g., `b/sc`, `bx/sc`).

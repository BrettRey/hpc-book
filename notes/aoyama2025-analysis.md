# Aoyama et al. 2025 — Induction Heads

**Paper:** `literature/aoyama2025-induction-heads.pdf`  
**Authors:** Tatsuya Aoyama, Ethan Gotlieb Wilcox, Nathan Schneider (Georgetown)  
**Venue:** NeurIPS 2025 Workshop (CogInterp)

## Summary

Studies when and why **induction heads** (specialized attention heads for in-context copying) form during LM training. Key findings:

1. Batch size × context size predicts IH formation point
2. Surface bigram repetition frequency/reliability strongly affect IH emergence
3. Categoriality and marginal distribution shape matter when frequency/reliability are low

## Relevance Assessment

**Marginal.** The paper demonstrates phase-transition-like emergence of discrete computational structures from continuous training dynamics — a computational analogy to HPC's core thesis.

**However:**
- Focused on LM internals, not linguistic categories
- Bridging from attention mechanisms to grammatical categories requires significant work
- Fedorenko 2024 papers already provide more directly relevant neural evidence

## Decision

**Skip for now.** Not integrated into book.

If computational/neural parallels become more central, could revisit for:
- Ch 5 (phase transitions, dynamic discreteness)
- Ch 14 (computational methodology)

---
*Reviewed: 2025-12-21*

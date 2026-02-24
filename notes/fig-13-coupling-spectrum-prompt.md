# Image Generation Prompt: Ch 13 Coupling-Tightness Spectrum

## Target file
`figures/13.coupling-spectrum.png`

## Specifications
- **Aspect ratio:** 1.83:1 landscape (2816 x 1536 px)
- **Style:** Scientific conceptual illustration, matte finish, no photorealism
- **No text labels** — all labelling is done in the LaTeX wrapper
- **Color progression:** Blue (left) → Teal → Amber → Red-orange (right)
- **Background:** Light warm gray, consistent with existing book figures

## Prompt (for Google Imagen / similar)

Scientific conceptual illustration, landscape format, four panels arranged left to right showing increasing structural looseness, separated by thin dashed vertical lines on a light warm-gray background.

**Panel 1 (leftmost — "Hard coupling"):** A rigid crystalline lattice of blue spheres connected by thick solid bonds, tightly interlocked like a mineral cross-section. Highly ordered, no gaps. Cool blue tones.

**Panel 2 ("Opaque coupling"):** Clusters of blue-green spheres connected by solid lines, but the clusters are separated by small gaps. The bonds within each cluster are strong; between clusters, connections are thinner and more sparse. Some spheres are isolated but nearby. Blue-green tones.

**Panel 3 ("Loose coupling"):** Two distinct cloud-like groupings of spheres (one teal, one amber) connected by flexible dashed lines that arc between them. The two clusters overlap partially at their edges, with some spheres shared between both colors. Teal and warm amber tones.

**Panel 4 (rightmost — "Composite coupling"):** A dispersed constellation of warm orange-red spheres with no direct bonds, instead connected by a translucent web of curved dotted lines radiating from a glowing central node. The pattern looks emergent — held together by the web, not by direct contact. Warm orange-red tones.

Style: clean scientific illustration, matte finish, no photorealism, no text labels. Consistent with academic textbook figures. Soft shadows, white background gradient. Blue-to-red color progression left to right.

## Visual reference
The existing `3.phase-transition.png` (ice → liquid → steam triptych) is the closest precedent in the book. Match its level of scientific illustration polish and clean panel layout.

## Alternative prompt (shorter, for models with token limits)

Four-panel scientific illustration, landscape 1.83:1 ratio. Left to right: (1) rigid blue crystalline lattice with thick bonds, (2) blue-green sphere clusters with sparse inter-cluster links, (3) two overlapping teal and amber clouds connected by dashed arcs, (4) dispersed orange-red spheres held by translucent web from glowing center. No text. Clean matte style, light gray background, blue-to-red progression.

## LaTeX integration
The placeholder is already in `chapters/chapter13.tex`. Replace the `\fbox{\parbox{...}}` block with:
```latex
\includegraphics[width=0.85\textwidth]{figures/13.coupling-spectrum.png}
```

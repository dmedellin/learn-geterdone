Use your image generation tool to create ONE image and save it as `video/art/simulation-and-variance-reduction/antithetic-variates/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about antithetic variates, pairing each uniform draw with its opposite so that a monotone quantity's two halves move in opposite directions. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the unit interval, axes and outlines; cyan (#37D7E7) for the draw and the monotone case that works; warm yellow (#FFC857) for the opposite draw and the symmetric case that fails; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. mirror-pair: a horizontal white line segment with a small tick at its midpoint, a cyan dot near the left end and a yellow dot at the mirror-image position near the right end, joined by a thin curved white arc.
2. step-monotone: white axes with a slate step function that is flat low on the left half and jumps to flat high on the right half, a cyan dot on the low part and a yellow dot on the high part at mirrored positions.
3. constant-means: a row of many small slate pairs of dots, one high and one low in each pair, with a single perfectly straight cyan horizontal line running exactly between them.
4. v-symmetric: white axes with a slate V-shaped curve whose lowest point is at the middle, a cyan dot and a yellow dot at the same height on opposite arms of the V.
5. opposite-signs: two balance beams side by side: on the left a beam perfectly level with a cyan and a yellow weight pulling opposite ways, on the right a beam tipped sharply with both weights stacked on the same side.
6. monotone-sampler: a cyan staircase that only ever climbs from left to right, with a white arrow running along the bottom from left to right and a matching arrow up the side.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/strings-and-pattern-matching/borders-and-the-failure-function/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about borders and the Knuth-Morris-Pratt failure function: the longest prefix of each part of a pattern that is also its suffix, and why sliding by it never skips a match. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for a border: the matching start and end of a string; warm yellow (#FFC857) for the mismatch, or the slide to the next alignment; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. border-overlap: one row of seven blank slate tiles with a cyan rounded bracket over its first three tiles and an identical cyan bracket over its last three tiles.
2. rise-and-collapse: a row of seven square cells containing small cyan columns that rise in height step by step across the middle and then drop to nothing at the sixth cell, which is yellow.
3. slide-by-border: a long row of blank text tiles with a pattern row above it; a faint copy of the pattern shows where it was, and a cyan copy shows it slid right so that its first three tiles sit under the faint copy's last three.
4. fallback-chain: three rounded cyan bars of decreasing length stacked top to bottom, each starting at the same left edge, joined by short curved white arrows from each bar to the next shorter one.
5. two-columns: two tall columns of square cells side by side, every pair of neighbouring cells identical in shade, cyan throughout, joined by thin white horizontal lines.
6. off-by-one: a row of square cells holding small cyan columns of varied heights, beside the same row where one column is shorter than it should be and drawn yellow.

When done, reply with the saved file path and pixel size only.

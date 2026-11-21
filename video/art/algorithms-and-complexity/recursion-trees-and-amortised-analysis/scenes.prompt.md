Use your image generation tool to create ONE image and save it as `video/art/algorithms-and-complexity/recursion-trees-and-amortised-analysis/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about recursion trees, which add up a recursion's work level by level, and amortised analysis, which shows a doubling array is cheap on average over any sequence of insertions. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the cheap, ordinary work; warm yellow (#FFC857) for the rare expensive step, or the part that dominates; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. uneven-tree: a recursion tree of rounded cyan bars drawn top down, where each bar splits into a short left piece and a longer right piece; every level has the same total width, and the right-hand branch reaches deeper than the left, joined by thin white lines.
2. shrinking-levels: a recursion tree drawn as stacked levels of bars: a wide yellow bar at the top, and each level below has twice as many cyan bars but a much smaller total width, so the levels shrink quickly toward the bottom.
3. doubling-array: a column of rows of slate cells, each row twice as long as the one above (one cell, two, four, eight), with white arrows copying the cells down from each row to the next and the newest cell in each row in yellow.
4. cost-spikes: a long white baseline with many short cyan bars standing on it in a row, and occasional tall yellow spikes, each spike taller than the last and the gaps between spikes doubling in length.
5. credit-coins: a row of slate cells on a white baseline, each with a small stack of cyan coins resting on top, and a white arrow carrying a coin from one cell to a yellow cell on the right.
6. fixed-steps: a dense column of rows of slate cells, each row only a little longer than the one above, with many white copy arrows packed between them, the longest row at the bottom in yellow.

When done, reply with the saved file path and pixel size only.

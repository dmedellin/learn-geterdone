Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/one-row-and-the-direction-of-the-loop/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the one-row knapsack: collapsing the table to a single array, where sweeping it backward uses each item once and sweeping it forward lets items be reused. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for cells already updated in this pass; warm yellow (#FFC857) for the cell being updated now and the cell it reads; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. row-above: two horizontal rows of square cells, the upper row cyan and the lower row slate with one yellow cell, two white arrows reaching up from the yellow cell to two cells in the upper row; faint empty rows above are dashed outlines.
2. backward-sweep: a single row of twelve square cells with a long white arrow running right to left above it; the cells to the right are cyan, one yellow cell is being updated, and a short white arrow reaches from it to a slate cell further left that is untouched.
3. forward-sweep: a single row of twelve square cells with a long white arrow running left to right above it; the cells to the left are cyan, one yellow cell is being updated, and a short white arrow reaches from it back to a cyan cell already updated.
4. stacking: a single row of square cells with small identical blocks stacked inside them, the stacks growing taller every two cells from left to right, all cyan.
5. lost-pointers: a single row of cyan cells with, above it, faint dashed white arrows that fade out and break apart into the background.
6. two-arrows: one row of square cells drawn twice, one above the other; the upper copy has a white arrow pointing left, the lower copy a yellow arrow pointing right.

When done, reply with the saved file path and pixel size only.

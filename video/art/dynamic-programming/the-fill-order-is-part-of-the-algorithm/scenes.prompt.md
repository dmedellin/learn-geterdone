Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/the-fill-order-is-part-of-the-algorithm/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the matrix-chain table: choosing the cheapest way to bracket a product of matrices, and why filling the table in the wrong order gives a cheaper, wrong answer without any error. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for cells already filled correctly; warm yellow (#FFC857) for a cell read before it was written, or the cell being filled now; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. chain-bracketing: a row of six slate rectangles of different widths and heights standing for matrices, with white curved brackets grouping them in nested pairs above the row.
2. last-split: the same row of six slate rectangles split into two groups by a vertical yellow line, each group wrapped in a cyan rounded outline.
3. diagonal-fill: a six by six square grid where only the upper right triangle is used; cells along the main diagonal and the next two diagonals are cyan, the rest of the triangle slate, the lower triangle empty.
4. row-fill: a six by six square grid filled row by row from the top: the whole first row is cyan except one yellow cell, with a white arrow from that yellow cell to an empty slate cell in the second row.
5. full-table: two six by six grids side by side: the left has only its upper triangle filled cyan, the right has every cell filled, with several cells drawn yellow.
6. catalan-growth: a row of small bracket diagrams growing in number from left to right, one, then two, then five, then many tiny ones packed together.

When done, reply with the saved file path and pixel size only.

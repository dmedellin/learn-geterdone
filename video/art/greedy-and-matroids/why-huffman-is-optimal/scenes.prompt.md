Use your image generation tool to create ONE image and save it as `video/art/greedy-and-matroids/why-huffman-is-optimal/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about why Huffman's code is optimal: two exchange lemmas on binary trees, an induction, and a brute-force check over every tree shape and every placement of the weights. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for leaves already in their final place; warm yellow (#FFC857) for the two leaves being swapped or merged; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. deepest-siblings: a full binary tree of white dots and branches, uneven in depth, with two yellow sibling leaves hanging from the same node at the very deepest level.
2. downhill-swap: a binary tree of white dots and branches where a large slate leaf near the bottom and a small yellow leaf near the top are joined by a curved two-headed white arrow, showing them trading places.
3. merge-leaf: two panels side by side: on the left a tree with a single cyan leaf; on the right the same tree with that leaf opened into a small node with two yellow child leaves beneath it.
4. induction-ladder: a row of four binary trees of increasing size from left to right, each one a single node larger than the last, joined by small white arrows.
5. every-shape: a neat grid of many tiny different binary tree shapes drawn in slate, with one of them drawn in cyan.
6. tree-cost: a binary tree of white dots and branches with leaves at different depths, each leaf a slate circle sized by its weight, and thin white horizontal guide lines marking each depth level.

When done, reply with the saved file path and pixel size only.

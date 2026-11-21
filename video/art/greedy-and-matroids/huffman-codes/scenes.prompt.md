Use your image generation tool to create ONE image and save it as `video/art/greedy-and-matroids/huffman-codes/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about Huffman codes: repeatedly merging the two lightest weights into a binary tree, so that common symbols get short codewords and rare ones long codewords. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for leaves and the paths already built; warm yellow (#FFC857) for the two lightest trees being merged, or the symbol being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. prefix-tree: a binary tree drawn top down with small white circle nodes and white branch lines, every leaf a cyan dot, each internal node having exactly two children.
2. merge-lightest: a row of slate circles of different sizes standing for weights; the two smallest circles are yellow and joined by two white lines to a new slightly larger circle above them.
3. weighted-leaves: a lopsided binary tree of dots and branches where one large cyan leaf sits just one step below the root, and two tiny yellow leaves sit at the deepest level.
4. equal-weights: a perfectly balanced binary tree of white dots and branches with four equal-size cyan leaves all on the same bottom level.
5. full-tree: a full binary tree of white dots and branches with every internal node having two children, beside a single square split into slate pieces of halves, quarters and eighths that fill it exactly with no gap.
6. bit-stream: a long horizontal row of small square slate boxes, broken into groups of different lengths by short white gaps, the first group cyan and one later group yellow.

When done, reply with the saved file path and pixel size only.

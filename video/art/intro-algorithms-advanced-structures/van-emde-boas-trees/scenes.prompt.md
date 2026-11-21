Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-advanced-structures/van-emde-boas-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about van Emde Boas trees, which split each integer key into a cluster and a position and recurse into a universe of square-root size. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for clusters, summary bits and the single path of recursion; warm yellow (#FFC857) for the min and max kept aside and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bit-vector: one long row of sixteen small blank boxes, a few of them filled cyan and the rest slate.
2. clusters-and-summary: a short row of four boxes on top, two of them cyan, with white lines down to four rows of four boxes each below, the cyan summary boxes leading to rows that hold cyan boxes.
3. halving-bits: five horizontal bars stacked top to bottom, each half the length of the one above, in cyan, shrinking to a tiny square.
4. two-calls: a nested set of squares, each containing a smaller summary square and smaller cluster squares; at every level two white arrows go down, one into the summary and one into a cluster, branching wider and wider in slate.
5. min-kept-out: the same summary-over-clusters picture with one yellow box lifted out above it on its own and a second yellow box at the top right corner, the clusters below cyan and slate.
6. one-path-down: nested squares like a target, with one single thick white arrow passing straight down through the levels into the smallest cyan square.

When done, reply with the saved file path and pixel size only.

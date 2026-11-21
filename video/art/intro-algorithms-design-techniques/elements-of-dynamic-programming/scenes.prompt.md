Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-design-techniques/elements-of-dynamic-programming/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about optimal substructure, overlapping subproblems and the longest simple path. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the parts of a solution and the stored subproblems; warm yellow (#FFC857) for the shared vertex or the piece being swapped; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. cut-paste: a long white path made of short segments between dots, with one middle segment lifted out above it in slate and a shorter cyan segment being dropped into its place.
2. subproblem-space: a single row of small cyan dots on the left, and on the right a triangular grid of cyan dots, larger and wider, showing a two-dimensional space.
3. shortest-split: a small graph of white dots and arrows with one path from a left dot to a right dot drawn in cyan, passing through a middle dot drawn in yellow that splits it into two parts.
4. path-clash: four white dots joined by six white arrows, with two paths traced on top, one cyan and one slate, both passing through the same dot, which is yellow.
5. recursion-repeats: a large wide tree of white dots where several identical small subtrees appear again and again in different branches, each copy outlined in yellow.
6. memo-table: a tree of white dots with most branches cut short and ending in small white arrows that point into a neat row of cyan table cells beside it.

When done, reply with the saved file path and pixel size only.

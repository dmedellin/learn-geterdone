Use your image generation tool to create ONE image and save it as `video/art/data-structures/the-shape-problem-and-random-bsts/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about how the insertion order decides the shape of a binary search tree. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the path a new key walks; warm yellow (#FFC857) for the key just inserted or the root chosen; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. insert-walk: a binary tree of slate dots with a cyan path from the root down to an empty white outlined spot at the bottom, where a yellow dot is landing.
2. sorted-path: a long diagonal chain of fifteen slate dots each the right child of the last, going down and to the right across the whole cell, the last dot yellow.
3. three-trees: three trees of the same number of slate dots side by side: a long diagonal path, a medium irregular tree, and a short perfectly balanced tree.
4. random-root: a row of slate dots with one yellow dot picked out and lifted up as a root, with white branches to two smaller groups of dots on its left and right.
5. online-stream: a stream of slate dots arriving one by one along a white conveyor line from the left into a tree that is growing into a long diagonal path.
6. depth-bands: a medium binary tree of slate dots with horizontal cyan bands behind each level and a white dashed horizontal line below the middle of the tree.

When done, reply with the saved file path and pixel size only.

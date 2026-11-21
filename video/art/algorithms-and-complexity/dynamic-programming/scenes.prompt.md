Use your image generation tool to create ONE image and save it as `video/art/algorithms-and-complexity/dynamic-programming/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about dynamic programming: when a recursion solves the same subproblems again and again, storing each answer once turns exponential work into polynomial work. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for subproblems already solved and stored; warm yellow (#FFC857) for the subproblem being computed now, or the repeated work being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. fib-tree: a wide branching recursion tree drawn top down with small circle nodes and white lines, where several identical-looking subtrees appear again and again in different places, each repeated subtree drawn in yellow and the rest in slate.
2. coin-table: a horizontal row of seven square slate cells; the first six are filled cyan, the seventh on the right is yellow, and three curved white arrows reach back from earlier cyan cells to the yellow cell.
3. lcs-grid: a square grid of small cells, most filled cyan, with a yellow staircase path of cells stepping diagonally from the top left corner to the bottom right corner.
4. path-graph: a small network of slate circle nodes joined by white lines; a short direct route between two nodes is cyan, and a long winding route between the same two nodes that visits many other nodes is yellow.
5. memo-table: on the left a small branching tree of slate circles with white lines, and on the right a neat column of cyan cells; white arrows run from the tree's nodes into the cells, and one yellow cell is being filled.
6. two-rows: a tall table of many rows of cells; all the upper rows are faint slate, and only the bottom two rows are bright cyan, with the very last cell yellow.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/overlapping-subproblems-and-the-memo/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about overlapping subproblems: a recursion that asks the same few questions thousands of times, and a memo that answers each one once. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for answers already stored; warm yellow (#FFC857) for the repeated work, or the answer being looked up; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. repeated-subtrees: a wide recursion tree of small slate circle nodes and white lines drawn top down, with the same small subtree shape appearing in yellow in four different places.
2. memo-lookup: on the left a branching tree of slate dots; on the right a neat vertical column of cyan cells; several white arrows from tree nodes point into the same cyan cell.
3. dependency-graph: a row of eighteen small slate dots in a line, each joined by curved white arcs to up to three earlier dots, the arcs from the last dot cyan.
4. coin-table: a grid of four rows by nineteen columns of small square cells, all cyan except one yellow cell in the bottom row, with one white arrow from the cell above it and one from a cell to its left in the same row.
5. crossing: plain white axes with a gentle cyan straight line and a steep yellow curve that starts below it and crosses above it.
6. merge-sort-tree: a balanced binary tree of slate dots splitting cleanly in halves at every level, no two subtrees alike, beside an empty column of slate cells with nothing pointing into it.

When done, reply with the saved file path and pixel size only.

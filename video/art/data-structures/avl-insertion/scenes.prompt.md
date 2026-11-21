Use your image generation tool to create ONE image and save it as `video/art/data-structures/avl-insertion/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about inserting into an AVL tree, the four rebalancing cases, single and double rotations. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the path back up from the new leaf and the rotation arrows; warm yellow (#FFC857) for the unbalanced node and the grandchild that rises; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. walk-back: a binary tree of slate dots with a new yellow leaf at the bottom and a cyan arrow climbing back up its path to the root.
2. single-rotation: on the left three slate dots in a straight diagonal line leaning left, the top one yellow; a curved cyan arrow; on the right the same three dots as a balanced little tree with the middle dot on top.
3. single-fails: three slate dots in a zigzag, top dot yellow, its left child, and that child's right child; a curved cyan arrow leads to a second zigzag that leans the other way, with a white warning ring around it.
4. double-rotation: three panels in a row joined by two cyan curved arrows: a zigzag of three dots, then a straight diagonal line of three dots, then a balanced little tree with the formerly middle yellow dot on top.
5. path-vs-avl: on the left a long diagonal chain of ten slate dots; on the right a short balanced tree of ten slate dots only four levels tall.
6. four-cases: four tiny three-dot shapes in a row: a diagonal leaning left, a diagonal leaning right, a zigzag left then right, and a zigzag right then left, each with a yellow top dot.

When done, reply with the saved file path and pixel size only.

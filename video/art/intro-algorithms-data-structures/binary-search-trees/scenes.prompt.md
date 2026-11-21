Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-data-structures/binary-search-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about binary search trees, search paths, successors and deletion. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the left subtree and the path being followed; warm yellow (#FFC857) for the node being found, moved or deleted; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bst-property: a binary tree of white dots and branches with a soft cyan region wrapped around the whole left subtree of the root and a soft slate region around the whole right subtree, the root yellow.
2. search-path: a binary tree of slate dots and white branches with one path from the root going left, right, then left drawn in cyan and ending at a yellow dot.
3. successor-climb: a binary tree of slate dots with a small yellow dot low in a left subtree and a cyan path of white arrows climbing up from it to an ancestor, which is reached from its left child and outlined in yellow.
4. delete-cases: three small trees of white dots side by side; in the first, a dot with only a right subtree; in the second, a dot with only a left subtree; in the third, a dot with two subtrees; the dot to delete is yellow in each.
5. successor-lift: a binary tree with a yellow node at the top of the drawing being replaced by a cyan node lifted up along a curved white arrow from deep in its right subtree, the leftmost node there.
6. chain-vs-bushy: on the left a long diagonal chain of yellow dots each with one child; on the right a short bushy balanced tree of cyan dots holding the same number of dots.

When done, reply with the saved file path and pixel size only.

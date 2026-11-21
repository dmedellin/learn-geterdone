Use your image generation tool to create ONE image and save it as `video/art/data-structures/binary-search-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about binary search trees, the subtree invariant, and deletion by successor. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the search path and correct subtrees; warm yellow (#FFC857) for the node being searched for, deleted or out of place; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. subtree-rule: a binary tree of slate dots with a node near the top, its whole left subtree enclosed in one cyan rounded outline and its whole right subtree enclosed in another.
2. search-path: a binary tree of slate dots over four levels with a cyan path running from the root down through three branches to a yellow dot.
3. bad-tree: a small tree of four slate dots: a root, its left and right child, and one dot hanging as the right child of the left child, that last dot yellow with a white warning ring.
4. successor: a binary tree where a yellow dot in the middle has two children; a cyan path goes from it one step right and then down-left as far as possible to a cyan dot with no left child, and a curved white arrow carries that dot back up to the yellow node's place.
5. path-tree: a long diagonal chain of slate dots each joined to the next by a single white branch going down and to the right, a path seven dots long.
6. inorder-walk: a binary tree of slate dots with a cyan dotted line weaving around it from left to right, and below it a row of blank slate boxes the dotted line drops into in order.

When done, reply with the saved file path and pixel size only.

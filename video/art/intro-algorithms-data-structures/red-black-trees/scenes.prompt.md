Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-data-structures/red-black-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about red-black trees, their five colour properties and rotations. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the leaves and the subtrees being moved; warm yellow (#FFC857) for the red nodes (shown yellow; slate nodes are the black ones); muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. nil-sentinel: a small binary tree of slate and yellow dots whose missing children are drawn as thin white lines that all run down to one single cyan square at the bottom.
2. rb-tree: a binary tree of eight dots, some slate and some yellow, with no yellow dot joined to another yellow dot, and tiny cyan squares as leaves under the lowest dots.
3. short-long-paths: two vertical paths of dots side by side: a short one of three slate dots, and a long one of six dots alternating slate and yellow, both ending at a cyan square.
4. rotation: two small trees side by side with a curved white arrow between them; on the left a parent dot with a right child, on the right the child lifted to the top with the old parent as its left child, three small cyan triangles as subtrees in both.
5. bad-red-pair: a binary tree of slate and yellow dots where one yellow dot has a yellow child directly below it, the link between them drawn thick in white.
6. black-count: a binary tree of slate and yellow dots with a thin cyan path traced from the root to each leaf, every path passing the same number of slate dots.

When done, reply with the saved file path and pixel size only.

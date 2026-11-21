Use your image generation tool to create ONE image and save it as `video/art/integer-programming/branch-and-bound/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about branch and bound for integer programmes: splitting on a fractional variable, bounding each child with a linear programme, and closing nodes. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes, tree branches and outlines; cyan (#37D7E7) for the feasible regions and open nodes; warm yellow (#FFC857) for the fractional point, the best whole plan and the one node being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. lp-corner: crossed white axes with a cyan shaded four-sided region bounded by two slanted lines, and a yellow dot on the corner where those lines meet, between grid positions.
2. branch-split: the same cyan region cut into two separate pieces by removing a narrow vertical strip; the yellow dot floats inside the empty strip, belonging to neither piece.
3. fixed-vs-inequality: two horizontal rows of small evenly spaced slate dots; in the top row only two neighbouring dots are cyan; in the bottom row every dot is cyan, split into a left group and a right group by one narrow gap.
4. three-closures: three separate slate dots in a row: the first drawn as an empty dashed outline, the second with a flat yellow bar resting just above it, the third a solid filled cyan dot.
5. search-tree: a tree of five dots: one root at the top joined by white lines to two children, and the left child joined to two children of its own; one of the bottom dots is yellow.
6. pruned-branch: the same five-dot tree with two of its leaf dots faded and a short thick yellow bar cutting across each of the white lines leading to them.

When done, reply with the saved file path and pixel size only.

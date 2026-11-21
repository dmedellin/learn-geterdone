Use your image generation tool to create ONE image and save it as `video/art/graphs-and-trees/graph-traversal/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about breadth-first and depth-first search of a graph. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) solid dots for the vertices and rounded lines of even weight for the edges; cyan (#37D7E7) for the search tree and the vertices already visited; warm yellow (#FFC857) for the starting vertex, the back edge or the one branch being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bfs-ripples: a yellow start dot in the centre with three faint slate concentric rings around it, white dots sitting on each ring, and cyan edges joining each dot to one dot on the ring inside it.
2. queue-vs-stack: on the left a horizontal row of slate rounded chips with a cyan arrow entering at the right end and a cyan arrow leaving from the left end; on the right a vertical pile of slate chips with a yellow arrow entering and a yellow arrow leaving at the top.
3. dfs-deep-branch: a tree of white dots growing downward from a yellow root dot, with one long branch going very deep traced in cyan, and the shorter side branches faint slate.
4. two-search-trees: the same graph drawn twice side by side: four dots on a square with a tail of two more dots from one corner; on the left all edges cyan except one side of the square, which is faint slate; on the right a different side of the square is faint slate and the rest cyan.
5. back-edge-cycle: a cyan search tree of white dots going down from a root, with one yellow curved dashed edge running from a deep dot back up to the root, closing a loop.
6. components-search: two separate clusters of white dots, each with its own yellow start dot and its own cyan tree spreading from it, with an empty gap between the clusters.

When done, reply with the saved file path and pixel size only.

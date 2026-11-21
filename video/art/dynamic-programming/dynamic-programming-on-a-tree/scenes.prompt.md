Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/dynamic-programming-on-a-tree/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about dynamic programming on a tree: the heaviest set of vertices with no two joined by an edge, found in one bottom-up pass by keeping two numbers at each vertex. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the vertices chosen for the set; warm yellow (#FFC857) for the vertex being decided, or a conflict between neighbours; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. independent-set: a small tree of white dots and branches drawn top down where several dots, none of them joined to each other, are filled cyan and the rest slate.
2. with-without: one parent dot with three child dots below; on the left copy the parent is cyan and all children slate, on the right copy the parent is slate and the children are a mix of cyan and slate.
3. disjoint-subtrees: a tree of dots and branches whose root has three subtrees, each subtree enclosed in its own separate rounded slate outline, the outlines not touching.
4. postorder: a tree of dots and branches with a curved white arrow tracing around it, the bottom leaves cyan, one middle dot yellow, and the root still slate.
5. alternate-levels: a tree of dots drawn in horizontal levels, every second level fully cyan, with one heavy large dot on an uncoloured level drawn yellow.
6. cycle-edge: a small tree of dots and branches with one extra yellow line joining two dots in different subtrees, closing a loop.

When done, reply with the saved file path and pixel size only.

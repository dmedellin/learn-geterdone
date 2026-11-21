Use your image generation tool to create ONE image and save it as `video/art/data-structures/rotations-and-the-avl-invariant/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about tree rotations and the AVL balance condition. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the subtree that changes parent and the pointers that move; warm yellow (#FFC857) for the node that rises; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. rotate-right: two small trees side by side with a curved white arrow between them; on the left a slate dot with a yellow left child and three small slate triangles as subtrees; on the right the yellow dot is on top, the slate dot is its right child, and the middle cyan triangle has moved across under the slate dot.
2. rotate-example: two trees of six slate dots side by side; the left one leans down to the left over four levels, the right one is three levels and nearly even, with a yellow dot at its root.
3. rotation-impossible: a single slate dot with only a right branch and an empty dashed white outline where a left child would be, with a small white stop bar beside it.
4. sparse-avl: a lopsided but balanced tree of slate dots, the left side one level deeper than the right at every node, with thin cyan bars beside each pair of subtrees showing heights that differ by one.
5. fib-growth: a row of slate bars growing taller left to right, each bar's height the sum of the two before it, with a smooth cyan curve over their tops.
6. table-vs-formula: two vertical cyan bars of nearly equal height side by side, the right one slightly taller, with a thin white horizontal line across the top of the shorter one.

When done, reply with the saved file path and pixel size only.

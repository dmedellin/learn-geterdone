Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-graphs/all-pairs-shortest-paths/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about all-pairs shortest paths by matrix products, Floyd-Warshall's interior vertices, and Johnson's reweighting. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for matrix cells already final and the arcs of a shortest path; warm yellow (#FFC857) for the interior vertex being allowed in and the cells it improves; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. distance-matrix: a four by four grid of blank square cells, a few filled cyan, the rest slate, with a short white arrow on the right showing one extra column being added.
2. interior-vertices: two dots at the left and right with a direct slate route between them, and a second route bending through a yellow dot in the middle, drawn in cyan.
3. path-rebuilt: four dots arranged in a square with one cyan route threading through three arcs from one corner round to its neighbour, the other arcs thin slate.
4. reweight: an extra slate dot at the top with thin white arrows down to four dots, each dot with a small vertical bar beside it of a different height.
5. same-shift: two different routes between the same two dots, one short and one long, each with a yellow bar beside it raised by exactly the same amount.
6. loop-order: three nested rounded rectangles like stacked frames, the outermost yellow, the inner two cyan.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/graphs-and-trees/shortest-paths/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about shortest paths in a weighted graph and Dijkstra's algorithm. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) solid dots for the vertices and rounded lines of even weight for the edges; cyan (#37D7E7) for the settled vertices and the routes being compared; warm yellow (#FFC857) for the cheapest route, the vertex being settled or the one edge being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. cheap-vs-few: a white start dot on the left and an end dot on the right, joined by two routes: an upper route of two long cyan edges through one middle dot, and a lower route of five short yellow edges through four small dots.
2. settle-frontier: a pale slate rounded region on the left holding several cyan dots joined by cyan edges, with white dots outside it and one dot on its edge turning yellow as the next to be settled.
3. relax-edge: one white target dot on the right reached by two routes: an old long route drawn as a faint dashed slate line, and a new cheaper route through a nearby cyan dot drawn as a solid yellow line with an arrow.
4. worked-route: four white dots in a diamond: a start dot on the left, an end dot on the right, and an upper and a lower dot; cyan edges join the start to both middle dots, the lower to the upper, and both middle dots to the end; the route start to lower to upper to end is thick yellow.
5. negative-edge-trap: a triangle of three white dots with cyan edges, one corner yellow as if already finished; a yellow curved arrow takes the long way round the other two sides back to it, arriving too late.
6. priority-queue: a small binary tree of slate rounded chips, smaller chips nearer the top, with the single top chip yellow and a white arrow lifting it out.

When done, reply with the saved file path and pixel size only.

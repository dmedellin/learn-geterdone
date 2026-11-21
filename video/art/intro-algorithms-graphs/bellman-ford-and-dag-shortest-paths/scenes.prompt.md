Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-graphs/bellman-ford-and-dag-shortest-paths/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about single-source shortest paths by relaxation, with Bellman-Ford's rounds and one pass over a dag in topological order. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for arcs of the shortest-paths tree and settled vertices; warm yellow (#FFC857) for the arc being relaxed and the negative cycle; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. negative-cycle: a directed graph of dots where a small closed loop of three arcs is drawn in yellow with a spiral arrow inside it going round and round, the rest slate.
2. relax-arc: two dots joined by one yellow arrow; above the right dot a tall slate bar drops down to a shorter cyan bar, showing the estimate lowered.
3. rounds: the same small directed graph of dots drawn four times in a row, left to right, with more of its arcs turning cyan in each copy.
4. topo-pass: five dots in one straight horizontal row with arcs curving forward between them, a white sweeping arrow passing along the row from left to right once.
5. shortest-tree: a directed graph of dots where one root dot is yellow and a cyan tree of arrows branches out from it to every other dot, the leftover arcs thin slate.
6. reverse-order: the same horizontal chain of dots drawn twice, the top copy with one long white arrow sweeping left to right, the bottom copy with several short white arrows going back and forth.

When done, reply with the saved file path and pixel size only.

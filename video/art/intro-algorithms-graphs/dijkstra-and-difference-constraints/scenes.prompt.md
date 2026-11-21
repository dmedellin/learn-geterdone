Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-graphs/dijkstra-and-difference-constraints/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about Dijkstra's algorithm settling the nearest vertex first, and systems of difference constraints solved as shortest paths. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the settled set and its tree arcs; warm yellow (#FFC857) for the next vertex to settle, a negative arc and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. settled-set: a graph of dots with a soft cyan rounded region enclosing three dots near the source and their cyan arcs; the nearest outside dot is yellow.
2. leaving-s: the same cyan region with a long dashed white route leaving it through one arc and wandering off and back to a dot just outside, clearly longer.
3. negative-trap: four dots; one dot inside the cyan settled region has a short yellow arc pointing back at it from a later dot outside, too late.
4. constraint-graph: a single extra slate dot at the left with thin white arrows fanning out to three dots, and white arcs between those three dots.
5. shift-solution: three vertical bars of different heights on a baseline, then the same three bars all raised by the same amount, the gaps between their tops unchanged, joined by a white arrow.
6. queue-choices: three small containers side by side: a flat row of boxes, a small binary tree of dots, and a loose bunch of small trees on a loop, the middle one cyan.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-graphs/topological-sort-and-strong-components/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about topological sorting of a dag by finish time and splitting a digraph into strongly connected components. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for vertices and arcs in order or inside a component; warm yellow (#FFC857) for the source component, the vertex that finishes last and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. dag-in-a-line: six dots in one straight horizontal row with white arcs curving above and below them, every arc pointing to the right.
2. components: a directed graph of dots with three soft rounded outlines enclosing groups of dots, each group joined inside by arrows forming loops, and a few arrows between groups going one way only.
3. source-component: four rounded groups of dots in a chain of white arrows left to right; the leftmost group is yellow and has no arrow coming into it.
4. wrong-order: a yellow dot on the left with a white arrow running into a cluster of slate dots, where a dashed outline wrongly lumps the yellow dot and the cluster together.
5. reversed-arcs: the same small directed graph drawn twice side by side, all arrows in the right copy pointing the opposite way.
6. finish-stack: a vertical stack of blank cyan boxes with a yellow box being placed on the very top, and a white arrow pointing down onto it.

When done, reply with the saved file path and pixel size only.

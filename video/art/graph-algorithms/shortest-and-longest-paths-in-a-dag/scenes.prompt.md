Use your image generation tool to create ONE image and save it as `video/art/graph-algorithms/shortest-and-longest-paths-in-a-dag/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about shortest and longest paths in a directed acyclic graph, one relaxation per arc in topological order, and slack. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for arcs already relaxed and the chosen route; warm yellow (#FFC857) for the critical path; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. tails-first: slate dots in a horizontal line with white arrows all pointing right, and a cyan sweep moving left to right, the dots behind the sweep cyan.
2. no-cycle: on the left a horizontal line of dots with forward arrows only; on the right a loop of dots with a small white spiral climbing endlessly upward, crossed with a short white stroke.
3. critical-path: a project-like digraph of slate dots from one start dot to one end dot, with one route along it thick and yellow and a parallel route thinner and cyan.
4. backward-pass: the same digraph with a white sweep moving from right to left, starting at the end dot.
5. cycle-refused: three dots in a loop of white arrows with a white stop bar beside it and an empty row of slots.
6. slack-bars: horizontal bars for tasks in a timeline, most tightly packed end to end, two of them with a small gap of empty space after them.

When done, reply with the saved file path and pixel size only.

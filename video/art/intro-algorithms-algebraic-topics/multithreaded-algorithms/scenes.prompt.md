Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-algebraic-topics/multithreaded-algorithms/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about multithreaded algorithms measured by work and span, with a greedy scheduler on several processors. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for strands and the work being done; warm yellow (#FFC857) for the critical path, the span; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. strand-dag: a small directed acyclic graph of seven rounded boxes joined by white arrows, splitting into two branches and joining again, all cyan.
2. greedy-steps: four horizontal lanes stacked like tracks, each filled with short cyan blocks; a few gaps where some lanes are empty slate.
3. serial-merge: a tree of boxes splitting downward in parallel, then one single very long yellow box at the bottom where everything merges, much longer than the rest.
4. parallel-merge: two rows of boxes with one yellow box picked from the middle of the longer row and a white arrow to a matching gap in the shorter row, each side then splitting into two separate cyan merges.
5. span-floor: a descending curve of cyan dots flattening onto a horizontal yellow floor line, never crossing it.
6. race: two cyan arrows from two separate boxes both pointing at one single slate box, with a small yellow jagged spark where they meet.

When done, reply with the saved file path and pixel size only.

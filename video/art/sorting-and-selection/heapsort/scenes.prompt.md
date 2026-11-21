Use your image generation tool to create ONE image and save it as `video/art/sorting-and-selection/heapsort/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about heapsort: building a max-heap in place, then swapping the root to the end. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the growing sorted suffix; warm yellow (#FFC857) for the root key being swapped to the end; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. max-heap: a complete binary tree of slate dots of decreasing size from the top, the largest dot at the root yellow.
2. heap-and-suffix: a long row of boxes split by a white vertical marker: on the left jumbled slate boxes, on the right cyan boxes in increasing height, with a curved white arrow carrying a yellow box from the far left into the first slot of the cyan section.
3. build-vs-teardown: two vertical bars side by side, a short slate bar and a much taller cyan bar.
4. long-moves: a row of boxes with a long white arc carrying a box from the far right all the way to the far left, jumping over many boxes.
5. swap-down: a small tree of slate dots with a yellow dot at the root and a cyan curved arrow carrying it down to a leaf.
6. equal-flip: two equal-height boxes trading places along crossed white arrows above a row.

When done, reply with the saved file path and pixel size only.

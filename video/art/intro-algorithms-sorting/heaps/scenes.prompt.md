Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-sorting/heaps/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about binary heaps and building a heap in linear time. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the nodes and array cells already in heap order; warm yellow (#FFC857) for the value that sinks and the root holding the largest value; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. array-as-tree: a row of seven blank boxes along the bottom and above it a binary tree of seven white dots, with thin white curves joining each box to its dot.
2. heap-tree: a binary tree of white branches with a large yellow dot at the root and cyan dots below that get smaller level by level.
3. sift-down: a binary tree of slate dots with one yellow dot at the top and a cyan path of short white arrows taking it down two levels, swapping places with a larger dot at each step.
4. build-order: a row of eight blank boxes whose right half is cyan, and a long white arrow under the left half pointing right to left, starting at the last slate box and ending at the first, which is yellow.
5. height-layers: a binary tree with a very wide bottom row of many cyan leaf dots, a narrower row above, a narrower one above that, and a single yellow root dot at the top.
6. loose-vs-tight: two vertical bars side by side on a white baseline, a tall slate bar and a much shorter cyan bar, with a small yellow marker resting exactly on top of the cyan bar.

When done, reply with the saved file path and pixel size only.

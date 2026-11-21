Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-sorting/heapsort-and-priority-queues/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about heapsort and priority queues built on a max-heap. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the sorted part of the array and the waiting items in the queue; warm yellow (#FFC857) for the root key being moved and the one item being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. root-to-end: a row of ten blank boxes, the first yellow, the last three cyan, with a long curved white arrow swapping the first box with the last slate box before the cyan run.
2. shrinking-heap: a binary tree of slate dots on the left getting smaller and a row of cyan boxes on the right getting longer, with a white arrow from the tree to the row.
3. unstable: two rows of boxes, before and after; in the top row two equal-height boxes, one cyan on the left and one yellow on the right; in the bottom row the same two boxes with the yellow now on the left, and a crossing white arrow between them.
4. job-queue: a binary tree of slate dots with a yellow dot lifting out of the top along a white arrow, and beside the tree a short queue of blank cyan tickets waiting in a line.
5. increase-key: a binary tree of slate dots where one low dot is yellow and a cyan path of short white arrows carries it upward toward the root, swapping with its parent at each step.
6. insert-slot: a binary tree of slate dots with one new small yellow dot added at the bottom row's next free place on the right, joined by a dashed white branch, with a short white upward arrow above it.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-sorting/quicksort/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about quicksort, the partition procedure and how evenly the pivot splits. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the keys at most the pivot and the even, balanced splits; warm yellow (#FFC857) for the pivot and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. pivot-regions: a row of ten blank boxes in four regions: three cyan boxes, then three slate boxes, then three boxes with only white outlines, and at the far right a yellow box.
2. partition-step: a row of ten blank boxes with two small white arrow markers beneath it, one under the end of a cyan run on the left and one further right, and a curved white arrow swapping a box just right of the cyan run with the box above the second marker.
3. worst-split: a tree of white dots where each dot has only one child, forming a long diagonal chain from top left to bottom right, the chain dots yellow.
4. sorted-input-trap: a row of seven boxes rising steadily from short to tall like a staircase, with the tallest box at the far right coloured yellow and every other box slate.
5. even-split: a balanced binary tree of white dots and branches four levels deep, each dot splitting into two equal halves, the dots cyan.
6. lopsided-split: a tree of white dots where every dot splits into one very short branch and one long branch, so the tree leans heavily to one side, with its longest path drawn in yellow.

When done, reply with the saved file path and pixel size only.

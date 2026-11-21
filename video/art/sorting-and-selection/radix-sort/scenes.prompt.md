Use your image generation tool to create ONE image and save it as `video/art/sorting-and-selection/radix-sort/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about least-significant-digit radix sort, a stable counting sort per digit. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the digit position being sorted in the current pass; warm yellow (#FFC857) for keys whose order is decided by an earlier pass; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. digit-passes: three stacked rows of seven blank slate cards, each card divided into three small blank segments; in the top row the right segment of every card is cyan, in the middle row the middle segment, in the bottom row the left segment; white arrows between rows.
2. suffix-sorted: a row of seven cards each with three blank segments, the right two segments cyan and visibly ordered in shade, the left segment slate and unordered.
3. stable-ties: two cards with an identical cyan left segment keeping their order as they slide down white arrows into a sorted row.
4. msd-overwrite: three stacked rows of cards where the bottom row's order scrambles the top row's arrangement, with a white crack line between the second and third rows.
5. base-tradeoff: two bar groups side by side: on the left many short passes drawn as many thin bars, on the right a few passes drawn as few thick bars with wide bins underneath.
6. bucket-row: ten small slate bins in a row with cards dropping into them along cyan arrows, in order.

When done, reply with the saved file path and pixel size only.

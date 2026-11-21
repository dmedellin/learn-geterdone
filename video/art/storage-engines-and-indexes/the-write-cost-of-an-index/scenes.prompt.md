Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/the-write-cost-of-an-index/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about why every secondary index adds a random write to each insert, so k indexes divide a table's insert throughput by k plus one. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for the device's write budget and the inserts it delivers; warm yellow (#FFC857) for the index writes each insert must also make; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. insert-fanout: one slate row block on the left with a white arrow into a table box and further yellow arrows scattering to several separate index boxes at different heights.
2. scattered-pages: a large grid of white outlined pages, with one cyan page in the table area and several yellow pages scattered far apart across the grid.
3. divided-bar: a long horizontal bar split into four equal parts, one cyan and three yellow.
4. share-curve: white axes with a cyan curve dropping steeply at first and then flattening out, a series of small dots along it with big gaps at the left and small gaps on the right.
5. unused-index: a row of white outlined index boxes each receiving a yellow arrow, one of them faded slate with no outgoing arrow yet still receiving its yellow arrow.
6. floor-steps: a white staircase descending from left to right with wide flat treads, and a cyan dot sliding along one tread toward its edge.

When done, reply with the saved file path and pixel size only.

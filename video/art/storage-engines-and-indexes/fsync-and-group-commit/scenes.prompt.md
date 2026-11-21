Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/fsync-and-group-commit/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about why durable writes are limited by how many fsyncs a device can do, and how grouping commits behind one fsync raises that limit at a latency cost. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for commits waiting and being acknowledged; warm yellow (#FFC857) for the fsync that makes them durable; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. page-cache-gap: a white outlined memory box holding slate blocks above a stack of white disk cylinders, with a dashed white gap between them and a yellow arrow that has not yet crossed.
2. one-per-fsync: a row of small cyan blocks each followed by its own short yellow bar, evenly spaced along a white timeline.
3. grouped-batch: a cluster of many small cyan blocks gathered inside a white bracket, followed by one single yellow bar on a white timeline.
4. growing-backlog: a white outlined box with a yellow bar inside, and in front of it a line of cyan blocks stretching off the edge and getting longer.
5. two-waits: two curves on white axes, a cyan straight line rising steadily and a yellow curve falling steeply then flattening, crossing near the middle.
6. u-curve: white axes with a single cyan curve shaped like a wide valley, falling and then rising, a white dot at its lowest point.

When done, reply with the saved file path and pixel size only.

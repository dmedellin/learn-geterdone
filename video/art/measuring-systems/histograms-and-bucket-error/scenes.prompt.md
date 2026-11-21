Use your image generation tool to create ONE image and save it as `video/art/measuring-systems/histograms-and-bucket-error/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about why a percentile read from a latency histogram is only known to the width of its bucket, and how geometric bucket boundaries set that width. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for bucket counts and the boundaries; warm yellow (#FFC857) for the bucket a percentile lands in, the interval it is known to; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. counts-not-values: a scatter of small slate dots dropping into a row of white outlined bins, each bin showing only a cyan bar of its count, the dots vanishing as they land.
2. geometric-edges: a long white horizontal line with tick marks whose spacing doubles from left to right, the gaps growing steadily wider.
3. rank-walk: a row of white outlined bins of different heights in cyan, with a white arrow stepping along their tops from the left and stopping at one bin highlighted in yellow.
4. interval-not-point: a white horizontal scale with a wide yellow bracket spanning one bucket, and a small cyan dot sitting inside it toward the left end.
5. finer-buckets: two rows of tick marks one above the other, the lower row with ticks three times as dense, and a narrower yellow bracket below the wider yellow bracket above.
6. more-traffic-same-width: two identical rows of bins, the right row with every bar ten times taller, and the same width yellow bracket over one bin in both.

When done, reply with the saved file path and pixel size only.

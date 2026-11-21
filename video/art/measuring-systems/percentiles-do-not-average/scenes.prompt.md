Use your image generation tool to create ONE image and save it as `video/art/measuring-systems/percentiles-do-not-average/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about why the average of per-host latency percentiles is not the fleet percentile, and what to merge instead. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for individual request latencies, merged into one sample; warm yellow (#FFC857) for per-host summary numbers that get averaged; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. three-hosts: three white outlined server boxes, two small ones holding a handful of short cyan bars each and one large one holding a tall dense stack of longer cyan bars.
2. merge-sample: many short and long cyan bars pouring from three boxes into one long white sorted row, ordered from shortest to longest.
3. average-summaries: three small yellow dots at very different heights joined by thin white lines to one yellow dot at their average height, below a thin white line marking the true middle.
4. votes-vs-requests: a white balance with three equal yellow dots on one pan, and on the other pan a large heap of small cyan squares with two tiny heaps beside it.
5. bounded-range: a white vertical scale with a short yellow tick at the bottom and a short yellow tick at the top, and a cyan dot somewhere between them, with a white bracket spanning the two ticks.
6. merge-histograms: three short stacks of white outlined bins being added together bin by bin into one taller stack of cyan bins.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/queues-and-utilisation/token-buckets-and-rate-limiting/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about token-bucket rate limiting compared with a fixed-window counter. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the bucket, timelines and outlines; cyan (#37D7E7) for the tokens and the admitted requests; warm yellow (#FFC857) for the rejected requests and the burst across a boundary; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bucket-refill: a white bucket with a level line, small cyan token discs dripping steadily into it from above, and a few discs inside.
2. window-boundary: a white timeline with tall white vertical boundary lines at even intervals; just before one boundary a cluster of four cyan dots, just after it a cluster of five more, all inside a yellow bracket of one window's width straddling the line.
3. downstream-burst: a white limiter box on the left sending a sudden thick clump of cyan arrows into a white server box on the right, with a queue piling up in front of it.
4. capped-level: a white bucket filled exactly to a white cap line at its rim, with extra cyan discs falling from above bouncing off and spilling away.
5. shaper: a white bucket with a short line of slate squares waiting in front of it, each one released through a narrow opening only when a cyan token is present.
6. rejected-arrivals: a row of arriving squares meeting a white gate; cyan ones pass through, yellow ones are turned back with a short curved arrow.

When done, reply with the saved file path and pixel size only.

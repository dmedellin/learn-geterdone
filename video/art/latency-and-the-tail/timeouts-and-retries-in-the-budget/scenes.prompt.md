Use your image generation tool to create ONE image and save it as `video/art/latency-and-the-tail/timeouts-and-retries-in-the-budget/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about choosing a timeout and retry count that fit a latency budget, and the good calls a timeout throws away. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes, outlines and cut lines; cyan (#37D7E7) for the calls that finish in time; warm yellow (#FFC857) for the good calls the timeout kills and the retry; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. timeout-cut: a row of vertical bars on white axes for a latency histogram, tall on the left and thinning to the right; a vertical white dashed line cuts through it, with cyan bars before the line and yellow bars after it.
2. retry-pair: two horizontal timeline bars end to end: a cyan bar stopped by a white dashed line, then a yellow bar of the same length starting right after it, all inside a white bracket.
3. gap-in-distribution: a histogram with a cluster of cyan bars at the left, one short bar further along, a long empty stretch, then a single lone bar far to the right; a white dashed line sits in the empty stretch.
4. mean-timeout: a histogram of cyan bars with a white dashed line placed right after the tallest bars, so that a large group of bars beyond it are yellow.
5. overloaded-retry: a single white server box drawn heavy and crowded with slate blocks, with a cyan arrow and then a yellow arrow both pointing into it.
6. budget-box: a long white-outlined box with two equal cyan and yellow blocks inside it, and a third block outside the box, faint slate, that does not fit.

When done, reply with the saved file path and pixel size only.

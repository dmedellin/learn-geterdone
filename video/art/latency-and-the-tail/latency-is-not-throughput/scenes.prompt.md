Use your image generation tool to create ONE image and save it as `video/art/latency-and-the-tail/latency-is-not-throughput/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about the difference between latency and bandwidth, and the bandwidth-delay product where they cross. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the pipes, outlines and arrows; cyan (#37D7E7) for the data in flight; warm yellow (#FFC857) for the round-trip waiting time; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. pipe-length-width: two white pipes stacked: the top one long and thin, the bottom one short and very wide, each with a curved yellow arrow running its full length and back.
2. bytes-in-flight: one long white pipe completely filled end to end with small cyan packets, with a curved yellow arrow above it showing the trip there and back.
3. crossover: white axes with two straight lines: a flat yellow line across the middle and a rising cyan line starting at zero, crossing it at a single white dot.
4. same-forty: two horizontal stacked bars, one short and one long, each made of a yellow segment and a cyan segment; the yellow segments are exactly the same length in both.
5. small-transfer: a long white pipe with only a few cyan packets near its far end and a long empty stretch behind them, the curved yellow return arrow dominating the picture.
6. wide-pipe-same-wait: two white pipes of the same length but very different widths, both with identical yellow return arrows, and the same small cluster of cyan packets in each.

When done, reply with the saved file path and pixel size only.

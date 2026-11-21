Use your image generation tool to create ONE image and save it as `video/art/queues-and-utilisation/the-knee/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about response time against utilisation for a single server, and the knee as utilisation approaches one. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes, asymptote and outlines; cyan (#37D7E7) for the response-time curve; warm yellow (#FFC857) for the chosen operating point and the headroom; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. hyperbola: white axes with a cyan curve that stays low and nearly flat across most of the width, then shoots up steeply, hugging a vertical white dashed line near the right edge.
2. headroom-axis: a horizontal white axis with three yellow gaps at its right end, each a tenth the width of the one before, and above them three cyan bars each ten times taller than the last.
3. capacity-target: the same cyan curve on white axes with one yellow dot sitting on it well before the steep part, and a horizontal yellow stretch of headroom between the dot and the dashed line.
4. doubling-two-ways: two copies of the curve side by side: on the left a dot moves a short way along the flat part; on the right a dot near the steep part is pushed past the dashed line and off the top.
5. tail-beyond-mean: the cyan curve with a thinner, fainter slate curve sitting above it, rising even more steeply.
6. queue-at-high-load: a single white server box with a long line of cyan squares waiting in front of it, stretching off to the left.

When done, reply with the saved file path and pixel size only.

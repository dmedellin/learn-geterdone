Use your image generation tool to create ONE image and save it as `video/art/queues-and-utilisation/bounded-queues-and-loss/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about a bounded queue that drops arrivals when full, its loss rate, its latency cap and its admitted rate. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the buffer outlines, server box and arrows; cyan (#37D7E7) for the admitted requests; warm yellow (#FFC857) for the dropped requests; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bounded-buffer: a white server box with a short white-outlined buffer in front of it holding exactly four cyan squares, full, and one yellow square bouncing off the buffer's entrance.
2. dropped-arrivals: a stream of squares arriving from the left; most are cyan and enter a white buffer, while about one in eight is yellow and falls away downward.
3. uniform-states: a row of five white circles joined by arrows, each with a cyan bar of exactly the same height beneath it.
4. bufferbloat: a white server box with an extremely long buffer stretching far to the left, packed with cyan squares, the oldest ones at the front faded to slate.
5. short-vs-deep: two panels: on the left a short buffer with a few yellow squares turned away quickly; on the right a very long buffer full of cyan squares slowly creeping forward.
6. boundary-crossing: a dashed white rectangle around a buffer and server; cyan arrows cross into the rectangle while yellow arrows stop at its edge and turn away.

When done, reply with the saved file path and pixel size only.

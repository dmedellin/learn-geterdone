Use your image generation tool to create ONE image and save it as `video/art/queues-and-utilisation/many-servers-and-pooling/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about pooling several servers behind one shared queue compared with giving each server its own queue. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the server boxes, lanes and outlines; cyan (#37D7E7) for the shared, pooled queue; warm yellow (#FFC857) for the separate queues and the idle server; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. separate-vs-pooled: two panels: on the left four white server boxes each with its own short line of yellow squares; on the right the same four boxes fed by one single line of cyan squares.
2. idle-while-waiting: four white server boxes each with its own line; one box is empty with no line at all, drawn in yellow outline, while the line next to it holds several slate squares waiting.
3. seconds-vs-ratio: white axes with two rising lines, a steep yellow one and a gentle cyan one, the gap between them widening towards the right.
4. pinned-sessions: four white server boxes with thin white threads tying particular slate squares in the queue to particular boxes, and one cyan line trying to feed all four.
5. dispatcher: one cyan queue feeding a small white diamond-shaped dispatcher that sends arrows out to four white server boxes.
6. four-servers: four identical white server boxes side by side, each holding one cyan square.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-concurrency-and-session-state/optimistic-and-pessimistic-control/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about optimistic and pessimistic concurrency control: an optimistic lock detects a conflict at commit, while a pessimistic lock prevents it by letting one session edit at a time. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the work each session does; warm yellow (#FFC857) for a lock or a detected conflict; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. optimistic-copies: one slate document in the centre with two cyan copies drawn out to each side; one copy's white arrow goes back into the document cleanly, the other copy's arrow stops at a bold yellow jagged mark just before the document.
2. pessimistic-lock: one slate document with a yellow padlock shape on it and a cyan copy joined to it by a white line on the left; on the right a second cyan dot waits behind a short white barrier.
3. session-timeline: two long parallel horizontal white lanes, each with a few small cyan dots spaced along it and one small yellow bar near its right end, the two bars at slightly different points.
4. read-write-locks: on the left one slate document with many thin white lines to a ring of small cyan dots; on the right the same document with a single thick yellow line to one cyan dot and nothing else.
5. deadlock: two slate boxes side by side, each with a cyan dot holding it by a short line, and two curved white arrows crossing between them, each dot reaching for the other's box, forming a closed loop.
6. version-steps: one slate document with a short row of small slate ticks beside it, and the newest tick at the end of the row drawn in yellow, slightly taller than the others.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/synchronous-writes-wait-for-the-slowest/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about synchronous replication, where a write is acknowledged only when the slowest follower replies. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the arrows, timelines and axes; cyan (#37D7E7) for follower replies that arrive quickly; warm yellow (#FFC857) for the slowest reply that holds the write; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. fan-out: one slate leader cylinder on the left sending white arrows at the same moment to two slate follower cylinders on the right; one reply arrow back is short and cyan, the other is long and yellow
2. parallel-vs-serial: two diagrams stacked: on top three bars laid end to end in a long row, on the bottom three bars stacked on top of each other starting at the same point, with only the longest one in yellow
3. leader-only: a slate leader cylinder holding a small glowing yellow block, with dashed white arrows to two follower cylinders that have not yet received it
4. tail-mass: white axes with a tall cyan bar at the left, a medium cyan bar next to it, then a long thin tail of tiny bars to the right ending in a small yellow bar
5. power-curve: white axes with two rising staircase curves, the lower one in yellow sitting only slightly below the upper one in cyan, both reaching the top
6. shared-switch: two slate follower cylinders both connected by white lines to a single small slate switch box with a yellow glow on it

When done, reply with the saved file path and pixel size only.

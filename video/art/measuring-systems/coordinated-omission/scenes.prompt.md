Use your image generation tool to create ONE image and save it as `video/art/measuring-systems/coordinated-omission/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how a closed-loop load generator stops sending requests during a stall and so hides the slow requests its percentile is meant to capture. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for requests the generator actually measured; warm yellow (#FFC857) for requests that were due during the stall and never sent; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. closed-loop: a white circle of arrows going from a slate client dot to a server box and back, with one small cyan request travelling around it.
2. stall-gap: a white timeline with small cyan request marks evenly spaced, then a long empty stretch with a single wide slate block, then the evenly spaced cyan marks resuming.
3. missing-requests: the same timeline, with the long empty stretch now filled by many small yellow request marks evenly spaced, each with a short yellow line rising above it, tallest at the left of the stretch and shortest at the right.
4. staircase-waits: a descending staircase of thin yellow vertical bars from tall on the left to short on the right, standing on a white baseline.
5. clock-driven: a round white clock shape emitting a steady row of small cyan request marks along a timeline, unaffected by a slate block in the middle of the line.
6. open-vs-closed: two panels side by side, on the left an open white funnel with arrows pouring in from outside, on the right a closed white loop of a few slate dots each waiting on its own arrow.

When done, reply with the saved file path and pixel size only.

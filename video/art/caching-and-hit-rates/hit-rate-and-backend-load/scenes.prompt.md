Use your image generation tool to create ONE image and save it as `video/art/caching-and-hit-rates/hit-rate-and-backend-load/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about hit rate and backend load, where a cache splits a stream of requests and the backend sees only the misses. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the arrows, pipes and axes; cyan (#37D7E7) for the requests served from the cache; warm yellow (#FFC857) for the misses that reach the backend; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. split-stream: a thick white pipe of many small cyan dots flowing left to right into a rounded slate box; most dots stay inside the box and a thin trickle of yellow dots continues out of its right side into a tall slate block
2. shrinking-misses: three rows, one above another, each with the same wide cyan stream entering a slate box from the left; the yellow stream leaving each box gets thinner row by row, the bottom one a single thin line
3. scale-of-points: a long white horizontal ruler with tick marks; near the left end two ticks are joined by a tiny yellow bar, and near the right end two ticks the same distance apart sit above a huge yellow bar that drops downward
4. wait-knee: white axes with a cyan curve that stays low and nearly flat across most of the width and then sweeps up steeply near the right edge; one yellow dot sits high on the steep part and another on the flat part
5. hot-key-burst: a slate box with a steady thin yellow trickle leaving it to the right, and in the middle of the trickle one sudden thick yellow burst like a wave, heading at a tall slate block
6. cache-wall: a tall slate wall in the middle with a crowd of cyan dots bouncing back from its left face and a single small gap letting a thin yellow line through to a slate block on the right

When done, reply with the saved file path and pixel size only.

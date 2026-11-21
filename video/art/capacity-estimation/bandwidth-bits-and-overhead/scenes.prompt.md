Use your image generation tool to create ONE image and save it as `video/art/capacity-estimation/bandwidth-bits-and-overhead/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about bandwidth in bits per second, and the fixed per-request cost of headers. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, pipes and arrows; cyan (#37D7E7) for the payload; warm yellow (#FFC857) for the headers and overhead; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bits-and-bytes: one slate square block on the left with a white arrow pointing right to a neat row of eight small cyan squares, the same block broken into eight pieces.
2. header-and-payload: a row of packets travelling right along a white pipe; each packet is a long cyan block with a short yellow block fixed to its front end.
3. crossover-point: three packets stacked vertically: a long cyan block with a short yellow head, then a cyan block exactly as long as its yellow head, then a tiny cyan block behind a much bigger yellow head.
4. split-requests: on the left one long cyan block with one yellow head; a white arrow points right to five short cyan blocks, each with its own yellow head of the same size as before.
5. link-pipe: a wide white-outlined pipe running left to right, filled with a stream of small cyan and yellow packets.
6. fixed-toll: a white gate across a road with a yellow block placed in front of every packet passing through it, small packets and large packets alike, the yellow blocks all the same size.

When done, reply with the saved file path and pixel size only.

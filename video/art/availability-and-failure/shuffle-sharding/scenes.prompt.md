Use your image generation tool to create ONE image and save it as `video/art/availability-and-failure/shuffle-sharding/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about shuffle sharding, where each tenant gets a random small set of nodes so few tenants ever share all of them. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the grid lines, outlines and connecting lines; cyan (#37D7E7) for healthy nodes a tenant can still use; warm yellow (#FFC857) for the poisoned node and anything that loses everything; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. fixed-shards: a grid of sixteen small slate squares grouped in eight fixed pairs by white outlines; one pair is filled entirely yellow
2. random-subsets: a grid of sixteen small slate squares with several thin white curves each connecting two scattered squares in different places, like random pairs
3. one-left: a pair of node squares joined by a white line; the left square is yellow and the right square is cyan and still glowing
4. blast-radius: a grid of sixteen node squares with one yellow square in the middle and thin white lines from it to a few scattered dots representing tenants, each of which also connects to a cyan square elsewhere
5. two-levers: two white sliders on slate tracks, one knob moved left and one moved right, beside a small cyan bar and a small yellow bar of opposite sizes
6. poison-request: a single yellow arrow entering one slate node square, which cracks, while the neighbouring squares remain cyan

When done, reply with the saved file path and pixel size only.

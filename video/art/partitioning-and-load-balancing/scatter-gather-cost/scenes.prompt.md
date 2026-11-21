Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/scatter-gather-cost/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about what a query costs when it cannot be routed to one shard and must ask all of them, in request rate and in latency. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for ordinary shard requests and fast answers; warm yellow (#FFC857) for the slowest shard answer and the routed path; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. scatter-fan: one white rounded router box on the left with many thin cyan arrows fanning out to a column of small white shard boxes on the right, and arrows returning to the router.
2. routed-one: one white rounded router box on the left with a single thick yellow arrow going to exactly one shard box in a column of shard boxes, the rest untouched slate.
3. request-multiplier: one small slate square on the left, a white arrow, and on the right a large grid of many identical small cyan squares.
4. slowest-answer: many short cyan horizontal bars stacked and aligned at the left, one bar much longer in yellow, and a white vertical line at its end where a white gather bracket closes.
5. consumer-ceiling: a row of white outlined partition boxes each with one slate worker dot beneath it, and one extra worker dot at the end in yellow standing alone with nothing above it.
6. key-choice: two panels side by side, each a column of shard boxes; on the left a yellow arrow reaches one box, on the right cyan arrows reach every box, with a curved white arrow between the panels showing them swap.

When done, reply with the saved file path and pixel size only.

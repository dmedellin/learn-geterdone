Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-concurrency-and-session-state/the-value-of-statelessness/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about the value of statelessness: a server object that keeps nothing between requests can serve anyone, so a small pool can do the work of one object for each idle user. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for a session's state, such as a cart; warm yellow (#FFC857) for an object that is busy serving a request; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. field-between-calls: one slate box with a small cyan square kept inside it, a white arrow entering from the left and another arriving later from the left, the cyan square still sitting in the box between them.
2. stateful-pinned: a column of small cyan dots on the left, each joined by its own white line to its own slate box on the right, ten pairs in all, with only one box filled yellow.
3. pooled-objects: many small cyan dots on the left sending white arrows into three slate boxes on the right, all three boxes filled yellow.
4. peak-bunching: a long horizontal white timeline with short vertical ticks bunched into tight clusters at a few places and bare stretches between them.
5. cart-in-store: one empty slate box with white arrows passing through it, and beside it a slate cylinder holding a cyan basket shape.
6. idle-grid: a grid of thirty small slate squares, most of them dim outlines and only a few filled yellow.

When done, reply with the saved file path and pixel size only.

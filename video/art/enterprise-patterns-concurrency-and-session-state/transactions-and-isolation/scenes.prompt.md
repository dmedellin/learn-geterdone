Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-concurrency-and-session-state/transactions-and-isolation/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about transactions and isolation levels: what a transaction promises a reader, and which read errors each weaker isolation level lets through. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the boundaries of a transaction; warm yellow (#FFC857) for another session's change that leaks through as a read error; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. request-transaction: a horizontal white timeline with three short slate segments for requests; the first segment is wrapped tightly in a cyan bracket, and a second, much longer dashed cyan bracket stretches over all three.
2. isolation-ladder: four wide slate steps descending from left to right, the top step solid with nothing passing through, and each lower step with one more small yellow drop falling through a gap in it.
3. phantom-row: a slate table of five plain horizontal rows, with a sixth row appearing at the bottom drawn as a yellow dashed outline.
4. business-vs-system: one long cyan arc spanning the top of the cell, and beneath it a row of four short slate brackets, each closed and separate, the last one filled solid.
5. threads-processes: on the left three separate slate bubbles, each holding its own small square; on the right one large slate square shared by three thin white lines from three small dots.
6. all-or-nothing: two rows of four small boxes; the top row all filled cyan, the bottom row all empty white outlines, with a curved white arrow from the end of the bottom row back to its start.

When done, reply with the saved file path and pixel size only.

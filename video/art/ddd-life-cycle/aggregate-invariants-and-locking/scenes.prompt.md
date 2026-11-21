Use your image generation tool to create ONE image and save it as `video/art/ddd-life-cycle/aggregate-invariants-and-locking/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-design education video about aggregate invariants under concurrent change, where locking single objects lets two correct edits break a rule that spans the group, and locking the whole aggregate keeps it. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the aggregate boundary and a lock on the whole group; warm yellow (#FFC857) for an edit, and a total that has gone over its limit; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. order-lines: a slate rounded rectangle like an order sheet holding four horizontal slate bars of different lengths, with a thin white limit line drawn across near the top.
2. two-copies: two identical slate order sheets side by side, each with a different single bar turned yellow, and beneath them one merged sheet whose stacked bars rise above a white limit line.
3. deadlock: two slate padlock shapes facing each other with white arrows forming a closed circle between them, each waiting on the other.
4. copied-price: a slate part shape on the left with a small cyan tag; a white arrow copies the tag into a bar inside a dashed cyan boundary on the right that encloses an order sheet.
5. refused-wait: a dashed cyan boundary with a cyan padlock on it enclosing three slate bars, and outside it a single yellow bar held back by a short white stop line.
6. limit-bar: three stacked slate blocks of different heights forming one column that reaches exactly up to a white horizontal limit line, with no block above it.

When done, reply with the saved file path and pixel size only.

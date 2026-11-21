Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/linearizability-by-enumeration/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about linearizability, checked by listing every order of a short history of overlapping operations. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the timelines, interval bars and outlines; cyan (#37D7E7) for orders and operations that are legal; warm yellow (#FFC857) for the operation that cannot be explained; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. intervals: three horizontal interval bars on separate rows above a white time axis; the top two overlap, the bottom one starts just after the top one ends
2. per-op-check: three interval bars, each with a small cyan tick mark beside it, as if each one passed a check on its own
3. zero-survivors: six small rows of three blank boxes each; three rows are greyed out in slate and the other three each have one box filled yellow
4. pruned-search: a white branching tree of dots spreading left to right, with most branches cut short by small slate bars and one path continuing in cyan
5. forced-pair: two interval bars on separate rows with a clear gap between the end of the first and the start of the second, and a bold white arrow from the first to the second
6. factorial-wall: a row of slate bars growing so fast from left to right that the last bar shoots off the top of the cell

When done, reply with the saved file path and pixel size only.

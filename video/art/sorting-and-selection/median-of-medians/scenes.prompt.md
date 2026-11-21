Use your image generation tool to create ONE image and save it as `video/art/sorting-and-selection/median-of-medians/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about the median-of-medians pivot and deterministic linear-time selection. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the elements guaranteed to be on one side of the pivot; warm yellow (#FFC857) for the group medians and the chosen pivot; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. groups-of-five: a long row of slate dots split into small columns of five, each column with its middle dot yellow.
2. three-below: several columns of five dots sorted so their yellow middle dots line up in a row; in the left half of the columns the yellow dot and the two dots below it are cyan, forming a block.
3. shrinking-levels: a recursion tree of horizontal bars where each level's total width is visibly a little narrower than the level above, tapering to a point.
4. flat-levels: a recursion tree of horizontal bars where every level has exactly the same total width, forming a tall rectangle that never narrows.
5. middle-band: a row of slate bars in increasing height with a cyan band covering the middle portion and a yellow bar inside it.
6. two-calls: a large slate bar with two curved white arrows below it pointing to a small bar and a larger bar, together slightly narrower than the original.

When done, reply with the saved file path and pixel size only.

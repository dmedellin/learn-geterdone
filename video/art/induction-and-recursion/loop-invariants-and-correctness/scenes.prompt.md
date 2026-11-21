Use your image generation tool to create ONE image and save it as `video/art/induction-and-recursion/loop-invariants-and-correctness/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about loop invariants, statements a loop keeps true on every pass, used to prove the loop correct. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the part of the data the loop has already handled; warm yellow (#FFC857) for the item being handled now, or what the loop preserves; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. loop-cycle: a thick white circular arrow forming a closed loop, with a solid yellow diamond token riding on it and small cyan tick marks spaced evenly around the loop.
2. running-total: a row of square cells across the top, the first few cyan and the rest slate; white arrows run down from the cyan cells into one growing yellow stack of blocks below them.
3. sorted-prefix: a row of vertical bars on a white baseline; the left part is cyan bars in increasing height, the right part is slate bars of jumbled heights, and one yellow bar is lifted above the boundary between them.
4. flattened-bars: on the left a row of cyan bars of varied heights in increasing order; on the right the same number of bars all squashed to the same tiny flat height in slate; a white arrow points from left to right.
5. rectangle-squares: a long slate rectangle repeatedly cut into the largest squares that fit, each cut-off square outlined in white and filled cyan, ending in one tiny yellow square in the corner.
6. invariant-scale: a simple flat white balance scale held perfectly level while the cyan weights on both pans are swapped for smaller cyan weights, shown as two stages side by side, with a yellow pointer at the centre that stays upright.

When done, reply with the saved file path and pixel size only.

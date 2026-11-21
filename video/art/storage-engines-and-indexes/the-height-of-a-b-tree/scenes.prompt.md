Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/the-height-of-a-b-tree/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how many levels a B-tree needs to hold a billion keys, and how many disk reads a lookup costs once the top levels are cached. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for tree levels that live on disk; warm yellow (#FFC857) for the top levels held in memory by the page cache; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. wide-tree: a tree drawn as dots and branches, one dot at the top with very many thin branches spreading to a wide row of dots, each of which spreads again into an even wider row.
2. descent-path: a tree of dots and branches with four rows, one path from the top dot to a bottom dot drawn thick, with a small white square page beside each dot on the path.
3. level-sizes: four horizontal bars stacked from top to bottom, each enormously wider than the one above, the top bar tiny and the bottom bar running nearly the full width.
4. cached-top: a tree of four rows of dots, the top two rows drawn in yellow inside a rounded white outline, the lower two rows in cyan below it.
5. narrow-vs-wide: two trees side by side, on the left a tall thin binary tree with many rows of dots, on the right a short wide tree of only a few rows with many branches per dot.
6. multiply-steps: four white outlined boxes in a row, each one much larger than the one before, joined by white arrows, the last box drawn in yellow.

When done, reply with the saved file path and pixel size only.

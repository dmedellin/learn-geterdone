Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/edit-distance-and-performing-the-script/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about edit distance: the fewest inserts, deletes and substitutions that turn one word into another, filled in a table and then checked by carrying the edits out. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for cells already filled, and characters kept; warm yellow (#FFC857) for the cell being filled, or the character being edited; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. three-neighbours: a square grid of cells, mostly cyan, with one yellow cell and three white arrows reaching into it from the cell above, the cell to the left, and the cell diagonally up and left.
2. row-major-safe: a square grid filled row by row from the top, the filled cells cyan and the remaining cells slate, with one yellow cell at the edge of the filled region whose three neighbours above and to the left are all already cyan.
3. perform-script: two rows of square blank tiles, the upper row of six slate tiles and the lower row of seven, with white arrows from each upper tile to a lower tile; two of the lower tiles are yellow replacements and one extra lower tile at the end is yellow, the rest cyan.
4. run-vs-cost: two panels side by side: on the left two equal slate bars standing level; on the right a row of blank tiles being carried one by one along a white track from left to right, one tile yellow, the rest cyan.
5. pointer-path: a square grid with a cyan staircase path of cells from the bottom right corner to the top left corner, moving diagonally most of the time with one straight step left.
6. tile-rows: two rows of blank rounded tiles one above the other, nearly identical, with three tiles in the lower row drawn yellow and the rest cyan.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming/subsets-as-a-table-and-where-it-loses/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the Held-Karp table for the travelling salesman problem, indexed by a set of visited cities and the current city, and the small sizes at which it still does more work than trying every route. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the shortest route found, or cities already visited; warm yellow (#FFC857) for the city being reached next, or the leg home; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. tour-loop: four white dots placed at the corners of a loose quadrilateral, joined by a closed cyan loop that visits each dot once, with one leg of the loop yellow.
2. subset-index: a set of dots, some enclosed together in a rounded slate outline and filled cyan, with one dot at the edge of the outline yellow, and a few slate dots outside it.
3. order-forgotten: two different wiggly white paths through the same cluster of cyan dots, both ending at the same yellow dot, one of them drawn faint as if discarded.
4. crossing-late: plain white axes with a cyan curve and a steeper yellow curve; the yellow curve stays below the cyan one for a long way and crosses above it only near the right edge.
5. all-orders: a fan of many small closed loops through the same four dots, each a different route, all slate except one cyan.
6. leg-home: an open path of white lines through four dots in a row of hops, with the final return leg back to the first dot drawn dashed yellow.

When done, reply with the saved file path and pixel size only.

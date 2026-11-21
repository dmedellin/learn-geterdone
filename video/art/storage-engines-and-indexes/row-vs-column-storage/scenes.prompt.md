Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/row-vs-column-storage/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how many bytes a scan reads in a row store and in a column store, and the query shape that reverses the answer. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for the columns a query actually needs; warm yellow (#FFC857) for bytes read that the query never asked for; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. row-layout: a grid of white outlined cells, several rows long and many columns wide, with whole horizontal rows highlighted as one continuous run, three columns in each row cyan and the rest of each row yellow.
2. column-layout: the same grid redrawn as separate vertical strips spaced apart, only three of the strips filled cyan and the rest left slate and untouched.
3. compress-column: one tall vertical strip of many identical small slate squares squeezing through a white funnel into a much shorter cyan strip.
4. compress-row: one horizontal row of mixed shapes, a circle, a triangle and a square, passing through a white funnel and coming out only slightly shorter.
5. whole-row-fetch: on the left one horizontal row read with a single white arrow; on the right the same row's values scattered across many vertical strips, each reached by its own white arrow.
6. two-workloads: a white balance with a wide flat slate scan bar on one pan and a single small row block on the other pan, the beam level.

When done, reply with the saved file path and pixel size only.

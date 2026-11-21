Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/hash-vs-tree-for-ranges/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about comparing a hash index and a B-tree on a workload that mixes point lookups with range queries, counted in page reads. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for the B-tree and its ordered path; warm yellow (#FFC857) for the hash index and the pages it has to read; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. hash-bucket: a slate dot with one short white arrow straight into a single highlighted yellow page in a long row of white outlined pages.
2. full-scan: a long row of many white outlined pages, every one of them filled yellow, with a white sweeping arrow running beneath the whole row.
3. tree-descent: a tree of dots and branches with three rows, one thick cyan path from the top down to a bottom dot, which sits in one cyan leaf page.
4. leaf-walk: a row of white outlined leaf pages at the bottom of a small tree, a cyan path descending to one leaf and a short cyan arrow along the row to its neighbour.
5. balance-tip: a white balance beam on a slate pivot with a heavy yellow block on one end and a light cyan block on the other, the yellow end pressed down.
6. scrambled-order: on the left a neat row of small slate squares in a gentle rising staircase, an arrow, and on the right the same squares scattered at random heights.

When done, reply with the saved file path and pixel size only.

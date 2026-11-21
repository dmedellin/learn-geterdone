Use your image generation tool to create ONE image and save it as `video/art/data-structures/open-addressing-and-linear-probing/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about open addressing with linear probing, deletion with tombstones, and clustering. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the probe path and stored keys; warm yellow (#FFC857) for the key being looked for or the slot that matters; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. probe-sequence: a horizontal row of twelve blank slate boxes, some filled with cyan dots, and a cyan curved arrow hopping from one box to the next two along to reach an empty box that turns yellow.
2. cut-chain: a horizontal row of slate boxes with three consecutive boxes, the middle one now empty white outline, a cyan hopping arrow stopping at that empty box with a small white stop bar, and a yellow dot stranded in the box just beyond.
3. tombstone: the same row with the middle box holding a small slate tombstone shape, and the cyan hopping arrow passing over it to reach the yellow dot in the next box.
4. clusters: a long horizontal row of slate boxes where cyan-filled boxes bunch into runs of different lengths, one very long run, with gaps of empty boxes between them.
5. steep-curve: crossed white axes with a cyan curve that rises slowly then shoots almost vertically upward near a white dashed vertical line on the right.
6. table-ceiling: crossed white axes with a cyan curve shooting upward past a flat yellow horizontal ceiling line, and a row of slate dots that levels off under the ceiling.

When done, reply with the saved file path and pixel size only.

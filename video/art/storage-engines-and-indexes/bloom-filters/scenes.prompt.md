Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/bloom-filters/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about sizing a Bloom filter from a target false-positive rate, the memory it costs per key, and the disk probes it saves in a log-structured tree. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for bits and answers that are certain; warm yellow (#FFC857) for set bits and the rare false positive; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. bit-array: a long row of small white outlined squares, several of them filled yellow, with three thin white arrows from one slate dot above pointing to three of the yellow squares.
2. clear-bit-no: a long row of small squares mostly yellow, three white arrows from a slate dot pointing down, one of them landing on an empty cyan outlined square marked by a thick white ring.
3. false-positive: a long row of small squares, three white arrows from a dashed slate dot all landing on yellow squares that were filled by other arrows drawn faintly from other dots.
4. grow-linear: two rows of small squares, the lower row exactly twice as long as the upper, both with the same density of yellow squares.
5. level-skip: five stacked white level bars, each with a small square filter beside it, a slate dot's arrow bouncing off four of the filters and passing through to only one bar, which is highlighted cyan.
6. nines-cost: a staircase of three white steps rising at an even height, and a falling cyan curve above them that drops steeply and then flattens.

When done, reply with the saved file path and pixel size only.

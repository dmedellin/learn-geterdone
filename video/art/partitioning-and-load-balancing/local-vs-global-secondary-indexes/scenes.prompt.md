Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/local-vs-global-secondary-indexes/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about choosing between a local secondary index, which puts the fan-out on reads, and a global one, which doubles every write. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for index reads; warm yellow (#FFC857) for writes and the index entries they touch; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. local-index: a row of white outlined shard boxes, each holding a slate data block with a small cyan index strip beside it, and cyan arrows from one router dot fanning out to every shard.
2. global-index: a row of white outlined shard boxes on the bottom and a separate row of index boxes above, one cyan arrow going straight to a single index box.
3. double-write: a single yellow write arrow splitting into two yellow arrows, one landing in a data shard box below and one in an index shard box above, on different machines.
4. cost-lines: white axes with two straight lines crossing once, one steep cyan line and one shallower yellow line, a small white dot at the point where they cross.
5. crossover-shrinks: a row of white balance scales getting progressively wider from left to right, each tipping further, with the pivot point sliding toward one end.
6. skewed-index: a row of index boxes where one box holds a towering yellow stack and the others hold short cyan stacks.

When done, reply with the saved file path and pixel size only.

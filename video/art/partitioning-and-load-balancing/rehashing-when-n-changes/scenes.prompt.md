Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/rehashing-when-n-changes/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how many keys move when one shard is added, under a mod-N assignment compared with a consistent-hash ring. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for keys that stay where they are; warm yellow (#FFC857) for keys that move to a different shard; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. mod-n-shuffle: a top row of seven white outlined boxes and a bottom row of eight, with many crossing yellow arrows running from almost every top box to a different bottom box, and only a few short straight cyan arrows going straight down.
2. ring-join: a large white circle with seven small slate dots spaced around it as tokens and one new yellow dot added between two of them, the short arc just before the new dot highlighted in yellow and the rest of the circle cyan.
3. residue-grid: a square grid of small white outlined cells, seven columns by eight rows, with a short diagonal run of cells filled cyan and every other cell filled yellow.
4. whole-split: one long horizontal bar split into a very long yellow part and a short cyan part, and beneath it the same bar with the colours swapped, the long part cyan and the short part yellow.
5. sample-scatter: a white horizontal line with one thin white vertical tick on it, and a small cluster of slate dots sitting close to the tick but not exactly on it.
6. bytes-to-move: two stacks of white disk cylinders side by side, the left stack almost entirely yellow, the right stack mostly cyan with only its top cylinder yellow.

When done, reply with the saved file path and pixel size only.

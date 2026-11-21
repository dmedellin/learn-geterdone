Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/working-set-and-the-page-cache/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how much of a dataset's read traffic a page cache absorbs when popularity is skewed, and the disk reads that remain. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for reads served from memory; warm yellow (#FFC857) for reads that miss and reach the disk; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. pages-vs-memory: a very long row of small white outlined page squares, a short section at the left end enclosed in a rounded white memory outline and filled cyan.
2. skew-curve: white axes with a cyan curve that starts very high at the left and drops steeply, then runs long and low to the right, the area under the left part shaded cyan and the long tail shaded slate.
3. uniform-flat: white axes with a perfectly flat horizontal cyan line, the short left section shaded cyan and the long remainder shaded slate.
4. miss-trickle: a white rounded memory box catching many cyan arrows, with a thin trickle of yellow arrows passing through to a stack of white disk cylinders.
5. doubling-steps: a white staircase with evenly sized steps rising from left to right, each step drawn under a memory block twice as wide as the one before.
6. units-convert: a large slate block on the left, a white arrow, and on the right the same block cut into a neat grid of many tiny white outlined squares.

When done, reply with the saved file path and pixel size only.

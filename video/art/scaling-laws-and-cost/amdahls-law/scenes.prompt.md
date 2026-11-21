Use your image generation tool to create ONE image and save it as `video/art/scaling-laws-and-cost/amdahls-law/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how the part of a job that cannot run in parallel caps the speedup any number of machines can give. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for the parallel part of the work, shared across machines; warm yellow (#FFC857) for the serial part that no machine count shrinks; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. split-job: one long horizontal bar, mostly cyan with a short yellow section at its left end.
2. shrinking-parallel: four horizontal bars stacked vertically, each with the same short yellow section at the left, followed by a cyan section that halves in length from one bar to the next.
3. ceiling-curve: white axes with a cyan curve rising quickly then bending and flattening toward a white dashed horizontal line it never touches.
4. straight-vs-curve: white axes with a straight white diagonal line rising steadily and a cyan curve below it that bends away and flattens, the gap between them shaded slate.
5. idle-machines: a grid of small white outlined machine boxes, only a small fraction of each box filled cyan and the rest slate, with one yellow box at the front of the grid.
6. odds-times-ratio: two white outlined rectangles side by side joined to a third, much larger rectangle on the right by white arrows, the third rectangle filled with a dense grid of small cyan squares.

When done, reply with the saved file path and pixel size only.

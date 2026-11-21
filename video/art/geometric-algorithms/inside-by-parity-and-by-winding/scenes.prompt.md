Use your image generation tool to create ONE image and save it as `video/art/geometric-algorithms/inside-by-parity-and-by-winding/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about point-in-polygon testing by counting ray crossings with a half-open vertex rule, and by the winding number, and where the two disagree. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the polygon outline; warm yellow (#FFC857) for the ray from the query point and the edges it crosses; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. ray-cast: a cyan irregular polygon with a white query dot inside it and a yellow horizontal ray from the dot to the right edge of the cell, with small white marks where the ray crosses the outline.
2. vertex-ray: a cyan polygon with a yellow horizontal ray passing exactly through one of its pointed vertices, the vertex marked with a white dot.
3. pass-vs-touch: two small panels; on the left a cyan zigzag boundary passing straight through a yellow horizontal line at a vertex, on the right a cyan boundary that dips down to touch the yellow line at a vertex and turns back up.
4. comb: a cyan comb-shaped polygon with three upward teeth, and a row of six white dots along one horizontal line crossing the teeth and notches, each with a short yellow ray to the right.
5. winding-loop: a white query dot with a cyan closed loop circling once around it, and a yellow curved arrow following the loop counter-clockwise.
6. double-loop: a white query dot with a cyan closed curve that winds twice around it in two nested loops, and two yellow curved arrows following the loops.

When done, reply with the saved file path and pixel size only.

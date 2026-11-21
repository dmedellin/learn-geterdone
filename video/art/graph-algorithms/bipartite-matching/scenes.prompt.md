Use your image generation tool to create ONE image and save it as `video/art/graph-algorithms/bipartite-matching/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about bipartite matching as a unit-capacity flow network, with the vertex cover as certificate. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for matched pairs; warm yellow (#FFC857) for the vertices in the cover or the overloaded vertex; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. flow-network: a column of three slate dots on the left and two on the right, a source dot further left joined to each left dot, a sink dot further right joined from each right dot, and lines between the columns.
2. cover: two columns of dots with four lines between them; one left dot and one right dot are yellow, and every line touches one of them.
3. deficient-set: two left dots both joined by lines only to the same single right dot, which is yellow and overloaded, with a soft white outline around the two left dots.
4. star: two columns of four dots where three left dots all have lines to the same top right dot, which is yellow, and one other line runs from the fourth left dot to the fourth right dot.
5. greedy-blocked: two columns of two dots with three lines; one diagonal line is cyan and taken, and the other two lines are faded and blocked by small white stop bars.
6. matched-pairs: two columns of three dots joined by three parallel cyan lines, one per pair, with other faded lines behind them.

When done, reply with the saved file path and pixel size only.

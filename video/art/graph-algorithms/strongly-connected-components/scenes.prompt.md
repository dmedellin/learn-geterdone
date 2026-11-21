Use your image generation tool to create ONE image and save it as `video/art/graph-algorithms/strongly-connected-components/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about strongly connected components of a digraph, found with two depth-first walks. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for arcs inside a component; warm yellow (#FFC857) for the source component; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. mutual-reach: two slate dots joined by two curved arrows, one cyan going right and one cyan going left, and a third dot off to the side reached by a single one-way white arrow.
2. condensation: on the left three clusters of slate dots, each cluster a small loop of cyan arrows; on the right three single larger dots in a line joined by white arrows.
3. last-finisher: three clusters of dots in a line joined by white arrows left to right, the leftmost cluster yellow, with no arrow entering it.
4. reversed-walk: the same three clusters with every white arrow now pointing right to left, and a cyan path circling inside the yellow leftmost cluster only.
5. wrong-start: three clusters of dots where a single cyan walk spills across two clusters at once, with a white warning ring around the spill.
6. one-way: two slate dots joined by a single white arrow, with a white dashed return path that is broken in the middle.

When done, reply with the saved file path and pixel size only.

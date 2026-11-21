Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-data-structures/open-addressing/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about open addressing, probe sequences and clustering in hash tables. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the occupied slots and the probe path; warm yellow (#FFC857) for the key being placed and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. probe-walk: a row of twelve rounded slots, some cyan and some empty, with a series of small white hopping arcs above it from one slot to the next ending at an empty slot outlined in yellow.
2. deleted-marker: a row of ten slots, mostly cyan, with one slot in the middle filled with a slate pattern of diagonal stripes, and a white arc passing over it to a cyan slot further right.
3. cluster-growth: a row of sixteen slots with one long run of eight neighbouring cyan slots and a yellow token dropping onto the empty slot just after the run.
4. double-hash-jumps: a row of sixteen slots with two sets of hopping arcs above it starting from the same slot, one making small white hops and the other making long yellow hops.
5. bound-curve: crossed white axes with a cyan curve that rises slowly at first and then shoots almost straight up near a thin white vertical dashed line at the right.
6. two-level: a vertical column of six slots, each joined by a short white line to a small horizontal table of its own of different sizes, one small table yellow, the rest cyan.

When done, reply with the saved file path and pixel size only.

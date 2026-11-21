Use your image generation tool to create ONE image and save it as `video/art/sorting-and-selection/quickselect/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about quickselect, finding the k-th smallest element without sorting. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for the side that is kept; warm yellow (#FFC857) for the pivot or the element found; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. discard-side: a row of bars split by a yellow pivot bar; the left side cyan and kept, the right side faded slate outlines drifting away.
2. middle-half: a row of slate bars in increasing height with the middle half of them highlighted cyan, and the quarters at each end left slate.
3. seed-scatter: crossed white axes with many small slate dots scattered around a horizontal white line, and a dashed yellow line above most of them.
4. sorted-trap: a long staircase of one-step-shorter cyan bars where each step drops just one small yellow bar off the end.
5. shrinking-ranges: three horizontal cyan bars stacked downward, each shorter than the one above, ending in a single yellow dot.
6. one-vs-two: on the left a branching recursion tree of bars splitting into two each level; on the right a single chain of bars shrinking downward.

When done, reply with the saved file path and pixel size only.

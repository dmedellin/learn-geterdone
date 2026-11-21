Use your image generation tool to create ONE image and save it as `video/art/integer-programming/the-travelling-salesman-problem/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the travelling salesman problem: counting tours, the assignment relaxation and its subtours, cutting them, and measuring a heuristic. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the dots, outlines and tree branches; cyan (#37D7E7) for the arcs of a tour or a relaxation; warm yellow (#FFC857) for the forbidden arc, the crossing edges and the one subtour being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. city-tour: seven slate dots scattered across the cell, joined by one single closed cyan loop that visits every dot exactly once and returns to its start.
2. subtours: six slate dots scattered across the cell, joined in three separate pairs, each pair linked by two curved cyan arrows going back and forth; one pair is yellow.
3. forbid-arc: a pair of slate dots linked by two curved arrows, one of them crossed by a short thick yellow bar, and beside them the same dots now joined into a bigger cyan loop with two other dots.
4. tour-tree: a tree of five white dots and branches, the bottom right leaf replaced by a small closed cyan loop drawn around a few tiny dots, outlined in yellow.
5. nearest-neighbour: seven slate dots joined by one closed cyan tour made of mostly short hops, with one very long edge cutting back across the middle drawn yellow.
6. two-opt: two small tours of six dots side by side; the left tour has two edges that cross each other, drawn yellow; the right tour is the same dots with those two edges swapped so nothing crosses, drawn cyan.

When done, reply with the saved file path and pixel size only.

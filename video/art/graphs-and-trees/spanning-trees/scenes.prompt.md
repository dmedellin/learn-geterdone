Use your image generation tool to create ONE image and save it as `video/art/graphs-and-trees/spanning-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about spanning trees and minimum spanning trees, built with Kruskal's greedy algorithm. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) solid dots for the vertices and rounded lines of even weight for the edges; cyan (#37D7E7) for the edges chosen for the tree; warm yellow (#FFC857) for the edge being added or the one part being singled out; muted slate (#3A4F63) flat fills and faint dashed lines for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. spanning-tree-highlight: a connected graph of eight white dots with many edges: the edges of one spanning tree reaching every dot are thick cyan, and the remaining edges are faint slate.
2. remove-cycle-edges: on the left a small graph of white dots containing two loops; a white arrow points right to the same dots with one edge from each loop shown as a faint dashed slate line, leaving a cyan tree.
3. kruskal-pentagon: five white dots on a pentagon: four consecutive sides of the pentagon form a cyan chain through all five dots; the fifth side and the two diagonals from the chain ends are faint dashed slate lines.
4. cut-crossing: a pale slate rounded region on the left holding four white dots and another on the right holding four white dots, with five white edges crossing the gap between the regions and exactly one of the crossing edges thick yellow.
5. cycle-swap: a cyan tree of white dots spanning a vertical dividing gap, with one new yellow edge across the gap closing a loop, and the other edge of that loop that crosses the gap drawn as a faint dashed slate line with a small curved white swap arrow between the two.
6. prim-growing: a yellow start dot with a cyan tree growing out from it inside a pale slate rounded region, white dots outside the region, and one yellow edge reaching from the region to a dot outside it.

When done, reply with the saved file path and pixel size only.

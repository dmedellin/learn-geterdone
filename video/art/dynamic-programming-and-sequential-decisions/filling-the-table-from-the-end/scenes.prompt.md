Use your image generation tool to create ONE image and save it as `video/art/dynamic-programming-and-sequential-decisions/filling-the-table-from-the-end/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about dynamic programming on a staged network, filled in backwards from the last stage. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the arcs between nodes and the stage columns; cyan (#37D7E7) for nodes whose value is already settled and the cheapest arcs; warm yellow (#FFC857) for the one node or route being singled out, and ties; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. staged-network: four vertical columns of round white-outlined dots, one dot in the first column, two in the second, two in the third and one in the last, joined left to right by thin white arrows that only ever point forward to the right.
2. backward-sweep: the same four-column dot network, with the rightmost column of dots filled cyan and the column to its left half filled cyan, and a large curved yellow arrow sweeping from right to left above the network.
3. tie-fork: one yellow dot on the left with two equally thick cyan arrows leaving it, splitting into two branches that run to two separate dots and then rejoin at a single dot on the right, the two branches perfectly symmetric.
4. three-routes: the four-column network drawn three times stacked vertically, small, each copy with a different single path from the left dot to the right dot traced in thick cyan, the remaining arcs thin slate.
5. all-paths: a fan of four separate thin white paths from one dot on the left to one dot on the right, each path drawn apart from the others like strands, three of them cyan and one of them slate.
6. skip-arc: the four-column dot network with one long yellow arc jumping from the first dot over the second column directly to a dot in the third column, the other arcs thin white.

When done, reply with the saved file path and pixel size only.

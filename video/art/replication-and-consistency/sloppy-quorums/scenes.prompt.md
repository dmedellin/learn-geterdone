Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/sloppy-quorums/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about sloppy quorums, where a read set can miss every node that received a write. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines and node rings; cyan (#37D7E7) for the read set; warm yellow (#FFC857) for the nodes that received the write; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. untouched-nodes: a row of five slate nodes; the left two glow yellow, and a cyan outline encloses two of the three plain nodes on the right
2. uniform-draw: a ring of slate nodes with several faint dashed cyan outlines around different random pairs of them, all equally faint
3. edge-not-safe: a row of three slate nodes, one glowing yellow; a cyan outline encloses the other two, just missing the yellow one
4. not-lost: a yellow glowing node with small white arrows spreading outward from it to neighbouring slate nodes, like ripples
5. read-chase: a slate client box writing a yellow square to one node and immediately reading from a different plain node
6. one-more-node: two rows of three nodes; in the top row the cyan and yellow outlines do not meet, in the bottom row the yellow outline is one node wider and now shares a node with the cyan one

When done, reply with the saved file path and pixel size only.

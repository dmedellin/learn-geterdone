Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-graphs/maximum-flow/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about flow networks, residual networks and the Ford-Fulkerson method for maximum flow. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for flow already sent along arcs; warm yellow (#FFC857) for the augmenting path and backward arcs that cancel flow; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. flow-network: a directed network of dots from a source on the left to a sink on the right, each arrow drawn as a pipe of different width, partly filled with cyan.
2. residual: a single arc drawn twice: on top a pipe half full of cyan; below it two thinner arrows, one forward slate for the spare room, one backward yellow for the flow that could be undone.
3. cut: the network of dots split by a dashed white curve near the source, with the arrows that cross it from left to right drawn thick and full of cyan.
4. stuck: the network with one long cyan path running through it and one full pipe in the middle blocking, and a dead-end white arrow stopped beside it.
5. bfs-path: the network with a short, straight yellow route of few arcs highlighted from source to sink and a long winding slate route beside it.
6. cancel-flow: two crossing routes through the network: a cyan route already sent, and a yellow route that runs partly backward along one cyan pipe and then forward elsewhere.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/replication-lag-and-stale-reads/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about replication lag and stale reads, where a follower read is stale if the follower has not yet caught up. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the timelines, axes and arrows; cyan (#37D7E7) for followers that have caught up and fresh reads; warm yellow (#FFC857) for lagging followers and stale reads; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. lag-gap: two parallel white timelines, the top one for a leader with a cyan dot, the bottom one for a follower with the same dot shifted to the right, joined by a short yellow bracket showing the delay
2. long-tail: white axes with a very tall cyan bar at the left, a shorter one beside it, and then small bars stretching far to the right in yellow
3. balance-point: a white horizontal beam balanced on a small slate triangle placed left of centre; a big pile of cyan blocks near the left end and a few small yellow blocks spread far out to the right
4. read-your-writes: a slate client box sending a yellow write arrow up to a leader cylinder and then a white read arrow down to a follower cylinder that is still empty
5. monotonic: a slate client box with two read arrows: the first to a cyan follower holding a full block, the second to a yellow follower holding a smaller older block
6. version-wait: a slate follower cylinder with a white progress ring around it partly filled cyan, and a small slate client box waiting beside it holding a yellow tag

When done, reply with the saved file path and pixel size only.

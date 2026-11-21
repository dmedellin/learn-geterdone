Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/vector-clocks-and-concurrency/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about vector clocks, where each event carries one counter per process and some pairs of events are concurrent. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the process lines and message arrows; cyan (#37D7E7) for events that are causally ordered; warm yellow (#FFC857) for pairs of events that are concurrent; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. vector-boxes: a single slate event dot on a white process line with a small row of three blank rounded boxes floating above it, one per process
2. refuses: two rows of three blank boxes facing each other, with a white arrow between them that splits and turns back on itself in both directions
3. sparse-messages: three long white process lines with many slate event dots and only one or two thin message arrows between the lines, several dot pairs ringed in yellow
4. wall-clock: two white process lines far apart, one yellow dot near the right end of the top line and another yellow dot near the middle of the bottom line, with a slate clock face between them
5. three-processes: three horizontal white process lines with slate event dots and three diagonal message arrows, drawn in cyan, joining dots on different lines
6. merge-max: two rows of three blank boxes of different heights merging through white arrows into one row whose boxes each take the taller of the two

When done, reply with the saved file path and pixel size only.

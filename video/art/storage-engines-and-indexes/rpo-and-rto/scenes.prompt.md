Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/rpo-and-rto/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about the two numbers a backup plan has to give, the bytes a failure can lose and the hours a restore takes. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for data safely backed up and restored; warm yellow (#FFC857) for writes at risk since the last backup, and the log to replay; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. interval-at-risk: a white horizontal timeline with evenly spaced white tick marks for backups, and between two ticks a growing yellow wedge of writes that ends abruptly at a jagged white break.
2. expected-half: the same timeline segment between two backup ticks, with the yellow wedge cut at its midpoint by a dashed white line.
3. copy-and-replay: one long horizontal bar made of a short cyan section followed by a much longer yellow section, laid along a white timeline.
4. floor-line: a set of four horizontal bars stacked vertically, each starting with the same short cyan section and followed by yellow sections of decreasing length, the cyan sections perfectly aligned.
5. rto-line: white axes with a straight cyan line rising from a point above the horizontal axis, not from the origin, with a white dashed horizontal line at its starting height.
6. untested-restore: a white outlined backup box connected by a dashed white arrow to a server box, the arrow broken partway with a small slate gap.

When done, reply with the saved file path and pixel size only.

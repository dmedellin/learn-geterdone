Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-concurrency-and-session-state/pessimistic-and-coarse-grained-locks/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about pessimistic and coarse-grained locks: lock before loading, refuse at once rather than wait, and cover a group of records with one lock. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the sessions; warm yellow (#FFC857) for locks and everything a lock covers; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. lock-manager-table: one slate table of four rows, each row joined by a thin white line on its right to a small cyan dot, with a small yellow padlock at the start of each row.
2. lock-before-load: a small yellow padlock already closed on a slate tag, and only after it, further right, a white arrow carrying a slate document into a cyan circle.
3. refuse-not-wait: a slate document with a yellow padlock, and a cyan dot approaching it that turns back along a curved white arrow, with no queue and no waiting line.
4. root-lock: a tree of slate dots joined by white branches, with a yellow padlock on the top root dot and every other dot ringed by a thin yellow outline.
5. line-locks: a slate rounded box holding two horizontal slate bars, each bar with its own small yellow padlock and its own cyan dot beside it.
6. implicit-lock: a row of five small slate boxes standing on one wide slate band beneath them, every box topped with an identical small yellow padlock, with a white line rising from the band to each padlock.

When done, reply with the saved file path and pixel size only.

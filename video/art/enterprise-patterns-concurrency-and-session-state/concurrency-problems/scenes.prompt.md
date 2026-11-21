Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-concurrency-and-session-state/concurrency-problems/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about concurrency problems: a lost update, where one session writes over another's change, and an inconsistent read, where two correct reads straddle a commit. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for a session's reads and its copy of the data; warm yellow (#FFC857) for a commit that changes the data; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. lost-update: one slate document shape in the centre with two cyan copies of it pulled out to the left and right; a yellow block from one copy has been written into the document, and the other copy's white arrow lands on top of it, covering the yellow block.
2. inconsistent-read: a long horizontal white timeline with one bold yellow vertical bar across its middle; one cyan dot sits on the line left of the bar and another cyan dot right of it, each dot joined by a thin line up to a row of small slate squares.
3. correctness-liveness: on the left a single narrow slate gate with a long queue of small cyan dots waiting in single file; on the right many cyan dots flowing freely through a wide opening.
4. execution-contexts: a short white arc between two slate boxes, and below it a longer chain of five such arcs joined end to end, the whole chain wrapped in one large rounded cyan outline.
5. isolation-zones: four separate slate rounded zones with wide gaps between them, each zone holding exactly one cyan dot and one small slate square.
6. immutable-shared: one solid slate block in the centre with a thick white border, joined by many thin white lines to many small cyan dots spread around it.

When done, reply with the saved file path and pixel size only.

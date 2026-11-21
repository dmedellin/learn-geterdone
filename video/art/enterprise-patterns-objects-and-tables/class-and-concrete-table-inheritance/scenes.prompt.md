Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-objects-and-tables/class-and-concrete-table-inheritance/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about two ways to map a class hierarchy to tables: a table per class, joined to load an object, and a table per concrete class, which loads from one table but changes everywhere a superclass does. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the shared key and the joins that load an object; warm yellow (#FFC857) for duplicated superclass columns and the changes they force; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. class-tables: four small slate grid tables arranged like a tree, one at the top, two below, one more below the left, each joined to its parent by a cyan line.
2. join-three: three small slate grid tables in a row, with cyan lines from one row in each table converging into a single merged row on the right.
3. concrete-tables: three separate self-contained slate grid tables side by side, each with the same first two columns coloured yellow.
4. superclass-change: the same three tables, each receiving one new yellow column at the same moment, with three small white arrows pointing to the new columns.
5. union-find: a long white sweeping arrow passing across all three side-by-side tables and gathering rows from each into one bundle at the end.
6. mapper-chain: a vertical stack of three slate mapper blocks joined by upward white arrows, each block calling the one above, with a cyan block at the top sending a white arrow back down to one of them.

When done, reply with the saved file path and pixel size only.

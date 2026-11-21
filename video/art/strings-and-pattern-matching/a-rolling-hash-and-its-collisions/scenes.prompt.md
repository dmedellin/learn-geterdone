Use your image generation tool to create ONE image and save it as `video/art/strings-and-pattern-matching/a-rolling-hash-and-its-collisions/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the Rabin-Karp rolling hash: turning each window of text into one number computed from the window before, and the collisions where two different windows get the same number. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for windows that really match the pattern; warm yellow (#FFC857) for collisions: windows whose number matches but whose characters do not; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. roll-window: a long row of blank text tiles with a three-tile window bracket; the tile leaving the window on the left is faded, the new tile entering on the right is yellow, and a curved white arrow shows the window moving one place.
2. collision-pair: two separate three-tile rows of different slate shades, one cyan and one yellow, each with a white line running down to the same single round slate token below them.
3. false-alarm: a long row of blank tiles with seven small white flags standing above it; four flags are cyan and three are yellow.
4. exact-digits: a very long horizontal strip of small blank square boxes running across the cell, every box filled cyan, with no gaps or rounding.
5. hash-tokens: a row of many three-tile windows along a text, each dropping a small round token below it, most tokens slate, seven of them matching in shape and drawn cyan or yellow.
6. recompute: two identical rows of round tokens one above the other, joined pair by pair with thin white vertical lines.

When done, reply with the saved file path and pixel size only.

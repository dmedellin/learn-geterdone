Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-domain-logic/special-case/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about Special Case: instead of returning null and making every caller check, return an object with the expected interface and harmless behaviour. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the special case object that stands in; warm yellow (#FFC857) for the null checks and the failed call; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. null-hole: a white arrow running right from a slate block towards an empty dashed white outline where an object should be, the arrow breaking apart at the outline with a small yellow jagged spark.
2. repeated-checks: four slate caller blocks in a row, each with the same small yellow diamond gate placed directly in front of it.
3. stand-in: a dashed white outline slot with a solid cyan block of exactly the same shape sliding into it from the side, beside a slate block of that same shape.
4. shared-flyweight: five slate caller blocks arranged in an arc, each with a thin white line converging on one single cyan block in the centre.
5. finder-gate: a slate box on the left with a chute out of its right side, handing out a row of blocks, mostly slate and one cyan, moving away along a white line.
6. two-specials: two cyan blocks of the same outline side by side, the left one hollow with only a cyan outline, the right one half filled with cyan, separated by a thin white gap.

When done, reply with the saved file path and pixel size only.

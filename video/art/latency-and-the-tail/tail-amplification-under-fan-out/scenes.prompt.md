Use your image generation tool to create ONE image and save it as `video/art/latency-and-the-tail/tail-amplification-under-fan-out/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how a request that fans out to many backends and waits for all of them inherits their tails. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the connecting lines and outlines; cyan (#37D7E7) for the backend calls that are fast; warm yellow (#FFC857) for the one slow call and the request it holds up; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. fan-out: one white dot on the left with many thin white lines fanning out to a tall column of small cyan dots on the right, one of which is yellow.
2. green-dashboards: a grid of small square cyan tiles all identical and calm, with one long yellow horizontal bar running beneath them.
3. fewer-calls: two fans side by side: on the left one dot fanning out to many dots, on the right the same dot fanning out to only a few, all cyan except one yellow dot in the larger fan.
4. clustered-slowness: a tall column of small cyan dots where three adjacent dots are yellow, bunched together, inside one slate rounded box.
5. multiplying-chance: a row of many identical cyan circles, each with a tiny yellow slice, in a long line getting denser towards the right.
6. waiting-for-all: a white finishing line on the right with many cyan arrows already arrived at it and one yellow arrow still far behind.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/scaling-laws-and-cost/autoscaling-lag/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about the requests lost while new instances boot during a rising load, and the warm reserve that removes that shortfall. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for capacity in service; warm yellow (#FFC857) for demand, and the shortfall between demand and capacity; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. lagging-lines: white axes with a rising yellow straight line for demand and a cyan line that stays flat for a while then rises parallel to it, always below it.
2. triangle-rectangle: the area between a rising yellow line and a lagging cyan line split into a small yellow triangle on the left and a long yellow rectangle on the right, divided by a thin white vertical line.
3. booting-instances: a row of white outlined server boxes, the first few filled cyan and serving, the next few hollow with a small white spinning ring inside each.
4. overflow-backlog: a white outlined server box with a long and growing line of small yellow squares queued in front of it, running off the edge.
5. level-end: white axes where a rising yellow line and a lagging cyan line both flatten out at the same height on the right, with the yellow region between them left behind on the left.
6. warm-reserve: a cyan line starting above a rising yellow line at the left, staying above it, with a slate shaded band of spare capacity between them.

When done, reply with the saved file path and pixel size only.

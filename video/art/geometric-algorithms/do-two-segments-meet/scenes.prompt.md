Use your image generation tool to create ONE image and save it as `video/art/geometric-algorithms/do-two-segments-meet/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about deciding whether two line segments meet using four orientation signs, and the collinear and touching cases where a sign is zero. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for the two segments; warm yellow (#FFC857) for the line being straddled, the crossing point or the case being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. straddle-one: a long yellow line running across the cell, with a short cyan segment crossing it whose two white endpoints sit on opposite sides of the line.
2. straddle-miss: two cyan segments that do not touch; each one's extended line, drawn faint yellow and dashed, passes through the other segment's line beyond the end of the segment.
3. x-crossing: two cyan segments crossing in a clean X with white endpoint dots and a yellow dot at the crossing point.
4. t-junction: a horizontal cyan segment with a second cyan segment standing on it so its lower white endpoint, highlighted yellow, rests exactly on the first segment, forming a T.
5. parametric-check: two cyan segments crossing, each with a small white slider dot moving along it from one end to the other, shown by small white arrows, meeting at a yellow crossing point.
6. box-overlap: two cyan segments that miss each other, each inside its own faint slate rectangle, with the two rectangles overlapping in a yellow region.

When done, reply with the saved file path and pixel size only.

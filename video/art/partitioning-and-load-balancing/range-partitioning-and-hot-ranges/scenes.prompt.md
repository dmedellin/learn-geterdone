Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/range-partitioning-and-hot-ranges/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about range partitioning keeps keys in order for cheap scans, but a monotonic key sends every current write to one range. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for idle or evenly loaded ranges; warm yellow (#FFC857) for the hot range taking the writes happening now; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. ordered-ranges: a long white horizontal bar cut into eight contiguous segments in cyan, with a short white bracket above two adjacent segments showing a scan touching only those two.
2. write-pointer: eight white outlined boxes in a row, seven empty slate, the rightmost filled bright yellow, with many small white arrows all converging on that one box.
3. moving-hotspot: three rows of eight boxes stacked one above another, the yellow box shifting one place to the right in each row, all other boxes slate.
4. flat-histogram: eight cyan vertical bars of exactly equal height side by side, perfectly level, with a thin white line across their tops.
5. hashed-spread: eight white outlined boxes in a row all filled with cyan to slightly uneven levels, small white arrows fanning out to every box, and a white bracket spanning all eight boxes.
6. bucket-dial: a white rotary dial with a pointer partway round, and beside it a row of eight boxes where four are filled cyan and the other four are slate.

When done, reply with the saved file path and pixel size only.

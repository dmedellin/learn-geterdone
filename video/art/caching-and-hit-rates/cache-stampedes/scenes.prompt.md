Use your image generation tool to create ONE image and save it as `video/art/caching-and-hit-rates/cache-stampedes/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about cache stampedes, where many requests for one hot key all reach the backend in the moment after it expires. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the timelines, arrows and capacity lines; cyan (#37D7E7) for requests served or held safely; warm yellow (#FFC857) for the burst of requests reaching the backend; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. expiry-gap: a white horizontal timeline that is solid cyan on the left and right with a short empty gap in the middle; a dense crowd of small yellow arrows drops straight down through the gap toward a slate block below
2. same-burst: two slate cache boxes side by side, one large and one small, each with an identical short gap and an identical yellow burst of arrows falling out of it
3. single-flight: many small cyan dots waiting in a neat row behind a white line, while exactly one yellow arrow continues past the line to a slate block
4. early-refresh: a white timeline of consecutive cyan windows that overlap slightly at their ends, with no gaps anywhere, and a small yellow dot at the start of each overlap
5. synced-expiry: several parallel white timelines stacked; on the left they all have gaps at exactly the same position lined up vertically, on the right the gaps are scattered at different positions
6. capacity-line: white axes with a horizontal white dashed line partway up; a tall yellow rectangle rises far above the dashed line beside a tiny cyan square below it

When done, reply with the saved file path and pixel size only.

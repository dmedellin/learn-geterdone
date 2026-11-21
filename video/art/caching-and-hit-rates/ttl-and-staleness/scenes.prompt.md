Use your image generation tool to create ONE image and save it as `video/art/caching-and-hit-rates/ttl-and-staleness/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about cache time to live and staleness, where a shorter expiry means fresher data but more misses. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the timelines, axes and tick marks; cyan (#37D7E7) for fresh cached time and the curves; warm yellow (#FFC857) for stale time and the misses; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. ttl-window: a long white horizontal timeline with a bracket spanning one window; the first part of the bracket is filled cyan and the rest after a small white tick is filled yellow
2. two-clocks: two parallel white timelines one above the other; the top one has evenly spaced white ticks, the bottom one has evenly spaced cyan ticks offset so they do not line up with the top ones
3. stale-climb: white axes with a curve that rises as a straight cyan line from the corner and then bends into a yellow curve flattening as it approaches a white dashed line near the top
4. seesaw: a white seesaw plank on a slate triangle pivot, with a small cyan block on the raised end and a large yellow block stack on the lowered end
5. phase-runs: many thin horizontal white timelines stacked, each with a small yellow segment in a slightly different place, and one cyan vertical band running down through their average position
6. expiry-ticks: a white timeline with many short cyan segments separated by frequent yellow dots, above a second timeline with long cyan segments and only a few yellow dots

When done, reply with the saved file path and pixel size only.

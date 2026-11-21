Use your image generation tool to create ONE image and save it as `video/art/caching-and-hit-rates/replacement-policies-on-a-trace/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about cache replacement policies measured on a sequence of requests, including a cache that misses more when it grows. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the slot outlines, arrows and baselines; cyan (#37D7E7) for keys that hit in the cache; warm yellow (#FFC857) for misses, evictions and the one result being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. reference-string: a long horizontal row of twelve small rounded squares in a few different slate shades, flowing from left to right into a white outline of three empty slots stacked vertically
2. crystal-ball: a white outlined cache of three slots on the left, with a white dotted arrow reaching far ahead along a long row of slate squares to the right, pointing at one square highlighted in yellow near the end
3. gap-to-bound: white baseline with four slate bars of different heights side by side; the tallest bar is cyan and outlined, and a yellow bracket spans the gap between the top of the shortest bar and the top of the tallest
4. bigger-worse: two white outlined caches side by side, a short one of three slots and a taller one of four slots; under the short cache a short yellow bar, under the taller cache a longer yellow bar
5. nested-sets: three white rounded rectangles nested inside one another like a set diagram, the innermost filled cyan, the middle and outer filled lighter slate, with a small yellow dot inside the innermost
6. evict-oldest: a horizontal white queue of four slots holding slate squares, with a yellow square being pushed out of the right end and a cyan square entering at the left

When done, reply with the saved file path and pixel size only.

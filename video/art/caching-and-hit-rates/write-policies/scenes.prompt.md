Use your image generation tool to create ONE image and save it as `video/art/caching-and-hit-rates/write-policies/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about cache write policies, comparing sending every write to the database with holding writes and flushing them in batches. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the arrows, pipes and timelines; cyan (#37D7E7) for writes that reach the backend; warm yellow (#FFC857) for dirty data held only in the cache, which is at risk; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. write-through: a small slate cache box and a tall slate database block side by side; a row of small cyan squares flows through the cache box and every one continues straight on into the database block
2. write-back: the same cache box holding a small pile of yellow squares, and a single short burst of a few cyan squares flowing from it to the database block
3. trade-scale: a white balance scale with two pans; one pan holds a short stack of cyan squares and sits high, the other holds a larger pile of yellow squares and sits low
4. distinct-trace: a horizontal row of ten small squares each a different slate shade, with all ten white arrows passing down from them to a long slate bar below
5. fleet-risk: a grid of many small identical slate cache boxes, each holding a tiny yellow square, with a few of the boxes cracked open
6. flush-windows: a long white timeline divided by two vertical white lines into windows; each window holds a few slate squares and sends one short cyan arrow down to a bar below

When done, reply with the saved file path and pixel size only.

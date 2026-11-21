Use your image generation tool to create ONE image and save it as `video/art/storage-engines-and-indexes/write-amplification-in-lsm-trees/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how a levelled log-structured merge tree writes everything sequentially but rewrites each byte many times, and the bandwidth that costs. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for bytes arriving from the application; warm yellow (#FFC857) for bytes rewritten by compaction; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. level-stack: five horizontal white outlined bars stacked from top to bottom, each about ten times wider than the one above, the top one tiny.
2. merge-rewrite: a short cyan run on top dropping along a white arrow into a long bar below, the overlapping section of the long bar turning yellow as it is rewritten.
3. half-full-cycle: a single white outlined bar shown four times in a column, filled slate to a quarter, a half, three quarters and full, with a curved white arrow from the full one back to the empty start.
4. bandwidth-pipes: a thin cyan pipe on the left feeding into a wide yellow pipe on the right that is many times thicker.
5. miss-probes: a small slate dot sending a white arrow down through every one of five stacked level bars in turn, a small white ring on each bar where it checks.
6. fanout-dial: a white rotary dial with its pointer, and two stacks of level bars beside it: a short stack of a few very wide bars and a taller stack of more, narrower-stepped bars.

When done, reply with the saved file path and pixel size only.

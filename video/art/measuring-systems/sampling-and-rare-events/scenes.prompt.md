Use your image generation tool to create ONE image and save it as `video/art/measuring-systems/sampling-and-rare-events/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about the chance that sampling a fraction of requests catches a rare problem, and how sampling the slow tail breaks averages unless each kept request is reweighted. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for requests kept by the sampler; warm yellow (#FFC857) for the rare slow requests of the problem; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. sparse-sample: a large grid of small slate squares with a few scattered cyan squares kept, and ten yellow squares elsewhere in the grid, none of them overlapping a cyan one.
2. capture-curve: white axes with a yellow curve rising from the origin, steep at first and then bending to flatten near the top, a white dashed horizontal line near the top.
3. miss-probability: a row of ten small yellow squares each passing a white gate, each with a small slate cross showing it was dropped, one of them slipping through in cyan.
4. tail-keep: a white funnel where every yellow square passes straight through and only a few of many slate squares get through.
5. skewed-average: a white balance with a small number of heavy yellow blocks on one pan and a thin scatter of light slate blocks on the other, the yellow side pressed down.
6. reweight: the same balance with the slate blocks each multiplied into a tall stack, now level with the yellow side.

When done, reply with the saved file path and pixel size only.

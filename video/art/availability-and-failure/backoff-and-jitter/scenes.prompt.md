Use your image generation tool to create ONE image and save it as `video/art/availability-and-failure/backoff-and-jitter/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about exponential backoff and jitter, where clients that failed together retry in waves unless their delays are spread. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes, baselines and capacity lines; cyan (#37D7E7) for retries spread out over time; warm yellow (#FFC857) for synchronised retry spikes; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. synced-waves: white axes with a flat baseline and six very thin tall yellow spikes, spaced further and further apart from left to right as if doubling each time
2. narrow-spike: one very thin tall yellow spike on white axes, with a wide slate rectangle drawn over it that is much shorter than the spike
3. smeared-waves: white axes with a row of low rounded cyan humps of different widths, each wider than the last, roughly where tall spikes would have been
4. recovery-capacity: white axes with a white dashed horizontal line; a tall yellow spike pierces far above it on the left, and a low cyan hump stays beneath it on the right
5. not-sufficient: white axes with a white dashed horizontal line low down and a cyan hump that is wider than a spike but still rises well above the dashed line
6. doubling-gaps: a white timeline with six small slate dots whose gaps double each time, the last dot far off to the right

When done, reply with the saved file path and pixel size only.

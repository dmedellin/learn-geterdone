Use your image generation tool to create ONE image and save it as `video/art/first-order-linear-equations/stiffness-when-the-step-is-too-big/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about stiffness, where Euler's method on a fast decay multiplies by a fixed factor each step and blows up when the step passes a bound, while the backward method decays at every step size. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the plain axes, arrows and dots; cyan (#37D7E7) for the true decaying solution; warm yellow (#FFC857) for the Euler steps, and the one feature being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. geometric-factor: three rows of white dots on a horizontal line: in the top row dots shrink steadily towards the line; in the middle row they alternate above and below and shrink; in the bottom row they alternate and grow.
2. blow-up-steps: plain white crossed axes with a cyan curve falling fast and hugging the horizontal axis, and a yellow zigzag polyline that alternates above and below the axis with every swing larger than the last.
3. fast-and-slow: two side-by-side panels with plain white axes; on the left a cyan curve decaying slowly across the panel; on the right a cyan curve plunging almost straight down to the axis, with a short yellow bracket marking a tiny step width beneath it.
4. stable-not-accurate: plain white crossed axes with a cyan curve falling fast onto the axis, and a slate polyline with white dots that also falls towards the axis but more slowly, staying clearly above the cyan curve.
5. alternating-decay: plain white crossed axes with a cyan curve falling to the axis, and a yellow zigzag polyline alternating above and below the axis with every swing smaller than the last, settling onto the axis.
6. step-bound: a horizontal white line with two yellow tick dots on it; the stretch before the first dot is cyan, the stretch between the dots is cyan dashed, and the stretch after the second dot is slate.

When done, reply with the saved file path and pixel size only.

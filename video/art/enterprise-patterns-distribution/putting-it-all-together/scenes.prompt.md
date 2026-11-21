Use your image generation tool to create ONE image and save it as `video/art/enterprise-patterns-distribution/putting-it-all-together/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-architecture education video about putting an enterprise application together: choose the domain logic first, let it choose the rest, and keep the layers in one process if you can. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the domain layer and calls that stay inside one process; warm yellow (#FFC857) for calls that cross a boundary between processes; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. domain-first: three wide horizontal bands stacked with gaps, the middle band cyan and slightly larger, the top and bottom bands slate, with thin white arrows pointing from the middle band to the other two.
2. choice-tree: a tree of dots and branches growing from one cyan root dot on the left, splitting into three branches, each of which splits again into smaller slate dots.
3. layer-calls: five thin horizontal bands stacked, with short cyan arrows between neighbouring bands, few arrows between the top bands and many dense arrows between the middle bands.
4. boundary-above-service: the same five stacked bands with a white dashed line cutting across between the second and third bands, and only two short yellow arrows crossing the dashed line.
5. boundary-under-service: the same five stacked bands with the white dashed line lower, between the third and fourth bands, and a dense crowd of yellow arrows crossing it.
6. other-schemes: three small stacks of slate bands on the left, with different numbers of bands, each joined by thin white lines to one three-band stack on the right whose middle band is cyan.

When done, reply with the saved file path and pixel size only.

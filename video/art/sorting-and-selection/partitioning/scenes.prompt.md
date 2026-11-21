Use your image generation tool to create ONE image and save it as `video/art/sorting-and-selection/partitioning/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer science education video about partitioning an array around a pivot in one pass, with its three-region invariant. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for outlines, edges and arrows; cyan (#37D7E7) for elements at most the pivot; warm yellow (#FFC857) for the pivot; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. pivot-split: a row of twelve slate bars of different heights with a yellow bar in the middle, the bars to its left all shorter than it and the bars to its right all taller, but each side in jumbled order.
2. three-regions: a row of bars split into three bands by two white vertical markers: a cyan band of short bars, a slate band of tall bars, and a band of faint unexamined outline bars, with a yellow bar at the far right end.
3. final-swap: a row of bars with a curved white swap arrow between a yellow bar at the far right end and the first tall slate bar after the cyan band.
4. two-pointers: a row of bars with two white downward arrows, one at the left moving right and one at the right moving left, about to meet in the middle.
5. equal-keys-side: a row of bars all exactly the same height, every one pushed into a single long group on one side of a yellow bar, with an empty space on the other side.
6. scan-step: a row of bars with a white downward arrow above one bar mid-row and a short cyan curved arrow moving that bar into the cyan band on the left.

When done, reply with the saved file path and pixel size only.

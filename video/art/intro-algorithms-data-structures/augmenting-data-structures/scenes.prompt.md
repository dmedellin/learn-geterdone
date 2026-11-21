Use your image generation tool to create ONE image and save it as `video/art/intro-algorithms-data-structures/augmenting-data-structures/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed computer-science education video about augmenting a red-black tree with subtree sizes, and interval trees. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for the subtree being counted and the path a query follows; warm yellow (#FFC857) for the node found and the one thing being singled out; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. size-tree: a binary tree of white dots where each dot sits on a short cyan bar whose length matches how many dots are in its subtree, the root's bar longest and the leaves' bars shortest.
2. select-walk: a binary tree of slate dots with a cyan path from the root going left, then right, then right, ending at a yellow dot, with small white turning arrows at each step.
3. rank-climb: a binary tree of slate dots with a yellow dot low on the right and a cyan path of white arrows climbing from it up to the root, the left subtrees passed on the way softly shaded cyan.
4. rotation-sizes: two small trees side by side with a curved white rotation arrow between them, and in each tree exactly two dots outlined in yellow, the two nodes the rotation moved.
5. four-steps: four rounded slate blocks in a row joined by white arrows left to right, with a thin cyan arrow looping from the third block back to the second, and the third block yellow.
6. interval-tree: a row of horizontal cyan bars of different lengths and offsets floating above a binary tree of white dots, with thin white lines joining each bar to its dot, and one bar yellow.

When done, reply with the saved file path and pixel size only.

Use your image generation tool to create ONE image and save it as `video/art/strings-and-pattern-matching/one-pass-for-every-word/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about the Aho-Corasick automaton: a trie of dictionary words with failure links, which finds every occurrence of every word in one scan of the text. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for trie edges and the path being walked; warm yellow (#FFC857) for failure links and word ends; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. trie-shape: a small rooted tree of white dots and branches drawn top down, splitting into two main branches, with four of the dots drawn as larger yellow circles marking ends.
2. shared-prefix: the same small tree, one branch shared at the top drawn thick cyan, splitting lower into two separate cyan paths.
3. failure-links: the small tree of white dots and branches with several curved dashed yellow arrows jumping from nodes in one branch across to nodes in the other branch or back up to the root.
4. scan-walk: a long row of blank text tiles at the bottom, a white pointer under one tile, and above it the small tree with a cyan path lit from the root down to one node.
5. suffix-chain: two paths in the tree, a longer one and a shorter one in another branch, each ending in a yellow circle, joined by one dashed yellow arrow from the end of the longer to the end of the shorter.
6. nested-prefixes: a single straight vertical chain of four white dots from the root downward, each dot a yellow circle, with no dashed arrows joining any of them.

When done, reply with the saved file path and pixel size only.

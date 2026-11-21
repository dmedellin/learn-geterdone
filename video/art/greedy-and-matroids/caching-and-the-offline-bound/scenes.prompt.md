Use your image generation tool to create ONE image and save it as `video/art/greedy-and-matroids/caching-and-the-offline-bound/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed mathematics education video about caching: which page to evict when a small cache is full, the farthest-in-future rule that is optimal but needs to see the future, and how a bigger FIFO cache can do worse. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the axes and tick marks; cyan (#37D7E7) for pages held in the cache, and hits; warm yellow (#FFC857) for the page being evicted or the request being served; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. cache-slots: three square slate slots in a row, two holding cyan blocks and one holding a yellow block being lifted out, with a long row of small slate boxes passing beneath like a conveyor of requests.
2. look-ahead: a long row of small slate boxes standing for future requests stretching to the right, with a white telescope-like rounded tube aimed along it from a small cache of three cyan slots at the left.
3. state-search: a wide branching tree of small slate dots and white lines spreading left to right, with one path through it drawn thick cyan from the root to a leaf.
4. bigger-cache: two caches side by side: on the left three slots, on the right four slots; the left holds more cyan blocks than the right, which holds more empty slate slots.
5. loop-trace: a closed loop of four slate boxes arranged in a circle with white arrows between them, and a yellow box being pushed out of a three slot cache beside it just before it is needed.
6. stack-sets: three nested rounded outlines, small, medium and large, each holding cyan blocks, every block in a smaller outline also present in the larger ones.

When done, reply with the saved file path and pixel size only.

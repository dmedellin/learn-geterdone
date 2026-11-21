Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/hot-keys-and-salting/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about why a single hot key defeats resharding, and how salting the key into several pieces trades write balance for read cost. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for ordinary traffic spread across shards; warm yellow (#FFC857) for the one hot key and its traffic; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. hot-key-shard: a row of white outlined boxes, each holding a short cyan bar, and one box holding a short cyan bar with a tall thick yellow block stacked on top of it.
2. floor-asymptote: white axes with a cyan curve falling from upper left and flattening onto a yellow dashed horizontal line well above the axis, never reaching it.
3. many-shards-same-hot: a very long row of many tiny white outlined boxes, each with a very thin cyan sliver, and one box still holding the same tall yellow block.
4. salt-split: one large yellow block on the left, a white arrow, and on the right eight small yellow blocks spread out into eight different white outlined boxes.
5. read-fanout: one slate dot on the left sending eight thin white arrows out to eight small yellow blocks, with eight arrows returning to the dot.
6. cache-in-front: a white rounded box drawn as a cache in front of a single white outlined shard box, many yellow arrows stopping at the cache and only a thin one passing through.

When done, reply with the saved file path and pixel size only.

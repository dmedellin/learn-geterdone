Use your image generation tool to create ONE image and save it as `video/art/partitioning-and-load-balancing/cross-shard-transactions/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about how often a transaction touching several hashed keys crosses shards, and what two-phase commit then adds to its latency. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, boxes and arrows; cyan (#37D7E7) for local transactions that stay on one shard; warm yellow (#FFC857) for transactions that cross shards and pay two-phase commit; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. two-keys-two-shards: two white outlined shard boxes side by side, two small dots joined by a short white line, drawn twice: once with both dots inside one box in cyan, once with one dot in each box and the joining line in yellow crossing the gap.
2. collapse-in-k: three white outlined squares side by side, each containing a smaller and smaller cyan region in one corner, the rest of each square slate.
3. prepare-commit: a white coordinator dot on the left and two participant boxes on the right, with two rounds of yellow arrows going out and back, and a small white disk cylinder beside each participant.
4. price-times-probability: a tall yellow bar on the left, a white arrow, and on the right the same bar slightly shorter with a thin cyan sliver removed from its top.
5. round-trip-vs-fsync: two horizontal bars, a long yellow bar that stretches out wide and a short slate bar that stays the same size, with a white double arrow above the long bar suggesting distance.
6. co-located-keys: a white outlined shard box holding a cluster of small dots all joined by white lines in cyan, with a shared slate tag shape attached to the cluster.

When done, reply with the saved file path and pixel size only.

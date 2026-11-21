Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/lamport-clocks/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about Lamport clocks, where each process keeps a counter and messages carry it between processes. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the process lines and message arrows; cyan (#37D7E7) for events linked by a causal chain; warm yellow (#FFC857) for events that are unrelated but look ordered; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. space-time: three horizontal white process lines stacked, each with a few slate event dots, and diagonal white arrows between dots on different lines representing messages
2. local-wins: one horizontal process line with three slate dots and a fourth dot at the end, and a diagonal arrow arriving from a much earlier point on another line below; the fourth dot is cyan
3. chain-increases: three process lines with a single path of cyan dots and arrows zig-zagging across them from left to right, each dot slightly larger than the last
4. total-queue: a single white horizontal queue of slate dots in a neat line, with dots from three process lines above dropping down into it in order
5. one-counter: a single small slate counter box with a short white bar on it, beside a row of three larger slate boxes each holding several short bars
6. false-pair: three process lines with two yellow dots on different lines, the left one on the middle line and the right one on the top line, with no arrows connecting their positions

When done, reply with the saved file path and pixel size only.

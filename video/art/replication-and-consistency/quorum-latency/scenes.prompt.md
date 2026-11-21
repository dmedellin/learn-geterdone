Use your image generation tool to create ONE image and save it as `video/art/replication-and-consistency/quorum-latency/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about quorum write latency, where a write waits only for the fastest W of N replicas to reply. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the lanes, arrows and finish lines; cyan (#37D7E7) for replies that count toward the quorum; warm yellow (#FFC857) for the straggling replies and the reply that completes the quorum; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. race: several horizontal white lanes with a vertical white finish line; two cyan dots have crossed it and the rest of the dots, slate, are still behind
2. more-racers: two race diagrams stacked: the top with three lanes, the bottom with four lanes; in the bottom one the second dot over the finish line is noticeably further left, highlighted yellow
3. floor: white axes with a cyan curve falling in steps from left to right and flattening onto a flat white floor line near the bottom
4. slower-read: two race diagrams side by side; the left waits for the second dot across the line, the right waits for a third dot, marked yellow, which crosses later
5. stragglers: a row of lanes where most dots are clustered near the start and one or two yellow dots lag far behind
6. broken-overlap: a row of four slate nodes with a cyan outline around the left two and a yellow outline around the right two, and no node inside both

When done, reply with the saved file path and pixel size only.

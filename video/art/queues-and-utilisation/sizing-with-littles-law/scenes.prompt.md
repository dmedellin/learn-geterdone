Use your image generation tool to create ONE image and save it as `video/art/queues-and-utilisation/sizing-with-littles-law/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed system design education video about sizing a connection pool with Little's Law, and the throughput ceiling a pool imposes. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight for the outlines, slots and arrows; cyan (#37D7E7) for the connections in use; warm yellow (#FFC857) for the requests waiting and the slower dependency; muted slate (#3A4F63) flat fills for everything else.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. pool-slots: a white-outlined rack of twenty small rectangular slots in two rows, each slot holding a cyan block, with a white arrow leading into a database cylinder at the right.
2. slower-database: two copies of the same rack of slots side by side; the right-hand one connects to a database cylinder drawn in yellow, and has a line of slate blocks waiting outside it.
3. waiting-threads: a white box with eight small cyan squares for cores, beside a much larger crowd of slate threads each with a small white pause mark, all waiting on a long white line to a distant cylinder.
4. bunching: a white timeline with small cyan blocks arriving unevenly, several bunched tightly together in one place and spread thinly elsewhere.
5. queue-before-pool: a rack of full cyan slots with a line of yellow blocks waiting in front of it.
6. three-forms: three small identical white triangles in a row, each divided into three parts, with a different one of the three parts filled cyan in each triangle.

When done, reply with the saved file path and pixel size only.

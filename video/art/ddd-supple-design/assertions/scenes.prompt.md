Use your image generation tool to create ONE image and save it as `video/art/ddd-supple-design/assertions/scenes.png` in this repository. Do not write code to draw it; generate it with the image model. Highest quality, as large as the tool allows, landscape if available.

It is a sheet of 6 explainer illustrations for a calm, well-designed software-design education video about assertions, stating the post-conditions of operations and the invariants of classes so that a client can use a command without tracing how it works. Strict grid: 2 columns x 3 rows. Each cell holds one landscape (16:9) illustration.

STYLE (identical across all six):
- Flat vector explainer graphics, like a carefully designed engineering blog or a 3Blue1Brown-style diagram. Clean geometry, generous whitespace, front-on, no perspective, no 3D, no gradients, no texture, no shading, no glow.
- Palette: white (#FFFFFF) rounded strokes of even weight; cyan (#37D7E7) for a guarantee that holds and the state it promises; warm yellow (#FFC857) for a broken invariant or a clause that is false; muted slate (#3A4F63) flat fills for every other shape.
- No people, no faces, no robots, no hands.
- ABSOLUTELY NO text, letters, numbers or labels anywhere.
- Background: one perfectly flat solid magenta (#FF00FF) across the whole image, with wide magenta gaps between cells. No frames, borders or cell backgrounds.

CELLS, left to right, top to bottom:
1. nested-commands: one slate box with a white arrow into a second box, which has arrows into two more boxes, each with arrows into further boxes, like a cascade of nested calls drifting off to the right, the far boxes faint.
2. two-implementations: one cyan outline shape like a plug socket at the top, with two different slate boxes plugged into it below; one box has a single small white mark changing, the other has a yellow splash spreading from it.
3. test-shape: three slate panels in a row joined by white arrows: the first holds a few neatly arranged blocks, the second a gear in motion, the third the blocks rearranged with a white rounded tick inside a cyan circle.
4. whose-fault: two dock racks drawn as slate rails with small bicycle wheel circles in slots; the right rack is overfull, one extra wheel hanging off its end glowing yellow, and a white arrow from the left rack points to it.
5. paint-split: a slate paint can shape on the left pouring into a second can, then a white arrow to the right where the single can has been cleanly split into two separate shapes, one cyan and one slate.
6. bikes-from-nothing: a cyan dock rack with its slots unchanged on the left and a second dock rack on the right gaining extra wheel circles that appear from empty air, drawn in yellow with small sparkle marks.

When done, reply with the saved file path and pixel size only.

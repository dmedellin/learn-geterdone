---
format: short
lesson: gof-behavioral-requests/interpreter
title: Where do the brackets go?
---

@art syntax-tree
Turn a pricing formula into objects. Where do the brackets go?

@words text="setup + copies * (pages * per_page + binding)"
They go nowhere. Each operator becomes a node, each name a leaf, and the brackets just decide the shape.

@art interpret-up
Call interpret on the root, and each node is interpreted once, from its children up. For the lesson's print job, that's nine nodes, nine calls, and a price of ninety.

@end text="Full lesson on Learn"
That's the Interpreter pattern. The full lesson is on Learn.

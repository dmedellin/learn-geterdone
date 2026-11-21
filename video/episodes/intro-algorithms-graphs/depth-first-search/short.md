---
format: short
lesson: intro-algorithms-graphs/depth-first-search
title: Reachable and discovered later, but not a descendant
---

@art white-path-trap
Reachable, and discovered later. So it's a descendant, right? Not always.

@math items="2 [2, 5] · 3 [6, 7]@two to five"
In the lesson's graph, vertex three is reachable from two and found later. But two's interval is two to five, and three's is six to seven. Not nested.

@words text="The path must be all white"
When two was discovered, the path to three ran through a grey vertex. The white path theorem says that's not enough.

@end text="Full lesson on Learn"
Stamp the times yourself in the full lesson on Learn.

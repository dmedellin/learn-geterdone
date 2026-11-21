---
format: short
lesson: graph-algorithms/strongly-connected-components
title: Five points at seven, and seven is still alone
---

@art mutual-reach
Vertex five has an arc to seven. So are they in the same strongly connected component?

@words text="each must reach the other"
No. Strong connectivity needs a path both ways. Five reaches seven, but nothing comes back from seven, so seven is a component all on its own.

@words text="half a conjunction is no evidence"
Reachability one way is only half of the condition. So a one way arc isn't weak evidence for membership. It's no evidence at all.

@end text="Full lesson on Learn"
The full lesson, with both walks, is on Learn.

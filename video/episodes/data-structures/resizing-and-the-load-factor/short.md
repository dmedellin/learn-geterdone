---
format: short
lesson: data-structures/resizing-and-the-load-factor
title: Grow when full, shrink when half empty? It thrashes
---

@art thrash
Grow when full, shrink when half empty. It sounds symmetric, and it's a disaster.

@words text="grow at ½ · shrink at ½" sub="39 rehashes in 40 operations"
Grow, and the load factor halves, landing right on the shrink threshold. So the next delete shrinks it back. On forty operations, that's thirty nine rehashes.

@words text="grow at 1 · shrink at ¼" sub="2 rehashes · total 52"
Leave a gap, and the same forty operations rehash twice.

@end text="Full lesson on Learn"
The full lesson, with both policies side by side, is on Learn.

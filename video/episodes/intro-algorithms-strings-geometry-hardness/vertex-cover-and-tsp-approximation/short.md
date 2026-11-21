---
format: short
lesson: intro-algorithms-strings-geometry-hardness/vertex-cover-and-tsp-approximation
title: Within twice the optimum, without knowing the optimum
---

@art matching-bound
How can you promise twice the optimum, when nobody can compute the optimum?

@art take-both-ends
Take any edge, and put both its ends in the cover. Repeat. The edges you took form a matching, and every cover needs at least one end of each.

@math items="|C| = 2|A| ≤ 2|C*|@twice"
So your cover is exactly twice the matching, and at most twice the optimum.

@end text="Full lesson on Learn"
Measure the ratio yourself in the full lesson on Learn.

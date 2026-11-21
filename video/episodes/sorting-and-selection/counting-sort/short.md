---
format: short
lesson: sorting-and-selection/counting-sort
title: Counting sort on twelve keys can cost four billion
---

@art wide-range
Counting sort is linear time. On twelve keys, it can cost four billion steps.

@math items="k = 5:  12 + 5 = 17@a range of five;;32-bit key:  12 + 2³²@thirty two bit"
The cost is n plus k. Twelve keys over a range of five, that's seventeen. Over a thirty two bit range, it's twelve plus two to the thirty two.

@words text="Linear in n + k, not in n"
So always name k. The range decides whether this is the fastest sort, or one you can't run.

@end text="Full lesson on Learn"
The full lesson, with a range you can widen, is on Learn.

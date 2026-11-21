---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/concurrency-problems
title: Two correct counts, one impossible total
---

@art inconsistent-read
Two correct counts can add up to a number that was never true.

@math items="7 (before) + 8 (after) = 15@fifteen;;before: 12 · after: 17@twelve"
Martin counts seven classes in one package. Then David adds five classes across both. Martin counts eight in the other, and gets fifteen. The real total was twelve, then seventeen.

@words text="Right reads. Wrong time."
Each read was true when he made it. The sum belongs to no state the data was ever in.

@end text="Full lesson on Learn"
The full lesson, with a lab that replays the commit, is on Learn.

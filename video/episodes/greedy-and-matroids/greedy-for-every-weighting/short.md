---
format: short
lesson: greedy-and-matroids/greedy-for-every-weighting
title: Greedy won twelve times in a row and was still wrong
---

@art weight-cube
Greedy won on twelve weightings in a row. The thirteenth beat it.

@art path-weights
Take three edges in a path, where no two chosen edges may share a vertex. That's not a matroid.

@words text="1 2 2" sub="greedy 2 · best 3"
With weights one, two, two, greedy grabs the middle edge, worth two. The two ends are worth three. For a non matroid, some weighting always beats greedy.

@end text="Full lesson on Learn"
Sweep the weightings yourself on Learn.

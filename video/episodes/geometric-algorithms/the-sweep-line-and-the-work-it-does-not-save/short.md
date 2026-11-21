---
format: short
lesson: geometric-algorithms/the-sweep-line-and-the-work-it-does-not-save
title: The sweep line that saves nothing
---

@art spread-pairs
A sweep line skipped twelve of fifteen pair tests. On another input, it skipped none.

@math items="spread out: 3 tests vs 15 pairs@three tests;;all crossing: 6 tests vs 6 pairs@six tests"
Six spread out segments need three tests instead of fifteen. But four segments that all cross the middle need six tests out of six. The status list holds everything at once.

@words text="The saving depends on the output"
The work grows with the number of crossings, so a tangle saves nothing.

@end text="Full lesson on Learn"
The full lesson on the sweep line is on Learn.

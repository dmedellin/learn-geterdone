---
format: short
lesson: dynamic-programming-and-sequential-decisions/the-state-is-what-is-left
title: Why give the next unit to the best bidder loses
---

@art jump-staircase
Give every unit to whoever gains most from it, and you lose by six.

@words text="P: 0 2 4 15 16" sub="+2, +2, then +11"
Activity P gains two, then two, then eleven. Looking one unit ahead, you never pay for those first two, so you never reach the eleven.

@math items="greedy: 15@fifteen;;recursion: 21@twenty one"
Greedy totals fifteen. Dynamic programming asks how much P should take, prices three, and gets twenty one.

@end text="Full lesson on Learn"
The full lesson, with the whole state grid, is on Learn.

---
format: short
lesson: the-simplex-method/degeneracy-cycling-and-blands-rule
title: Six pivots and the simplex method is back where it started
---

@art cycle-loop
The simplex method can run forever, and the arithmetic is exact.

@math items="six pivots, every step 0@step zero;;tableau 7 = tableau 1, entry for entry@entry for entry;;z = 0 forever,  optimum 1/20@one twentieth"
On Beale's example, every pivot has step zero. After six of them, the tableau is identical to the start, entry for entry. It circles forever at zero, while the true optimum is one twentieth.

@words text="Bland's rule: lowest index, always"
Choose by lowest index instead, and no basis can repeat.

@end text="Full lesson on Learn"
The full lesson, with the cycle and the fix, is on Learn.

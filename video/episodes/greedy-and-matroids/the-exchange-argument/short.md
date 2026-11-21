---
format: short
lesson: greedy-and-matroids/the-exchange-argument
title: How one swap disproves a greedy rule
---

@art swap-overlap
One swap is all it takes to break a wrong greedy rule.

@words text="A 0–5 · B 4–6 · C 5–10" sub="optimum: A C"
The best answer for these three intervals is A and C. Shortest first picks B instead.

@words text="B in for A → B C" sub="same size, but they overlap"
The exchange argument swaps B in for A, giving B and C. Same size, but B and C overlap. The proof stops right there.

@end text="Full lesson on Learn"
Watch the chain survive or break, swap by swap, on Learn.

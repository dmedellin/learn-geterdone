---
format: short
lesson: networks-flows-paths-and-assignments/the-transportation-problem
title: The zero you must never erase from a transportation table
---

@art broken-forest
A transportation start with one cell too few can't be solved at all.

@math items="basis = m + n − 1 cells@m plus n minus one;;3 + 4 − 1 = 6@three plus four"
A basis needs m plus n minus one occupied cells. Three plants and four depots: three plus four minus one is six.

@words text="A basic zero is still in the basis"
Sometimes one of those cells carries zero. It still counts. Erase it, and the cells split into pieces, and the potentials never get values.

@end text="Full lesson on Learn"
The full lesson, with both starting rules to run, is on Learn.

---
format: short
lesson: intro-algorithms-sorting/analysis-of-randomized-quicksort
title: When do two keys get compared in quicksort?
---

@art between-set
Two keys in quicksort meet with a probability you can write in one line.

@art split-apart
Look at every key between them. The first pivot chosen from that set decides. If it lands strictly between, they're split apart forever. If it's one of the two, they're compared.

@math items="Pr = 2 / (j − i + 1)@two over j minus i plus one"
So the chance is two over j minus i plus one. Add that over all pairs, and you get O of n log n, on every input.

@end text="Full lesson on Learn"
Work the sum yourself in the full lesson on Learn.

---
format: short
lesson: sorting-and-selection/radix-sort
title: Radix sort from the top digit gets it backwards
---

@art msd-overwrite
Radix sort from the most important digit first? You end up sorted by the least important one.

@math items="720 355 436 457 657 329 839@seven twenty"
Run the passes hundreds, tens, units, with no recursion, and you get seven twenty, three fifty five, four thirty six, and so on. Sorted on the units digit, and nothing else.

@words text="The last pass decides the order"
So the most significant digit has to go last, and every pass has to be stable.

@end text="Full lesson on Learn"
The full lesson, with both broken variants, is on Learn.

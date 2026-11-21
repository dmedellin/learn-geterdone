---
format: short
lesson: randomised-algorithms/balls-in-bins-and-the-birthday-bound
title: A thousand slots, and a collision by key 38
---

@art balls-bins
A hash table with a thousand slots likely collides by the thirty eighth key.

@list items="m = 365:  n = 23@three hundred and sixty five|m = 1000:  n = 38@a thousand"
Multiply out the exact chance that every key lands apart. With three hundred and sixty five slots, it drops below a half at twenty three keys. With a thousand, at thirty eight.

@words text="Collisions start near √m"
Collisions arrive near the square root of the table size, not near the size.

@end text="Full lesson on Learn"
The full lesson is on Learn.

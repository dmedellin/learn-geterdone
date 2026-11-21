---
format: short
lesson: gof-introduction/inheritance-versus-composition
title: Twelve subclasses, or nine classes?
---

@art class-explosion
A music player with four sources and three play orders. How many classes?

@math items="4 × 3 = 12 subclasses, 13 classes@one subclass;;(4 + 1) + (3 + 1) = 9@one hierarchy"
One subclass per combination is twelve, thirteen with the parent. One hierarchy per aspect, composed together, is nine.

@words text="Products vs sums"
Subclassing multiplies. Composition adds. Add a new play order, and that's four more subclasses, or just one class. And you can swap the order while it runs.

@end text="Full lesson on Learn"
The full lesson, and what composition costs, is on Learn.

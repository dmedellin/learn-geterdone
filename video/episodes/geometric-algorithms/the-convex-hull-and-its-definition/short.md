---
format: short
lesson: geometric-algorithms/the-convex-hull-and-its-definition
title: Every convex hull algorithm secretly sorts
---

@art parabola-lift
Any convex hull algorithm can sort numbers for you. Here's how.

@words text="5, 1, 9, 3, 7  →  (x, x²)"
Take five, one, nine, three, seven, and lift each to the point x, x squared, on a parabola.

@art rubber-band
Every one of those points is a hull vertex, and the lower chain lists them in sorted order. So computing a hull means sorting, and you can't beat the n log n lower bound.

@end text="Full lesson on Learn"
The full lesson on the convex hull is on Learn.

---
format: short
lesson: greedy-and-matroids/fractional-and-0-1-knapsack
title: The greedy knapsack that grabbed a crumb
---

@art crumb
Greedy by value per weight can get two percent of the best answer.

@words text="1/2 and 50/100 · capacity 50"
One item weighs one and is worth two. Another weighs fifty and is worth a hundred. The bag holds fifty.

@words text="density greedy: 2 · optimum: 100"
The tiny item is denser, so greedy takes it first. Now the big one won't fit. Two, against a hundred. Taking the better of greedy and the best single item fixes it.

@end text="Full lesson on Learn"
Try it on Learn.

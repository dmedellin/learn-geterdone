---
format: short
lesson: strings-and-pattern-matching/the-amortised-bound-as-a-count
title: How a loop that can run m times stays linear
---

@art potential-meter
An inner loop that can run m times still adds up to linear work.

@words text="k rises ≤ 1 per character"
Building the KMP failure function, the border length k rises by at most one per character. The inner loop only ever lowers it, and it can't go below zero.

@words text="falls ≤ rises ≤ m − 1"
So all the falls together can't outnumber the rises. At most m minus one inner steps, in total.

@end text="Full lesson on Learn"
Count them on Learn.

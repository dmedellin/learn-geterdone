---
format: short
lesson: randomised-algorithms/kargers-contraction
title: Merge random edges, find the minimum cut
---

@art contract-edge
Merge random edges until two blobs remain. Surprisingly often, you've found the minimum cut.

@words text="P(hit the cut) ≤ 2/n"
A small cut is hard to hit. If it has k edges, every vertex has at least k, so a random edge crosses it with probability at most two over n.

@math items="two triangles:  19/35 ≈ 0.54@nineteen thirty fifths;;bound:  1/15@one fifteenth"
On two triangles joined by two edges, it succeeds nineteen thirty fifths of the time. The guarantee is only one fifteenth.

@end text="Full lesson on Learn"
The full lesson is on Learn.

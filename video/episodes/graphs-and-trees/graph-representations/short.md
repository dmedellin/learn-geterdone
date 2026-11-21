---
format: short
lesson: graphs-and-trees/graph-representations
title: Square a graph's matrix and it counts walks
---

@art matrix-grid
Square a graph's adjacency matrix, and it counts walks for you.

@math items="A²[i][j] = walks of length 2 from i to j@from i to j"
The entry in row i, column j of A squared is the number of walks of length two from i to j.

@art walk-two-steps
In the four cycle, one to three has two of them: through vertex two, or through vertex four. And that's exactly the two the matrix reports, because multiplying sums over every middle vertex.

@end text="Full lesson on Learn"
The full lesson, with the matrix to square yourself, is on Learn.

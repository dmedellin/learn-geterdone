---
format: short
lesson: graphs-and-trees/planar-graphs
title: Why K5 can never be drawn without crossings
---

@art k5-and-k33
Five points, every pair joined, no crossings. It's impossible, and here's the proof.

@math items="E ≤ 3V − 6@at most three V;;K₅:  3 · 5 − 6 = 9@three times five;;but K₅ has 10 edges  ✗@ten edges"
Any simple planar graph with at least three vertices has at most three V minus six edges. For K five, that's three times five minus six, nine. But K five has ten edges. One too many.

@words text="Planar ⟺ no K₅, no K₃,₃ inside"
And K five is one of only two culprits. A graph can be drawn flat exactly when it hides no subdivision of K five or K three three.

@end text="Full lesson on Learn"
The full lesson on planar graphs is on Learn.

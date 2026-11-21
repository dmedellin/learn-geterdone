---
format: short
lesson: graphs-and-trees/graph-colouring
title: Two colours is easy. Three is NP-complete.
---

@art odd-even-cycles
Can you colour a graph with two colours, so neighbours differ? Easy to check. With three? Nobody knows a fast way.

@words text="χ ≤ 2: one search"
Two colours work exactly when the graph has no odd cycle, and one breadth first search tells you.

@words text="χ ≤ 3: NP-complete"
But deciding whether three colours are enough is NP complete. One more colour, and the problem goes from linear time to one of the hardest we know.

@end text="Full lesson on Learn"
The full lesson on graph colouring is on Learn.

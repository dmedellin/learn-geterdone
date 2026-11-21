---
format: short
lesson: graph-algorithms/negative-weights-and-bellman-ford
title: Same graph, six rounds or two
---

@art chain-orders
Same five arcs, same weights, same answer. One run takes six rounds, the other takes two.

@math items="typed backwards:  6 rounds@backwards;;typed forwards:  2 rounds@forwards"
Bellman Ford relaxes arcs in the order they're stored. Type a chain backwards, and each round moves one step. Forwards, one sweep carries it all the way.

@words text="The round count depends on the arc order"
So the rounds needed aren't a property of the graph alone.

@end text="Full lesson on Learn"
The full lesson, with the negative cycle certificate, is on Learn.

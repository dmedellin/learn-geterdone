---
format: short
lesson: graphs-and-trees/spanning-trees
title: The cheapest network, built greedily
---

@art kruskal-pentagon
Always grab the cheapest edge, and you get the cheapest network. That's rare.

@words text="Cheapest edge that closes no cycle"
Kruskal's algorithm sorts the edges by weight, then takes each one unless it would close a cycle. It never reconsiders a choice.

@words text="The cut property" sub="lightest crossing edge is in some optimum"
Usually greed fails. Here it's provably right, because the lightest edge across any split of the vertices belongs to some minimum spanning tree.

@end text="Full lesson on Learn"
The full lesson on minimum spanning trees is on Learn.

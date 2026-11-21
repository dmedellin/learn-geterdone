---
format: long
lesson: graph-algorithms/max-flow-and-min-cut
title: Max flow equals min cut, and the algorithm proves it
thumb: The failed search is the proof
---

@chapter The question
@title text="Max Flow and Min Cut" sub="Graph Algorithms" art=thumb
The augmenting path method stops when it can't find a path. But how do you know no cleverer method could push more? The answer is beautiful. The failed search hands you a proof.

@chapter Cuts
@art st-cut
An s t cut splits the vertices into a set S containing the source, and the rest, containing the sink. Its capacity is the total capacity of arcs leaving S. Arcs coming back into S count for nothing.

@chapter Weak duality
@words text="every flow value ≤ every cut capacity"
Here's the easy direction. Any flow's value is at most any cut's capacity. Everything reaching the sink has to cross out of S somewhere, and it can't cross faster than the capacity allows.

@math heading="Why" items="value = flow out of S − flow into S@net flow;;flow out ≤ capacity of S@at most;;flow in ≥ 0@at least zero"
More carefully: add up conservation over every vertex of S. Arcs inside cancel, so the value is the net flow across the cut, out minus in. The flow out is at most the capacity, and the flow in is at least zero. So the value is at most the capacity.

@words text="equal flow and cut ⟹ both optimal"
That one inequality makes an equality decisive. If you ever find a flow and a cut of the same size, each proves the other optimal.

@chapter The certificate
@art reachable-set
So here's the theorem. When no augmenting path remains, let S be every vertex the source can still reach in the residual network. The sink isn't in S, or the search would have succeeded. So S is a cut.

@list heading="Why its capacity equals the flow" items="Arcs out of S are full@Every arc leaving|Arcs into S carry nothing@every arc coming"
Every arc leaving S is full. If one had room, its forward residual arc would have extended the search. And every arc coming into S carries nothing. If one carried flow, its backward residual arc would have extended the search too. So the net flow across the cut is exactly its capacity.

@words text="max flow = min cut"
That capacity equals the flow's value. By weak duality, no flow beats this cut, and no cut is below this flow. Both are optimal. The algorithm produced its own proof.

@chapter Six vertices
@math heading="Source 1, sink 6" items="max flow:  23, in 3 augmentations@twenty three;;reachable:  {1, 2, 3, 5}@reachable set;;leaving:  2>4 12 + 5>4 7 + 5>6 4 = 23@arcs leaving it"
On the lab's six vertex network, the shortest path rule reaches twenty three in three augmentations. The reachable set afterwards is one, two, three and five. The arcs leaving it are two to four at twelve, five to four at seven, and five to six at four. Twenty three, all full.

@art all-cuts-list
Separately, the lab enumerates all sixteen sets containing one and not six. The smallest capacity among them is twenty three, attained by exactly one set, and it's the one the algorithm returned. Three numbers, three routes, one value.

@chapter Saturated isn't the cut
@art saturated-not-cut
A full arc isn't automatically in a minimum cut. On this four vertex network, the maximum flow is two, and three arcs end up full. But the cut is only the two arcs out of the reachable set, which is just the source. Delete the third full arc, and the sink is still reachable.

@words text="full: a fact about one arc" sub="in a cut: a fact about a partition"
That third arc is full because of what happens downstream, not because it's a bottleneck between the sides. Being full is local. Being in a cut is a statement about a partition.

@chapter Two more cautions
@art chain-cuts
The minimum cut isn't unique either. On a chain of three unit arcs, there are four sets containing the source, and three have capacity one. The algorithm returns one of them, the reachable set.

@math heading="The backwards preset, max flow 5" items="{1, 2, 3}:  5 + 1 = 6@one, two, three;;{1, 2}:  6, with 9 pointing back@one and two"
And direction matters. Here the maximum flow is five. The set one, two, three has capacity six. The set one and two also has capacity six, with nine units of capacity pointing back into it. Count those, and you'd get fifteen, and the theorem would break.

@art backward-arcs
Those nine units simply aren't part of the number. Net them off instead, and you'd get minus three. The one arithmetic that's right is to ignore them.

@chapter Where people slip
@list heading="Common slips" items="Counting arcs that point back into the cut@The first|Reading the saturated arcs as the cut@The second|Treating the enumeration as the proof@And the third"
The first slip is counting arcs that point back into the cut. The second is reading all the saturated arcs as the cut. The check is cheap: delete them and see whether the sink is still reachable. And the third is treating the sixteen cut enumeration as the proof. The reachable set argument covers every network.

@chapter Try it
@words text="Find the reachable set yourself" sub="six-vertex network, after the flow reaches 23"
Your turn. After the flow reaches twenty three, draw the residual network, find everything the source can reach, and add up the capacities of the arcs leaving it.

@end text="Read the certificate"
You can run the flow, read off the cut, and check it against every cut there is, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: intro-algorithms-graphs/maximum-flow
title: Maximum flow: why Ford-Fulkerson needs backward arcs
thumb: Sometimes you send it back
---

@chapter Material in motion
@title text="Flow Networks and Ford-Fulkerson" sub="Introduction to Algorithms, Sections 26.1–26.2" art=thumb
Chapter twenty six asks how much can move through a network at once.

@quote text="Imagine a material coursing through a system from a source, where the material is produced, to a sink, where it is consumed." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 26"
It opens with a picture. Imagine a material coursing through a system from a source, where the material is produced, to a sink, where it is consumed.

@art flow-network
Arcs are conduits with capacities. Vertices are junctions where nothing collects. A flow keeps each arc between zero and its capacity, and at every vertex except the source and sink, flow in equals flow out. Its value is the net flow out of the source. Several sources or sinks can be joined to one supersource or supersink.

@chapter The method
@art residual
Ford Fulkerson starts with zero flow and builds the residual network. For each arc, there's the spare capacity forward, and the flow already carried, as capacity backward. Sending against an arc's flow cancels some of it. It's a method, not one algorithm, because it leaves open how to choose each path.

@list heading="Repeat" items="find an augmenting path@an augmenting path|push its bottleneck@push|stop when none is left@until no"
Find any route from source to sink in the residual network, an augmenting path. Push along it the least residual capacity on the path, its bottleneck. Repeat until no augmenting path remains.

@chapter Why it stops at the maximum
@art cut
A cut splits the vertices into a side with the source and a side with the sink. The net flow across any cut equals the flow's value, so no flow can exceed any cut's capacity.

@words text="max flow = min cut" sub="Theorem 26.6"
The max flow min cut theorem says three things are equivalent. The flow is maximum. There's no augmenting path. And the flow equals some cut's capacity. When the method stops, the vertices still reachable from the source form that cut.

@chapter Stuck without backward arcs
@math heading="1>2 2 · 1>3 1 · 2>3 2 · 2>4 1 · 3>4 2 · 4>5 3" items="push 2 on 1 → 2 → 3 → 4 → 5@pushes two;;no backward arcs: stuck at 2, max is 3@stops at two"
Here's the lesson's network: five vertices, six arcs, source one and sink five. With backward arcs left out, the first path found pushes two along one, two, three, four, five, and the lab stops at two. The true maximum is three.

@art stuck
Nothing out of the source is full. But the arc from three to four is, and the only way past it is to take back flow already sent along two to three.

@math heading="With backward arcs" items="1 → 3, back along 2 → 3, 2 → 4 → 5: bottleneck 1@back along;;flow 3 · cut {1}: 2 + 1 = 3@flow equals cut"
Put the backward arcs in, and the second path is one to three, then back along two to three against its flow, then two, four, five, with bottleneck one. The flow is three, and the cut around vertex one has capacity two plus one, three. Flow equals cut.

@art cancel-flow
That push cancels one unit on two to three, and sends it by two to four instead. Switch to the shortest path rule, and the lab makes three augmentations, none of them backward, and also reaches three. Either way, the final search reaches only vertex one.

@chapter How long it takes
@art bfs-path
With integer capacities, each push adds at least one, so the method makes at most f star augmentations, O of E times f star. That can be terrible when capacities are large. Edmonds and Karp choose the path with fewest arcs, by breadth first search, and the bound becomes O of V E squared, whatever the capacities.

@words text="zigzag: 4 augmentations vs 2" sub="first-found vs shortest"
On the lab's zigzag preset, with backward arcs in, first found paths need four augmentations to reach two hundred. Shortest paths need two.

@chapter Where people slip
@list heading="Common slips" items="Flow can only be added to@The first|Full arcs are the minimum cut@The second|Time depends only on graph size@the third"
The first slip is thinking flow, once sent, can only be added to. The second is taking the full arcs to be the minimum cut. Here five arcs end full, but the cut has two. And the third is assuming the time depends only on the graph's size. With poor paths, it grows with the capacities.

@chapter Try it
@words text="1>2 3 · 1>3 2 · 2>3 1 · 2>4 2 · 3>4 3 · 4>5 4" sub="source 1 · sink 5 · shortest paths"
Your turn. Run Ford Fulkerson by hand with shortest augmenting paths, writing each residual network, and name a minimum cut. Then try first found paths with backward arcs out. Does it get stuck?

@end text="Push some flow"
You can push flow with and without backward arcs, on Learn. That's learn dot get er done dot I O.

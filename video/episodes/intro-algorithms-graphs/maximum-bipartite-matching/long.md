---
format: long
lesson: intro-algorithms-graphs/maximum-bipartite-matching
title: Maximum bipartite matching is a maximum flow in disguise
thumb: Every capacity is one
---

@chapter A problem in disguise
@title text="Maximum Bipartite Matching" sub="Introduction to Algorithms, Section 26.3" art=thumb
Some problems look nothing like flow, and turn out to be flow anyway.

@quote text="Some other combinatorial problems seem on the surface to have little to do with flow networks, but can in fact be reduced to maximum-flow problems." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 26.3"
Section twenty six point three puts it this way. Some other combinatorial problems seem on the surface to have little to do with flow networks, but can in fact be reduced to maximum flow problems.

@art machines-tasks
The authors' example is machines and tasks. An edge says a machine can do a task. You want as many machines busy as possible, at once.

@chapter Matchings
@art matching
A matching is a set of edges in which no vertex appears twice. A maximum matching has as many edges as any matching can. The graph is bipartite: its vertices split into two sides, L and R, with every edge running between them.

@words text="Maximal ≠ maximum" sub="nothing can be added · but more is possible"
Careful with one word. A maximal matching is one that nothing can be added to. That's weaker. It can still be smaller than the maximum.

@chapter Build the network
@art unit-network
Add a source with an arc to every vertex in L, and a sink with an arc from every vertex in R. Direct every edge from L to R, and give every arc capacity one.

@math heading="Lemma 26.9" items="matching of size k → flow of value k@a matching of size k;;integer flow of value k → matching of size k@an integer flow"
Then a matching of size k gives a flow of value k, one unit along each matched edge. And an integer flow of value k gives a matching of size k, since each vertex of L receives at most one unit, and each vertex of R passes on at most one.

@chapter Why whole numbers matter
@words text="Integrality theorem" sub="integer capacities ⇒ Ford-Fulkerson returns an integer flow"
But a maximum flow could, in principle, split units in half. Theorem twenty six point ten closes the gap. With integer capacities, Ford Fulkerson only ever pushes whole bottlenecks, so every arc of its flow carries zero or one. The arcs from L to R carrying one are a matching.

@art half-flow
Why does that matter? If L one and L two are both joined to R one and R two, half a unit on each of the four middle arcs is a maximum flow of value two. And it's no matching at all.

@math heading="Running time" items="at most min(|L|, |R|) = O(V) augmentations@at most;;each O(E) → O(VE)@each found"
A matching has at most the smaller side's size of edges, which is O of V. So there are O of V augmentations, each found in O of E time. That's O of V E in all.

@chapter Four machines, four tasks
@math heading="1-1, 1-2, 2-1, 3-2, 3-3, 4-3, 4-4" items="greedy: L1–R1, L3–R2, L4–R3 · stuck at 3@The greedy pass;;flow: L1–R2, L2–R1, L3–R3, L4–R4 · 4@The flow finds"
The lesson's graph has four machines, four tasks, and seven allowed pairs. The greedy pass takes L one with R one, L three with R two, L four with R three, and stops at three, because L two's only task is taken. The flow finds four, every machine busy.

@art augmenting-zigzag
How? Along one augmenting path from L two. To R one, back to L one, on to R two, back to L three, on to R three, back to L four, and on to R four. Three greedy pairs are undone, and four new ones made.

@art vertex-cover
The lab checks the answer other ways. The cut gives a vertex cover, a set of vertices touching every pair, and a cover can never be smaller than a matching. This one has four vertices. All one hundred twenty eight subsets of the pairs agree on four, and Hall's condition holds.

@chapter Where people slip
@list heading="Common slips" items="Maximal means maximum@The first|Every maximum flow is a matching@The second|Push-relabel is needed@the third"
The first slip is thinking a matching nothing can be added to is maximum. The second is believing every maximum flow is a matching. The theorem is only about the flow Ford Fulkerson returns. And the third is expecting push relabel to be needed. O of V E is already enough.

@chapter Try it
@words text="1-1, 1-2, 2-2, 3-2, 3-3, 3-4" sub="3 people · 4 shifts"
Your turn. Three people, four shifts, and these pairs. Draw the flow network, find a maximum matching by hand with augmenting paths, and check whether a greedy pass in that order finds it.

@end text="Match machines to tasks"
You can match your own pairs and watch greedy get stuck, on Learn. That's learn dot get er done dot I O.

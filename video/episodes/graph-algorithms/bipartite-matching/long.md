---
format: long
lesson: graph-algorithms/bipartite-matching
title: Bipartite matching as max flow, with the cover as proof
thumb: Pairs are a flow problem
---

@chapter The question
@title text="Bipartite Matching" sub="Graph Algorithms" art=thumb
You've got people and jobs, and a list of who can do what. Pair as many as possible, with nobody used twice. That's a max flow problem in disguise. And when not everyone can be paired, the same run tells you exactly why.

@chapter Words first
@list heading="Matchings" items="Matching: pairs sharing no vertex@A matching|Maximal: nothing more can be added@maximal|Maximum: none is larger@maximum"
A matching is a set of allowed pairs, no two sharing a vertex. It's maximal if no more pairs can be added, and maximum if no matching is larger. Those aren't the same thing.

@chapter The construction
@art flow-network
Add a source with an arc of capacity one to every left vertex. Add a sink with an arc of capacity one from every right vertex. And for each allowed pair, an arc of capacity one from left to right. Find a maximum flow. The pair arcs carrying flow are a maximum matching.

@list heading="Why the maxima are equal" items="Matching of size k → flow of value k@A matching|Integer flow of value k → matching of size k@an integer flow"
A matching gives a flow of the same value: one unit through each matched pair, and no vertex is used twice. And an integer flow gives a matching. If two flow carrying pair arcs shared a left vertex, it would emit two while receiving at most one. So each maximum bounds the other.

@words text="every bottleneck is 1" sub="so the flow is whole"
And the flow comes out in whole numbers, because every capacity is one, so every push is by one. A fractional flow would carry no matching at all, so the lab checks it.

@chapter Three competing for two
@math heading="L1–R1, L2–R1, L3–R1, L3–R2" items="network:  7 vertices, 9 arcs@seven vertices;;max flow:  2, in 2 augmentations@maximum flow"
Three on the left, two on the right. The allowed pairs are L one with R one, L two with R one, L three with R one, and L three with R two. The network has seven vertices and nine arcs, and the maximum flow is two, reached in two augmentations.

@art matched-pairs
The pair arcs carrying flow are the matching: L one with R one, and L three with R two. A search over every subset of the four pairs, which knows nothing about flow, also finds two.

@art cover
And the cut, read back, is a cover: L three and R one. It touches every pair. L one R one and L two R one by R one, L three R one by both, and L three R two by L three. Four pairs, two vertices. And no single vertex could do it, because two of the pairs share nothing.

@chapter Why it stopped at two
@art deficient-set
L one and L two have only R one between them. Two left vertices can't both be matched into one right vertex. The lab exhibits that set: L one and L two, a set of two, with a neighbourhood of size one.

@words text="|N(S)| < |S|" sub="a proof you can check by eye"
That's the general shape of the obstruction: a set of left vertices whose combined neighbourhood is smaller than itself. It's a proof that no better matching exists, checkable by looking at four pairs, not by trusting a flow.

@art star
The star case is the same thing bigger. Four on each side, and the first three left vertices only like R one. The maximum is two, the cover is L four and R one, and one popular right vertex is the whole story.

@chapter Greedy depends on order
@math heading="Pairs L2–R2, L1–R2, L2–R1" items="in that order:  1 pair@in that order;;order L1–R2, L2–R1, L2–R2:  2 pairs@the same three pairs"
Take two on each side, with pairs L two R two, L one R two, and L two R one. Greedy in that order takes L two R two, which blocks both others. One pair. Taking the same three pairs in the order L one R two, L two R one, L two R two gives two.

@art greedy-blocked
So a matching nothing can be added to may be half the largest one. And an augmenting path is exactly what repairs it. In this network it alternates between unmatched and matched pairs, and swaps them.

@chapter Where people slip
@list heading="Common slips" items="Giving source or sink arcs capacity above 1@The first|Taking all saturated arcs as the matching@The second|Reporting a shortfall without the obstruction@And the third"
The first slip is giving the source or sink arcs a capacity above one, which lets a vertex be used twice. The second is taking all the saturated arcs as the matching. It's only the middle layer. And the third is reporting a shortfall without the obstruction. L one and L two both need R one. That's something you can act on.

@chapter Try it
@words text="Three left, three right, your own pairs" sub="find the matching and the cover"
Your turn. Write down three people, three jobs, and who can do what. Build the network, find a maximum matching, and read off a cover of the same size.

@end text="Find the obstruction"
You can build a pairing problem and read the matching, the cover and the obstruction off one run, on Learn. That's learn dot get er done dot I O.

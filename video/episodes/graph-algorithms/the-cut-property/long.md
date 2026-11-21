---
format: long
lesson: graph-algorithms/the-cut-property
title: The cut property: the lemma behind every minimum spanning tree
thumb: Lightest across the cut
---

@chapter The question
@title text="The Cut Property" sub="Graph Algorithms" art=thumb
Kruskal and Prim build minimum spanning trees in completely different ways. Yet one short lemma justifies every edge either of them takes. This is that lemma.

@chapter The words
@art cut
A cut splits the vertices into a set S and the rest. S can't be empty, and can't be everything. An edge crosses the cut if exactly one end is in S. Nothing requires S to be connected, or half the graph.

@words text="spanning tree: V − 1 edges, connected, no cycle"
A spanning tree connects every vertex with no cycle, and on V vertices it has V minus one edges. A minimum spanning tree has the least total weight. There may be several.

@chapter The lemma
@words text="Lightest crossing edge is in SOME minimum tree" sub="strictly lightest → in EVERY one"
Here it is. Take any cut, and a lightest crossing edge e. Then some minimum spanning tree contains e. And if e is strictly the lightest, every minimum spanning tree contains it.

@art exchange
The proof is an exchange. Take a minimum tree T without e. Adding e makes exactly one cycle. That cycle starts on one side and ends on the other, so it crosses the cut again, at some edge g.

@math heading="Swap g for e" items="T + e − g is a spanning tree@a spanning tree;;weight:  w(T) + w(e) − w(g)@with weight;;w(e) ≤ w(g)  ⟹  ≤ w(T)@at most"
Remove g. It was on a cycle, so nothing disconnects, and you still have V minus one edges. So it's a spanning tree, with weight T plus e minus g. Since e is a lightest crossing edge, that's at most T. So it's minimum too, and it contains e.

@words text="strict: w(e) < w(g) ⟹ lighter than T, impossible"
And if e is strictly lightest, the new tree would weigh strictly less than a minimum tree. That's impossible. So no minimum tree could have left e out.

@chapter Checked by enumeration
@math heading="S = {1, 2, 3}" items="crossing:  2-4 at 5,  3-4 at 7@two edges cross;;8 spanning trees,  1 minimum,  weight 17@eight spanning trees;;the minimum tree contains 2-4@contains"
The lab doesn't quote the lemma. It enumerates every spanning tree. On its six vertex graph, with S as one, two and three, two edges cross: two to four at weight five, and three to four at seven. There are eight spanning trees, exactly one minimum, at weight seventeen. And it contains two to four.

@art all-cuts
Those weights are distinct, so the minimum tree is unique. Sweep all sixty two proper cuts of those six vertices, and the lightest crossing edge is in a minimum tree every time.

@chapter Where some and every split
@art equal-triangle
Now a triangle with all three weights equal to one, and S as vertex one alone. Two edges cross, tied. There are three spanning trees, all three minimum, at weight two. Each edge is in exactly two of them. So the lightest crossing edge is in some minimum tree, but not every one.

@chapter The cycle property
@words text="Strictly heaviest on a cycle → in NO minimum tree"
Run the exchange backwards and you get the cycle property. If an edge is strictly the heaviest on some cycle, no minimum spanning tree contains it.

@art heaviest-on-cycle
On a square with a diagonal, there are eight spanning trees and one minimum, at weight six. Two edges appear in none: four to one at weight nine, and the diagonal, two to four, at four. That second one isn't the heaviest in the graph. It's the heaviest on the cycle two, three, four.

@chapter What it doesn't say
@art lightest-per-vertex
It doesn't say that taking the lightest edge at each vertex builds a tree. On a path with weights one, five, one, six, one, that rule picks three edges and leaves three separate pieces. Each is in the minimum tree. They're just not enough of it.

@chapter Where people slip
@list heading="Common slips" items="Thinking it's about the lightest edge overall@The first|Upgrading some to every despite a tie@The second|Treating the enumeration as the proof@And the third"
The first slip is reading the lemma as being about the lightest edge in the whole graph. The cut is part of the statement. The second is upgrading some to every without checking for ties. And the third is treating the enumeration as the proof. It stops at seven vertices. The exchange covers the rest.

@chapter Try it
@words text="Pick a cut on the six-vertex graph" sub="find the lightest crossing edge, check it's in the tree"
Your turn. On the six vertex graph, choose a different S. Find its crossing edges and the lightest one, and check that it's in the minimum tree of weight seventeen.

@end text="Check every spanning tree"
You can pick any cut and see every spanning tree listed, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: graphs-and-trees/graph-isomorphism
title: Graph isomorphism: when two drawings are the same graph
thumb: Same graph, different drawing
---

@chapter The question
@title text="Subgraphs and Graph Isomorphism" sub="Graphs and Trees" art=thumb
Here are two drawings. One is a square with both diagonals. The other is a triangle with a dot in the middle joined to every corner. Are they different graphs?

@art k4-two-drawings
They're not. Both are K four, four vertices with every pair joined. The drawing carries no information, so the real question is: when are two graphs the same, and how would you prove it, or disprove it?

@chapter Subgraphs
@art subgraph-induced
First, a piece of a graph. H is a subgraph of G when its vertices are some of G's vertices, and its edges are some of G's edges. It's the subgraph induced by a set of vertices S when it keeps every edge of G that has both ends in S.

@chapter Isomorphism
@math heading="Isomorphism" items="f : V₁ → V₂, a bijection@a bijection;;u ~ v in G₁  ⟺  f(u) ~ f(v) in G₂@if and only if"
Two graphs are isomorphic when there's a bijection f from the vertices of one to the vertices of the other, so that u and v are adjacent in the first if and only if f of u and f of v are adjacent in the second.

@words text="Same graph, new labels, new drawing"
Notice that it works both ways. Adjacent goes to adjacent, and non adjacent goes to non adjacent. Isomorphic graphs are the same graph with different labels and a different picture. So anything defined by adjacency alone, like degrees, cycles or connectivity, they share.

@chapter Proving it
@art bijection-arrows
To prove two graphs are isomorphic, there's only one way: show the bijection, and check every edge. Take the four cycle one two three four, and a graph on a, b, c, d with edges a b, b d, d c and c a.

@math heading="1→a, 2→b, 3→d, 4→c" items="12 → ab  ✓@one two goes;;23 → bd  ✓@two three;;34 → dc  ✓@three four;;41 → ca  ✓@four one;;4 edges each  ⟹  isomorphic@four edges"
Map one to a, two to b, three to d, and four to c. Then one two goes to a b. Two three goes to b d. Three four goes to d c, and four one goes to c a. Every edge lands on an edge. And both have four edges, so no non edge can land on an edge. They're isomorphic.

@chapter Disproving it
@list heading="Invariants" items="number of vertices@vertices|number of edges@edges|degree sequence@degree sequence|components@components|cycle lengths, triangles@cycle lengths"
To prove they're not isomorphic, find an invariant that differs. That's a property isomorphic graphs always share. The count of vertices, the count of edges, the degree sequence, the number of components, the cycle lengths and the number of triangles.

@art triangles-vs-hexagon
Here's the standard warning. Two separate triangles, and a six cycle. Both have six vertices and six edges, and every vertex has degree two.

@math heading="Two triangles vs C₆" items="|V|: 6 · 6  same@six vertices;;|E|: 6 · 6  same@six edges;;degrees: 222222 · 222222  same@degrees;;components: 2 · 1  different@components;;shortest cycle: 3 · 6  different@shortest cycle"
Six vertices each, six edges each, and degrees all two. Three agreements, and they're worth nothing. But components: two against one. And shortest cycle: three against six. Either one of those disagreements is a complete proof that they're not isomorphic.

@words text="Invariants disprove. They never prove."
That's the whole asymmetry. One difference disproves. Agreement on every invariant you can list still proves nothing. Only an explicit bijection does.

@chapter How hard is it?
@art many-bijections
So how hard is deciding isomorphism? Nobody knows a polynomial time algorithm, and nobody has shown it's NP complete. Very few natural problems sit in that middle. In 2015, Babai announced a quasi polynomial algorithm, faster than exponential, slower than polynomial. In practice, testers handle graphs with thousands of vertices routinely.

@chapter Where people slip
@list heading="Common slips" items="Treating matching invariants as proof@The first|Trusting similar drawings@The second|Checking only that edges map to edges@And the third"
The first slip is treating matching invariants as proof. The second is trusting how the drawings look. And the third is checking only that edges map to edges. That's enough when the edge counts are equal, but you have to say so. In general, check both directions.

@chapter Try it
@words text="Same degree sequence." sub="Are they isomorphic?"
Your turn. Two graphs have the same degree sequence. Must they be isomorphic? Think of the triangles, and then build your own pair with the same degrees, and find the invariant that tells them apart.

@art same-degrees
And remember why the degree sequence is so tempting. It's the first invariant everyone reaches for, and it's genuinely weak. There are pairs of graphs that agree on every invariant in the list and still aren't isomorphic.

@end text="Compare invariants yourself"
You can load both graphs and compare their invariants side by side, on Learn. That's learn dot get er done dot I O.

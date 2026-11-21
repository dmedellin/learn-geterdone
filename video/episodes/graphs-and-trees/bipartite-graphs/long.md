---
format: long
lesson: graphs-and-trees/bipartite-graphs
title: Bipartite graphs: two colours, and the odd cycle that breaks them
thumb: No odd cycle, two sides
---

@chapter The question
@title text="Bipartite Graphs" sub="Graphs and Trees" art=thumb
Can you colour every vertex of a graph with one of two colours, so that every edge joins two different colours? Sometimes you can. And there's exactly one thing that can stop you.

@chapter Two sides
@art two-sides
A graph is bipartite when its vertices split into two sets, X and Y, with every edge joining a vertex of X to a vertex of Y. No edge stays inside a side. The sides are independent sets, and the graph is a relation between two populations.

@list heading="Bipartite or not?" items="C₄, C₆, every tree: bipartite@The four cycle|C₃, C₅: not@the triangle|Kₙ for n ≥ 3: not@complete graph|Kₘ,ₙ: bipartite, mn edges@by construction"
The four cycle, the six cycle and every tree are bipartite. The triangle and the five cycle aren't, and neither is a complete graph on three or more vertices. The complete bipartite graph K m n is bipartite by construction, with m times n edges.

@chapter The theorem
@words text="Bipartite ⟺ no odd cycle"
Here's the whole story in one line. A graph is bipartite if and only if it has no cycle of odd length. Odd cycles are the only obstruction. Nothing else can prevent it.

@art even-cycle-colours
One direction is quick. In a bipartite graph, every step crosses to the other side. After an odd number of steps, you're on the opposite side from where you began. A cycle has to come home, so its length must be even.

@art bfs-layers
The other direction is the real content. Suppose there's no odd cycle. Pick a vertex r, and put each vertex in X or Y by whether its distance from r is even or odd. If an edge ever joined two vertices on the same side, it would close an odd cycle. So none does, and the split works.

@words text="The proof is the algorithm" sub="colour by parity of distance"
And notice what that proof did. It coloured by the parity of the distance from a root. That's exactly the test you run, so the proof and the algorithm are the same thing.

@chapter Two cycles
@math heading="C₆: 1–2–3–4–5–6–1" items="distance from 1:  0 1 2 3 2 1@distances from one;;colours:  X Y X Y X Y@colour them;;X = {1,3,5}   Y = {2,4,6}  ✓@one, three and five"
Take the six cycle. The distances from one are zero, one, two, three, two, one. Colour them X, Y, X, Y, X, Y. Every edge crosses, so it's bipartite, with X being one, three and five, and Y being two, four and six.

@math heading="C₅: 1–2–3–4–5–1" items="distance from 1:  0 1 2 2 1@distances are;;colours:  X Y X X Y@colours are;;edge 3–4 joins X to X  ✗@three four"
Now the five cycle. The distances are zero, one, two, two, one. So the colours are X, Y, X, X, Y. And the edge three four joins two X vertices. It's not bipartite.

@art odd-cycle-clash
That clashing edge closes the odd cycle, one two three four five and back, of length five. It isn't bad luck in the order you coloured. Wherever you start, the odd cycle is there, and you'll hit a conflict somewhere.

@chapter Fast, and why it matters
@words text="One search: Θ(n + |E|)" sub="3 colours: NP-complete"
The test is one breadth first search, so it's linear in the size of the graph. Compare that with three colours, which is NP complete. Two colours is easy, three is hard, and the boundary is right here.

@chapter Matching
@art matching-pairs
Bipartite graphs model assignments: workers and jobs, students and projects, rooms and time slots. A matching is a set of edges where no two share a vertex. Here, it pairs members of X with members of Y.

@art hall-bottleneck
When can every member of X be matched? Hall's marriage theorem says exactly when every set S of vertices in X has at least as many neighbours as S has members. If some group has fewer neighbours than members, two must share, like the pigeonhole principle.

@chapter Where people slip
@list heading="Common slips" items="Triangle-free means bipartite@The first|Testing only one component@The second|Saying not bipartite without the cycle@And the third"
The first slip is assuming triangle free means bipartite. The five cycle has no triangle, and it isn't. The second is testing only one component, when each needs its own colouring. And the third is reporting failure without naming the odd cycle that proves it.

@chapter Try it
@words text="C₆ plus a chord" sub="1–3 or 1–4?"
Your turn. Take the six cycle and add one chord. Does adding one three keep it bipartite? What about one four? Find the cycle each chord closes, and check its length.

@end text="Two-colour it yourself"
You can two colour the six cycle and the five cycle yourself, and add chords, on Learn. That's learn dot get er done dot I O.

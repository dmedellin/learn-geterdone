---
format: long
lesson: graphs-and-trees/euler-and-hamilton
title: Euler vs Hamilton: two puzzles that look alike and aren't
thumb: Every edge, or every vertex?
---

@chapter The question
@title text="Euler and Hamilton Paths" sub="Graphs and Trees" art=thumb
Here are two puzzles. Can you trace a graph using every edge exactly once? And can you tour a graph visiting every vertex exactly once? They sound almost the same. One is easy, and the other is one of the hardest problems we know.

@chapter Königsberg
@art konigsberg-abstract
In 1736, the city of Konigsberg had four land masses joined by seven bridges. Could you take a walk crossing every bridge exactly once? Euler threw away the map entirely. He kept only which land masses were joined, and that turned the question into a graph.

@math heading="Königsberg" items="A: 5 · B: 3 · C: 3 · D: 3@five, three, three and three;;four odd-degree vertices@four vertices;;a path allows at most 2  ✗@at most two"
The four vertices have degrees five, three, three and three. That's four vertices of odd degree. And a walk like this allows at most two. So no such walk exists. The geometry and the distances never mattered, only the degrees.

@chapter Euler's theorem
@list heading="Euler's theorem (connected graph)" items="0 odd degrees: an Euler circuit@zero odd|exactly 2 odd: an Euler path, odd to odd@exactly two|otherwise: neither@anything else"
An Euler path uses every edge exactly once, and an Euler circuit is one that ends where it started. For a connected graph, if there are zero odd degree vertices, there's a circuit. If there are exactly two, there's a path, starting at one odd vertex and ending at the other. Anything else, neither.

@art enter-and-leave
Why even degrees? Every time the circuit enters a vertex, it leaves again, using two edge ends there. The start and finish are the same vertex, so even its first and last edges pair up. Every edge is used once, so every degree is even.

@art splice-circuits
And it's sufficient too. Start anywhere and walk without repeating an edge. With even degrees you can only get stuck back at the start, so you've made a circuit. If it missed some edges, find a vertex on it with unused ones, build a second circuit there, and splice it in. That's Hierholzer's algorithm, and it's linear time.

@chapter Fixing Königsberg
@math heading="Add bridges to fix the parity" items="+ B–C:  A 5 · B 4 · C 4 · D 3@between B and C;;two odd (A, D)  ⟹  Euler path, A to D@exactly two odd;;+ A–D:  A 6 · B 4 · C 4 · D 4@between A and D;;all even  ⟹  Euler circuit@all even"
Now fix it. Add one bridge between B and C. The degrees become five, four, four and three. Now there are exactly two odd vertices, A and D, so an Euler path exists, from A to D. Add a second bridge, between A and D, and the degrees are six, four, four, four. All even, so there's an Euler circuit, starting anywhere.

@words text="The obstruction is parity" sub="so parity is what you repair"
Any bridge joining two odd vertices would have done. That's the practical form of the theorem.

@chapter Hamilton
@art hamilton-tour
A Hamilton path visits every vertex exactly once. A Hamilton circuit returns to its start. And here the story changes completely. There's no known criterion. There are only sufficient conditions.

@list heading="Sufficient conditions (n ≥ 3)" items="Dirac: every degree ≥ n/2@Dirac's|Ore: deg u + deg v ≥ n for non-adjacent u, v@Ore's"
Dirac's theorem says that if every vertex has degree at least n over two, there's a Hamilton circuit. Ore's theorem says the same if, for every pair of non adjacent vertices, their degrees add to at least n. Both are sufficient. Neither is necessary. The cycle C n has a Hamilton circuit with every degree just two.

@words text="Hamilton circuit: NP-complete"
Deciding whether a Hamilton circuit exists is NP complete. No polynomial time algorithm is known, and finding one would prove P equals NP.

@chapter Side by side
@art euler-vs-hamilton
So put them side by side. Euler covers every edge once, Hamilton every vertex once. Euler has a criterion: all degrees even. Hamilton has none known. Euler is decided and built in linear time, while Hamilton, in general, takes exponential search. Nothing in the wording tells you which is which.

@chapter Where people slip
@list heading="Common slips" items="Confusing the two problems@The first|Using Dirac's condition in reverse@The second|Forgetting connectivity@not necessary"
The first slip is confusing the two problems: edges, or vertices. The second is using Dirac's condition in reverse. It's sufficient, not necessary.

@art two-disjoint-cycles
And the third is forgetting connectivity. Two separate cycles have every degree even, and still no Euler circuit, because the edges have to lie in one component.

@chapter Try it
@words text="C₆, minus the edge 1–2" sub="Euler circuit? Euler path? Hamilton?"
Your turn. Take the six cycle and remove the edge one two. Which vertices are odd now? Is there an Euler path, and where must it start and end? And is there still a Hamilton circuit, or only a path?

@end text="Ask both questions of your graph"
You can build a graph and ask both questions of it, on Learn. That's learn dot get er done dot I O.

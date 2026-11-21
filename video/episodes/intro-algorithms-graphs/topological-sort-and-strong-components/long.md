---
format: long
lesson: intro-algorithms-graphs/topological-sort-and-strong-components
title: Topological sort and strong components from finish times
thumb: Finish last, list first
---

@chapter One observation
@title text="Topological Sort and Strongly Connected Components" sub="Introduction to Algorithms, Sections 22.4–22.5" art=thumb
Two classic algorithms rest on one fact about depth first search. Along any arc that isn't a back arc, the tail finishes after the head.

@chapter Sorting a dag
@art dag-in-a-line
A dag is a directed graph with no cycle. A topological sort lists its vertices so that every arc points forward. Think of tasks, each listed before the tasks that need it.

@words text="Sort by decreasing finish time" sub="Θ(V + E)"
The algorithm is almost nothing. Run depth first search, and as each vertex finishes, put it at the front of a list. The list ends in decreasing finish time. That's theta of V plus E.

@art finish-stack
Each insertion at the front costs constant time, so the list costs nothing extra. The vertex that finishes last sits on top, and the one that finished first sits at the bottom.

@math heading="Why it works" items="no cycle ⇔ no back edge@no back edge;;arc u → v in a dag ⇒ v.f < u.f@for every arc"
Lemma twenty two point eleven says a digraph has no cycle exactly when a depth first search finds no back edge. So in a dag, for every arc from u to v, v finishes before u. Listing by decreasing finish time puts u first.

@chapter The lesson's dag
@math heading="1>3, 2>3, 3>4, 2>5, 5>4, 4>6" items="finish: 2 (12), 5 (11), 1 (8), 3 (7), 4 (6), 6 (5)@two at twelve;;sort: 2, 5, 1, 3, 4, 6@the order;;✗ by discovery: 1, 3, 4, 6, 2, 5@by discovery time"
On the lesson's dag of six tasks, the first pass finishes two at twelve, five at eleven, one at eight, three at seven, four at six, and six at five. So the order is two, five, one, three, four, six, and every arc points forward. Sort by discovery time instead, and the arc from two to three points backward.

@chapter Strong components
@art components
Now drop the requirement that the graph be acyclic. A strongly connected component is a largest set of vertices where every one can reach every other. Shrink each component to a single vertex, and the component graph is always a dag.

@list heading="Two searches" items="DFS on G: record finish times@The first|Transpose: reverse every arc@reverse every arc|DFS on the transpose, latest finish first@The second"
Here's the procedure. The first search runs on the graph and records finish times. Then reverse every arc to get the transpose, which has exactly the same components. The second search runs on the transpose, taking vertices in decreasing finish time. Each tree it grows is one component.

@art reversed-arcs
Why the transpose? Mutual reachability survives reversing every arc. If u reaches v and v reaches u, both paths still exist, just flipped. So the components don't change, but the arcs between them all turn round.

@chapter Why the order matters
@quote text="We now consider a classic application of depth-first search: decomposing a directed graph into its strongly connected components." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 22.5"
Section twenty two point five calls it a classic application of depth first search: decomposing a directed graph into its strongly connected components.

@art source-component
Lemma twenty two point fourteen says that if an arc runs from component C to C prime, C's latest finish is later. So the vertex that finishes last is in a source component, with no arcs coming in. In the transpose, every arc out of it points in instead, so a search started there can't leave.

@math heading="1>2, 2>3, 3>1, 3>4, 4>5, 5>4, 2>6, 6>4, 7>6" items="first pass: 7 finishes last, at 14@finishes last;;second pass: {7}, {1, 2, 3}, {6}, {4, 5}@peels"
On the lesson's graph of seven vertices and nine arcs, seven finishes last, at fourteen. The second pass, on the reversed arcs, peels seven alone, then one two three, then six, then four and five. Four components.

@art wrong-order
Search the original arcs from seven, and you'd follow seven to six, six to four, four to five, and wrongly report all four as one piece. Seven reaches six, but six never reaches seven. On the reversed arcs, the search from seven stops at seven.

@chapter Where people slip
@list heading="Common slips" items="Second pass on G, or in any order@The first|Sorting a dag by discovery time@The second|Expecting one topological sort@the third"
The first slip is running the second pass on the original graph, or in any old order. The second is sorting a dag by discovery time. And the third is expecting one topological sort. The lesson's dag also has one, two, three, five, four, six, and others.

@chapter Try it
@words text="1>2, 2>1, 2>3, 3>4, 4>5, 5>3, 5>6, 6>7, 7>6" sub="two passes · name the components"
Your turn. Run the first search by hand from one, list the vertices by decreasing finish time, then run the second search on the reversed arcs in that order. Name the components, and draw the condensation.

@end text="Peel a graph into components"
You can run both passes and check them against reachability, on Learn. That's learn dot get er done dot I O.

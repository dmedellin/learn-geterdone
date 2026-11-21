---
format: long
lesson: graph-algorithms/strongly-connected-components
title: Strongly connected components in two depth-first walks
thumb: Reverse, then walk again
---

@chapter The question
@title text="Strongly Connected Components" sub="Graph Algorithms" art=thumb
In a directed graph, which vertices can all reach each other? Those groups are the strongly connected components. You can find every one of them with two depth first walks, and the trick is in the second.

@chapter The relation
@art mutual-reach
Write u related to v when there's a path from u to v, and a path back from v to u. That's reflexive, by the empty path. Symmetric, by its own statement. And transitive, by joining paths. So it's an equivalence relation, and its classes partition the vertices.

@words text="maximal set where everyone reaches everyone"
A strongly connected component is a maximal set where every vertex reaches every other. Maximal matters. Without it, every vertex alone would count, and the definition would say nothing.

@chapter The condensation
@art condensation
Collapse each component to one point, and keep an arc between two points when some arc ran between their components. The result is always acyclic. A cycle among components would make them all mutually reachable, so they'd have been one component.

@chapter Two passes
@list heading="The algorithm" items="Walk G, record finish times@Walk the graph|Reverse every arc@Reverse|Walk again, largest finish first@largest finish time|Each tree is one component@Each tree"
Walk the graph depth first, and record every finish time. Reverse every arc. Walk the reversed graph, starting each new tree at the undiscovered vertex with the largest finish time. Each tree of that second walk is one component.

@art last-finisher
Why does that work? The vertex that finishes last lies in a source component, one that nothing points into. Say an arc came in from another component B. Whichever the walk entered first, something in B would finish later. So no such arc exists.

@art reversed-walk
Now stand in that source component and follow the reversed arcs. The arcs that would lead out are the reversed versions of arcs that came in, and there are none. So the first tree is exactly one component. Remove it, and the argument repeats.

@chapter Seven vertices
@math heading="1>2 2>3 3>1 3>4 4>5 5>6 6>4 5>7" items="decreasing finish:  1 2 3 4 5 7 6@decreasing finish list;;components:  {1, 2, 3}  {4, 5, 6}  {7}@three components;;condensation:  3 points in a line@three points"
Here's the lab's graph. The first walk gives the decreasing finish list one, two, three, four, five, seven, six. The second pass, on reversed arcs, gives three components: one, two, three. Four, five, six. And seven alone. The condensation is three points in a line, acyclic.

@art one-way
Two things to notice. Seven is its own component, not because it's isolated. Five points at it. It's alone because nothing comes back from it. And seven comes before six in the list because the walk reached six first from five, and closed it before opening seven.

@chapter The two extremes
@math heading="Two ends" items="cycle 1>2>3>4>1:  one component@a single cycle;;1>2 2>3 1>3 3>4:  four components@acyclic"
A single cycle through all four vertices is one component, and its condensation is one point. An acyclic graph is the other extreme. Every vertex is its own component, and the condensation is the graph itself. Run those two first, to convince yourself.

@words text="7 visits · 8 arc reads" sub="Θ(V + E): two walks and a reversal"
On the opening graph, the second pass counts seven vertex visits and eight arc reads. The whole thing is Theta of V plus E, two walks plus one pass to reverse the arcs.

@chapter Where people slip
@art wrong-start
The first slip is starting the second pass at the lowest numbered vertex, as every other traversal does. It terminates, and it partitions the vertices into neat disjoint sets. And it's wrong. Nothing about the output looks broken, which is why the lab recomputes the partition straight from the definition and compares.

@list heading="Common slips" items="Starting pass two at the lowest number@The first|Reading a one-way arc as membership@The second|Trusting the condensation without checking@And the third"
So the first slip is that starting point. The second is reading a one way arc as membership. Five points at seven, and seven is still alone. And the third is assuming the condensation is acyclic without checking. A cycle there is the signature of wrong components.

@chapter Try it
@words text="Add 7>5 to the graph" sub="find the components again"
Your turn. Add an arc from seven back to five. Run both passes by hand, find the new components, and draw the new condensation. Then check your answer from the definition, testing reachability both ways for every pair.

@end text="Compare both partitions"
You can type a digraph and compare the two pass algorithm with the definition, on Learn. That's learn dot get er done dot I O.

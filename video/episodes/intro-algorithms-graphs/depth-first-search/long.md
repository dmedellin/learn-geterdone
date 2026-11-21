---
format: long
lesson: intro-algorithms-graphs/depth-first-search
title: Depth-first search: two timestamps and four kinds of edge
thumb: Go deep, stamp twice
---

@chapter Deeper whenever possible
@title text="Depth-First Search" sub="Introduction to Algorithms, Section 22.3" art=thumb
Breadth first search spreads out one layer at a time. Depth first search does the opposite.

@quote text="The strategy followed by depth-first search is, as its name implies, to search ‘deeper’ in the graph whenever possible." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 22.3"
Section twenty two point three opens: the strategy followed by depth first search is, as its name implies, to search deeper in the graph whenever possible.

@art deep-walk
It follows one edge after another from the vertex it reached last. Only when that vertex has nothing new to offer does it back up. And when everything reachable is done, it starts again from any vertex still white, so the result is a forest, not one tree.

@chapter A clock
@art two-stamps
The search keeps the same three colours, white, grey and black, and adds a clock. When a vertex turns grey, the clock ticks and the vertex records d, its discovery time. When it turns black, the clock ticks again and it records f, its finish time. So the times run from one to two V.

@words text="Θ(V + E)" sub="one call per vertex · one look per adjacency entry"
The running time is exact. The visit procedure is called once per vertex, and its loop looks once at each adjacency entry. So it's theta of V plus E.

@chapter Nesting intervals
@art nested-brackets
The parenthesis theorem says two intervals either don't meet, or one lies entirely inside the other. And containment means descent. Write each discovery as an opening bracket and each finish as a closing one, and the brackets balance.

@words text="White-path theorem" sub="descendants of u: reachable along an all-white path when u is discovered"
The white path theorem says which vertices end up below u. Exactly those reachable from u along a path of vertices that are all still white, at the moment u is discovered. Reachability alone isn't enough.

@chapter Four kinds of edge
@list heading="The head's colour decides" items="White head: tree edge@white head|Grey head: back edge@grey head|Black head, tail first: forward edge@tail was discovered first|Black head, otherwise: cross edge@otherwise"
The search classifies each edge as it first explores it. A white head makes it a tree edge. A grey head, a back edge, since the grey vertices are the chain of open calls. A black head makes it a forward edge if the tail was discovered first, and a cross edge otherwise.

@art edge-kinds
So a back edge points up to an ancestor. A forward edge skips down to a descendant that isn't its child. And a cross edge goes to a vertex that's neither.

@chapter The lesson's graph
@math heading="Six vertices, eight arcs, from 1" items="1>2, 1>4, 1>3, 2>4, 4>1, 3>4, 5>3, 5>6@the lesson's graph;;1 [1,8] · 2 [2,5] · 4 [3,4] · 3 [6,7]@The intervals are;;5 [9,12] · 6 [10,11]@five, nine to twelve"
Here's the lesson's graph, starting at one. The intervals are: one, one to eight. Two, two to five. Four, three to four. Three, six to seven. Then five, nine to twelve, and six, ten to eleven. Two trees, rooted at one and five.

@math heading="Read the classes" items="4 → 1: back@four to one;;1 → 4: forward@one to four;;3 → 4, 5 → 3: cross@three to four"
Four to one is back: one was still grey. One to four is forward: four is a finished descendant, reached first through two. Three to four is cross, since their intervals are disjoint, and so is five to three.

@art white-path-trap
Now look at two and three. Three is reachable from two, and discovered later. Yet six to seven isn't inside two to five. Three isn't a descendant of two, because when two was discovered, the path to three ran through one, which was grey.

@chapter Graph or walk?
@art restart-forest
Start the same graph at five, and you get five tree arcs, three back arcs, and nothing else. The classes describe one walk. Read it as undirected from one, and there are no forward or cross edges at all, just as theorem twenty two point ten says.

@words text="A back arc exists, or it doesn't" sub="that fact belongs to the graph"
What doesn't change is whether there's a back arc at all. The next lesson proves that this one fact belongs to the graph.

@chapter Where people slip
@list heading="Common slips" items="Reachable and later means descendant@The first|Edge classes belong to the graph@The second|Expecting one tree@the third"
The first slip is thinking that reachable and discovered later means descendant. The path must be white. The second is treating the edge classes as properties of the graph. And the third is expecting one tree. Depth first search restarts, so it builds a forest.

@chapter Try it
@words text="1>2, 2>3, 3>1, 3>4, 4>2, 1>5" sub="from 1: intervals, classes"
Your turn. Run depth first search by hand from one on this digraph. Write every interval, classify all six arcs, and look for a vertex reachable from another and discovered after it, that still isn't its descendant.

@end text="Stamp a graph of your own"
You can classify every arc and check the parenthesis theorem, on Learn. That's learn dot get er done dot I O.

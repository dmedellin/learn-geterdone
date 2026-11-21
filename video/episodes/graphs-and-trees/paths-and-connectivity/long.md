---
format: long
lesson: graphs-and-trees/paths-and-connectivity
title: Paths, components and bridges: what holds a graph together
thumb: One edge holds it together
---

@chapter The question
@title text="Paths and Connectivity" sub="Graphs and Trees" art=thumb
Can you get from any vertex of a graph to any other? And if one road closed, or one junction, would the network fall apart? Those are connectivity questions, and they start with three words.

@chapter Walks, paths and cycles
@art walk-path-cycle
A walk is any sequence of vertices where each one is adjacent to the next. It can repeat anything. A path is a walk that repeats no vertex. And a cycle is a walk of length at least three that comes back to its start, repeating nothing else.

@words text="A path repeats no vertex"
On this course, path always means no repeated vertex. It isn't just any route, and several theorems, including one about bridges later, depend on that.

@art shortcut-walk
Here's a small theorem you'll use constantly. If there's a walk from u to v, there's a path. Take the shortest walk. If it visited some vertex twice, you could cut out the loop between the two visits and get a shorter walk. So the shortest walk repeats nothing. It's a path.

@chapter Components
@words text="Connected: every pair joined by a path"
A graph is connected if every pair of vertices is joined by a path. A component is a maximal connected piece, one you can't grow without losing connectivity.

@list heading="Joined by a path is an equivalence" items="Reflexive@Reflexive|Symmetric@Symmetric|Transitive@Transitive"
Being joined by a path is an equivalence relation. Reflexive: the walk of length zero joins v to itself. Symmetric: reverse the path. Transitive: join two walks end to end, then pull out a path. So its classes split the vertices, and those classes are the components.

@chapter How many edges it takes
@art merging-components
How many edges does it take to connect n vertices? Start with no edges, and n separate components. Each new edge can merge at most two components, so it lowers the count by at most one. To get from n components down to one, you need at least n minus one edges.

@words text="n − 1 edges: necessary, not sufficient"
But that's a floor, not a guarantee. Fewer than n minus one edges means the graph is certainly disconnected. More than that doesn't promise anything, because the edges could all be crowded into one corner while another vertex sits alone.

@chapter Weak points
@art bridge-edge
Now the weak points. A bridge is an edge whose removal increases the number of components. And here's the key fact: an edge is a bridge exactly when it lies on no cycle. On a cycle, the rest of the cycle is a detour. Off every cycle, there's no detour at all.

@art cut-vertex
A cut vertex is a vertex whose removal increases the number of components. Don't confuse the two. Here, two triangles share one vertex. Remove it, and they separate, yet every edge is on a triangle, so there's no bridge.

@chapter A worked example
@math heading="7 vertices · edges 1–2, 2–3, 3–1, 3–4, 5–6" items="from 1: {1, 2, 3, 4}@From one;;from 5: {5, 6}@from five;;7 alone: {7}@seven;;n − 1 = 6 > 5 edges@six"
Seven vertices, with edges one two, two three, three one, three four, and five six. Search from one, and you reach one, two, three and four. From five, you reach six. And seven is alone. Three components. You could have known it was disconnected in advance: it needs at least six edges, and it has five.

@art three-components
And its weak points? Vertex three is a cut vertex, because removing it cuts four off from one and two. The edges three four and five six are bridges, since neither lies on a cycle. But one two, two three and three one sit on the triangle, so none of them is a bridge.

@chapter Where people slip
@list heading="Common slips" items="Calling any route a path@The first|Thinking enough edges means connected@The second|Mixing up cut vertices and bridges@And the third"
The first slip is calling any route a path. The second is thinking enough edges means connected: n minus one is necessary, not sufficient. And the third is mixing up cut vertices and bridges. One is a vertex, one is an edge, and neither implies the other.

@chapter Try it
@words text="A connected graph on 10 vertices" sub="at least how many edges?"
Your turn. What's the smallest number of edges a connected graph on ten vertices can have? Then load a tree and check: is every one of its edges a bridge?

@end text="Find the bridges yourself"
You can load this graph and find its components, bridges and cut vertices, on Learn. That's learn dot get er done dot I O.

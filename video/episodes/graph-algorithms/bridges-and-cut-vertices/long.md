---
format: long
lesson: graph-algorithms/bridges-and-cut-vertices
title: Bridges and cut vertices in one depth-first walk
thumb: How high can it climb?
---

@chapter The question
@title text="Bridges and Cut Vertices" sub="Graph Algorithms" art=thumb
Which single link, if it failed, would split your network in two? Which single machine? You could delete each one and recount. Or you could find them all in one walk, with one extra number per vertex.

@chapter The definitions
@art bridge
A bridge is an edge whose removal leaves more components. A cut vertex is a vertex whose removal, with its edges, does the same. Neither definition mentions an algorithm.

@words text="delete, recount, restore" sub="one walk per candidate: Θ(E(V + E))"
The slow method transcribes the definitions. Delete a candidate, recount the components, restore it. That's a whole walk per candidate. But it's completely reliable, so the lab runs it beside the fast method as an independent check.

@chapter The low-link value
@art low-climb
Here's the extra number. Low of v is the smallest discovery time you can reach from v, by going down tree edges, then along at most one non tree edge. Think of it as how high the subtree at v can climb.

@math heading="low[v] = min of" items="d[v]@d of v;;low[c] for each child c@each child;;d[w] for each non-tree edge v–w@joined to v"
It's the minimum of d of v, of low of each child, and of d of every vertex joined to v by a non tree edge. It's finished exactly when v closes, because by then every child has closed. So the cost is just the walk's cost.

@chapter The bridge test
@words text="tree edge (u, v) is a bridge ⟺ low[v] > d[u]"
Take a tree edge from u down to its child v. It's a bridge exactly when low of v is greater than d of u. If the subtree at v can't reach u or anything above, then this edge is its only way out, so deleting it cuts the subtree off.

@art cycle-not-bridge
And the other way: if low of v is at most d of u, something in the subtree has an edge back up to u or higher. That edge, with the tree paths, makes a cycle through u and v. No edge on a cycle is a bridge.

@chapter Two triangles
@math heading="1-2 2-3 3-1 3-4 4-5 5-6 6-4" items="d:  1, 2, 3, 4, 5, 6@discovery times;;low:  1, 1, 1, 4, 4, 4@the low values;;edge 3–4:  low[4] = 4 > d[3] = 3  ⟹  bridge@three and four"
Two triangles joined by one edge. The discovery times are one to six in order. The low values are one, one, one, four, four, four. For the edge between three and four, low of four is four, more than d of three, which is three. So it's a bridge. Every other child sits on a triangle and can climb back.

@words text="cut vertices: low[v] ≥ d[u]" sub="3: low[4] ≥ d[3] · 4: low[5] = 4 ≥ d[4] = 4"
The cut vertex test is almost the same, with greater than or equal. Three is a cut vertex, because its child four has low at least d of three. And four is one too, because low of five is four, equal to d of four. Delete and recount gives the same three answers.

@chapter One comparison apart
@art shared-vertex
Equality is the case where the subtree climbs back to u, but no higher. The edge is on a cycle, so not a bridge, but u is still the only way in, so it's a cut vertex. And they don't come in pairs. Two triangles sharing one vertex have a cut vertex and no bridge at all.

@art root-rule
The root needs its own rule. It has no parent to be cut off from, so the test is vacuous. Instead, the root is a cut vertex exactly when the walk gave it two or more children.

@chapter Excluding by edge
@art parallel-edges
The walk mustn't follow back the edge it arrived on. Remember the edge, not the parent vertex. With two edges between one and two, skipping the parent would skip both, and report a bridge that isn't there. The lab's matrix check can't even represent two edges, so it says so instead of answering.

@chapter Where people slip
@list heading="Common slips" items="Excluding the parent by vertex, not edge@The first|Finalising low on the way down@The second|Assuming bridges and cut vertices pair up@And the third"
The first slip is excluding the parent by vertex instead of by edge. The second is finalising low on the way down, before the children have closed, which gives values too large and invents bridges. And the third is assuming bridges and cut vertices come in pairs.

@chapter Try it
@words text="A path of five vertices" sub="find every bridge and cut vertex"
Your turn. On a path of five vertices, compute d and low, and find every bridge and cut vertex. You should find four bridges, and three cut vertices.

@end text="Find the weak links"
You can type a graph and compare the one pass method with delete and recount, on Learn. That's learn dot get er done dot I O.

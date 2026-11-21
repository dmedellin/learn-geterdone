---
format: long
lesson: graphs-and-trees/planar-graphs
title: Planar graphs and Euler's formula: why K5 can't be drawn flat
thumb: V − E + F = 2
---

@chapter The question
@title text="Planar Graphs and Euler's Formula" sub="Graphs and Trees" art=thumb
Three houses, three utilities, and every house needs a line to every utility. Can you draw it without any lines crossing? The answer is no, and by the end you'll be able to prove it in two lines.

@chapter Planar graphs
@art k4-crossing-uncrossed
A graph is planar if it can be drawn in the plane with no two edges crossing. Notice the word can. K four drawn as a square with both diagonals has a crossing. But move one diagonal outside, and the crossing disappears. So K four is planar.

@art faces-drawing
A crossing free drawing cuts the plane into regions called faces. And one of them is easy to forget: the unbounded outer face, all the space around the outside of the drawing.

@chapter Euler's formula
@words text="V − E + F = 2" sub="connected, planar, outer face counted"
For any connected planar graph drawn without crossings, the vertices minus the edges plus the faces equals two. That's Euler's formula, and the faces include the outer one.

@art remove-edge-merge-faces
Why? Induct on the edges. If the graph is a tree, it has V minus one edges and just one face, so V, minus the quantity V minus one, plus one, is two. If there's a cycle, remove one of its edges. The graph stays connected, and the two faces on either side merge into one. So edges and faces each drop by one, and the total doesn't change.

@art cube-flat
Here's a cube, drawn flat. Eight vertices, twelve edges and six faces. Eight minus twelve plus six is two. It works for every convex polyhedron, which is where Euler first stated it, in 1758.

@chapter The edge bound
@math heading="Counting edge–face incidences" items="every face has ≥ 3 edges, every edge borders ≤ 2 faces@at least three;;3F ≤ 2E@three F;;3(2 − V + E) ≤ 2E@substitute;;E ≤ 3V − 6@E is at most"
Now count. Every face is bounded by at least three edges, and every edge borders at most two faces. So three F is at most two E. Substitute F equals two minus V plus E, and simplify. E is at most three V minus six, for a simple connected planar graph with at least three vertices.

@words text="No triangles: E ≤ 2V − 4" sub="every face has ≥ 4 edges"
If there are no triangles, every face needs at least four edges, so four F is at most two E, and the same steps give E at most two V minus four. It's the handshake theorem's double count again, applied to faces.

@chapter Two graphs that fail
@math heading="K₅ and K₃,₃" items="K₅:  V = 5, E = 10, 3V − 6 = 9 < 10  ✗@K five;;K₃,₃:  V = 6, E = 9, 3V − 6 = 12  inconclusive@K three three;;bipartite → no triangles: 2V − 4 = 8 < 9  ✗@bipartite"
K five has five vertices and ten edges. The bound allows at most nine. So it's not planar. K three three has six vertices and nine edges, and the first bound allows twelve, so it passes. But it's bipartite, so it has no triangles, and the sharper bound allows only eight. Nine is too many. Not planar.

@art k5-and-k33
And K three three is exactly the three houses and three utilities. It has no solution. That's why we needed both bounds.

@chapter Kuratowski
@art subdivision
Here's the remarkable part. A subdivision replaces edges with paths through new vertices of degree two. Kuratowski's theorem says a graph is planar exactly when it contains no subdivision of K five or K three three. Infinitely many graphs are non planar, and every one of them fails for one of those two reasons.

@words text="Petersen: passes both bounds, not planar" sub="V = 10, E = 15 · contains a K₃,₃ subdivision"
The bounds alone don't settle it. The Petersen graph has ten vertices and fifteen edges, and passes both bounds. But it contains a subdivision of K three three, so it isn't planar.

@chapter Where people slip
@list heading="Common slips" items="Concluding planar from the edge bound@The first|Forgetting the outer face@The second|Triangle-free bound on a graph with triangles@And the third"
The first slip is concluding a graph is planar because it passes the bound. The second is forgetting the outer face, which turns the two into a one and breaks every bound after it. And the third is using the triangle free bound on a graph that has triangles.

@chapter Try it
@words text="V = 10, E = 15, connected and planar" sub="How many faces?"
Your turn. A connected planar graph has ten vertices and fifteen edges. How many faces does it have? Use Euler's formula, and don't forget the outer face.

@end text="Check the bound yourself"
You can load K five and K three three and check both bounds yourself, on Learn. That's learn dot get er done dot I O.

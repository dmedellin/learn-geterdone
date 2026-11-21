---
format: long
lesson: graphs-and-trees/degree-and-the-handshake-theorem
title: The handshake theorem: why degrees always add to an even number
thumb: Every edge has two ends
---

@chapter The question
@title text="Degree and the Handshake Theorem" sub="Graphs and Trees" art=thumb
Can five people at a party each shake exactly three hands? You could try drawing it. Or you could settle it in one line, without drawing anything at all.

@words text="deg(v) = edges at v"
Start with one word. The degree of a vertex is the number of edges that meet it. A vertex of degree zero is isolated. A vertex of degree one is a leaf, or a pendant vertex.

@art isolated-and-leaf
Here's a small graph. The lone dot off to the side touches no edges, so it's isolated. The dot hanging off the end by a single edge is a leaf.

@chapter The theorem
@math heading="The handshake theorem" items="Σ deg(v) = 2|E|@add up the degrees"
Now add up the degrees of every vertex in any graph. You always get twice the number of edges. That's the handshake theorem, and it holds for every graph there is.

@art edge-two-ends
Why? Count the places where a vertex meets an edge. Count them vertex by vertex, and each vertex gives its degree, so you get the degree sum. Count them edge by edge, and every edge has exactly two ends, so you get twice the number of edges. One set, counted two ways.

@words text="Count one thing two ways"
That's a combinatorial proof, and it's the cleanest one you'll see. Name the objects, count them two ways, and conclude that the counts are equal.

@chapter Odd degrees come in pairs
@art odd-pairs
Here's the corollary you'll use all through the course. In any graph, the number of vertices with odd degree is even. The total is twice the edges, which is even. The even degrees add to something even. So the odd degrees must too, and a sum of odd numbers is even only when there's an even number of them.

@words text="5 vertices, all degree 3?" sub="five odd degrees: impossible"
Back to the party. Five people each shaking three hands would mean five vertices of odd degree. Five is odd. So no such party exists, and you never had to draw a thing.

@chapter Three existence questions
@math heading="Settled by counting" items="7 vertices, every degree 3 → 7 odd degrees  ✗@seven vertices;;8 vertices, every degree 3 → Σ = 24, |E| = 12  ✓@eight vertices;;6 vertices, degrees 5,5,5,5,5,5 → Σ = 30, |E| = 15 = C(6,2)  ✓@six vertices"
Seven vertices, every degree three? Seven odd degrees, an odd count, so it's impossible. Eight vertices, every degree three? Eight is even, the sum is twenty four, so there are twelve edges. And six vertices, all of degree five? The sum is thirty, so fifteen edges, which is six choose two. That's K six.

@art cube-graph
For eight vertices of degree three, here's one: the cube graph, Q three. Eight corners, each joined to three others, twelve edges.

@art remove-one-edge
And watch what happens if you remove one edge. Exactly two vertices become odd. Never one, never three. The degree sum and twice the edges both drop by exactly two.

@chapter Even sums aren't enough
@art too-many-neighbours
Now the fourth question. Degrees five, three, three, two, one, on five vertices. The sum is fourteen, which is even. But a vertex of degree five needs five neighbours, and there are only four other vertices. Impossible.

@list heading="Two quick tests" items="The degree sum is even@the degree sum|No degree above n − 1@no degree"
So keep two necessary tests. The degree sum must be even, and no degree can be bigger than n minus one. Together they catch most impossible sequences. The complete criterion, the Erdos Gallai theorem, is beyond this course.

@words text="k-regular on n vertices: nk/2 edges" sub="so nk must be even"
One more consequence. A graph is k regular if every vertex has degree k. Then it has n times k over two edges, so n times k must be even. A three regular graph needs an even number of vertices.

@chapter Where people slip
@list heading="Common slips" items="Writing Σ deg = |E|@The first|Trusting an even sum alone@The second|Equal sequences as proof of isomorphism@And the third"
The first slip is forgetting the doubling: every edge counts at both ends. The second is assuming any even sum works, which five, three, three, two, one disproves. And the third is treating equal degree sequences as proof two graphs are the same. Different sequences prove they're different. Equal ones prove nothing.

@chapter Try it
@words text="A graph has 10 edges." sub="What is the sum of its degrees?"
Your turn. A graph has ten edges. What's the sum of its degrees? You don't need to know how the edges are arranged. Then ask yourself whether any graph could have exactly three vertices of odd degree.

@end text="Remove an edge, watch the parity"
You can load the cube graph, remove edges, and watch the degrees change, on Learn. That's learn dot get er done dot I O.

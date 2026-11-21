---
format: long
lesson: geometric-algorithms/inside-by-parity-and-by-winding
title: Is the point inside? Ray parity, winding numbers, and the vertex rule
thumb: Count the crossings
---

@chapter The question
@title text="Inside, by Parity and by Winding" sub="Geometric Algorithms" art=thumb
Is a point inside a polygon? There are two classic ways to answer. They agree on every simple polygon, and they genuinely disagree on one that crosses itself.

@chapter Count the crossings
@art ray-cast
The first way: cast a horizontal ray from the point, out to the right, and count how many edges it crosses. Odd means inside. Even means outside. Far enough out, you're certainly outside, and every real crossing flips the side.

@art vertex-ray
The delicate case is a ray passing exactly through a vertex. It touches two edges, and counting both, or neither, gives the wrong parity. Nudging the point is tempting, but it changes the question, and on grid data it often lands on another vertex.

@chapter The half-open rule
@words text="count an edge when exactly one endpoint is strictly above the ray"
Instead, use a rule. Count an edge only when exactly one of its endpoints is strictly above the ray's height, and the edge meets the ray at or beyond the point. A vertex at exactly that height counts as below.

@art pass-vs-touch
So when the boundary passes from below to above through a vertex, exactly one of its two edges is counted. And when it touches and turns back, either both are counted or neither. That's the right answer in both cases, with no perturbation and no tolerance.

@words text="pass through: 1 · touch and return: 0 or 2"
A pass through changes the side and contributes one. A touch and return doesn't, and contributes zero or two. So the parity of the count is exactly the number of side changes on the way out to infinity.

@chapter The comb
@art comb
The lab's comb has fourteen vertices and three upward teeth. Its doubled area is ninety six, so the area is forty eight. Now walk a query point along the horizontal line at height four.

@math heading="Along height 4" items="(−1, 4):  6 crossings, outside@six edges;;(3, 4):  5, inside@five crossings;;(5, 4):  4, outside@four, outside;;(7, 4):  3, inside@three, inside;;(9, 4):  2, outside@two, outside;;(11, 4):  1, inside@one, inside"
At minus one, four, the ray crosses six edges, outside. At three, four, five crossings, inside. Then four, outside. Three, inside. Two, outside. One, inside. Each step right passes one edge, so the count falls by one and the parity flips. That's the proof, made visible.

@art ray-cast
Past the last tooth the count reaches zero, and the point is outside again. It's worth typing those query points into the lab in order.

@chapter The winding number
@art winding-loop
The second way counts how many times the boundary goes counter clockwise around the point, minus the clockwise times. Walk the edges, and add one or subtract one each time an edge crosses the horizontal line through the point on its right, depending on direction. On the right is decided by an orientation determinant, the same test as everywhere else on this course.

@list heading="Simple polygon" items="+1 inside, if counter-clockwise@plus one|−1 inside, if clockwise@minus one|0 outside@zero outside"
On a simple polygon, the winding number is plus one inside if the vertices run counter clockwise, minus one if clockwise, and zero outside. So winding not zero and odd parity agree. The clockwise square from last lesson has winding minus one at its centre, and it's inside.

@chapter Where they part
@art double-loop
Now a doubly wound loop. At its centre the winding number is two, and the parity is even. Parity says outside. Winding says inside, twice over. Neither is wrong. Filling a region and integrating round a contour want different answers. So the lab checks the polygon is simple before claiming they must agree, and says so in amber when it isn't.

@words text="on the boundary: a third answer"
A point exactly on an edge is neither inside nor outside. Both routes detect it with an exact on segment test and report it as its own verdict, because where it belongs is a convention, not a fact. The checker also casts the ray upward, so a slip in the half open rule shows up as a disagreement.

@chapter Where people slip
@list heading="Common slips" items="Nudging the point off a vertex@The first|Treating parity and winding as one test@The second|Folding the boundary into inside or outside@And the third"
The first slip is nudging the query point off a vertex. Use the rule instead. The second is assuming parity and winding are the same test. And the third is quietly folding on the boundary into inside or outside. Report it, and let the consumer decide.

@end text="Count the crossings yourself"
Walk a point across the comb and watch the count fall, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: geometric-algorithms/the-vertex-a-rounded-determinant-deletes
title: How one rounded determinant deletes a corner from a convex hull
thumb: Three corners in, two out
---

@chapter One change
@title text="The Vertex a Rounded Determinant Deletes" sub="Geometric Algorithms" art=thumb
Run the same convex hull algorithm twice. Change only the predicate, from exact to double precision. The first run returns three corners. The second returns two. Here's how one rounded number deletes a vertex for good.

@chapter The monotone chain
@art sorted-sweep
Andrew's monotone chain starts by sorting the points by x, then by y. Then it walks them left to right, keeping a stack.

@art stack-pop
Before pushing the next point p, it looks at the top two points on the stack and p. While they fail to turn left, it pops the top. Then it pushes p. That builds the lower chain. Walk back right to left and you get the upper chain. Join them, dropping the shared endpoints, and that's the hull.

@math heading="The pop rule" items="pop while orient(s₂, s₁, p) ≤ 0@pop while;;then push p@then push"
In symbols: pop while the orientation of the second from top, the top, and p is less than or equal to zero, then push p. It's a sort and one comparison. That's what makes swapping the comparison such a clean experiment.

@words text="sort n log n · scan ≤ 4n" sub="2n pushes, at most 2n pops"
The sort costs n log n and dominates. The scan is linear: each chain pushes every point once, so two n pushes, and it can't pop more than it pushed. At most four n stack operations.

@chapter Why a zero pops
@art edge-midpoint
The rule says less than or equal to zero, so a zero pops. With exact arithmetic that's right. It throws away points sitting strictly inside an edge, which aren't corners. But with a rounded determinant, a genuine corner whose determinant rounded to zero is popped too, and never looked at again.

@chapter The needle triple
@math heading="Sorted" items="(0, 0)@zero, zero;;(134217728, 134217727)@then the point;;(134217729, 134217728)@then the one"
Take the needle triple from the last lesson. Sorted, it's zero, zero, then the point one three four two one seven seven two eight, one three four two one seven seven two seven, then the one just above it and to the right.

@math heading="Two predicates" items="exact:  orient = +1, left turn  ⟹  3 vertices@exact determinant;;double:  orient = 0  ⟹  pop  ⟹  2 vertices@double determinant"
The exact determinant of those three, in that order, is plus one, a left turn. So the lower chain keeps all three, and the hull has three vertices. The double determinant is zero, which counts as less than or equal to zero. So the middle point is popped at step three, and the hull comes back with two.

@art two-traces
Read the traces side by side. The exact run pushes all three. The double run pushes two, pops the middle one, and pushes the third. One extra pop, one fewer vertex, and the pop is at exactly the step where the rounded determinant was consulted.

@chapter Nothing downstream can fix it
@art well-formed-wrong
Now feed that hull to a diameter calculation, or a point in polygon test. It gets a convex polygon on two of the three points. Every invariant holds. The consumer has no evidence anything is missing. The diameter it computes is a real distance between real points, just not the right one if the missing corner was an endpoint.

@words text="right discrete answer, or a corrupted structure" sub="no third option"
That's the case for exact predicates. A predicate that returns a discrete answer either returns the right one, or corrupts what's built on it. And by the one sidedness result, a vertex can be lost, but one can't be invented.

@chapter The referee
@art separating-line
So how does the lab know which hull is right? It doesn't trust either chain. It classifies every point from the definition first, by rotating a separating line about it. No sort, no stack. On the needle triple the definition says three vertices, the exact chain agrees, and the double chain is one short.

@chapter Where people slip
@list heading="Common slips" items="Blaming the algorithm, not the predicate@The first|Expecting the drawing to show it@The second|Calling a missing vertex a small error@And the third"
The first slip is blaming the algorithm. Gift wrapping or an incremental method uses the same comparison and fails the same way. The second is expecting the drawing to show it. The three points are collinear to within a pixel. And the third is calling a missing vertex a small error. It's a different answer.

@end text="Two predicates, one difference"
Run both chains on the needle triple yourself, and count the corners, on Learn. That's learn dot get er done dot I O.

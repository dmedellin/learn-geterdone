---
format: long
lesson: geometric-algorithms/three-answers-on-a-square-with-midpoints
title: Four, six or eight: three right answers for one convex hull
thumb: Four, six and eight, all right
---

@chapter Three answers
@title text="Three Right Answers on a Square with Midpoints" sub="Geometric Algorithms" art=thumb
Put a point in the middle of each side of a square. Ask three correct procedures for the hull. You get four, six and eight. None of them is a bug.

@art square-midpoints
Here's the input. The four corners of a square of side four, the midpoint of each side, and the centre. Nine points. The monotone chain returns four. The boundary oracle returns eight. Gift wrapping returns six.

@chapter Two different questions
@art vertex-test
A point is a boundary point when some line through it has every other point on one side. It's a vertex when, on top of that, every point on that line lies strictly beyond it. A midpoint passes the first test and fails the second. The line along its side has everything on one side, but the two corners lie on it in opposite directions.

@list heading="Nine points" items="4 corners: vertices@four corners|4 midpoints: on an edge@four midpoints|1 centre: inside@the centre"
So the four corners are vertices. The four midpoints are on the boundary but aren't corners. And the centre is the only point that's neither.

@chapter Who wants which
@list heading="Different consumers" items="A renderer wants the vertices@A renderer|Point location may want every boundary point@point location|A convex-position test compares both with the input@convex position"
Both questions are legitimate. A renderer wants the vertices, since an extra collinear vertex draws the same shape and costs more. A point location structure may want every boundary point. A convex position test wants to know if both sets equal the whole input. The mistake isn't choosing one. It's not saying which.

@chapter Why six
@art gift-wrap-ties
Gift wrapping walks the boundary. From each point it picks the one making the most clockwise turn. When several points are collinear with the current one, they all give the same determinant, and the tie goes to whichever the scan reaches first, in sorted order.

@math heading="Gift wrapping on the square" items="keeps (2, 0) and (4, 2)@keeps two;;drops (2, 4) and (0, 2)@and drops"
On this square that keeps two, zero and four, two, and drops two, four and zero, two. Nothing geometric separates those pairs. It's a correct boundary walk, returning an arbitrary subset of the collinear points.

@chapter Pinned on purpose
@words text="a boundary walk, not a vertex list"
The lab labels this honestly. It checks gift wrapping against the boundary oracle, not the vertex set, and only asserts that every point it returns is on the boundary. The disagreement with the chain is recorded, not smoothed over, so a change to either one would fail loudly.

@art square-midpoints
Making gift wrapping return all eight, or exactly four, would remove the most instructive input on the page. What matters is that the page never calls its six the vertex count, and never calls the chain's four the boundary.

@chapter When the sets agree
@art interior-triple
When do vertices and boundary points coincide? Exactly when no input point sits strictly between two other points that are both on the boundary. If no three points are collinear, they always agree. But collinear triples inside the hull don't matter, as last lesson's nine points showed.

@chapter More degeneracy
@art segment-hull
Push further. Five collinear points have a hull that's a segment. The chain returns the two ends. The boundary oracle and gift wrapping both return all five. And a single point typed twice has a hull that's that point. The lab removes the duplicate and reports it.

@art duplicate-points
One more wrinkle. The monotone chain in the shared library returns an empty hull for a single point, because both chains are that point and both get sliced away when they're joined. The hull of one point is that point, so that's a defect. The geometry kit works around it, and the checker pins the disagreement so an upstream fix can't land silently.

@words text="Deduplicate first, and count" sub="duplicates change what n means"
A repeated point breaks both algorithms: the chain can return it twice, and gift wrapping does. So the lab deduplicates first and shows the count. It's a real fact about the input, and it changes what n means in every cost below it.

@chapter Where people slip
@list heading="Common slips" items="Calling the disagreement a bug@The first|Perturbing the input away@The second|Treating a repeat as harmless@And the third"
The first slip is calling the disagreement a bug. Ask what each was computing. The second is nudging a midpoint so all three agree. That answers a question about different points, and real inputs, like grids, are full of collinear points. And the third is treating a repeated point as harmless.

@end text="Four, six and eight"
Type the square yourself and read the three columns, on Learn. That's learn dot get er done dot I O.

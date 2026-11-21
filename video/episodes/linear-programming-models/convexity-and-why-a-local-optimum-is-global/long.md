---
format: long
lesson: linear-programming-models/convexity-and-why-a-local-optimum-is-global
title: Why a local optimum is global in a linear programme
thumb: The licence to stop
---

@chapter The question
@title text="Convexity, and Why a Local Optimum Is Global" sub="Linear Programming Models" art=thumb
An algorithm walks from corner to corner, and at some point it has to stop. But it can only see nearby. How can a local check ever prove a point is best everywhere?

@words text="Two facts" sub="convex region · affine objective"
The answer is two facts put together. The feasible region is convex. And a linear objective is affine along any segment.

@chapter Convex sets
@art segment-inside
A set is convex when, for any two points in it, the whole segment between them is in it too. Write the segment as x plus t times y minus x, with t from zero to one. At t equals zero you're at x. At t equals one you're at y.

@math heading="One row at a time" items="a·z = (1 − t)(a·x) + t(a·y)@one minus t;;≤ (1 − t)b + tb = b@at most b"
Here's why a linear programme's region is convex. Take one row, a dot x at most b. At a point z on the segment, a dot z is one minus t times a dot x, plus t times a dot y. That's a weighted average of two numbers, both at most b. So it's at most b.

@words text="Every row survives on its own"
That argument used nothing about the other rows. So each row survives separately, and the whole set does. Sign restrictions are rows too, so they survive the same way.

@chapter Affine along a segment
@math heading="3x + 2y from (1, 1) to (5, 3)" items="5, 7, 9, 11, 13, 15, 17, 19, 21@five, seven, nine;;first difference: 2, every step@exactly two"
Take the region x plus y at most eight, x at most five, y at most six, and the objective three x plus two y. Walk from one, one to five, three in eight equal steps. The objective reads five, seven, nine, and so on up to twenty one. The first difference is exactly two, every step.

@art straight-objective
That constant step is what affine means. Along a segment, the objective is a straight line in t. There's no bump in the middle where a better point could hide.

@chapter The stopping principle
@art no-improving-direction
Now put them together. Suppose you're at a feasible point p, and no direction towards any feasible point improves the objective. Take any other feasible q. The segment from p to q is feasible, and the objective changes along it at a constant rate.

@words text="No improving feasible direction → optimal" sub="globally"
If q were better, that constant rate would be an improvement, starting the moment you leave p. But you assumed no direction improves. So no better q exists. p is optimal, globally.

@words text="Where to look ≠ when to stop"
Compare the corner point theorem. It says an optimum can be found at a corner. That's where to look. It says nothing about the corner you're standing on. Convexity plus a linear objective is what licenses stopping.

@chapter Take convexity away
@art two-blocks
Replace the region with two blocks and a gap. One has x from zero to three, the other x from five to eight, both with y from zero to six. Each block is feasible, but the union isn't convex.

@math heading="From (1, 1) to (5, 3)" items="inside for 0 ≤ t ≤ 1/2@stays inside up to;;3 of 9 samples outside@three of the nine;;best in west: (3, 6), worth 21@twenty one;;east: (8, 6), worth 36@thirty six"
The segment from one, one to five, three stays inside up to t equals one half, then leaves the set. Three of the nine samples are outside. And the best corner of the western block is three, six, worth twenty one, with no improving step inside that block. Meanwhile, eight, six in the east is worth thirty six.

@art local-trap
The objective was still linear, and still affine along every segment. What failed was convexity. Losing it is enough to make a local optimum just local.

@chapter Where people slip
@list heading="Common slips" items="Using the corner theorem as a stopping rule@The first|Reading constant differences as feasibility@The second|Testing convexity by sampling@The third"
The first slip is using the corner point theorem as a stopping rule. The second is reading constant first differences as proof that a segment is feasible. On the two blocks, they're still constant. The third is testing convexity by sampling. For one block the condition collapses to an interval of t, so it can be decided exactly.

@chapter The hand-over
@art corner-walk
So a corner is algebraic, there are finitely many, and a corner with no improving direction is optimal everywhere. An algorithm can walk from corner to adjacent corner, improving each time, and stop when nothing improves. That's the simplex method.

@end text="Walk a segment, watch the differences"
You can pick two points, walk the segment, and see exactly where it leaves a set, on Learn. That's learn dot get er done dot I O.

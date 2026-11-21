---
format: long
lesson: intro-algorithms-strings-geometry-hardness/convex-hull-and-closest-pair
title: Convex hull and the closest pair of points
thumb: Pop unless it turns left
---

@chapter Nails in a board
@title text="Convex Hull and the Closest Pair" sub="Introduction to Algorithms, Sections 33.3–33.4" art=thumb
Two sections of chapter thirty three, and the only geometry they need is the cross product from the last lesson.

@quote text="Intuitively, we can think of each point in Q as being a nail sticking out from a board." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 33.3"
Intuitively, we can think of each point in Q as being a nail sticking out from a board.

@art rubber-band
Stretch a rubber band around the nails and let it snap tight. That's the convex hull: the smallest convex polygon with every point on its boundary or inside. Its corners are points of the set.

@chapter Graham's scan
@art angle-sort
Graham's scan takes the lowest point, the leftmost on a tie, as p zero. It sorts the others by polar angle around it, and pushes p zero and the first two points onto a stack.

@art pop-right-turn
Then, for each remaining point in angle order, it pops the stack while the top two entries and the new point fail to make a left turn, and pushes the new point. When the loop ends, the stack holds the hull's corners, counterclockwise.

@list heading="Why it's right, and fast" items="invariant: stack = hull so far@The invariant|popped point lies in a triangle@A popped point|each point pushed once, popped at most once@pushed once"
The invariant is that the stack always holds the hull of the points processed so far. A popped point lies inside a triangle of other points, so it can't be a corner. And each point is pushed once and popped at most once, so the loop is linear, and the O of n log n sort dominates.

@chapter Jarvis's march
@art gift-wrap
Jarvis's march wraps the set like paper. From the lowest point, it repeatedly picks the point with the smallest polar angle about the corner just found, one pass over all n points per corner. With h corners, that's O of n times h.

@words text="O(n·h) vs O(n lg n)" sub="better only when h grows slower than lg n"
That beats Graham's scan when h grows more slowly than log n, and loses when nearly every point is a corner.

@chapter The lesson's points
@math heading="1,0 · 7,1 · 4,3 · 9,5 · 5,9 · 0,6 · 6,6 · 2,3" items="hull: (1, 0), (7, 1), (9, 5), (5, 9), (0, 6)@five hull vertices;;inside: (4, 3), (6, 6), (2, 3)@inside;;n·h = 40 · n·lg n = 24@n times h"
On the lesson's eight points, the lab finds five hull vertices: one, zero; seven, one; nine, five; five, nine; and zero, six. Four, three, six, six, and two, three are inside. Gift wrapping's work, n times h, is forty, against n log n of twenty four. That's about this set, not the algorithms.

@art edge-midpoints
Careful with points in the middle of a side. On a square with its midpoints, the lab's monotone chain returns four corners, the boundary holds eight points, and gift wrapping returns six. Each answers a slightly different question. Graham's scan drops such points, by keeping only the farthest at each angle, or by popping on a colinear turn, and returns the four corners.

@chapter The closest pair
@art strip
Section thirty three point four finds the closest pair of n points in n log n, where checking every pair is n squared. Split the points by a vertical line, and solve each half to get the smaller distance, delta. Any closer pair must cross the line, inside a strip of width two delta.

@math heading="In the strip" items="≤ 8 points in a δ × 2δ box@at most eight;;compare each with the next 7 by y@the next seven;;T(n) = 2T(n/2) + O(n)@T of n"
At most eight points fit in a delta by two delta box, so each strip point, taken in order of y, needs comparing with only the next seven. Presorting keeps each level linear, so T of n is two T of n over two plus linear.

@chapter Where people slip
@list heading="Common slips" items="Testing points for being inside@The first|Expecting every algorithm's list to match@The second|Reading n·h as always faster or slower@the third"
The first slip is thinking the hull algorithm must find interior points to discard them. It never asks. Four, three is pushed, then popped. The second is expecting every algorithm to return the same list, when points sit on a side. And the third is reading O of n h as always faster, or always slower.

@chapter Try it
@code block=1 lines=1-1 focus="1@six points"
Your turn. Run Graham's scan by hand on these six points. Choose p zero, sort the rest by polar angle, and record every push and pop with the turn that caused it. Give the hull counterclockwise, and count the pops.

@end text="Wrap your own points"
You can compute hulls by two methods and compare their work, on Learn. That's learn dot get er done dot I O.

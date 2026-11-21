---
format: long
lesson: geometric-algorithms/the-closest-pair-and-the-strip
title: The closest pair of points, and why seven neighbours are enough
thumb: Seven neighbours, at most
---

@chapter The problem
@title text="The Closest Pair and the Strip" sub="Geometric Algorithms" art=thumb
Find the two closest points in a set. Checking every pair costs n squared. Divide and conquer gets it down to n log n, and the clever part is one narrow strip.

@chapter Split and recurse
@art split-halves
Sort the points by x, once. Split at the median into a left half and a right half, and solve each half recursively. Three points or fewer, just compare every pair. Each half returns its closest distance, and d is the smaller of the two.

@words text="d² stays an integer" sub="(x − mid)² < d²,  (Δy)² ≥ d²"
d is held as d squared throughout, so it's an integer. Every comparison is between squares, and nothing is ever rooted.

@chapter The pair at risk
@art straddling-pair
A pair with both points on one side was already considered by that side's recursive call. So the only pair the recursion can miss has one point on each side. And if it beats d, both of its points are within d of the dividing line. That's the merge step's whole job.

@art strip
So form the strip: the points within d of the dividing line. Sort it by y. For each strip point, compare it with the following ones, and stop as soon as the y gap alone reaches d. Those points can't beat d anyway.

@chapter Why seven
@art eight-squares
Here's where the constant comes from. Above a strip point, every candidate lies in a two d by d rectangle. Cut it into eight squares of side d over two. Each square's diagonal is d over root two, less than d. So two points in one square would be closer than d, which the recursion rules out.

@words text="8 squares − 1 = at most 7 neighbours"
At most one point per square, eight in all, including the point itself. So each point needs at most seven comparisons. That's a packing argument, not an average. Other partitions give six or four, with the same asymptotics.

@chapter Twelve points
@math heading="The lab's twelve points" items="closest d² = 2@squared distance is two;;(11, 4)–(12, 5)  and  (12, 5)–(13, 4)@two pairs tie;;17 comparisons  vs  66 pairs@seventeen comparisons;;strip: 5 comparisons  vs  7n = 84@five of those"
The lab opens on twelve points, with eleven, four, twelve, five and thirteen, four bunched near the middle. The closest squared distance is two, and two pairs tie. The recursion made seventeen comparisons, against sixty six pairs. And five of those were in a strip, against a bound of seven n, eighty four.

@art base-case
Where was the winning pair found? Those three points all land in the same three point base case, so brute force finds it there. The strip above just confirms it. That's common, and it's exactly why the strip can't be dropped. Nothing in the algorithm knows in advance that it wasn't needed.

@words text="5 measured · 84 proved" sub="busiest strip: 4/5 per point"
The per merge table shows strips of two, five and two, making one, four and zero comparisons. The busiest ran at four fifths of a comparison per strip point. Five and eighty four aren't the same kind of number. One is a count from this run. The other is a worst case bound. The gap isn't slack in the proof.

@art pairs-grid
Seventeen against sixty six is a real saving at twelve points, and a small one. At these sizes the constants matter more than the asymptotics. On a two point example the recursion does one comparison against one. The reason to build it is the bound: n log n for every input, while the full scan is n squared for every input.

@words text="two columns, one unit apart" sub="the top strip holds all ten points"
And the strip can hold everything. One lab example is two columns one unit apart, where the top level strip holds all ten points. The y sort and the early break are what keep that merge linear.

@chapter Where people slip
@list heading="Common slips" items="Re-sorting at every level@The first|Comparing every pair in the strip@The second|Taking a square root@And the third"
The first slip is sorting by x again at every level, which gives n log squared n. Sort once and pass slices. The second is comparing every pair in the strip. Without the early break, the merge goes quadratic. And the third is taking a square root anywhere. Even two coincident points just give zero, exactly, with no special case.

@end text="At most seven neighbours"
Step through the recursion and its strips on Learn. That's learn dot get er done dot I O.

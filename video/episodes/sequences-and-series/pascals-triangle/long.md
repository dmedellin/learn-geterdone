---
format: long
lesson: sequences-and-series/pascals-triangle
title: Pascal's triangle: add the two above, count the choices
thumb: Add the two above
---

@chapter Build it
@title text="Pascal's Triangle" sub="Sequences and Series" art=thumb
Start with a single one. Make every row begin and end with one, and every other entry the sum of the two above it. That's all it takes to build Pascal's triangle.

@math heading="The first rows" items="1@a single one;;1   1@row one;;1   2   1@one, two, one;;1   3   3   1@one, three, three, one;;1   4   6   4   1@one, four, six;;1   5   10   10   5   1@one, five, ten"
Row zero is a single one. Row one is one, one. Then one, two, one. Then one, three, three, one. Then one, four, six, four, one. And row five is one, five, ten, ten, five, one. Each ten is the four plus the six above it.

@art triangle-build
The ones down the edges aren't a special rule. They only have one entry above them, so there's nothing to add. And the name is a historical accident. The array appears in Chinese, Indian and Persian mathematics centuries before Pascal.

@chapter Naming an entry
@words text="C(n, k)" sub="row n, position k, both counted from 0"
Write C of n, k for the entry in row n, at position k. Both are counted from zero: the top is row zero, and the leftmost entry is position zero. So the third number in row six is C of six, two, which is fifteen.

@math heading="The building rule" items="C(n, 0) = C(n, n) = 1@the edges;;C(n, k) = C(n−1, k−1) + C(n−1, k)@the sum of the two"
In symbols: the edges are one, and any other entry is the sum of the two above it, C of n minus one, k minus one, plus C of n minus one, k.

@chapter What the entries count
@art delegations
Now a question with nothing to do with triangles. Three people, A, B and C, must send a delegation. There's one way to send nobody, three ways to send one person, three ways to send two, and one way to send all three.

@words text="1, 3, 3, 1" sub="row 3 · total 8 = 2³"
One, three, three, one. That's row three. In general, the number of ways to choose k objects from n distinct objects is C of n, k.

@art include-exclude
Here's why. Pick out one particular object. Every choice of k either includes it, and the other k minus one come from the remaining n minus one, or it doesn't, and all k do. Those two counts add. That's exactly the sum of the two above.

@art lattice-routes
There's a second count in the same picture. Walk down from the top, going left or right at each step. The number of routes reaching an entry is that entry, because every route arrives from one of the two entries above it.

@chapter Checks you can run
@art row-total
Each row adds up to a power of two. Sorting all the subsets of a set of n things by size counts each one once, and there are two to the n of them. Row six gives one plus six plus fifteen plus twenty plus fifteen plus six plus one, sixty four.

@words text="1 − 4 + 6 − 4 + 1 = 0" sub="alternating signs give 0 for n ≥ 1"
With alternating signs, every row after the first gives zero. Row four: one minus four plus six minus four plus one is zero.

@art mirror-row
And the triangle is symmetric, because choosing k to take is the same act as choosing n minus k to leave. Row eight starts one, eight, twenty eight, fifty six, seventy, and the rest is that read backwards.

@chapter A worked count
@math heading="Row 8 and a choice" items="row 8:   1   8   28   56   70   56   28   8   1@row eight;;sum = 256 = 2⁸  ✓@two hundred and fifty six;;C(8, 3) = 56@fifty six ways"
Build up to row eight: one, eight, twenty eight, fifty six, seventy, then back down. It adds to two hundred and fifty six, two to the eighth. So the number of ways to choose three people from eight is entry three, fifty six ways.

@chapter Common slips
@list heading="Common slips" items="Counting rows or positions from 1@First|Adding the wrong pair@Second|Trusting the row total alone@Third"
First, counting rows or positions from one. Second, adding the wrong pair: use the two immediately above. Third, trusting the row total alone. Two errors can cancel and still add to two to the n, so check symmetry and the parents too.

@words text="C(20, 10) = 184756" sub="twenty rows · 190 additions"
And the entries grow fast. C of twenty, ten is one hundred eighty four thousand seven hundred fifty six. Reaching it by addition takes twenty rows and one hundred and ninety additions. That's the argument for a formula, which comes next.

@chapter Try it
@words text="row 8  →  row 9" sub="edges 1 and 1 · then check symmetry and 2⁹"
Your turn. Start from row eight and build row nine. The two edge ones are given; every interior entry is yours. Check the row is symmetric, add it up against two to the ninth, and read C of nine, four as a sentence about choosing four people from nine.

@end text="Rows, and what they add to"
You can build the triangle row by row and compare every total with its power of two, on Learn. That's learn dot get er done dot I O.

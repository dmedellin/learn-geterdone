---
format: long
lesson: systems-and-matrices/gaussian-elimination
title: Gaussian elimination: row reduce, then read the answer
thumb: Count the pivots
---

@chapter The idea
@title text="Gaussian Elimination" sub="Systems and Matrices" art=thumb
Elimination by hand means choosing, every time, which variable to remove next. Gaussian elimination takes the choice away. It works one column at a time from the left, and at the end you read the number of solutions straight off the matrix.

@art staircase
The target is a shape called row echelon form. A row's first nonzero entry is its pivot. All zero rows go to the bottom, and each pivot sits strictly to the right of the one above it. So everything below a pivot is zero.

@art rref-identity
Reduced row echelon form goes further. Every pivot is one, and it's the only nonzero entry in its column. Then the answer is sitting in the constant column. And every matrix reduces to exactly one reduced form, whatever route you take.

@chapter The algorithm
@list heading="Column by column" items="Find the leftmost column still needing work@Find the leftmost|Get a nonzero entry on top@swap a row up|Divide to make the pivot 1@make the pivot one|Clear the rest of the column@Clear every|Cover that row and repeat@repeat"
Find the leftmost column that isn't all zero in the rows still being worked. If its top entry is zero, swap a row up from below. Divide the pivot row to make the pivot one, in exact fractions. Clear every other entry in that column. Then cover that row and repeat.

@art clear-column
To clear, subtract each other row's entry times the pivot row. Clear only below each pivot and you get echelon form, finished by back-substitution. Clear above as well, and that's Gauss-Jordan elimination.

@chapter Worked example
@math heading="Start" items="[  1   1   1 |  6 ]@one, one, one, six;;[  2  −1   3 |  9 ]@two, minus one;;[ −1   2   4 | 15 ]@minus one, two"
Here's the system from Systems in Three Variables once more. The rows are one, one, one, six. Two, minus one, three, nine. And minus one, two, four, fifteen.

@math heading="Clear below the pivots" items="R2 − 2R1 → R2:    [ 0  −3   1 | −3 ]@R two minus two R one;;R3 + R1 → R3:    [ 0   3   5 | 21 ]@R three plus R one;;R3 + R2 → R3:    [ 0   0   6 | 18 ]@R three plus R two"
R two minus two R one gives zero, minus three, one, minus three. R three plus R one gives zero, three, five, twenty one. Then R three plus R two gives zero, zero, six, eighteen. Three pivots for three variables, and no row of zeros: exactly one solution is already settled.

@math heading="Make the pivots 1" items="(−1/3)R2 → R2:    [ 0  1  −1/3 | 1 ]@minus a third;;(1/6)R3 → R3:    [ 0  0   1 | 3 ]@a sixth"
Now scale. Minus a third of R two gives zero, one, minus a third, one. A sixth of R three gives zero, zero, one, three.

@math heading="Clear above" items="R1 − R2 → R1:    [ 1  0  4/3 | 5 ]@R one minus R two;;R1 − (4/3)R3 → R1:    [ 1  0  0 | 1 ]@Subtract four thirds;;R2 + (1/3)R3 → R2:    [ 0  1  0 | 2 ]@Add a third;;x = 1,   y = 2,   z = 3@one, two, three"
R one minus R two gives one, zero, four thirds, five. Subtract four thirds of R three, and R one becomes one, zero, zero, one. Add a third of R three to R two, and it becomes zero, one, zero, two. So x, y and z are one, two, three.

@art rounding-drift
That minus a third isn't a mistake. It cancels two steps later. Round it to minus zero point three three, and y comes out as one point nine nine and x as one point zero one, in a matrix that looks just as convincing. Keep the fractions exact.

@chapter Reading the answer
@art dead-row
First, look for a row of zeros ending in a nonzero constant. It says zero equals k, so there's no solution. Stop there. Reducing further only produces a tidy matrix that means nothing.

@math heading="An inconsistent pair" items="x + y = 2      2x + 2y = 5@x plus y equals two;;R2 − 2R1:    [ 0  0 | 1 ]@R two minus two R one;;0x + 0y = 1   →   no solution@zero x plus zero y"
Take x plus y equals two, and two x plus two y equals five. One operation, R two minus two R one, gives the row zero, zero, one. That reads zero x plus zero y equals one, so there's no solution.

@art free-column
Otherwise, count pivots. A pivot in every variable column means exactly one solution. A variable column with no pivot means that variable is free. Give it a parameter, and you get infinitely many solutions.

@math heading="A free variable" items="[ 1  2  0 | −1 ]      [ 0  0  1 | 2 ]@reduce to;;y = t,    z = 2,    x = −1 − 2t@y is free;;{(−1 − 2t, t, 2)}@the solution set"
x plus two y plus three z equals five, and two x plus four y plus eight z equals fourteen, reduce to one, two, zero, minus one, and zero, zero, one, two. Column two has no pivot, so y is free: put y equals t. Then z is two and x is minus one minus two t. That's the solution set.

@chapter Where people slip
@list heading="Common slips" items="Reducing past an inconsistent row@The first|Rounding a pivot@The second|Treating a free variable as zero@the third"
The first slip is reducing past an inconsistent row. The second is rounding a pivot, because a third is not zero point three three. And the third is treating a free variable as zero, which reports one triple out of infinitely many. Then check in the original equations.

@chapter Try it
@math heading="Finish this one" items="[ 1  2  −1 | 3 ]@one, two, minus one;;[ 0  1   4 | 2 ]@zero, one, four;;[ 0  0   0 | 0 ]@all zeros"
Your turn. Start with the rows one, two, minus one, three. Zero, one, four, two. And a row of all zeros. Clear the two above the second pivot, name the free variable before you give it a parameter, and write the whole family of solutions.

@end text="Reduce it, then read it"
You can reduce a matrix step by step and read off its solutions, on Learn. That's learn dot get er done dot I O.

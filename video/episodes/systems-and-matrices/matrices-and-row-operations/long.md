---
format: long
lesson: systems-and-matrices/matrices-and-row-operations
title: Augmented matrices and the three row operations
thumb: Delete the letters
---

@chapter The idea
@title text="Matrices and Row Operations" sub="Systems and Matrices" art=thumb
Look back at a system you solved by elimination. The letters x, y and z never did any work. They just sat in their columns while the numbers changed.

@words text="one row per equation" sub="one column per variable · one column for the constants"
So delete them. An augmented matrix is a system with the variable names removed: one row per equation, one column per variable, and one final column for the constants.

@math heading="Matrix" items="m × n:   m rows, n columns@m by n;;a₂₃:   row 2, column 3@a two three"
A matrix is a rectangular array of numbers. One with m rows and n columns is an m by n matrix, rows first, always. Entries are named by position: a two three is the entry in row two, column three.

@chapter From system to matrix
@math heading="One row per equation" items="x + y + z = 6     →    [  1   1   1 |  6 ]@x plus y plus z;;2x − y + 3z = 9    →    [  2  −1   3 |  9 ]@two x minus y;;−x + 2y + 4z = 15   →    [ −1   2   4 | 15 ]@minus x plus two y"
Here's the system from Systems in Three Variables. x plus y plus z equals six becomes the row one, one, one, six. Two x minus y plus three z equals nine becomes two, minus one, three, nine. And minus x plus two y plus four z equals fifteen becomes minus one, two, four, fifteen.

@art augmented-grid
The vertical bar marks where the equals signs were. It's a reading aid and nothing more. Position carries all the meaning: in the second row, the minus one means minus one y only because it sits in the second column.

@math heading="Standard form first" items="2y − 5 = 3x − z   →   −3x + 2y + z = 5   →   [ −3  2  1 | 5 ]@two y minus five;;x + 4z = 0   →   x + 0y + 4z = 0   →   [ 1  0  4 | 0 ]@x plus four z"
The translation is mechanical, on one condition: every equation in standard form, with the variables in the same order. Two y minus five equals three x minus z becomes minus three x plus two y plus z equals five. And x plus four z equals zero needs a zero for the missing y.

@art missing-zero
That zero isn't padding. In a three variable system every row has four entries. A row with three has lost its alignment, and every later operation adds the wrong numbers together.

@chapter Three row operations
@list heading="Elementary row operations" items="Swap:   R1 ↔ R3@Swap two rows|Scale:   kR2 → R2,  k ≠ 0@Multiply a row|Replace:   R3 + kR1 → R3@add k times"
There are three row operations, and you've already done all of them to equations. Swap two rows. Multiply a row, constant included, by a number k that isn't zero. Or add k times one row to another, and store the result in that other row.

@art row-swap
Each one can be undone. A swap is undone by itself. It's just writing the equations in a different order.

@art row-scale
Scaling by k is undone by scaling by one over k, which exists exactly when k isn't zero.

@art row-replace
And replacing R three by R three plus k R one is undone by subtracting k R one. Only the row named after the arrow changes. Since every step reverses, row operations preserve the solution set, and the matrices are called row equivalent.

@chapter Two operations, written out
@math heading="R2 − 2R1 → R2" items="2 − 2(1) = 0      −1 − 2(1) = −3@Two minus two;;3 − 2(1) = 1      9 − 2(6) = −3@Three minus two;;[ 0  −3   1 | −3 ]@zero, minus three, one"
R two minus two R one, into R two. Two minus two is zero. Minus one minus two is minus three. Three minus two is one. And nine minus twelve is minus three. The new row is zero, minus three, one, minus three.

@math heading="R3 + R1 → R3" items="[ 0   3   5 | 21 ]@zero, three, five"
R three plus R one gives zero, three, five, twenty one. Those are exactly the equations A and B from Systems in Three Variables, entry for entry. The matrix didn't make the arithmetic easier. It made the position of every number decidable in advance.

@chapter What isn't allowed
@list heading="Not row operations" items="Multiplying a row by 0@by zero|Swapping columns@Swapping columns|Two operations at once@two operations at once"
Three things aren't row operations. Multiplying a row by zero destroys an equation for good. Swapping columns silently renames two variables, so the answers land on the wrong letters. And two operations at once aren't a sequence: from rows one, zero, one and zero, one, one, adding each to the other gives one, one, two, twice.

@list heading="Common slips" items="Leaving out the constant column@The first|Building a row before standard form@The second"
Two more slips. The first is leaving the constant column out. Doubling two, minus one, three, nine gives four, minus two, six, eighteen. The second is building a row before standard form. Three x equals two y plus five is not the row three, two, five.

@chapter Try it
@words text="2x − z = 5    y + 3z = −1    x + 2y = 4" sub="the first row begins  2  0  −1"
Your turn. Write the augmented matrix for two x minus z equals five, y plus three z equals minus one, and x plus two y equals four, in the order x, y, z. The first row begins two, zero, minus one. Then do R one minus two R three on the whole row, and translate it back.

@end text="Apply one operation at a time"
You can type a matrix and apply one row operation at a time, on Learn. That's learn dot get er done dot I O.

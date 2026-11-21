---
format: long
lesson: the-simplex-method/the-simplex-tableau
title: The simplex tableau: read a corner, then pivot exactly
thumb: Pivot the z-row too
---

@chapter The question
@title text="The Simplex Tableau" sub="The Simplex Method" art=thumb
The simplex method walks from corner to corner. But how do you actually do a step, by hand, without solving a fresh system every time? You keep everything in one grid, called a tableau.

@words text="[A | b]  +  one row:  z − cᵀx = 0"
A tableau is the standard form system, A next to b, with one extra row for the objective. That row says z minus c times x equals zero. It's an equation, like the others.

@chapter The first tableau
@math heading="maximise 3x₁ + 5x₂" items="s₁:   1   0   1   0   0  |  4@s one;;s₂:   0   2   0   1   0  |  12@s two;;s₃:   3   2   0   0   1  |  18@s three;;z:   −3  −5   0   0   0  |  0@minus three"
Take maximise three x one plus five x two, with x one at most four, two x two at most twelve, and three x one plus two x two at most eighteen. Add one slack per row. The s one row reads one, zero, one, zero, zero, and four. The s two row has a two under x two, and twelve. The s three row has three and two, and eighteen. And the objective row holds minus three and minus five.

@art identity-columns
The three slack columns already form an identity. Each has a single one and zeros elsewhere. So the first tableau needs no work beyond writing those negated costs.

@chapter Reading it for free
@words text="s₁ = 4,  s₂ = 12,  s₃ = 18,  z = 0" sub="x₁ = x₂ = 0"
Now read it. The basic variables are the slacks, so s one is four, s two is twelve, s three is eighteen. x one and x two are nonbasic, so they're zero, and z is zero. That's the origin. Nothing was solved. The right hand column was just copied out.

@art read-rhs
That's the whole point of the shape. When basic columns are identity columns, each row's right hand entry is the value of the variable that row carries. The bottom right is z.

@chapter One pivot
@art pivot-cell
A pivot on row r and column j has two moves. Divide row r by its entry in column j. Then clear column j in every other row, including the objective row.

@math heading="Row operations" items="R2′ = R2 ÷ 2:   0  1  0  1/2  0  |  6@halving row two;;R1′ = R1:   unchanged@row one;;R3′ = R3 − 2·R2′:   3  0  0  −1  1  |  6@twice the new row;;z′ = z + 5·R2′:   −3  0  0  5/2  0  |  30@five times"
Pivot on row two, column x two, where the entry is two. Halving row two makes it a one, with a half under s two, and six on the right. Row one has a zero in that column, so it doesn't change. Row three loses twice the new row. And the objective row gains five times the new row, which brings it to thirty.

@words text="x₂ = 6,  s₁ = 4,  s₃ = 6,  z = 30" sub="the corner (0, 6)"
The basis is now s one, x two, s three. Read it again. x two is six, s one is four, s three is six, x one is zero, and z is thirty. That's the corner zero, six.

@art edge-step
One pivot, one edge of the region. And the new reading is free, for the same reason the old one was.

@chapter Why the z-row pivots
@art stale-row
The objective row goes through the pivot because it's an equation. Carry it along, and the bottom right entry is always the objective at the current basis. Leave it out, and the tableau still looks finished. The constraint rows are right, x is right, but z is stale.

@words text="Silent, with a plausible answer"
It's the same error as dropping the constant column part way through an elimination. And it fails the same way: silently, with a plausible answer at the end.

@chapter A legal, bad pivot
@math heading="Pivot row 3, column x₂ instead" items="x₂ = 9@nine;;s₂ = −6@minus six;;z = 45 > 36@forty five"
Any non zero entry is a legal pivot, and the arithmetic doesn't care if the result is a corner. Pivot on row three, column x two instead, and you get x two equals nine, s two equals minus six, and z equals forty five. That's higher than the true optimum of thirty six.

@art outside-point
The point, zero, nine, is outside the region. It uses eighteen of plant B's twelve hours. The tableau is still a correct system. It just isn't describing a feasible point. Choosing the row safely is the ratio test, and choosing the column is the optimality test.

@chapter Where people slip
@list heading="Common slips" items="Leaving the z-row out@The first|Reading a nonbasic value from the rhs@The second|Pivoting wherever looks convenient@The third"
The first slip is leaving the objective row out of the row operations. The second is reading a nonbasic variable's value off the right hand column. It's zero, because it was set to zero. And the third is pivoting on whatever looks convenient. Until you know the ratio test, check the right hand column for a negative entry after every pivot.

@end text="Pivot it yourself"
You can choose a pivot and watch every row, the objective row included, change, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: linear-programming-models/basic-solutions-and-corners
title: Basic solutions: finding corners without a picture
thumb: Corners are just arithmetic
---

@chapter The question
@title text="Basic Solutions and Corners" sub="Linear Programming Models" art=thumb
With two variables you can draw the region and point at its corners. With twenty, there's no picture. So what exactly is a corner, when you can't see one?

@math heading="The workshop, as equalities" items="C + s₁ = 4@carpentry;;2T + s₂ = 12@finishing;;3C + 2T + s₃ = 18@assembly;;all five ≥ 0@all five"
Take the small workshop in equality form. C plus s one equals four, for carpentry. Two T plus s two equals twelve, for finishing. Three C plus two T plus s three equals eighteen, for assembly. And all five variables at least zero. Three equations, five unknowns.

@chapter Choosing zeros
@art zeros-as-lines
Choose two of the five to be zero. That leaves three unknowns and three equations, and row reduction settles them. Each zero is a line the point lies on. A decision set to zero puts you on an axis. A slack set to zero puts you on that row's boundary.

@words text="basic solution · basic feasible solution"
The result is a basic solution. If none of its entries is negative, it's a basic feasible solution. And here's the key fact: the basic feasible solutions are exactly the corners.

@chapter All ten choices
@math heading="Feasible: the five corners" items="s₂, s₃ = 0  →  (2, 6)@two, six;;s₁, s₃ = 0  →  (4, 3)@four, three;;T, s₁ = 0  →  (4, 0)@four, zero;;C, s₂ = 0  →  (0, 6)@zero, six;;C, T = 0  →  (0, 0)@zero, zero"
There are ten ways to pick two zeros. Five give feasible points: two, six. Four, three. Four, zero. Zero, six. And zero, zero. They're exactly the five corners of the picture.

@art five-corners
Read that again. You never looked at the picture. You chose zeros, solved, and checked signs, and the corners came out on their own. That's what replaces the drawing once there are too many variables to draw.

@math heading="Infeasible: outside" items="s₁, s₂ = 0  →  (4, 6),  s₃ = −6@four, six;;C, s₃ = 0  →  (0, 9),  s₂ = −6@zero, nine;;T, s₃ = 0  →  (6, 0)@six, zero"
Three solve to points outside. Four, six scores forty two, better than the optimum's thirty six. But solving its basis gives s three equals minus six. The assembly row is over by six hours, recorded as a negative slack. Zero, nine scores forty five and fails with s two equals minus six. And six, zero is outside too.

@art crossings-outside
These are crossings a picture throws away by eye. Here, throwing them away is a number with a sign. And a negative entry works in any number of variables. Outside the shaded region only works in two.

@chapter Not a point at all
@art parallel-lines
The last two choices aren't points. Set T and s two to zero, and you're asking where T equals zero meets two T equals twelve. Those lines are parallel, and never meet. The other one, C and s one, is the same story with C equals zero and C equals four.

@words text="parallel lines, not “singular”"
Row reduction stops at rank two out of three. The lab reports that as two named parallel lines, not just singular. The geometry is the explanation. The rank is only the symptom.

@chapter Degeneracy
@art three-lines-one-point
Push assembly from eighteen hours to twenty four. Now C equals four, two T equals twelve, and three C plus two T equals twenty four all pass through four, six.

@words text="4 corners, 6 basic feasible solutions"
Three different bases solve to that same point, each with a basic variable equal to zero. That's called degenerate. The picture has four corners, but the enumeration reports six basic feasible solutions. The extra ones aren't extra points. They're extra descriptions of one point.

@chapter Why an algorithm
@math heading="Bases to try" items="C(n + m, m)@n plus m choose m;;C(5, 3) = 10@ten;;10 decisions, 10 rows:  184,756@one hundred and eighty four thousand"
There are at most n plus m choose m bases to try. Here that's five choose three, which is ten. With ten decisions and ten rows, it's one hundred and eighty four thousand, seven hundred and fifty six.

@art growing-count
Enumerating bases defines what a corner is. It isn't a method for finding the best one, except on problems too small to matter. That gap is exactly what the simplex method exists to close.

@chapter Where people slip
@list heading="Common slips" items="Assuming every basic solution is a corner@The first|Reading singular as broken arithmetic@The second|Treating the count as a method@The third"
The first slip is assuming every basic solution is a corner. Three of the ten here aren't, and two of those beat the optimum. The second is reading singular as a failure of the arithmetic. The third is treating the count of bases as a method.

@end text="Enumerate all ten bases"
You can pick any two zeros and see the basic solution it gives, and its verdict, on Learn. That's learn dot get er done dot I O.

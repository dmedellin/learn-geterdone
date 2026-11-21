---
format: long
lesson: systems-and-matrices/systems-in-three-variables
title: Three equations, three unknowns: elimination twice
thumb: Same variable, both times
---

@chapter The problem
@title text="Systems in Three Variables" sub="Systems and Matrices" art=thumb
Three unknowns, three equations. The method barely changes from two. You use elimination twice, and the one rule that matters is about which variable you remove.

@math heading="An ordered triple" items="ax + by + cz = d@a x plus b y;;(x, y, z) satisfies every equation@an ordered triple"
A linear equation in three variables can be written a x plus b y plus c z equals d. A solution is an ordered triple that satisfies every equation. A triple that satisfies two of the three isn't a partial solution. It isn't a solution.

@art corner-planes
Each equation is a plane in space. Exactly one solution means the three planes meet in a single point, the way two walls and a floor meet in a corner.

@chapter The method
@list heading="The plan" items="Choose a variable@Choose a variable|Eliminate it from two different pairs@two different pairs|Solve the two-variable system@Solve that|Back-substitute and check all three@back-substitute"
Here's the plan. Choose a variable, and eliminate it from two different pairs of equations. That leaves two equations in two unknowns. Solve that, the way you already know. Then back-substitute to recover the third variable, and check in all three.

@math heading="The system" items="E1:    x +  y +  z =  6@E one;;E2:   2x −  y + 3z =  9@E two;;E3:   −x + 2y + 4z = 15@E three"
E one: x plus y plus z equals six. E two: two x minus y plus three z equals nine. E three: minus x plus two y plus four z equals fifteen. The x coefficients are one, two and minus one, so x is the cheap one to remove.

@chapter Worked example
@math heading="Remove x, twice" items="E2 − 2E1 :   −3y + z = −3@E two minus two;;E3 + E1 :    3y + 5z = 21@E three plus E one"
E two minus two E one gives minus three y plus z equals minus three. Call it A. E three plus E one gives three y plus five z equals twenty one. Call it B. Both times, x is the variable that left.

@math heading="Solve, then back-substitute" items="A + B :   6z = 18  →  z = 3@six z;;A :   −3y + 3 = −3  →  y = 2@minus three y plus three;;E1 :   x + 2 + 3 = 6  →  x = 1@x plus two plus three"
Add A and B: six z equals eighteen, so z is three. Into A: minus three y plus three equals minus three, so y is two. Into E one: x plus two plus three equals six, so x is one.

@math heading="Check all three" items="E1:   1 + 2 + 3 = 6 ✓@One plus two;;E2:   2 − 2 + 9 = 9 ✓@Two minus two;;E3:   −1 + 4 + 12 = 15 ✓@Minus one plus four"
Check in all three originals. One plus two plus three is six. Two minus two plus nine is nine. Minus one plus four plus twelve is fifteen. The solution is one, two, three.

@art reverse-order
The back-substitution ran backwards through the work: z from the sum, then y from A, then x from E one. The last variable found comes first.

@chapter The rule that matters
@art same-variable
Both eliminations must remove the same variable. E two plus two E three would also be fine: a different pair, the same variable. But two E two plus E three gives three x plus ten z equals thirty three. That's true, but it's in x and z, while A is in y and z.

@art same-variable-wrong
Together those two equations still hold three unknowns between them, so nothing has been reduced. The new equations must also come from different pairs. Two combinations of E one and E two alone say nothing new, and E three never enters.

@chapter The other cases
@art prism-planes
No solution can mean two parallel planes. Or the three planes can meet in pairs along three parallel lines, like the sides of a triangular prism, with no point on all three. That case is invisible until the algebra gives a false statement.

@math heading="A third equation that adds nothing" items="E3  →  3x + 4z = 15    (E1 + E2)@E one plus E two;;0 = 0@zero equals zero;;(9 − 4t, t, 3t − 3)@nine minus four t"
Replace E three with three x plus four z equals fifteen, which is just E one plus E two. Eliminating x twice now ends in zero equals zero, and the solution set is a line: nine minus four t, t, three t minus three.

@art line-planes
At t equals one the triple is five, one, zero. At t equals two it's one, two, three, the original solution. One of the three equations was never carrying any information.

@chapter Bookkeeping
@list heading="Keep it straight" items="Label every new equation@Label every|Write a 0 for a missing variable@write a zero|Back-substitute in reverse order@reverse order|Check in E1, E2 and E3@as they were given"
Label every new equation with the combination that made it, like E two minus two E one. Keep the columns aligned, and write a zero for any missing variable. Back-substitute in reverse order. And check in all three equations as they were given, because A and B fit by construction.

@chapter Try it
@words text="x + y + z = 4    2x − y + z = 1    −x + 3y + 2z = 9" sub="form E2 − 2E1 and E3 + E1"
Your turn. Solve x plus y plus z equals four, two x minus y plus z equals one, and minus x plus three y plus two z equals nine. Form E two minus two E one, and E three plus E one, so x leaves both. Solve what's left, and test the triple in all three.

@end text="Watch one solution become a line"
You can make the third equation the sum of the first two and watch one solution become a line, on Learn. That's learn dot get er done dot I O.

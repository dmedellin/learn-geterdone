---
format: long
lesson: systems-and-matrices/solving-by-elimination
title: Solving by elimination: add the equations, lose a variable
thumb: Make one variable cancel
---

@chapter The idea
@title text="Solving by Elimination" sub="Systems and Matrices" art=thumb
Substitution always works. But when both equations sit in standard form, there's usually a quicker way: add the equations, and make one variable cancel.

@art balance-add
Adding equations is legal. If a equals b, and c equals d, then a plus c equals b plus d. The sum of two true equations is a true equation.

@art opposites-cancel
So choose multiples that make one variable's coefficients opposites, then add. That variable leaves, and you're left with one equation in one unknown.

@chapter A worked example
@math heading="3x + 4y = 10 and 5x − 2y = 8" items="3x + 4y = 10@three x plus four y;;5x − 2y = 8   × 2  →  10x − 4y = 16@double the second;;13x = 26  →  x = 2@thirteen x"
Take three x plus four y equals ten, and five x minus two y equals eight. The y coefficients are four and minus two, so double the second equation: ten x minus four y equals sixteen. Add, and y is gone. Thirteen x equals twenty six, so x is two.

@math heading="Back-substitute, then check" items="3(2) + 4y = 10  →  4y = 4  →  y = 1@three times two;;3(2) + 4(1) = 10 ✓@six plus four;;5(2) − 2(1) = 8 ✓@ten minus two"
Put x equals two into an original equation: three times two plus four y equals ten, so four y is four, and y is one. Check both: six plus four is ten, and ten minus two is eight. The solution is two, one.

@art aligned-columns
Before any of this, line the equations up in standard form: x above x, y above y, constants on the right. Elimination adds columns, and columns that aren't aligned add the wrong things together.

@chapter Choosing the multipliers
@math heading="Least common multiple" items="2x + 3y = 5    × 2  →  4x + 6y = 10@by two;;5x − 2y = −16   × 3  →  15x − 6y = −48@by three;;19x = −38  →  x = −2@nineteen x;;3y = 9  →  y = 3@three y is nine"
Take two x plus three y equals five, and five x minus two y equals minus sixteen. The y coefficients are three and minus two, and their least common multiple is six. So multiply by two and by three, and add. Nineteen x equals minus thirty eight, so x is minus two. Then three y is nine, so y is three.

@words text="(−2, 3)" sub="check: 5(−2) − 2(3) = −10 − 6 = −16 ✓"
The pair is minus two, three. Check it in the second equation: five times minus two, minus two times three, is minus ten minus six, which is minus sixteen.

@words text="one multiplication, not two" sub="eliminating x: 15x + 20y = 50 and −15x + 6y = −24"
Either variable can go. In the first example, eliminating x means multiplying by five and by minus three, giving fifteen x plus twenty y equals fifty, and minus fifteen x plus six y equals minus twenty four. Same pair, longer road. Look at all four coefficients first.

@chapter Why it's safe
@art one-at-a-time
The new system has exactly the same solutions as the old one. Keep the first equation, and replace the second by itself plus k times the first. Subtracting k times the first undoes it, so nothing is lost and nothing is invented.

@words text="x = 1 and y = 1" sub="add each to the other at once: x + y = 2, twice"
But change one equation at a time. From x equals one and y equals one, add each to the other at once, and you get x plus y equals two, twice. That has a whole line of solutions. And never multiply by zero.

@chapter When both variables go
@math heading="0 = 14" items="2x − 6y = 4@two x minus six y;;−x + 3y = 5   × 2  →  −2x + 6y = 10@minus x plus three y;;0 = 14    false  →  no solution@zero equals fourteen"
Sometimes both variables leave. Take two x minus six y equals four, with minus x plus three y equals five. Double the second and add, and you get zero equals fourteen. False, so there's no solution.

@art parallel-lines
The system is inconsistent. Its two lines are parallel, and never meet.

@math heading="0 = 0" items="−x + 3y = −2   × 2  →  −2x + 6y = −4@minus two instead;;0 = 0    true  →  infinitely many@zero equals zero;;{(3t + 2, t)}@three t plus two"
Make the second constant minus two instead, and the sum is zero equals zero. True. The second equation carried nothing new, and the solution set is a line: three t plus two, t.

@art same-line-dots
At t equals zero that's two, zero. At t equals one it's five, one. Both satisfy both equations. But zero, zero isn't on the line. Infinitely many is a count, and the answer is a set.

@chapter Where people slip
@list heading="Common slips" items="Adding equations that aren't aligned@The first|Multiplying only the left side@The second|Reading 0 = 0 as x = 0@the third"
The first slip is adding equations that aren't aligned. Standard form first, every time. The second is multiplying only the left side. Doubled, five x minus two y equals eight becomes ten x minus four y equals sixteen, and the sixteen is what gets left behind. And the third is reading zero equals zero as x equals zero.

@chapter Try it
@words text="4x + 3y = 1  and  2x − 3y = 11" sub="both multipliers are 1: just add"
Your turn. Solve four x plus three y equals one, and two x minus three y equals eleven. Both multipliers are one, so just add. Finish the other coordinate, check in both originals, and say why eliminating x would cost more.

@end text="Pick the multipliers"
You can pick the multipliers and watch both routes reach the same pair, on Learn. That's learn dot get er done dot I O.

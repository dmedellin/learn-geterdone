---
format: long
lesson: systems-and-matrices/solving-by-substitution
title: Solving a system by substitution, without losing the answer
thumb: Put it in the other one
---

@chapter The idea
@title text="Solving by Substitution" sub="Systems and Matrices" art=thumb
Two equations, two unknowns, and you already know how to solve an equation with one unknown. Substitution turns the first problem into the second.

@list heading="Four moves" items="Solve one equation for one variable@Solve one|Substitute into the other equation@put that expression|Solve the one-variable equation@Solve it|Back-substitute, then check both@put that value back"
The method has four moves. Solve one equation for one of its variables. Then put that expression into the other equation, which now has a single variable. Solve it. Then put that value back into the isolated equation to get the partner, and check the pair in both originals.

@art swap-in
The target is one equation in one unknown. Everything else is bookkeeping, and the method always works. What you choose to isolate decides whether it's pleasant.

@art two-names
Why is it allowed? If x equals y plus one, then x and y plus one are two names for the same number, so either may be written where the other stands. One proviso: the isolated equation stays in the system. It's what gives you the second value at the end.

@chapter A worked example
@math heading="Look for a coefficient of 1" items="5x − 2y = 4@five x minus two y;;3x + y = 9  →  y = 9 − 3x@three x plus y"
Look for a variable whose coefficient is one or minus one. In five x minus two y equals four, and three x plus y equals nine, the y in the second equation has coefficient one. So y equals nine minus three x arrives with no division.

@math heading="Substitute, in brackets" items="5x − 2(9 − 3x) = 4@into the first;;5x − 18 + 6x = 4@minus eighteen;;11x = 22  →  x = 2@eleven x;;y = 9 − 3(2) = 3@Back in"
Put it into the first equation, in brackets. The minus two multiplies both terms, so you get five x minus eighteen plus six x equals four. Eleven x equals twenty two, so x is two. Back in the isolated equation, y is nine minus six, which is three.

@math heading="Check both originals" items="5(2) − 2(3) = 10 − 6 = 4 ✓@five times two;;3(2) + 3 = 6 + 3 = 9 ✓@three times two"
Now check in both originals. Five times two, minus two times three, is ten minus six, which is four. Three times two plus three is nine. The solution is the pair two, three.

@art bracket-reach
That bracket matters. Minus two times minus three x is plus six x. Write five x minus eighteen minus six x instead, and you get x equals minus twenty two, which fails the very first check.

@chapter The unspent equation
@math heading="No coefficient of 1" items="3x + 2y = 4    2x − 5y = 9@three x plus two y;;x = (9 + 5y)/2@nine plus five y;;3(9 + 5y) + 4y = 8@multiply through;;19y = −19  →  y = −1,  x = 2@nineteen y"
With three x plus two y equals four, and two x minus five y equals nine, nothing has coefficient one. Isolate x from the second: nine plus five y, over two. Substitute into the first and multiply through by two. Nineteen y equals minus nineteen, so y is minus one and x is two.

@art spent-equation
It has to go into the first equation. Put that expression back into the one it came from, and you get nine equals nine. True, and completely uninformative. Information comes from the equation you haven't spent yet.

@chapter When the variable disappears
@math heading="A contradiction" items="x − 2y = 3  →  x = 2y + 3@so x equals;;2(2y + 3) − 4y = 1@four y plus six;;6 = 1    false  →  no solution@six equals one"
Sometimes both variables vanish. Take x minus two y equals three, so x equals two y plus three, with two x minus four y equals one. Substituting gives four y plus six minus four y equals one, so six equals one.

@art parallel-lines
That's false, so no pair works. The two lines are parallel.

@math heading="An identity" items="2x − 4y = 6@equals six;;6 = 6    true for every y@six equals six;;{(2t + 3, t) : t real}@two t plus three"
Change the second equation to two x minus four y equals six, and you get six equals six. That's true for every y, so there are infinitely many solutions: the pairs two t plus three, t.

@art parameter-line
That's a recipe. Choose t, get a pair. t equals zero gives three, zero. t equals one gives five, one. Each satisfies both equations. The letter is arbitrary, and any correct description of the line is a correct answer.

@chapter Where people slip
@list heading="Common slips" items="Substituting back where you isolated@The first|Dropping the brackets@The second|Stopping at one number@the third"
The first slip is substituting back into the equation you isolated from, which only ever gives something like nine equals nine. The second is dropping the brackets, so the minus two reaches only the nine. And the third is stopping at one number. The answer is a pair.

@chapter Try it
@words text="4x − y = 11  and  2x + 3y = 9" sub="isolate y from the first"
Your turn. Solve four x minus y equals eleven, and two x plus three y equals nine. Isolate y from the first equation, put the whole expression into the second in brackets, finish the pair, and check it in both originals.

@end text="Switch what you isolate"
You can switch which variable gets isolated and compare the two routes, on Learn. That's learn dot get er done dot I O.

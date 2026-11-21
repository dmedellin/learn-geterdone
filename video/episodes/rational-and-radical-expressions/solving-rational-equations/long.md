---
format: long
lesson: rational-and-radical-expressions/solving-rational-equations
title: Solving rational equations, and why you must check every answer
thumb: Check in the original
---

@chapter A legal step that can lie
@title text="Solving Rational Equations" sub="Rational and Radical Expressions" art=thumb
Multiply a rational equation by its L C D, and it turns into a polynomial equation you already know how to solve. That step is legal. It's also not reversible, so it can hand you numbers that solve the new equation and not the one you started with.

@list heading="The method" items="Factor every denominator@Factor every|List the excluded values@list the excluded|Multiply both sides by the LCD@multiply both sides|Solve the polynomial equation@solve whatever|Test each candidate in the original@test each"
The method is short. Factor every denominator, list the excluded values, multiply both sides by the L C D, solve whatever polynomial equation appears, and then test each candidate in the original.

@chapter Why candidates can be fake
@art balance-beam
Multiplying both sides by the L C D means multiplying by an expression whose value depends on x. At an excluded value, that expression is zero.

@art empty-balance
And multiplying an equation by zero gives zero equals zero, which is true no matter what the original said. So the cleared equation can be true at a value where the original isn't even defined.

@math heading="One way only" items="A = B  ⟹  A·M = B·M@always;;A·M = B·M  ⟹  A = B  only if M ≠ 0@only when"
Put precisely. If A equals B, then A M equals B M, always. But A M equals B M gives back A equals B only when M isn't zero. Clearing uses the first direction, so the solution set can only grow, never shrink.

@art one-way-arrow
That's why the check is part of the method, not a politeness. You can't avoid a fake candidate by being careful. You can only detect it.

@art growing-set
A value that solves the cleared equation but not the original is called an extraneous solution. For rational equations, those are exactly the candidates that are excluded values. And it isn't a mistake. It's the predictable residue of a legal step.

@chapter No solution at all
@math heading="x/(x − 3) = 3/(x − 3) + 2" items="LCD = x − 3,   x ≠ 3@the L C D;;x = 3 + 2(x − 3)@clearing gives;;x = 2x − 3@so x equals two x;;x = 3  ✗  excluded@extraneous"
Here's the first example. x over x minus three equals three over x minus three, plus two. The L C D is x minus three, and three is excluded. Clearing gives x equals three plus two times x minus three, so x equals two x minus three, and x equals three. The only candidate is excluded, so it's extraneous.

@art no-survivor
So the equation has no solution. Nothing went wrong. The algebra is right at every line. The equation simply has no solution, and the method reports that honestly, as a candidate you have to throw away.

@chapter One survivor
@math heading="1/(x − 2) + 1/x = (x² + x − 4)/(x(x − 2))" items="LCD = x(x − 2),   x ≠ 0,  x ≠ 2@the exclusions;;x + (x − 2) = x² + x − 4@clearing gives;;x² − x − 2 = 0@so x squared;;(x − 2)(x + 1) = 0@it factors"
One over x minus two, plus one over x, equals x squared plus x minus four, over x times x minus two. The exclusions are zero and two. Clearing gives x plus x minus two equals x squared plus x minus four. So x squared minus x minus two is zero, and it factors as x minus two, times x plus one.

@math items="candidates: 2 and −1@candidates are;;x = 2:  excluded  ✗@two is excluded;;x = −1:  LHS = −1/3 − 1 = −4/3@the left side;;RHS = (1 − 1 − 4)/((−1)(−3)) = −4/3  ✓@the right side;;solution set: {−1}@solution set"
The candidates are two and minus one. Two is excluded, so it goes. At minus one, the left side is minus one third minus one, minus four thirds. The right side is one minus one minus four, over minus one times minus three, also minus four thirds. The solution set is just minus one.

@art candidate-filter
Substitute into the original equation, never into the cleared one. Every candidate satisfies the cleared equation by construction, so checking there confirms nothing. It's the one test guaranteed to pass. And cross multiplying, a over b equals c over d becoming a d equals b c, is the same step, with the same duty to check.

@chapter Where people slip
@list heading="Common slips" items="Skipping the check because the algebra looked clean@The first|Checking in the cleared equation@The second|Reporting no solution as an error@the third"
The first slip is skipping the check because the algebra looked clean. It usually is clean. The second is checking in the cleared equation. And the third is reporting no solution as an error. No solution is a real answer, and it isn't the same as I couldn't solve it.

@chapter Try it
@words text="1/(x − 1) + 1/(x + 1) = (x² − x + 2)/(x² − 1)" sub="LCD (x − 1)(x + 1),  x ≠ −1, 1"
Your turn. One over x minus one, plus one over x plus one, equals x squared minus x plus two, over x squared minus one. The L C D is x minus one times x plus one, and minus one and one are excluded. Clear every term, factor the quadratic, and check both candidates in the original.

@end text="Check every candidate"
You can practise clearing and checking rational equations on Learn. That's learn dot get er done dot I O.

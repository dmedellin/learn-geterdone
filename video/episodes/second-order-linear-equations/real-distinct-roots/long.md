---
format: long
lesson: second-order-linear-equations/real-distinct-roots
title: Two real roots: building and fitting the general solution
thumb: Two roots, two constants
---

@chapter The question
@title text="Real Distinct Roots" sub="Second-Order Linear Equations" art=thumb
When the characteristic quadratic has two different real roots, what does the solution look like? And can you tell where the motion is heading before you work out a single constant?

@art two-decays
Each root r gives an exponential solution, e to the r t. Since combinations of solutions are solutions, you can add a multiple of each.

@math heading="General solution" items="y = C₁·e^(r₁t) + C₂·e^(r₂t)@y equals C one"
So the general solution is y equals C one e to the r one t, plus C two e to the r two t. The word general matters. The form carries both constants, and a particular motion is picked out by giving them values.

@words text="every solution has this form" sub="stated here, not proved in full"
Every such function is a solution, and the lab checks that case by case. That there are no others is something this course states without a full proof. A later lesson shows why two constants are always enough.

@chapter Fitting the constants
@art fan-of-starts
To fit the constants, use the start. At t equals zero both exponentials are one, so y of zero is C one plus C two. The rate at zero is r one C one plus r two C two. Two equations, two unknowns, and exactly one answer whenever the roots differ.

@math heading="y″ + 3y′ + 2y = 0" items="roots −1 and −2@minus one and minus two;;y = C₁·e^(−t) + C₂·e^(−2t)@so y is;;y(0) = C₁ + C₂ = 1@the value is;;y′(0) = −C₁ − 2·C₂ = 0@the rate is"
For y double prime plus three y prime plus two y, the roots are minus one and minus two, so y is C one e to the minus t plus C two e to the minus two t. Start at one, rate zero. The value is C one plus C two, equals one. The rate is minus C one minus two C two, equals zero.

@math heading="Solve" items="add:  −C₂ = 1,  C₂ = −1@Add them;;C₁ = 1 − C₂ = 2@So C one;;y = 2·e^(−t) − e^(−2t)@The solution"
Add them, and minus C two equals one, so C two is minus one. So C one is one minus C two, which is two. The solution is two e to the minus t, minus e to the minus two t.

@chapter Check it
@art fitted-curve
Checking by substitution is what makes the answer trustworthy. The rates are y prime equals minus two e to the minus t plus two e to the minus two t, and y double prime equals two e to the minus t minus four e to the minus two t.

@math heading="y″ + 3y′ + 2y" items="e^(−t):  2 − 6 + 4 = 0@two minus six plus four;;e^(−2t):  −4 + 6 − 2 = 0@minus four plus six minus two"
Collect the e to the minus t terms: two minus six plus four, zero. The e to the minus two t terms: minus four plus six minus two, zero. The lab prints the same residual, zero, and checks both starting values too.

@chapter Reading the roots
@art both-grow
With roots minus one and minus two, both terms shrink, so every solution tends to zero. With roots two and three, as in y double prime minus five y prime plus six y, both terms grow.

@art one-grows-one-shrinks
And with roots minus one and one, as in y double prime minus y, one term shrinks and one grows. The growing one wins as soon as its constant isn't zero.

@math heading="y″ − y = 0,  y(0) = 1" items="y′(0) = −1:  C₁ = 0, C₂ = 1, y = e^(−t)@a starting rate of minus one;;y′(0) = −99/100:  C₁ = 1/200@minus ninety nine"
With a starting rate of minus one, C one is zero and C two is one, so y is e to the minus t, which decays. Change the rate to minus ninety nine over a hundred, and C one is one over two hundred. Tiny, but the e to the t term is there, and it grows past everything.

@art knife-edge
A decaying solution here is balanced on one exact value. With measured data that never happens, so the safe forecast is that a positive root means growth.

@chapter Where people slip
@list heading="Common slips" items="Leaving out the constants@The first|Dropping the sign in the exponent@The second|Forecasting from one root@The third"
The first slip is leaving out the constants. The bare sum always starts at two, so it can't fit a start at one with rate zero. The second is dropping the sign in the exponent. E to the t gives one plus three plus two, six, not zero. And the third is forecasting decay from one negative root. You need both.

@chapter Try it
@words text="y″ − 5y′ + 6y = 0" sub="roots 2 and 3"
Your turn. Take y double prime minus five y prime plus six y, with roots two and three. Pick a starting value and rate, set up the two equations for C one and C two, solve them, and check the residual by substitution.

@end text="Fit the constants, check the residual"
You can fit the constants and watch every term grow or die away, on Learn. That's learn dot get er done dot I O.

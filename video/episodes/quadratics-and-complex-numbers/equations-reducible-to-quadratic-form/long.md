---
format: long
lesson: quadratics-and-complex-numbers/equations-reducible-to-quadratic-form
title: Equations that are quadratics in disguise
thumb: Rename it, solve it, come back
---

@chapter A quadratic in disguise
@title text="Equations Reducible to Quadratic Form" sub="Quadratics and Complex Numbers" art=thumb
This course has no formula for a quartic. But a quartic with no odd powers isn't really a quartic. It's a quadratic wearing x squared where a quadratic wears x, and renaming that part is enough to finish it exactly.

@art rename-box
An equation is in quadratic form if it can be written a u squared plus b u plus c equals zero, where u is some expression in x. The test is that the same inner expression appears squared and on its own, with nothing else depending on x.

@chapter The method
@math heading="x⁴ − 5x² + 4 = 0" items="u = x²  →  u² − 5u + 4 = 0@put u;;(u − 1)(u − 4) = 0  →  u = 1 or u = 4@factor;;x² = 1 → x = ±1     x² = 4 → x = ±2@back to x"
Take x to the fourth minus five x squared plus four. Put u equal to x squared, so x to the fourth is u squared. Then factor u squared minus five u plus four, and u is one or four. Now go back to x. x squared equals one gives plus or minus one, and x squared equals four gives plus or minus two.

@art one-to-two
So there are four solutions: minus two, minus one, one and two. The substitution is legal because it's a renaming in both directions. Nothing's been done to the equation. Part of it has just been given a shorter name.

@art round-trip
But solving for u is only half the work. u is a temporary name, not the answer. The question was about x, so the last step is always the return journey: push every value of u back through the substitution. Writing the substitution down at the start makes that step hard to forget.

@chapter When u gives no x
@math heading="x⁴ − 3x² − 4 = 0" items="(u − 4)(u + 1) = 0  →  u = 4 or u = −1@u minus four;;x² = 4  →  x = ±2@plus or minus two;;x² = −1  →  no real x@minus one"
Now x to the fourth minus three x squared minus four. With u equal to x squared, that factors as u minus four, times u plus one. So u is four or minus one. x squared equals four gives plus or minus two. But x squared equals minus one has no real solution.

@art dead-end
So this quartic has two real solutions, not four. Over the complex numbers, x squared equals minus one gives plus or minus i, so there are four complex solutions: two, minus two, i and minus i. Say which number system you mean.

@chapter Radicals
@math heading="x − 5√x + 6 = 0" items="u = √x  →  u² − 5u + 6 = 0  →  u = 2 or 3@put u equal to root x;;x = 4  or  x = 9@four or nine;;4 − 10 + 6 = 0     9 − 15 + 6 = 0@both check"
The inner expression can be a root. In x minus five root x plus six, put u equal to root x, so u squared is x. That gives u equals two or three, so x is four or nine. Both check.

@math heading="x + √x − 6 = 0" items="(u + 3)(u − 2) = 0  →  u = 2 or u = −3@u plus three;;√x is never negative  →  discard u = −3@never negative;;x = 4@x is four"
But in x plus root x minus six, the quadratic factors as u plus three, times u minus two, so u is two or minus three. Root x is never negative, so throw out minus three before squaring it. That leaves just one answer: x is four.

@art discard-bin
Square minus three anyway, and you get nine. But nine plus three minus six is six, not zero. That's an extraneous solution.

@chapter Other inner expressions
@math heading="x⁻² − x⁻¹ − 6 = 0" items="u = 1/x  →  (u − 3)(u + 2) = 0@one over x;;x = 1/3  or  x = −1/2@one third"
Negative powers work too. Put u equal to one over x, and you get u minus three, times u plus two. So x is one third or minus one half. A negative u is fine here. What matters for this one is that x isn't zero.

@math heading="(x² − 3)² − 2(x² − 3) − 8 = 0" items="u = x² − 3  →  u = 4 or u = −2@put u equal to;;x² = 7  or  x² = 1@seven;;x = ±√7,  ±1@root seven"
The inner part needn't be a power. Here, put u equal to x squared minus three. Then u is four or minus two, so x squared is seven or one. The four solutions are plus or minus root seven, and plus or minus one.

@chapter Where people slip
@list heading="Common slips" items="Stopping at u@The first|Keeping a u that no real x produces@The second|Dividing by a power of x@The third"
The first slip is stopping at u. u equals four isn't a solution of an equation in x. The second is keeping a value of u that no real x produces. The third is dividing by a power of x. x to the fourth equals four x squared has solutions zero, two and minus two, and dividing by x squared loses zero.

@art four-dots
One last check. A quartic has at most four real solutions. If you come back with five, or with one that fails when you substitute, the return journey went wrong.

@end text="Rename, solve in u, come back to x"
Practise spotting the hidden quadratic, on Learn. That's learn dot get er done dot I O.

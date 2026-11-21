---
format: long
lesson: first-order-linear-equations/the-standard-form
title: First-order linear equations: getting the standard form right
thumb: Divide first, then read p and q
---

@chapter The question
@title text="The Standard Form" sub="First-Order Linear Equations" art=thumb
Every method in this course starts from the same line: y prime plus p of t times y equals q of t. Getting an equation into that shape, and reading p and q correctly, is where most later errors begin.

@chapter What linear means
@math heading="First-order linear" items="a(t)·y′ + b(t)·y = c(t)@a of t;;y′ + p(t)·y = q(t)@standard form;;p = b/a,   q = c/a@p equal to b over a"
A first order linear equation is one you can write as a of t times y prime, plus b of t times y, equals c of t. Divide through by a, and you get the standard form, y prime plus p of t times y equals q of t, with p equal to b over a and q equal to c over a.

@words text="q = 0: homogeneous    q ≠ 0: forced"
When q is zero, the equation is homogeneous. Nothing pushes on it from outside. When q isn't zero, it's forced, and q is the forcing.

@art linear-pieces
Linear is about y, never about t. The unknown y and its rate y prime each appear once, alone, to the first power. That rules out y squared, y times y prime, sine of y and one over y. The factors in front can be anything in t.

@chapter Divide first
@math heading="2y′ + 6y = 4t" items="divide every term by 2@divide every term;;y′ + 3y = 2t@y prime plus three y;;p = 3,   q = 2t,   forced@p is three"
Take two y prime plus six y equals four t. Divide every term by two, the right side too. That's y prime plus three y equals two t. So p is three, q is two t, and since q isn't zero, it's forced.

@art divide-first
The formulas in this course, for the steady state, the integrating factor and the particular solution, are all written for y prime with coefficient one. Each goes wrong by exactly the leftover factor if you skip this. Dividing first is cheap. Dividing in the middle of a formula is where errors happen.

@chapter Sorting equations
@list heading="Linear or not?" items="y′ = 2y + t²·y   linear@two y plus t squared y|y′ = t·y   linear, homogeneous@t times y|y′ + y² = t   not linear@y squared equals t|y·y′ = 1   not linear@y times y prime"
y prime equals two y plus t squared y is linear: the t squared is a coefficient of y, not a power of it. y prime equals t times y is linear and homogeneous. y prime plus y squared equals t is not linear, because of the y squared. And y times y prime equals one is not, because it multiplies y by y prime.

@math heading="y′ = 4 − 2y" items="y′ + 2y = 4@collect;;p = 2,   q = 4@p is two"
Watch the sign. In y prime equals four minus two y, the unknown is on both sides. Collect it on the left, and you get y prime plus two y equals four. So p is two, not minus two.

@art sign-move
Moving a term across the equals sign changes its sign, and that's the commonest slip in reading p. It matters later. A positive constant p makes homogeneous solutions die away. A negative one makes them grow.

@chapter Scaling
@math heading="If y′ + p·y = 0" items="(C·y)′ + p·(C·y) = C·(y′ + p·y) = C·0 = 0@C times"
Here's what homogeneous buys you. If y solves y prime plus p y equals zero, so does C times y, for any constant. The constant comes straight out of the derivative, so you get C times zero, which is zero. For y prime equals y squared, that fails.

@math heading="t·y′ − 2y = 0" items="y′ − (2/t)·y = 0@divide by t;;y = t²:   t·(2t) − 2·t² = 0@check;;C·t² for every C@scaling"
Take t y prime minus two y equals zero, and divide by t. So p is minus two over t, homogeneous. One solution is t squared. Check: t times two t, minus two t squared, is zero. By scaling, C times t squared is a solution for every C.

@art scaled-family
That's a whole family from one solution, and the lab prints exactly C times t squared as the homogeneous solution.

@art two-stretches
One care point. Dividing by t is only allowed where t isn't zero. So you work on the stretch where t is positive, or where it's negative, never across zero.

@chapter Where people slip
@list heading="Common slips" items="Calling y′ = 2y + t²·y nonlinear@The first|Dividing the left side only@The second|Keeping the sign before the move@The third"
The first slip is calling y prime equals two y plus t squared y nonlinear because of the t squared. The second is dividing the left side by the coefficient and leaving the right side alone. The third is reading p with the sign it had before the term moved across.

@art wrong-forcing
From two y prime plus six y equals four t, dividing only the left gives y prime plus three y equals four t. Test it with two thirds t minus two ninths, which solves the correct line. It gives two t, not four t. The slipped line is a different equation.

@chapter Try it
@words text="y′ = 4 − 2y" sub="standard form? p? q? homogeneous?"
Your turn. Put y prime equals four minus two y in standard form. Read off p and q, with their signs, and say whether it's homogeneous or forced.

@end text="Divide first"
You can type an equation and see p and q read off, on Learn. That's learn dot get er done dot I O.

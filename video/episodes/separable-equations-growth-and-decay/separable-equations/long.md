---
format: long
lesson: separable-equations-growth-and-decay/separable-equations
title: Separable equations: y with y prime, t on the other side
thumb: Keep y′ with the y
---

@chapter The question
@title text="Separable Equations" sub="Separable Equations, Growth and Decay" art=thumb
Some differential equations need only two antiderivatives and one constant. The trick is spotting them, and knowing exactly what separating means.

@art family-of-curves
A first order equation tells you the slope of y at every point, and its solutions form a whole family of curves. You want the one curve that passes through your starting point.

@chapter The separable form
@math heading="Separable" items="g(y)·y′ = h(t)@g of y times y prime"
An equation is separable when you can write it as g of y times y prime equals h of t. On the left, a function of y only, multiplying y prime. On the right, a function of t alone.

@art two-sides
Think of it as sorting. Everything with a y goes on one side, and y prime travels with the y it multiplies. Everything with a t goes on the other.

@chapter The four moves
@list heading="The four moves" items="Write g(y)·y′ = h(t)@First|Find G and H@Second|Write G(y) = H(t) + C@Third|Use the initial value to fix C@Fourth"
First, write the equation in that separated form. If you can't, stop, because this method doesn't apply. Second, find G whose derivative is g, and H whose derivative is h. Third, write G of y equals H of t plus C. Fourth, put in the initial value and solve for C.

@art offset-curves
Why only one constant? Each side could carry its own, but their difference is a single number, so one C is enough.

@math heading="One constant" items="C = G(y₀) − H(t₀)@then C is"
If the solution passes through t nought, y nought, then C is G of y nought minus H of t nought.

@chapter A worked example
@math heading="y′ = t/y,  y(0) = 2" items="y·y′ = t@Multiply both sides by y;;G(y) = y²/2,  H(t) = t²/2@The antiderivatives;;y²/2 = t²/2 + C@So along any solution"
Take y prime equals t over y, starting from y of zero equals two. Multiply both sides by y, and you get y times y prime equals t. The antiderivatives are y squared over two and t squared over two. So along any solution, y squared over two equals t squared over two, plus C.

@math heading="y(0) = 2" items="2²/2 = 0²/2 + C@Put in t equals zero;;C = 2@so C equals two;;y² = t² + 4@y squared equals"
Put in t equals zero and y equals two. Two squared over two is two, and zero squared over two is zero, so C equals two. Doubling through, y squared equals t squared plus four.

@art pinned-curve
Before you fixed C, the answer was a whole family of curves. After, it's one, the curve through zero, two. It's still a relation between y and t, not yet a formula for y. That comes in a later lesson.

@chapter Two more shapes
@math heading="y′ = t·y²,  y(0) = 1" items="(1/y²)·y′ = t@It separates;;G(y) = −1/y,  H(t) = t²/2@G is minus one over y;;C = −1/1 − 0 = −1@so C is minus one;;−1/y = t²/2 − 1@The relation is"
Now y prime equals t times y squared, with y of zero equal to one. It separates as one over y squared, times y prime, equals t. G is minus one over y, and H is t squared over two, so C is minus one. The relation is minus one over y equals t squared over two, minus one.

@art lost-zero
But dividing by y squared was only allowed where y isn't zero. The constant function y equals zero also solves this equation, and the separated form can never produce it. Starting at one, you never go near it. But the method can't hand back a solution it divided away.

@math heading="3y²·y′ = 2t + 1,  y(0) = 1" items="G(y) = y³,  H(t) = t² + t@G is y cubed;;C = 1³ − 0 = 1@C is one;;y³ = t² + t + 1@so y cubed equals"
A polynomial in y works too. Three y squared times y prime equals two t plus one. G is y cubed, and H is t squared plus t. With y of zero equal to one, C is one, so y cubed equals t squared plus t plus one.

@chapter What it can't do
@art tangled-sum
Not everything separates. y prime equals t plus y has no separated form. The right side is a sum, and a sum like that can't be written as a function of t over a function of y. y prime equals t squared plus y squared fails for the same reason. A later course solves these another way.

@chapter Where people slip
@list heading="Common slips" items="Moving y across, leaving y′ behind@The first|Getting C with the subtraction reversed@The second|Forgetting where g(y) is zero@The third"
The first slip is moving the y across and leaving y prime behind. The second is getting C with the subtraction the wrong way round, which flips its sign. Put the starting point back in, and it catches this every time. The third is dividing by g of y and forgetting where it's zero.

@math heading="The first slip, from y′ = t/y" items="y² = t²/2 + 2y@it gives;;y′ = t/(2y − 2)@slope is;;✓  y·y′ = t@keeps y prime"
That first one is sneaky. With y of zero equal to two it gives y squared equals t squared over two, plus two y. Its slope is t over two y minus two, not t over y. Both slopes are zero at the start, so it passes a check there and fails one step later. The correct move keeps y prime with the y.

@chapter Try it
@words text="3y²·y′ = 2t + 1,  y(0) = 1" sub="target: y³ = t² + t + 1"
Your turn. Take three y squared times y prime equals two t plus one, with y of zero equal to one. Find G and H, fix the constant, and check you reach y cubed equals t squared plus t plus one.

@end text="Separate it, then pin the constant"
You can run each example and watch the four tiles fill in, on Learn. That's learn dot get er done dot I O.

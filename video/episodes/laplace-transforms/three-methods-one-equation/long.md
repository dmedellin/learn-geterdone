---
format: long
lesson: laplace-transforms/three-methods-one-equation
title: Three methods, one equation, one answer
thumb: Different routes, same function
---

@chapter The question
@title text="Three Methods, One Equation" sub="Laplace Transforms" art=thumb
You now have more than one way to solve a forced equation. Undetermined coefficients. The Laplace transform. And, for first order, the integrating factor. Do they really give the same answer? And if they do, which should you reach for?

@chapter Route one: guess and fit
@math heading="y″ + 3y′ + 2y = 4,  from rest" items="y_p = K:  2K = 4,  y_p = 2@guesses a constant;;y = 2 + C₁·e^(−t) + C₂·e^(−2t)@general solution;;C₁ + C₂ = −2,   −C₁ − 2C₂ = 0@two equations;;C₂ = 2,   C₁ = −4@C two is two"
Take y double prime plus three y prime plus two y equals four, from rest. The forcing is constant, so undetermined coefficients guesses a constant, K. Then two K equals four, and the particular solution is two. Add the homogeneous part, with roots minus one and minus two, to get the general solution. Fitting the constants takes two equations. C one plus C two is minus two, and minus C one minus two C two is zero. So C two is two and C one is minus four.

@art guess-then-fit
That route goes through a general solution, and the constants are found last, from a two by two system.

@chapter Route two: transform
@math heading="(s² + 3s + 2)·Y = 4/s" items="Y = 4/(s·(s + 1)·(s + 2))@Y is four over;;= 2/s − 4/(s + 1) + 2/(s + 2)@two over s;;y = 2 − 4e^(−t) + 2e^(−2t)@the table backwards"
Now transform. s squared plus three s plus two, times Y, equals four over s. So Y is four over s times s plus one times s plus two. Substituting the roots gives two over s, minus four over s plus one, plus two over s plus two. Read the table backwards, and y is two minus four e to the minus t, plus two e to the minus two t.

@art two-routes-meet
The same function from two directions. Here the starting values went in at the first line, and the constants came out as the coefficients of the fractions.

@chapter Why they must agree
@math heading="d = y₁ − y₂" items="d″ + 3d′ + 2d = 0@the four cancels;;d(0) = 0,   d′(0) = 0@starts at zero;;C₁ + C₂ = 0,   −C₁ − 2C₂ = 0  ⇒  d = 0@so d is zero"
Suppose two functions both solve this problem. Their difference, d, satisfies the homogeneous equation, because the four cancels. And d starts at zero with slope zero. Fitting its constants gives C one plus C two is zero, and minus C one minus two C two is zero. Both are zero, so d is zero.

@art one-solution
An initial value problem has one solution. So the methods aren't three theories that might disagree. They're one theory, run in different orders.

@chapter Route three: first order
@math heading="y′ + 2y = e^t,   y(0) = 0" items="μ = e^(2t):  (e^(2t)·y)′ = e^(3t)@integrating factor;;e^(2t)·y = e^(3t)/3 + C,   C = −1/3@a third;;y = e^t/3 − e^(−2t)/3@e to the t over three"
For a first-order equation there's a third route. Take y prime plus two y equals e to the t, from zero. With the integrating factor e to the two t, the left side becomes the derivative of e to the two t times y, and the right side is e to the three t. Integrate, and the start gives C as minus a third. So y is e to the t over three, minus e to the minus two t over three.

@art three-routes
The transform gives one over s minus one times s plus two, with coefficients a third and minus a third. Undetermined coefficients guesses A e to the t, and three A equals one. All three return the same function.

@chapter When to choose which
@art route-choice
So which should you reach for? Each method has a kind of problem it's best at.

@list heading="Choosing a route" items="Guessable forcing, long-run response: undetermined coefficients@shortest when the forcing|Switched forcing or non-zero starts: the transform@The transform is shortest|First order: the integrating factor@needs a first-order|Always: substitute@Substitution"
Undetermined coefficients is shortest when the forcing is one of the shapes it guesses, and when you want the long-run response itself. The transform is shortest when the forcing switches on or off, or the starting values aren't zero. The integrating factor needs a first-order equation, and then works for any forcing you can integrate. Substitution isn't a method, it's the referee.

@chapter Where people slip
@list heading="Common slips" items="Believing the methods can disagree@The first|Fitting the start to y_p alone@The second|Transforming 4 as 4, not 4/s@And the third"
The first slip is believing the methods can disagree. If one route gives two minus two e to the minus t plus two e to the minus two t, check: it starts at two, not zero. It's wrong on its face. The second is applying the starting values to the particular solution, or to the homogeneous part, alone. They belong to the whole sum. And the third is transforming the constant four as four, instead of four over s.

@art residual-referee
That last one gives four e to the minus t minus four e to the minus two t. It starts at zero, but its slope at zero is four. Whatever route you take, finish by putting the answer into the equation and the starting values.

@chapter Try it
@words text="y″ + 4y = 3cos(t),  from rest" sub="y = cos(t) − cos(2t)"
Your turn. Solve this one both ways. Guess A cos t for the particular solution and fit the constants. Then transform, split three s over s squared plus one times s squared plus four, and invert. Both should give cos t minus cos two t.

@end text="Solve it twice, then check"
You can run each route and see the residual on Learn. That's learn dot get er done dot I O.

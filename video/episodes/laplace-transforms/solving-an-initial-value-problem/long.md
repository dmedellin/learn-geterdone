---
format: long
lesson: laplace-transforms/solving-an-initial-value-problem
title: Solving an initial value problem with the Laplace transform
thumb: No constants left to fit
---

@chapter The question
@title text="Solving an Initial Value Problem" sub="Laplace Transforms" art=thumb
You've solved equations like y double prime plus three y prime plus two y equals zero before, by fitting two constants at the end. The Laplace transform does it differently. The starting values go in at the very first line, and nothing is left to fit.

@chapter Four moves
@list heading="The method" items="Transform both sides@transform both sides|Solve for Y@solve for Y|Partial fractions@partial fractions|Read the table backwards@read the table"
There are four moves. First, transform both sides with the derivative rules. Second, solve for Y, which is just algebra. Third, take Y apart by partial fractions. And fourth, read the table backwards to get y of t.

@math heading="a·y″ + b·y′ + c·y = q" items="(a·s² + b·s + c)·Y = a·(s·y(0) + y′(0)) + b·y(0) + ℒ[q]@collect"
Transform each term and collect everything that multiplies Y. On the left you get a s squared plus b s plus c, times Y. That's the characteristic polynomial, with s in place of r. On the right sit the starting values, and the transform of the forcing.

@chapter A first-order case
@math heading="y′ + 2y = 6,   y(0) = 0" items="(s + 2)·Y = 6/s@six over s;;Y = 6/(s·(s + 2)) = A/s + B/(s + 2)@A over s;;A = 6/2 = 3,   B = 6/(−2) = −3@A is three;;y = 3 − 3e^(−2t)@three minus three"
Solve y prime plus two y equals six, with y of zero equal to zero. The transform of six is six over s, so s plus two, times Y, equals six over s. Split Y into A over s plus B over s plus two. At s equals zero the other factor is two, so A is three. At s equals minus two, B is minus three. So y is three minus three e to the minus two t.

@art settles-at-three
It starts at zero and settles at three, exactly as the starting value said. No constant was fitted.

@chapter A second-order case
@math heading="y″ + 3y′ + 2y = 0,   y(0) = 1,  y′(0) = 0" items="(s²Y − s) + 3(sY − 1) + 2Y = 0@s squared Y minus s;;(s² + 3s + 2)·Y = s + 3@s plus three;;Y = (s + 3)/((s + 1)(s + 2))@Y is s plus three"
Now y double prime plus three y prime plus two y equals zero, starting at one with slope zero. Transform: s squared Y minus s, plus three times s Y minus one, plus two Y, equals zero. Collect, and s squared plus three s plus two, times Y, equals s plus three. So Y is s plus three over s plus one times s plus two.

@math heading="cover-up" items="A = (−1 + 3)/(−1 + 2) = 2@set s equal to minus one;;B = (−2 + 3)/(−2 + 1) = −1@minus two;;y = 2e^(−t) − e^(−2t)@two e to the minus t"
To find A, multiply by s plus one and set s equal to minus one. That's two over one, two. For B, set s to minus two: one over minus one, minus one. Read the table backwards, and y is two e to the minus t, minus e to the minus two t.

@art two-decays
Check it. y of zero is two minus one, one. y prime of zero is minus two plus two, zero. And in the equation, both exponentials' coefficients cancel to zero. It's the same answer the characteristic equation gave, without the two by two system for the constants.

@chapter When it doesn't factor
@math heading="y″ + 2y′ + 5y = 0,   y(0) = 0,  y′(0) = 2" items="(s² + 2s + 5)·Y = 2@just two;;s² + 2s + 5 = (s + 1)² + 4@Complete the square;;Y = 2/((s + 1)² + 4)@two over;;y = e^(−t)·sin(2t)@sine of two t"
Here s squared plus two s plus five has no real roots, and the right side is just two. Complete the square: it's s plus one, squared, plus four. So Y is two over that. The sine entry is b over s squared plus b squared, and replacing s by s plus one multiplies the signal by e to the minus t. So y is e to the minus t times sine of two t.

@art decaying-sine
The shift in s is the decay in t. The peaks shrink inside an envelope of e to the minus t.

@art plain-sine
Drop that shift, and you'd read the fraction as plain sine of two t, which keeps the frequency and loses the decay.

@chapter Where people slip
@list heading="Common slips" items="Applying the initial values after inverting@The first|Dropping the b·y(0) term@The second|Inverting the shifted sine without e^(−t)@And the third"
The first slip is applying the initial values after inverting, out of habit. Leave them out and the second-order example gives Y equals zero, and y equals zero, which doesn't start at one. The second is dropping the b times y of zero term. Without the three, y prime of zero comes out as minus three. And the third is inverting the shifted sine without its exponential.

@art residual-check
Every time, finish by substitution. Put the answer into the equation and its starting values. The residual must be zero, and the answer must start where the problem says.

@chapter Try it
@art four-moves
Your turn. Solve this first-order problem by transform yourself. Transform both sides, solve for Y, split it into partial fractions, and read the table backwards. Then check that your answer starts at zero.

@end text="Solve by transform, step by step"
You can run the whole chain in exact fractions, and check the residual, on Learn. That's learn dot get er done dot I O.

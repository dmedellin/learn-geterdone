---
format: long
lesson: laplace-transforms/the-transfer-function-and-its-poles
title: The transfer function: read stability from the poles
thumb: Left of zero, it dies out
---

@chapter The question
@title text="The Transfer Function and Its Poles" sub="Laplace Transforms" art=thumb
Push a system from rest. Will its response settle down, oscillate, or blow up? You can tell without solving anything, just by looking at where one fraction's denominator is zero.

@chapter From rest
@math heading="a·y″ + b·y′ + c·y = q,   y(0) = y′(0) = 0" items="(a·s² + b·s + c)·Y = ℒ[q]@the starting terms vanish;;Y = H(s)·ℒ[q]@H of s;;H(s) = 1/(a·s² + b·s + c)@the transfer function"
Start from rest, so both starting values are zero. Transform the equation, and the starting terms vanish. What's left is one product: Y is H of s times the transform of the forcing. H of s, one over a s squared plus b s plus c, is the transfer function.

@art system-and-input
H is built from the left side alone, so it describes the system. The second factor describes what you do to it. The transform has separated the two.

@chapter Poles
@words text="poles of H = characteristic roots"
The poles of H are the values of s where its denominator is zero. That denominator is the characteristic polynomial with s in place of r. So the poles are exactly the characteristic roots you've already met. Nothing new to compute.

@art pole-terms
Each pole becomes one term of the solution. A real pole p gives a term built on e to the p t. A complex pair, alpha plus or minus beta i, gives e to the alpha t times a cosine or a sine. A repeated pole adds a factor of t.

@chapter A worked example
@math heading="y″ + 3y′ + 2y = 1,  from rest" items="Y = 1/(s·(s + 1)·(s + 2))@one over s;;= (1/2)/s − 1/(s + 1) + (1/2)/(s + 2)@a half over s;;y = 1/2 − e^(−t) + (1/2)·e^(−2t)@y is a half"
Take y double prime plus three y prime plus two y equals one, from rest. The forcing transforms to one over s, so Y is one over s times s plus one times s plus two. Substitute the roots to get a half over s, minus one over s plus one, plus a half over s plus two. So y is a half, minus e to the minus t, plus a half e to the minus two t.

@art settles-half
The poles of H, minus one and minus two, became the two exponentials that die out. The pole at zero came from the forcing, not the equation. It's the constant a half that the solution settles at. The poles of H decide whether the transient dies. The forcing's poles decide what it settles into.

@chapter The stability criterion
@words text="every pole of H has real part < 0" sub="⇔ every pole term dies out"
Here's the criterion. Every term built on a pole of H dies out, whatever the forcing and starting values, if and only if every pole of H has negative real part. One pole with positive real part gives a term that grows without bound.

@art pole-plane
Why? e to the p t shrinks to zero when p is negative, and grows without bound when p is positive. Sine and cosine only stay between minus one and one. So the real part decides, and the imaginary part just sets the frequency.

@chapter A complex pair, and a pole on the right
@math heading="y″ + 2y′ + 5y = 5,  from rest" items="s² + 2s + 5 = (s + 1)² + 4@s plus one;;poles −1 ± 2i@minus one plus or minus two i;;y = 1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)@oscillates"
For y double prime plus two y prime plus five y equals five, the denominator is s plus one, squared, plus four. The poles are minus one plus or minus two i. Real part minus one, so the transient dies, with frequency two. The solution oscillates about one, inside an envelope shrinking like e to the minus t.

@math heading="y″ − y′ − 2y = 2,  from rest" items="s² − s − 2 = (s − 2)(s + 1)@s minus two;;y = −1 + (1/3)·e^(2t) + (2/3)·e^(−t)@minus one plus;;t = 5:  (1/3)·e^(10) ≈ 7342.16@about seven thousand"
Now y double prime minus y prime minus two y equals two. The denominator is s minus two times s plus one, so there's a pole at two. The solution is minus one, plus a third e to the two t, plus two thirds e to the minus t. At t equals five, the growing term is about seven thousand three hundred and forty two.

@art blow-up
It starts at zero, as it must from rest, and then the exponential takes over.

@chapter Where people slip
@list heading="Common slips" items="A right pole only makes it bigger@The first|Reading stability from the forcing's pole@The second|Calling −1 ± 2i unstable@And the third"
The first slip is thinking a pole on the right just makes the response larger. Every extra unit of time multiplies that term by e squared, about seven point three nine. There's no bound at all. The second is reading stability from the forcing's pole at zero. And the third is calling minus one plus or minus two i unstable because of the i. The i gives oscillation, not growth.

@art imaginary-axis
One edge case. A pole exactly on the imaginary axis, like plus or minus two i for y double prime plus four y equals zero, has real part zero. Its term neither shrinks nor grows, and the strict criterion doesn't call that stable.

@chapter Try it
@words text="y″ + 3y′ + 2y = 1" sub="poles of H, then the long run"
Your turn. Write the transfer function, find its poles, and read their real parts. Then transform the forcing, decompose and invert, and check that each term behaves the way its pole predicted.

@end text="Move the poles, watch the response"
You can read the poles and watch the response settle or grow on Learn. That's learn dot get er done dot I O.

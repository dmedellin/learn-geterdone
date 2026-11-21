---
format: long
lesson: first-order-linear-equations/exponential-and-sinusoidal-forcing
title: Exponential and sinusoidal forcing, and the factor of t
thumb: A cosine needs a sine
---

@chapter The question
@title text="Exponential and Sinusoidal Forcing" sub="First-Order Linear Equations" art=thumb
Polynomials aren't the only forcing. What do you guess when the right side is an exponential, or a cosine? Each has its own shape, and there's one trap to watch for.

@chapter Exponential forcing
@math heading="y′ + 2y = e^t" items="try y_p = A·e^t@Try;;A·e^t + 2A·e^t = 3A·e^t@the left side;;3A = 1,   y_p = (1/3)·e^t@a third"
Start with y prime plus two y equals e to the t. Try A e to the t. Its derivative is A e to the t, so the left side is three A e to the t. Matching gives three A equals one, so y p is a third of e to the t.

@art comes-back
An exponential comes back as itself. The derivative of e to the b t is b times e to the b t. So in general, for forcing e to the b t, y p is e to the b t over a plus b, whenever a plus b isn't zero. The sum, not the difference.

@chapter A cosine needs a sine
@art sine-cosine-pair
Two facts are used here and stated rather than derived. The rate of sine is cosine, and the rate of cosine is minus sine. So sine and cosine come back as each other.

@math heading="y′ + 2y = cos(t),  try A·cos(t)" items="−A·sin(t) + 2A·cos(t)@minus A sine;;sine: −A = 0,   cosine: 2A = 1   ✗@contradict"
For y prime plus two y equals cosine t, try A cosine t alone. You get minus A sine t plus two A cosine t. The sine terms need minus A to be zero, and the cosine terms need two A to be one. Those contradict each other.

@math heading="Try A·cos(t) + B·sin(t)" items="(2A + B)·cos(t) + (2B − A)·sin(t)@collect;;2A + B = 1@cosine terms;;2B − A = 0@sine terms;;B = 1/5,   A = 2/5@B is a fifth"
So the guess needs both, A cosine plus B sine. Collect, and you get two A plus B times cosine, plus two B minus A times sine. The cosine terms give two A plus B equals one. The sine terms give two B minus A equals zero. So A is two B, five B is one, B is a fifth and A is two fifths.

@art lagging-wave
So y p is two fifths cosine plus a fifth sine, even though the forcing had no sine at all. The sine appears because the unknown's rate depends on its own value, so the response lags the forcing.

@math heading="In general,  y′ + a·y = cos(ωt)" items="A = a/(a² + ω²)@A is a over;;B = ω/(a² + ω²)@B is omega"
In general, A is a over a squared plus omega squared, and B is omega over the same. With a equals two and omega one, that's two fifths and one fifth. The denominator is positive whenever a isn't zero, so a sinusoid never collapses the guess.

@chapter When the forcing is a solution
@math heading="y′ + 2y = e^(−2t)" items="homogeneous: C·e^(−2t)@homogeneous solutions;;A·e^(−2t):   −2A·e^(−2t) + 2A·e^(−2t) = 0@The guess"
Now take y prime plus two y equals e to the minus two t. The homogeneous solutions are C e to the minus two t, so the forcing is one of them. The guess A e to the minus two t gives minus two A plus two A, which is zero.

@art annihilated
The left side wipes the guess out, and no A can turn zero into the forcing. The formula fails too, since a plus b is two minus two, zero.

@math heading="Multiply by t" items="y_p = A·t·e^(−2t)@factor of t;;y_p′ + 2y_p = A·e^(−2t)@derivative leaves;;A = 1,   y_p = t·e^(−2t)@A is one"
The fix is one more factor of t. Try A t e to the minus two t. Its derivative leaves behind A e to the minus two t, which the left side doesn't cancel. So A is one, and y p is t e to the minus two t.

@art repair-not-growth
That factor of t is a repair, not growth. The general solution is t plus C, times e to the minus two t. With y of zero equal to one, C is one, and t plus one times e to the minus two t still goes to zero. The exponential falls faster than t rises.

@chapter Three shapes, one test
@art three-guesses
Put together, each forcing has a guess with its own shape, and the left side sends that shape back.

@list heading="Guess by forcing" items="e^(bt):   A·e^(bt)@an exponential|cos(ωt):   A·cos(ωt) + B·sin(ωt)@a sinusoid|forcing in C·e^(−a·t)?   multiply by t@one test"
So there are three shapes of guess. For an exponential, A e to the b t. For a sinusoid, A cosine plus B sine, same frequency. And one test before substituting: does the forcing appear in the homogeneous solution? If it does, multiply by t.

@chapter Where people slip
@list heading="Common slips" items="Guessing A·cos(t) alone@The first|Using 1/(a − b)@The second|Concluding there's no solution@The third"
The first slip is guessing A cosine alone, which leaves a sine nothing can match. The second is using one over a minus b. For e to the t, that gives one, and substituting gives three times the forcing. The third is concluding there's no solution when the guess gives zero. That says the guess was wrong, not the equation.

@chapter Try it
@words text="y′ + 2y = cos(t)" sub="check: 2·(2/5) + 1/5 = 1"
Your turn. Substitute two fifths cosine plus a fifth sine back into y prime plus two y. Check that the cosine terms give one and the sine terms give zero.

@end text="Match the shape of the forcing"
You can try exponential, sinusoidal and resonant forcing, on Learn. That's learn dot get er done dot I O.

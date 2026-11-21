---
format: long
lesson: laplace-transforms/the-laplace-transform
title: The Laplace transform: from a signal to a fraction in s
thumb: Weight it, add it up
---

@chapter The question
@title text="The Laplace Transform" sub="Laplace Transforms" art=thumb
What if you could turn a differential equation into a fraction problem? That's what the Laplace transform is for. But first, what is it? It's a recipe that turns a function of time into a function of a new variable, s.

@chapter The recipe
@math heading="The Laplace transform" items="ℒf = ∫₀^∞ e^(−st)·f(t) dt@the transform of f;;= lim of ∫₀ᵀ as T grows@from zero to T"
Here it is. The transform of f is the integral from zero to infinity of e to the minus s t, times f of t. And the integral to infinity means the integrals from zero to T, as T grows.

@art weighted-signal
In words: fix a value of s. Multiply the signal by the weight e to the minus s t, which shrinks faster the larger s is. Add up the area under the product from zero onward. That's one number. Do it for every s, and you get a function, F of s.

@chapter The simplest signal
@math heading="f = 1" items="∫₀ᵀ e^(−st) dt = (1 − e^(−sT))/s@one minus e;;s = 1:  1 − e^(−T)@At s equals one;;T = 1, 2, 5:  ≈ 0.632121,  ≈ 0.864665,  ≈ 0.993262@nought point six three"
Take f equals one. The antiderivative of e to the minus s t is minus e to the minus s t, over s. So the integral from zero to T is one minus e to the minus s T, all over s. At s equals one, that's one minus e to the minus T. For T of one, two and five it's about nought point six three, nought point eight six, and nought point nine nine.

@art area-closing-in
Those numbers are closing in on one. For positive s, the term e to the minus s T shrinks toward zero as T grows, so the integral approaches one over s.

@chapter The first entries
@math heading="for s > a" items="e^(−st)·e^(at) = e^(−(s − a)t)@add the exponents;;∫₀ᵀ = (1 − e^(−(s − a)T))/(s − a)@from zero to T;;ℒ[e^(at)] = 1/(s − a)@one over s minus a;;a = 0:  ℒ[1] = 1/s@one over s"
Now the exponential, e to the a t. Multiply by the weight and add the exponents, to get e to the minus s minus a, t. Integrate from zero to T. When s is bigger than a, the exponential term dies away, and you're left with one over s minus a. Put a equal to zero and you get back the transform of one, one over s.

@art growing-vs-weight
Take e to the two t. The signal grows, but at s equals three the weight shrinks faster, and the product is e to the minus t. The transform, one over s minus two, is one at s equals three, which is exactly where those integrals were heading.

@chapter The floor under s
@words text="1/(s − 2) at s = 1:  −1 ✗"
But try s equals one in that same formula, and you get minus one. That's an impossible area for a positive function. At s equals one the weighted signal is e to the t, which grows, and the integral is infinite.

@art floor-line
So every entry has a floor. One over s minus two is the transform only for s bigger than two. And look at the denominators: each one is zero at exactly that floor. Those values of s are called the poles, and they'll matter more than anything else in this course.

@art ramp
One more entry, the ramp, f equals t. Its transform is stated in this lesson, not computed, because the integral needs a rule this course doesn't develop.

@math heading="the ramp, f = t" items="ℒ[t] = 1/s²@one over s squared;;s = 1,  T = 1, 2, 5:  ≈ 0.264241,  ≈ 0.593994,  ≈ 0.959572@nought point two six"
The transform of t is one over s squared. At s equals one the truncated integrals are about nought point two six, nought point five nine, and nought point nine six, closing in on one.

@chapter Where people slip
@list heading="Common slips" items="Treating the transform as a number@The first|Using 1/(s − a) below the floor@The second|Flipping the sign: 1/(s + 2)@And the third"
The first slip is treating the transform as a number. One over s is one at s equals one, a half at two, and a quarter at four. It's a function. The second is using one over s minus a below its floor. And the third is flipping the sign, writing one over s plus two for e to the two t. At s equals three that gives a fifth, not one.

@art function-of-s
That first habit matters most. The equations in the next lessons are equations between functions of s. They're solved with algebra only because a function of s can be added, multiplied and divided like a fraction.

@chapter Try it
@words text="ℒ[e^(2t)]" sub="combine, integrate to T, find the floor"
Your turn. Transform e to the two t from the definition. Combine the exponentials, integrate from zero to T, let T grow, and say where the floor is. Then check your fraction at s equals three.

@end text="Watch the integrals close in"
You can type a signal and watch its integrals close in on the transform on Learn. That's learn dot get er done dot I O.

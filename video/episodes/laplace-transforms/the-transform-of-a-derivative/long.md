---
format: long
lesson: laplace-transforms/the-transform-of-a-derivative
title: The Laplace transform of a derivative, and where y of 0 comes from
thumb: Times s, minus the start
---

@chapter The question
@title text="The Transform of a Derivative" sub="Laplace Transforms" art=thumb
Differential equations are full of derivatives. So for the Laplace transform to help, you need to know what it does to one. The answer is surprisingly tidy, and it carries the starting value along for free.

@words text="Y = ℒ[y]   F = ℒ[f]"
A quick convention first. A capital letter stands for the transform of the lower-case one. So capital Y is the transform of y, and capital F is the transform of f.

@chapter The rule
@math heading="First derivative" items="ℒ[y′] = s·Y − y(0)@s times Y"
Here's the rule. The transform of y prime is s times Y, minus y of zero.

@art derivative-to-times
In t, the operation is a derivative. In s, it's a multiplication and a subtraction. That exchange is the whole reason the transform is useful for differential equations.

@chapter Why it's true
@art endpoint-values
The proof uses two things you already have: the product rule, and the fundamental theorem, which turns the integral of a derivative into a difference of its values at the two ends.

@math heading="product rule" items="(e^(−st)·y)′ = −s·e^(−st)·y + e^(−st)·y′@product rule;;e^(−sT)·y(T) − y(0)  =  −s·∫ e^(−st)·y  +  ∫ e^(−st)·y′@Integrate both sides;;T grows:  −y(0) = −s·Y + ℒ[y′]@Let T grow"
Start with the product rule. The derivative of e to the minus s t times y is minus s e to the minus s t y, plus e to the minus s t y prime. Integrate both sides from zero to T. The left side becomes e to the minus s T y of T, minus y of zero. Let T grow, the first term goes to zero, and you're left with minus y of zero equals minus s Y plus the transform of y prime.

@art lower-limit
So the starting value isn't added by hand afterwards. It comes from the lower limit of the integral, at t equals zero. It's part of the rule, and any equation you transform with the rule already contains it.

@chapter Twice over
@math heading="Second derivative" items="ℒ[y″] = s·ℒ[y′] − y′(0)@to y prime;;= s·(s·Y − y(0)) − y′(0)@replace;;= s²·Y − s·y(0) − y′(0)@s squared Y"
For a second derivative, apply the rule to y prime. That's s times the transform of y prime, minus y prime of zero. Then replace the transform of y prime by s Y minus y of zero. Multiply out, and you get s squared Y, minus s times y of zero, minus y prime of zero.

@art two-corrections
So a second derivative brings two starting values, and they enter differently. y of zero is multiplied by s. y prime of zero is not.

@chapter Check it on a signal
@math heading="y = e^(2t),   y(0) = 1" items="ℒ[y′] = ℒ[2e^(2t)] = 2/(s − 2)@two over s minus two;;s·Y − y(0) = s/(s − 2) − 1@s over s minus two;;= (s − (s − 2))/(s − 2) = 2/(s − 2)  ✓@common denominator"
Take y equals e to the two t. Its derivative is two e to the two t, which transforms to two over s minus two. Now the rule. s Y minus y of zero is s over s minus two, minus one. Over a common denominator, that's s minus s minus two, over s minus two, which is two over s minus two. They agree.

@art one-too-large
That subtraction of one is what makes it match. Without it, the right side is s over s minus two, which is exactly one too large, at every s.

@chapter The invisible slip
@math heading="y = t²,   y(0) = 0" items="ℒ[y′] = ℒ[2t] = 2/s²@two over s squared;;s·Y − 0 = s·(2/s³) = 2/s²  ✓@s times two"
Now try y equals t squared. The derivative is two t, which transforms to two over s squared. And s times two over s cubed, minus zero, is also two over s squared. Equal again.

@art starts-at-zero
But here the starting value is zero, and the same goes for sine of t. On signals like these, forgetting the correction changes nothing. That's why the slip survives. It only shows when the start isn't zero, and then it's wrong by exactly that value.

@chapter Where people slip
@list heading="Common slips" items="Writing ℒ[y′] = s·Y@The first|Writing s·(Y − y(0))@The second|One correction for y″@And the third"
The first slip is forgetting y of zero and writing just s Y. The second is subtracting y of zero from Y before multiplying by s. For e to the two t, that gives something that isn't two over s minus two. And the third is giving the second derivative only one correction, or dropping the factor of s on y of zero. Applying the first rule twice is the safe way.

@chapter Try it
@words text="y = e^(2t)" sub="ℒ[y′] two ways"
Your turn. Rebuild the check yourself. Transform e to the two t and its derivative from the table, form s Y minus y of zero, and compare. Then drop the correction and see what's left over.

@end text="Check the rule on any signal"
You can compare both sides of the rule on your own signals on Learn. That's learn dot get er done dot I O.

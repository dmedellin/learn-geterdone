---
format: long
lesson: second-order-linear-equations/the-second-order-equation
title: y'' + y = 0: checking a second-order solution exactly
thumb: Zero for every t
---

@chapter The equation
@title text="The Second-Order Equation" sub="Second-Order Linear Equations" art=thumb
A second-order equation mentions the rate of the rate of the unknown. The one this lesson works with is y double prime plus y equals zero.

@art position-on-line
Read y as the position of something moving along a line. Then y prime is its velocity and y double prime is its acceleration. The equation says the acceleration is always minus the position. The further out it goes, the harder it's pulled back.

@list heading="Second-order linear" items="Highest rate is y″@its highest rate|y, y′ and y″ each alone, to the first power@each appear alone"
It's second order because its highest rate is y double prime. It's linear because y, y prime and y double prime each appear alone and to the first power.

@chapter The residual
@words text="residual = y″ + y" sub="substitute the candidate and its rates, then simplify"
How do you check a candidate? Move everything to the left, substitute the candidate and its two rates, and simplify. What's left is the residual. A candidate is a solution exactly when the residual is zero for every t.

@math heading="y = cos t" items="y = cos t@try cosine;;y′ = −sin t@its rate is minus sine;;y″ = −cos t@its second rate;;y″ + y = −cos t + cos t = 0@add them"
Try cosine. Its rate is minus sine, and its second rate is minus cosine. Now add them: minus cosine of t plus cosine of t is zero.

@art residual-zero
That cancellation doesn't depend on t at all, so the residual is zero for every t. The lab does exactly this with symbolic rates. It never plugs in a number to decide. And sine works the same way, since sine double prime is minus sine.

@chapter Combinations
@math heading="C·y₁ + D·y₂" items="(C·y₁ + D·y₂)″ = C·y₁″ + D·y₂″@the rate of a sum;;= C·(y₁″ + y₁) + D·(y₂″ + y₂)@regroup;;= C·0 + D·0 = 0@times zero"
If y one and y two are solutions, so is C times y one plus D times y two. The rate of a sum is the sum of the rates, and constants come out. Regroup, and you get C times zero plus D times zero, which is zero.

@words text="C·cos t + D·sin t" sub="a family with two free constants"
Only the form of the equation was used. So every combination of cosine and sine solves it, a whole family with two free constants.

@chapter Almost a solution
@art growing-wave
Now a trap. Try y equals t times cosine of t. Plotted, it's a wave that looks a lot like cosine, with its amplitude growing. Your eye can't tell whether it solves the equation.

@math heading="y = t·cos t" items="y′ = cos t − t·sin t@the product rule;;y″ = −2·sin t − t·cos t@and y double prime;;y″ + y = −2·sin t@So the residual"
The product rule gives y prime equals cosine of t minus t sine of t, and y double prime equals minus two sine of t minus t cosine of t. So the residual is minus two sine of t.

@art residual-crossings
That's zero at t equals zero, and at every multiple of pi. But at t equals one it's about minus one point six eight two nine four. Zero at some places isn't zero for every t, so the lab's verdict is not a solution.

@chapter Two starting values
@art same-start-different-motion
Here's why the two constants matter. For the family C cosine t plus D sine t, the value at zero is C. Fix y of zero equals one, and D is still free. Cosine t, cosine t plus sine t, and cosine t minus five sine t all start at one, and they're different motions.

@math heading="Pick C and D" items="y(0) = C@the value at zero is C;;y′(0) = D@the rate at zero is D;;y(0) = 1, y′(0) = −2  ⟹  C = 1, D = −2@a starting value of one"
So the value at zero is C, since cosine of zero is one and sine of zero is zero. The rate is minus C sine t plus D cosine t, so the rate at zero is D. The starting rate is what chooses. With a starting value of one and a starting rate of minus two, C is one and D is minus two.

@chapter Where people slip
@list heading="Common slips" items="Expecting one constant@The first|Zero at one t means solution@The second|Judging by the graph@The third"
The first slip is expecting one constant, as in a first-order equation. C cosine t alone can't start with a rate of minus two. The second is calling a candidate a solution because its residual vanishes at one t. And the third is testing a candidate by drawing it. The residual decides.

@chapter Try it
@art start-value-and-rate
Your turn. Pick a starting value and a starting rate, say y of zero equals one and y prime of zero equals minus two, and give the lab the family with two constants. Check that it prints C equals one and D equals minus two.

@end text="Substitute, read the residual"
You can substitute any candidate and read its residual exactly, on Learn. That's learn dot get er done dot I O.

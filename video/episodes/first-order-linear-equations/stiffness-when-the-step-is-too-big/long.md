---
format: long
lesson: first-order-linear-equations/stiffness-when-the-step-is-too-big
title: Stiffness: when Euler's step is too big
thumb: Small means h < 2/a
---

@chapter The question
@title text="Stiffness: When the Step Is Too Big" sub="First-Order Linear Equations" art=thumb
Take y prime equals minus five y, starting at one. The true solution, e to the minus five t, falls quickly towards zero. Does Euler's polygon fall with it? The answer depends on the step alone.

@chapter One factor
@math heading="y′ = −5y" items="yₙ₊₁ = yₙ + h·(−5·yₙ) = (1 − 5h)·yₙ@one Euler step;;yₙ = (1 − 5h)ⁿ@after n steps"
One Euler step adds h times minus five y, so it multiplies the value by one minus five h. After n steps, you've multiplied by that factor n times. Everything is carried by one exact fraction, the factor.

@art geometric-factor
The factor's sign says whether successive values change sign. Its size says whether they shrink. A geometric sequence goes to zero for every start exactly when its factor's size is less than one.

@chapter The step bound
@math heading="Forward Euler on y′ = −a·y" items="|1 − a·h| < 1@is less than one;;−1 < 1 − a·h < 1@between minus one and one;;0 < a·h < 2@subtract one;;0 < h < 2/a@so h"
In general, for y prime equals minus a y, the factor is one minus a h. Its size is less than one when it's between minus one and one. Subtract one and change signs, and a h is between zero and two. So h has to be less than two over a.

@words text="h = 2/a:  factor −1" sub="values alternate forever"
Right at h equals two over a, the factor is exactly minus one, and the values alternate for ever without shrinking. The true solution decays for every h, so this bound belongs to the method alone.

@chapter Three steps on one decay
@art step-bound
There's a second marker too. Below one over a, the factor is positive and the steps decay smoothly. Between one over a and two over a, it's negative, so they alternate in sign and still shrink. Above two over a, they alternate and grow.

@math heading="a = 5:   1/a = 1/5,   2/a = 2/5" items="h = 1/10:   factor 1/2,   y₈ = 1/256@one tenth;;h = 1/4:   factor −1/4,   y₈ = 1/65536@a quarter;;h = 1/2:   factor −3/2,   y₈ = 6561/256@one half"
For a equals five, the bound is two fifths. With one tenth, the factor is a half, and after eight steps you're at one over two hundred fifty six. With a quarter, it's minus a quarter, and you reach one over sixty five thousand five hundred thirty six. With one half, the factor is minus three halves.

@art blow-up-steps
That last one grows. After eight steps, at t equals four, the polygon holds three halves to the eighth, six thousand five hundred sixty one over two hundred fifty six, about twenty five point six. The true value is about two times ten to the minus nine. Every fraction is correct. The method has turned a decay into a growth.

@chapter Small is relative
@art fast-and-slow
A step of one half looks small, and for a slow decay like y prime equals minus y it is. The bound there is two. But the bound shrinks as a grows. So a quickly decaying part of a problem forces a small step, even after it has stopped mattering to the answer.

@words text="stiff" sub="the step is capped by the fastest decay"
That's what stiff means here. The step is capped by the fastest decay in the problem, not by the accuracy you want.

@chapter The backward step
@math heading="Backward Euler" items="yₙ₊₁ = yₙ + h·(−a·yₙ₊₁)@at the new point;;yₙ₊₁ = yₙ/(1 + a·h)@Solving;;a = 5,  h = 1/2:   factor 2/7@two sevenths"
Backward Euler evaluates the rate at the new point instead. Solving for the new value, you divide by one plus a h. For positive a and h, that denominator is bigger than one, so the factor is between zero and one at every step size. With a equals five and h equals a half, it's two sevenths. The steps decay.

@art stable-not-accurate
But stable doesn't mean accurate. The true factor over one step is e to the minus five halves, about zero point zero eight two. Two sevenths is about zero point two eight six, more than three times as large. After eight steps, the backward column is still far above the true value, but it hasn't blown up.

@words text="linear: one division" sub="nonlinear: an equation at every step"
For this linear equation, the backward step is one division. For a nonlinear right side, the new value appears on both sides inside the function, and finding it takes solving an equation at every step. That's the price of losing the bound.

@chapter Where people slip
@list heading="Common slips" items="Thinking any small step will do@The first|Treating backward Euler as accurate@The second|Taking a sign change as failure@The third"
The first slip is thinking any small step will do. Small means less than two over a, which depends on the equation. The second is treating the backward method as the accurate one. It removes the bound, not the error. The third is taking any sign change as the method failing.

@art alternating-decay
With a step of a quarter, the values alternate in sign, and they decay all the same. The failure is the factor's size passing one, at two over a, not the sign changing, at one over a. The wobble is inaccurate, but it isn't unstable.

@chapter Try it
@words text="y′ = −5y,  h = 2/5" sub="factor? what do the steps do?"
Your turn. Take the step exactly at the bound, two fifths. Work out the forward factor, write the first four values from one, and describe what they do.

@end text="Check the factor before you step"
You can change the step and watch the polygon decay, wobble or blow up, on Learn. That's learn dot get er done dot I O.

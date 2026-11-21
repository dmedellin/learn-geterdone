---
format: long
lesson: separable-equations-growth-and-decay/exponential-growth
title: Exponential growth: y′ = ky, solved and stepped
thumb: Every Euler step multiplies
---

@chapter The question
@title text="Exponential Growth" sub="Separable Equations, Growth and Decay" art=thumb
What happens when a quantity changes at a rate proportional to its own size? The bigger it gets, the faster it changes, in the same proportion. That one idea gives you exponential growth.

@art proportional-rate
In symbols, y prime equals k times y, for a constant k. When k is positive, that's growth. When k is negative, it's decay. The number k is the rate constant, and it has units of one over time.

@chapter Solving it
@math heading="y′ = k·y,  y(0) = y₀" items="(1/y)·y′ = k@one over y;;ln y = kt + C@ln y equals;;C = ln y₀@C is ln y nought;;y = y₀·e^(kt)@y nought times e"
While y is positive, the equation separates as one over y times y prime equals k. Integrating gives ln y equals k t plus C. At t equals zero, C is ln y nought. So the solution is y equals y nought times e to the k t.

@words text="rate of y₀·e^(kt) = k·y₀·e^(kt) = k·y"
Check it by differentiating. The rate of y nought times e to the k t is k times y nought times e to the k t, which is k times y. And a start of zero gives the constant solution zero, which the formula covers too.

@art growth-decay
That's a solution in closed form. It's the only thing here that isn't an exact fraction. e to the k t has no finite fraction, so the lab rounds it to six figures and marks it approximate.

@chapter What Euler's method does
@math heading="Euler on y′ = k·y" items="yₙ₊₁ = yₙ + h·(k·yₙ) = (1 + kh)·yₙ@one Euler step;;yₙ = (1 + kh)ⁿ·y₀@after n steps"
Now run Euler's method on the same equation. One Euler step adds h times the rate, and the rate is k times the value. So the new value is one plus k h, times the old one. After n steps, you've multiplied by one plus k h, n times.

@art geometric-bars
That's a geometric sequence. Each term is the previous one times a fixed ratio, one plus k h. Euler's method on a growth equation is that sequence under another name. And the ratio is a rational number, so nothing is rounded.

@chapter A worked example
@math heading="y′ = y,  y(0) = 1,  h = 1/4" items="1 + (1/4)·1 = 5/4@The first step;;5/4 + (1/4)·(5/4) = 25/16 = (5/4)²@The second;;y₄ = (5/4)⁴ = 625/256@after four steps"
Take y prime equals y from one, with a step of a quarter. The first step is one plus a quarter of one, five quarters. The second is five quarters plus a quarter of five quarters, twenty five sixteenths, five quarters squared. After four steps, at t equals one, you get six hundred twenty five over two hundred fifty six.

@chapter Beside the true value
@math heading="At t = 1" items="625/256 ≈ 2.44141@about two point four four;;e ≈ 2.71828@the closed form;;error ≈ 0.276876@the difference"
That's about two point four four one four one. The closed form at t equals one is e, about two point seven one eight two eight. The difference is about zero point two seven six eight seven six.

@art euler-staircase
No step was computed wrongly. Each step assumed the rate stayed at its starting value across the step, while the real rate kept climbing. So for growth, the exact sequence always sits below the curve.

@math heading="(1 + 1/n)ⁿ" items="n = 1:  2@n equals one;;n = 2:  9/4 = 2.25@n equals two;;n = 4:  625/256 ≈ 2.44141@With four;;n = 16:  (17/16)¹⁶ ≈ 2.63793@sixteen"
Shrink the step to one over n. With n equals one you get two. With n equals two, nine quarters, two point two five. With four, about two point four four. With sixteen, about two point six three seven nine three.

@art climbing-to-curve
As the step shrinks, the values climb towards e, the same sequence you may have met as the number e. The table suggests that limit. It doesn't prove it.

@chapter Where people slip
@list heading="Common slips" items="Thinking exponential means fast@The first|Reading yₙ as the solution at tₙ@The second|Forgetting the 1 in the factor@The third"
The first slip is thinking exponential means fast. y prime equals one hundredth of y is exponential, and with a step of a quarter its factor is four hundred one over four hundred. The second is reading the Euler value as the solution. The third is forgetting the one in the factor.

@art slow-growth
Exponential growth means the rate is proportional to the size, not that it's large. And Euler adds the change to the old value, so the factor is one plus k h, not k h. For growth, the factor must be bigger than one.

@chapter Try it
@words text="y′ = y,  y(0) = 1,  h = 1/2" sub="target: 9/4 at t = 1"
Your turn. Take y prime equals y from one, with a step of one half. Find the factor, take two steps to reach t equals one, and check you get nine quarters. Then compare it with e.

@end text="Watch the sequence climb towards e"
You can shrink the step and watch the exact fractions climb, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: differential-equations-and-eulers-method/runge-kutta-four-slopes-per-step
title: Runge–Kutta: four slopes per step, and an error that falls by sixteen
thumb: Weights 1, 2, 2, 1
---

@chapter The next rung
@title text="Runge–Kutta: Four Slopes per Step" sub="Differential Equations and Euler's Method" art=thumb
Euler's method is first order. The improved method is second order. The classical Runge Kutta method reads four slopes in each step, and it climbs to fourth order. Halve the step, and its error falls by sixteen.

@math heading="RK4" items="k₁ = f(tₙ, yₙ)@at the start;;k₂ = f(tₙ + h/2, yₙ + h·k₁/2)@at the middle;;k₃ = f(tₙ + h/2, yₙ + h·k₂/2)@the middle again;;k₄ = f(tₙ + h, yₙ + h·k₃)@at the end"
The first slope, k one, is read at the start: Euler's slope. The second is read at the middle of the step, using a half step along the first. The third is read at the middle again, using a half step along the second. And the fourth is read at the end, using a whole step along the third.

@art four-slopes
Each later slope corrects the point where the previous one was taken. Then all four are combined into a single step.

@math heading="The step" items="yₙ₊₁ = yₙ + h·(k₁ + 2k₂ + 2k₃ + k₄)/6@one, two, two, one"
The step uses the weights one, two, two, one, over six. The middle gets two readings, so it gets double weight, and the weights add to six.

@art weights-bars
When the right side depends on t alone, the two middle slopes are the same. Then the average is one at the start, four at the middle and one at the end, over six. That's Simpson's rule on one piece.

@chapter One step by hand
@math heading="y′ = t⁴,  y(0) = 0,  h = 1" items="k₁ = 0,   k₂ = k₃ = 1/16,   k₄ = 1@The slopes;;y₁ = (0 + 2/16 + 2/16 + 1)/6 = 5/24@five twenty fourths;;true 1/5,   error 1/120@The truth"
Take y prime equals t to the fourth, from zero, with one step of size one. The slopes are zero at the start, one sixteenth twice at the middle, and one at the end. So y one is five quarters over six: five twenty fourths. The truth is a fifth, so the error is one over a hundred and twenty.

@chapter Exact on a cubic
@art cubic-exact
On y prime equals t cubed, the lab prints zero for the error at every step size. The ratio tile shows a dash, because there's nothing to divide, and the order tile says exact. Simpson's rule integrates a cubic without error, so Runge Kutta has nothing to get wrong.

@chapter Exactly sixteen
@math heading="y′ = t⁴,  T = 1" items="h = 1/4:   1/30720@At a quarter;;h = 1/8:   1/491520@at an eighth;;h = 1/16:   1/7864320@at a sixteenth;;ratios:  16,  16@Both ratios"
On y prime equals t to the fourth, the error at a quarter is one over thirty thousand seven hundred and twenty. At an eighth, it's one over four hundred and ninety one thousand five hundred and twenty. And at a sixteenth, one over seven million eight hundred and sixty four thousand three hundred and twenty. Both ratios are sixteen.

@art sixteen-shrink
Each error is exactly h to the fourth over a hundred and twenty. Every step misses by h to the fifth over a hundred and twenty, and there are one over h steps. Halve h, and h to the fourth falls to a sixteenth.

@words text="error ≈ C·h⁴" sub="fourth order"
In general, for a right side with continuous fourth derivatives, the error is about C times h to the fourth. On y prime equals y, the rounded ratios are about fourteen point four and fifteen point two, climbing toward sixteen. The lab shows this, and doesn't prove it for every equation.

@art order-ladder
So the ladder goes like this. Each halving of the step halves Euler's error, quarters the improved method's, and divides Runge Kutta's by sixteen.

@chapter Not four Euler steps
@art rk-vs-euler
Four Euler steps of a quarter the size also read four slopes. But each advances only a quarter, starting from the last step's inexact value. Runge Kutta combines its four slopes into one step. Same work, very different result.

@math heading="y′ = t⁴,  16 slope readings each" items="RK4,  h = 1/4:   1/30720@Runge Kutta at a quarter;;Euler,  h = 1/16:   19627/655360 ≈ 0.0299484@Euler at a sixteenth"
On y prime equals t to the fourth, with sixteen slope readings each, Runge Kutta at a quarter has an error of one over thirty thousand seven hundred and twenty. Euler at a sixteenth has about zero point zero three. That's about nine hundred and twenty times larger.

@chapter Where people slip
@list heading="Common slips" items="Thinking it's just four Euler steps@The first|Averaging the four slopes equally@The second|Taking fourth order to mean exact@the third"
The first slip is thinking it's just four Euler steps. The second is averaging the four slopes equally. On the worked step, that gives nine thirty seconds, against five twenty fourths with the right weights, and a fifth for the truth. And the third is taking fourth order to mean exact. On y prime equals y, the error is never zero.

@chapter Try it
@words text="y′ = t³,  one step,  h = 1" sub="slopes 0, 1/8, 1/8, 1"
Your turn. Take a single step on y prime equals t cubed, with h equal to one. The slopes are zero, an eighth, an eighth and one. Combine them with the weights one, two, two, one, over six, and compare with the true value, a quarter.

@end text="Four slopes, one step"
You can run Runge Kutta in exact fractions and read the ratio of sixteen yourself, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: first-order-linear-equations/constant-coefficients-and-the-steady-state
title: Constant coefficients: the steady state b over a
thumb: Steady state b/a, never reached
---

@chapter The question
@title text="Constant Coefficients and the Steady State" sub="First-Order Linear Equations" art=thumb
Take y prime plus two y equals six, starting at zero. Before solving anything, ask a simpler question. Where is the rate zero? That one value tells you most of the story.

@chapter The steady state
@math heading="y′ + 2y = 6" items="y′ = 6 − 2y@six minus two y;;= 0  at  y = 3@zero at"
Rearrange: y prime equals six minus two y, which is zero at y equals three. If y ever sat at three, it would stay there for ever.

@words text="steady state  y = b/a" sub="attracting if a > 0, repelling if a < 0"
In general, for y prime plus a y equals b with a not zero, the steady state is the constant b over a. It's the one constant solution. It attracts when a is positive, and repels when a is negative.

@chapter The shifted exponential
@math heading="The gap" items="u = y − b/a@the gap;;u′ = b − a·y = −a·u@u prime;;u = u₀·e^(−a·t)@decay;;y = b/a + (y₀ − b/a)·e^(−a·t)@add b over a back"
Let u be the gap, y minus b over a. Then u prime is y prime, which is b minus a y, and that's minus a times u. That's the decay equation, so u is its starting value times e to the minus a t. Add b over a back, and you have the solution.

@math heading="y′ + 2y = 6,  y(0) = 0" items="steady state 3@steady state;;starting gap 0 − 3 = −3@starting gap;;y = 3 − 3·e^(−2t)@So y equals"
For our example, the steady state is three, and the starting gap is zero minus three, minus three. So y equals three minus three e to the minus two t.

@chapter Never quite there
@art gap-never-zero
The gap, three e to the minus two t, is positive for every t, because an exponential is never zero. So y comes closer to three and never reaches it at any finite time. A curve that looks flat in a drawing just has a gap smaller than a pixel.

@art from-above
Nor is the steady state the starting value. The start fixes the gap, and the steady state fixes where it's measured from. Start at five, and the gap is plus two, so y is three plus two e to the minus two t, falling towards three from above and never crossing it.

@chapter When a is negative
@math heading="y′ − y = 2" items="a = −1,  b = 2,  steady state −2@a is minus one;;y = −2 + 2·e^t@from zero"
Take y prime minus y equals two. Now a is minus one and b is two, so the steady state is minus two. From zero, the solution is minus two plus two e to the t. The gap is multiplied by e to the t, so it grows.

@art repelling
The lab prints minus two as repelling. Start exactly at minus two and you stay. Start anywhere else, however close, and you leave.

@chapter Euler, exactly
@math heading="h = 1/4,  factor 1 − a·h = 1/2" items="yₙ = 3 − 3·(1/2)ⁿ@three minus three;;y₁ = 3/2   (≈ 1.18041)@three halves;;y₂ = 9/4   (≈ 1.89636)@nine quarters;;y₄ = 45/16 = 2.8125   (≈ 2.59399)@forty five"
Run Euler from zero with a step of a quarter. Each step multiplies the gap by one minus a h, which is one half. So the values are three minus three times a half to the n: three halves, nine quarters, and at t equals one, forty five sixteenths. The true values beside them are rounded, ending about two point five nine.

@art polygon-ahead
Every fraction is right, and none of them is the solution. Euler's gap halves each step, but the true gap shrinks by e to the minus a half, about zero point six one. So the polygon runs ahead, about zero point two two above the curve at t equals one.

@art factor-dial
One warning for later. The factor one minus a h is positive and below one for a small step. It goes negative when h is bigger than one over a, and its size passes one when h is bigger than two over a.

@art one-step-landing
At h equals a half exactly, the factor is zero, and the polygon lands on three in one step and stays, which the curve never does. A bigger step on the same equation can run away. A later lesson on stiffness takes that up.

@chapter Where people slip
@list heading="Common slips" items="Thinking the steady state is reached, or is the start@The first|Reading the steady state off the right side@The second|Taking Euler's fraction for the solution@The third"
The first slip is thinking the steady state is the starting value, or that it's reached. The second is reading it off the right side. y equals six gives twelve on the left, not six. They match only when a is one. The third is taking Euler's final fraction for the solution. Forty five sixteenths is correct arithmetic on a polygon.

@chapter Try it
@words text="y′ + 2y = 6,  y(0) = 5" sub="Euler with h = 1/4: y₄ = ?"
Your turn. Start at five instead. Find the starting gap, write Euler's values with the factor one half, and check you get twenty five eighths after four steps, above three at every step.

@end text="Find the steady state first"
You can set a, b and the step, and watch the gap shrink or grow, on Learn. That's learn dot get er done dot I O.

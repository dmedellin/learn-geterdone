---
format: long
lesson: laplace-transforms/the-unit-step-and-switched-forcing
title: The unit step: solving equations with a switch
thumb: Invert first, then shift
---

@chapter The question
@title text="The Unit Step and Switched Forcing" sub="Laplace Transforms" art=thumb
Some forcing switches on and off. It might switch on at t equals two, or run as a pulse from one to three. How do you put a switch into an equation, and what does the transform do with it?

@chapter The switch
@math heading="unit step" items="u(t − c) = 0  for t < c@zero before;;u(t − c) = 1  for t ≥ c@one from"
The unit step, u of t minus c, is zero before t equals c, and one from then on.

@art step-switch
It's a switch. Multiply a signal by it, and the signal is blanked out before c.

@art shifted-copy
And u of t minus c, times f of t minus c, is the signal f shifted right by c. It's zero up to c, and from there it repeats f exactly as it was from t equals zero.

@chapter The shift rule
@math heading="if ℒ[f] = F(s)" items="ℒ[u(t − c)·f(t − c)] = e^(−cs)·F(s)@e to the minus c s;;ℒ[u(t − c)] = e^(−cs)/s@Putting f equal to one"
Here's the rule. The transform of the shifted, switched-on copy is e to the minus c s, times F of s. Putting f equal to one gives the case that matters most for forcing: the step itself transforms to e to the minus c s, over s.

@art slide-area
Why? The signal is zero before c, so the integral starts at c. Write t as c plus tau. The weight splits into e to the minus c s, times e to the minus s tau. The constant comes outside, and what's left is the ordinary transform. Sliding a graph along the axis doesn't change its area.

@chapter A worked switch
@math heading="y′ + y = u(t − 2),   y(0) = 0" items="(s + 1)·Y = e^(−2s)/s@s plus one;;Y = e^(−2s)·1/(s·(s + 1))@a passenger;;1/(s·(s + 1)) = 1/s − 1/(s + 1)@Partial fractions;;f = 1 − e^(−t)@one minus e to the minus t"
Take y prime plus y equals u of t minus two, from zero. Transform, and s plus one, times Y, equals e to the minus two s over s. That exponential factor is a passenger. Partial fractions are done on one over s times s plus one, which is one over s minus one over s plus one. That inverts to f equals one minus e to the minus t.

@math heading="then shift by 2" items="y = u(t − 2)·(1 − e^(−(t − 2)))@replace t;;t < 2:  y = 0@before two;;t ≥ 2:  y = 1 − e^(−(t − 2))@from two on"
Now apply the shift once, at the end. Replace t by t minus two and multiply by the step. Before two, y is zero. From two on, y is one minus e to the minus t minus two.

@art charge-from-switch
Nothing happens until two. Then the charging curve starts from zero, as if time began at the switch. The pieces meet: at two, the second piece is one minus e to the zero, which is zero.

@chapter A pulse
@math heading="y′ + y = u(t − 1) − u(t − 3)" items="t < 1:  y = 0@Before one;;1 ≤ t < 3:  1 − e^(−(t − 1))@From one to three;;t ≥ 3:  e^(−(t − 3)) − e^(−(t − 1))@From three on"
Two steps with a minus sign make a pulse, on from one up to three. Before one, y is zero. From one to three, it's the charging curve, one minus e to the minus t minus one. From three on, a second copy is subtracted, leaving e to the minus t minus three, minus e to the minus t minus one.

@art pulse-response
The output rises while the pulse is on, and decays once it's off. The two pieces meet at three, where both are one minus e to the minus two.

@chapter Second order
@math heading="y″ + 4y = u(t − 1),   from rest" items="1/(s·(s² + 4)) = (1/4)/s − (1/4)·s/(s² + 4)@a quarter over s;;y = (1/4)·(1 − cos(2(t − 1))),  t ≥ 1@cos of two"
The same works at second order. For y double prime plus four y equals u of t minus one, decompose one over s times s squared plus four into a quarter over s, minus a quarter s over s squared plus four. Invert and shift, and y is a quarter times one minus cos of two times t minus one, from one on.

@art switched-wave
It sits at zero until the switch, then oscillates between zero and a half.

@chapter Where people slip
@list heading="Common slips" items="Expecting the switch to act early@The first|Shifting the step but not the signal@The second|Leaving out the step@And the third"
The first slip is expecting the solution to move before the switch, or to depend on when it switches off. It can't. The second is shifting the step but not the signal. u of t minus two times one minus e to the minus t jumps to nearly one at the switch. And the third is leaving out the step. Then at t equals zero you'd get one minus e squared, about minus six point three nine.

@chapter Try it
@words text="y′ + y = u(t − 1) − u(t − 3)" sub="y(0) = 0"
Your turn. Solve the pulse yourself. Transform the two steps, solve for Y, invert the ordinary fraction, and apply each shift. Then write the three pieces, and check that each one meets the next.

@end text="Flip the switch yourself"
You can switch the forcing on and off and see the pieces of the solution on Learn. That's learn dot get er done dot I O.

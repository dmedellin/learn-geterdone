---
format: long
lesson: equilibria-stability-and-phase-lines/linearisation-and-the-sign-of-f-prime
title: Linearisation: the sign of f′ decides stability, unless it's zero
thumb: The slope decides, unless it's zero
---

@chapter The question
@title text="Linearisation and the Sign of f′" sub="Equilibria, Stability and Phase Lines" art=thumb
The sign test needs the whole phase line. Is there a test that looks only at the equilibrium itself? There is: the slope of f there. It's also the method that carries over to systems later, so it's worth seeing once by hand.

@chapter Zoom in on the gap
@math heading="Shift to zero" items="u = y − ȳ@the gap;;u′ = f(ȳ + u)@u prime;;= f′(ȳ)·u + (terms in u² and higher)@expanding"
Shift the equilibrium to zero. Let u be y minus y bar, the gap. Then u prime is f of y bar plus u. Expanding, that's f of y bar, plus f prime of y bar times u, plus terms in u squared and higher. At an equilibrium f of y bar is zero, so what's left starts with f prime times u.

@art zoom-in
For a small gap, the higher terms are far smaller than the first. So close in, the equation is nearly u prime equals f prime of y bar times u, the growth or decay equation for the gap.

@chapter A worked example
@math heading="y′ = y² − 1,  ȳ = −1,  f′(y) = 2y" items="u = y + 1,  y = u − 1@Put u;;y² − 1 = (u − 1)² − 1 = u² − 2u@u minus one squared;;u′ = −2u + u²@exactly"
Take y squared minus one, at the equilibrium minus one. Put u equal to y plus one. Then y squared minus one becomes u minus one squared, minus one, which is u squared minus two u. So u prime equals minus two u plus u squared, exactly. The slope f prime of minus one is minus two.

@math heading="u = 1/10" items="−2/10 + 1/100 = −19/100@full right side;;−2/10 = −20/100@first term alone"
How much does the u squared matter? Take u equals one tenth. The full right side is minus nineteen hundredths, against minus twenty hundredths for the first term alone. The neglected piece is a twentieth of it, and it shrinks faster than u, so it matters less as the solution closes in.

@chapter The slope test
@list heading="The slope test" items="f′(ȳ) < 0   →   stable@negative|f′(ȳ) > 0   →   unstable@positive|f′(ȳ) = 0   →   says nothing@zero"
So here's the test. If f prime at the equilibrium is negative, it's stable: the gap closes. If it's positive, it's unstable: the gap opens. If it's zero, the test says nothing.

@art tangent-signs
Picture the graph of f crossing the axis. Crossing downwards, f goes from plus to minus, which is stable. Crossing upwards, minus to plus, unstable. The lab prints f prime beside the verdict from the signs, and they agree whenever the slope isn't zero.

@math heading="f′(y) = 3y² − 8y + 3" items="f′(0) = 3   unstable@three;;f′(1) = −2   stable@minus two;;f′(3) = 6   unstable@six"
For the cubic with roots zero, one and three, f prime is three y squared minus eight y plus three. The slopes are three, minus two and six. Unstable, stable, unstable, the same as the sign test.

@art cubic-slopes
Each crossing of the cubic has its own tangent. Up, down, up. The steeper the tangent, the faster nearby solutions move away or close in.

@chapter The rate
@art gap-closing
The slope is a rate, not only a sign. If u prime were exactly minus two u, the gap at time one would be e to the minus two of its starting size, about zero point one three five. With slope minus one, it closes like e to the minus t instead, a factor of about zero point three six eight per unit time.

@words text="slope 2:  gap grows by e² ≈ 7.38906 per unit"
So slope minus two is twice as strongly stable as slope minus one. And at an unstable equilibrium with slope two, the gap grows by e squared, about seven point three nine, per unit of time.

@chapter When the slope is zero
@math heading="f′(0) = 0 in all three" items="y′ = y³:   u′ = u³,  gap opens,  unstable@y cubed;;y′ = −y³:   gap closes,  stable@minus y cubed;;y′ = y²·(1 − y):   u′ ≈ u²,  semistable@semistable equation"
Three equations have slope zero at zero, and no two behave alike. For y cubed, u prime is u cubed, with the sign of u, so the gap opens: unstable. For minus y cubed, the opposite sign: stable. For the semistable equation, u prime is about u squared, positive on both sides: semistable.

@art three-flat
Same slope, three verdicts. A zero slope means the first order term vanished, and you need the next order, which is the sign of f on both sides. For minus y cubed, f of minus one is one and f of one is minus one: positive then negative, stable.

@chapter Where people slip
@list heading="Common slips" items="Reading f′ = 0 as semistable@The first|Mixing up f′(ȳ) and y′@The second|Using f′ where f isn't zero@The third"
The first slip is reading a zero slope as semistable. You just saw three answers. The second is mixing up f prime and y prime. At an equilibrium y prime is always zero. f prime measures how fast nearby solutions pull in or push out. The third is using the slope at a point that isn't an equilibrium.

@art not-a-root
On the cubic, f prime of one half is minus a quarter, negative. But one half isn't an equilibrium, and a solution there is rising, not being drawn in. Find the root first.

@chapter Try it
@words text="y′ = y² − 1,  ȳ = 1" sub="find f′(1) and the verdict"
Your turn. Take y squared minus one at its other equilibrium, one. Compute f prime there, decide the type, then confirm it with the signs of f at zero and two.

@end text="Check the slope at each root"
You can see f prime printed beside every verdict, on Learn. That's learn dot get er done dot I O.

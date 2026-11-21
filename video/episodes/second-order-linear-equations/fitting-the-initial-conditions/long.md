---
format: long
lesson: second-order-linear-equations/fitting-the-initial-conditions
title: Fitting the initial conditions: two numbers, two equations, two constants
thumb: One start, one fit
---

@chapter The question
@title text="Fitting the Initial Conditions" sub="Second-Order Linear Equations" art=thumb
Every lesson so far ended by fitting two constants in a line or two. It turns out those lines are all one computation.

@art start-dot-and-arrow
The unknowns are C one and C two. The data are the starting value, y of zero, and the starting rate, y prime of zero. Put t equals zero into the general solution and into its rate, and each gives one linear equation.

@words text="at t = 0:  e⁰ = 1,  cos 0 = 1,  sin 0 = 0"
That's why the equations are short. At t equals zero every exponential is one, cosine is one and sine is zero.

@chapter Three pairs
@math heading="The two equations" items="real r₁, r₂:  C₁ + C₂ = y(0),  r₁·C₁ + r₂·C₂ = y′(0)@For two real roots;;repeated r:  C₁ = y(0),  r·C₁ + C₂ = y′(0)@For a repeated root;;complex α ± βi:  C₁ = y(0),  α·C₁ + β·C₂ = y′(0)@For a complex pair"
For two real roots, C one plus C two is the start, and r one C one plus r two C two is the starting rate. For a repeated root, C one is the start, and r C one plus C two is the rate. For a complex pair, C one is the start again, and alpha C one plus beta C two is the rate.

@chapter Eliminate once
@math heading="Two real roots" items="(r₁ − r₂)·C₁ = y′(0) − r₂·y(0)@for C one;;(r₁ − r₂)·C₂ = r₁·y(0) − y′(0)@for C two"
For two real roots, you can eliminate once and for all. Multiply and subtract, and the unknowns separate. For C one, r one minus r two times C one is the starting rate minus r two times the start. For C two, it's r one times the start minus the starting rate.

@art crossing-lines
That factor, r one minus r two, is why the roots have to differ. If they do, you can divide by it, and there's exactly one pair of constants for every start.

@art parallel-lines
If they're equal, the two exponentials are one function, the equations stop pinning down two constants, and the repeated root form takes over.

@chapter The first preset
@math heading="y″ + 3y′ + 2y = 0,  y(0) = 0,  y′(0) = 1" items="r₁ = −1,  r₂ = −2,  r₁ − r₂ = 1@the roots are;;C₁ = (1 − 0)/1 = 1@C one is;;C₂ = (0 − 1)/1 = −1@C two is;;y = e^(−t) − e^(−2t)@The solution"
In the lab's first preset, the roots are minus one and minus two, so r one minus r two is one. Start at zero with rate one. C one is one minus zero, over one, so one. C two is zero minus one, over one, so minus one. The solution is e to the minus t minus e to the minus two t.

@art rise-from-zero
It starts at zero and is positive afterwards, rising at rate one. The rate at the start isn't the rate of the number zero.

@chapter A complex fit
@math heading="y″ + 2y′ + 5y = 0,  y(0) = 2,  y′(0) = 0" items="C₁ = 2@C one is two;;−2 + 2·C₂ = 0  ⟹  C₂ = 1@minus two plus two C two;;y = e^(−t)·(2·cos(2t) + sin(2t))@The solution"
With roots minus one plus or minus two i, the pair is C one equals the start, and minus C one plus two C two equals the rate. Start at two, rate zero, so C one is two. Then minus two plus two C two is zero, so C two is one. The solution is e to the minus t, times two cosine two t plus sine two t.

@art flat-start-wave
Its starting rate is zero because two effects cancel exactly. The exponential pulls it down by two, and the sine pushes it up by two.

@chapter When the lab declines
@math heading="y″ − y′ − y = 0,  y(0) = 1,  y′(0) = 0" items="roots (1 ± √5)/2@one plus or minus root five;;C₁ = (5 − √5)/10,  C₂ = (5 + √5)/10@By hand"
For y double prime minus y prime minus y, the roots are one plus or minus root five, over two. By hand, with start one and rate zero, C one is five minus root five over ten, and C two is five plus root five over ten. They add to one, as the first equation needs.

@art irrational-zoom
But the lab fits rational constants only, so here it prints a dash and says the roots are irrational. That's a limit of its arithmetic, not of the method. A surd would have to be rounded, and then the residual would be a rounded number instead of a zero.

@chapter Where people slip
@list heading="Common slips" items="Differentiating the number y(0)@The first|Putting constants on the wrong roots@The second|Taking a dash for a failed method@The third"
The first slip is finding the starting rate by differentiating the number y of zero. It's a second piece of data. The second is putting the constants on the wrong roots. The lab writes the larger root first. And the third is taking a dash for a failure of the method.

@words text="y(0) = 0,  y′(0) = 1" sub="name the root beside each constant"
Your turn. Redo the first preset with the constants swapped, and check that the starting rate comes out as minus one, not one.

@end text="Two numbers, two equations"
You can fit the constants for every kind of root, on Learn. That's learn dot get er done dot I O.

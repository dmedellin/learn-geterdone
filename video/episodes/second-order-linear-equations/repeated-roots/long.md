---
format: long
lesson: second-order-linear-equations/repeated-roots
title: Repeated roots: where the second solution t·e^(rt) comes from
thumb: Multiply by t
---

@chapter The problem
@title text="Repeated Roots" sub="Second-Order Linear Equations" art=thumb
When the discriminant is zero, the characteristic quadratic has just one root. That gives you one exponential solution, and a second-order equation needs two.

@art one-root-parabola
The quadratic formula gives r equals minus b over two a, once. For y double prime plus four y prime plus four y, the quadratic is r squared plus four r plus four, which is r plus two, squared. Its only root is minus two.

@math heading="y″ + 4y′ + 4y = 0" items="r² + 4r + 4 = (r + 2)²@So you get;;y = C·e^(−2t)@one constant;;y(0) = 1  ⟹  C = 1@the first;;y′(0) = 1  ⟹  −2·C = 1@the second"
So you get e to the minus two t and its multiples, a family with one constant. Now ask for a start at one with rate one. The first condition says C is one. The second says minus two C is one. They disagree.

@art one-family-curves
And writing C one e to the r t plus C two e to the r t doesn't help. That's just C one plus C two times e to the r t, one function with one constant. Every member starts with the wrong rate.

@chapter The second solution
@words text="t·e^(rt)" sub="also a solution when r is a repeated root"
Here's the fix. When r is the only root, t times e to the r t is also a solution. So the general solution is C one plus C two t, all times e to the r t.

@math heading="Why it works" items="(t·e^(rt))′ = (1 + r·t)·e^(rt)@The product rule;;(t·e^(rt))″ = (2r + r²·t)·e^(rt)@second rate;;[(a·r² + b·r + c)·t + (2a·r + b)]·e^(rt)@Substitute"
The product rule gives the rate, one plus r t, times e to the r t, and the second rate, two r plus r squared t, times e to the r t. Substitute, and you get a r squared plus b r plus c, times t, plus two a r plus b, all times e to the r t.

@words text="both brackets are zero" sub="r is a root,  and  r = −b/(2a)"
The first bracket is zero because r is a root. The second is zero because a repeated root is minus b over two a. So the residual is zero.

@chapter A concrete check
@art t-times-exp
Try it on y equals t e to the minus two t. It starts at zero, rises, and dies away.

@math heading="y = t·e^(−2t)" items="y′ = (1 − 2t)·e^(−2t)@one minus two t;;y″ = (4t − 4)·e^(−2t)@four t minus four;;(4t − 4) + 4·(1 − 2t) + 4t = 0@Add up"
Its rate is one minus two t, times e to the minus two t. Its second rate is four t minus four, times the same exponential. Add up the brackets for y double prime plus four y prime plus four y. The t terms are four minus eight plus four, zero, and the constants are minus four plus four, zero.

@chapter Fitting both constants
@math heading="y(0) = 1,  y′(0) = 1" items="y(0) = C₁ = 1@C one is one;;y′(0) = −2·C₁ + C₂ = 1@minus two C one;;C₂ = 3@so C two is three;;y = (1 + 3t)·e^(−2t)@The solution"
At zero, the value is just C one, so C one is one. The rate at zero is r C one plus C two, here minus two C one plus C two, equals one, so C two is three. The solution is one plus three t, times e to the minus two t.

@art rise-then-decay
One plus three t grows, but e to the minus two t shrinks faster. So the solution rises at first, then decays, a shape no single exponential can make.

@art straight-line
Here's a neat special case. For y double prime equals zero, the root is zero, twice. The general solution is C one plus C two t, a straight line. That's right: a zero second rate means a constant first rate. Start at one with rate two, and the line is one plus two t.

@chapter Where people slip
@list heading="Common slips" items="Using C·e^(rt) alone@The first|Reading C₂ as the starting rate@The second|Writing a second copy of e^(rt)@The third"
The first slip is using C e to the r t alone. The second is reading C two as the starting rate. Here it's one minus minus two times one, which is three. And the third is writing a second copy of e to the r t. It passes the residual check, but it can't fit the start.

@chapter A boundary case
@art boundary-case
The repeated root is a boundary. A tiny change in b makes the discriminant positive or negative, and the form changes, though the solution itself changes only a little. The next course uses it as the line between motion that overshoots and motion that doesn't.

@words text="y″ + 4y′ + 4y = 0" sub="try y(0) = 1,  y′(0) = 1"
Your turn. Fit the constants yourself for this start, then put them back to check both starting values.

@end text="Multiply by t, then fit"
You can verify t e to the r t and fit both constants, on Learn. That's learn dot get er done dot I O.

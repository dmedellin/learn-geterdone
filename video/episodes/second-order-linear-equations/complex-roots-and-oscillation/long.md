---
format: long
lesson: second-order-linear-equations/complex-roots-and-oscillation
title: Complex roots: how a negative discriminant becomes an oscillation
thumb: Complex roots, real waves
---

@chapter The puzzle
@title text="Complex Roots and Oscillation" sub="Second-Order Linear Equations" art=thumb
What happens when the characteristic quadratic has no real roots at all? You might think the equation has no real solution. It does, and it oscillates.

@math heading="y″ + 2y′ + 5y = 0" items="disc = 4 − 20 = −16@four minus twenty;;r = (−2 ± 4i)/2 = −1 ± 2i@so the roots are"
Take y double prime plus two y prime plus five y. The discriminant is four minus twenty, minus sixteen, so the roots are minus two plus or minus four i, over two. That's minus one plus or minus two i.

@art no-real-root-parabola
No real number solves the quadratic. But that doesn't mean no real function solves the equation. The roots are numbers that satisfy a quadratic. The solutions are functions of t built from them.

@chapter The solutions
@math heading="Roots α ± βi" items="e^(αt)·cos(βt)@e to the alpha t;;e^(αt)·sin(βt)@and e to the alpha t;;y = e^(αt)·(C₁·cos(βt) + C₂·sin(βt))@The general solution"
Write the roots as alpha plus or minus beta i, with alpha and beta real. Then e to the alpha t times cosine of beta t, and e to the alpha t times sine of beta t, both solve the equation. The general solution puts a constant on each.

@words text="α = −b/(2a)     α² + β² = c/a" sub="why the residual is zero"
Why? Substitute, and the sine term carries two a alpha plus b, which is zero because alpha is minus b over two a. The cosine term comes to c minus a times alpha squared plus beta squared, which is zero because that's the product of the roots. No i in sight.

@chapter A check by hand
@math heading="y = e^(−t)·sin(2t)" items="α = −1,  β = 2@alpha is minus one;;y′ = e^(−t)·(2·cos(2t) − sin(2t))@Its rate;;y″ = e^(−t)·(−4·cos(2t) − 3·sin(2t))@its second rate"
Here alpha is minus one and beta is two. Take e to the minus t times sine of two t. Its rate is e to the minus t, times two cosine two t minus sine two t. And its second rate is e to the minus t, times minus four cosine two t minus three sine two t.

@math heading="y″ + 2y′ + 5y" items="cos:  −4 + 2·2 + 0 = 0@the cosine terms;;sin:  −3 + 2·(−1) + 5 = 0@the sine terms"
Now collect the residual. The cosine terms give minus four, plus two times two, plus zero. The sine terms give minus three, plus two times minus one, plus five. Both are exactly zero, and the lab reports the same.

@chapter Reading the root
@art decaying-oscillation
The real part alpha is the envelope. Here it's minus one, so the factor e to the minus t shrinks the swings.

@art steady-oscillation
For y double prime plus four y, alpha is zero. It neither shrinks nor grows, and keeps its size for ever.

@art growing-oscillation
And with a positive alpha, the oscillation grows. Take y double prime minus two y prime plus two y. The discriminant is four minus eight, minus four, and the roots are one plus or minus i.

@math heading="y″ − 2y′ + 2y = 0" items="y = e^t·(C₁·cos t + C₂·sin t)@The general solution;;y(0) = 1  ⟹  C₁ = 1@a start at one;;α·C₁ + β·C₂ = 1 + C₂ = 0  ⟹  C₂ = −1@alpha C one plus beta C two"
The general solution is e to the t, times C one cosine t plus C two sine t. With a start at one and rate zero, C one is one. The rate condition is alpha C one plus beta C two, one plus C two, equals zero, so C two is minus one.

@art two-speeds
The imaginary part beta is the speed. One full turn takes two pi over beta. For beta equals two, that's pi units of t. Here beta is one, so it turns once every two pi, and its size multiplies by e each time t goes up by one.

@chapter Where people slip
@list heading="Common slips" items="Complex root means no real solution@The first|Dropping the exponential@The second|Reading C₂ as the starting rate@The third"
The first slip is deciding a complex root means no real solution. E to the minus t sine two t is real, and its residual is exactly zero. The second is dropping the exponential. The third is reading C two as the starting rate. It's the starting rate minus alpha C one, all over beta.

@art dropped-envelope
Drop the exponential for minus one plus or minus two i, and substitute cosine of two t. You get cosine two t minus four sine two t, not zero. Only a root with real part zero lets you leave the exponential out.

@chapter Try it
@words text="y″ + 2y′ + 5y = 0" sub="y(0) = 1,  y′(0) = 0"
Your turn. Fit this start. C one is one, and C two is zero plus one, over two. Write the solution and check its starting rate.

@end text="Read the envelope and the speed"
You can try each preset and watch the envelope shrink, hold or grow, on Learn. That's learn dot get er done dot I O.

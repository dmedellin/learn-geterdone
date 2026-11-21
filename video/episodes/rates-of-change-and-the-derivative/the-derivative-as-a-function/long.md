---
format: long
lesson: rates-of-change-and-the-derivative/the-derivative-as-a-function
title: The derivative as a function, and the power rule
thumb: Bring the exponent down
---

@chapter A function of rates
@title text="The Derivative as a Function" sub="Rates of Change and the Derivative" art=thumb
Every place on a curve has its own derivative. Collect them all, and the derivative becomes a function of t in its own right. For a polynomial, there's a quick rule for finding it.

@art tangents-along-curve
Picture the tangent line at every point along a curve. Each one has a slope. Write that slope as a formula in t, and you have f prime of t. For t squared, it's two t. For t cubed, it's three t squared.

@chapter The power rule
@math heading="The power rule" items="(tⁿ)′ = n·tⁿ⁻¹@t to the n;;(c)′ = 0@a constant"
Here's the rule. For a whole number n, at least one, the derivative of t to the n is n times t to the n minus one. Bring the exponent down, and lower the power by one. And a constant has derivative zero.

@art choose-copies
Why? Multiply out n copies of t plus h. Take t from every copy, and you get t to the n. Take h from just one copy, and there are n ways to do that, which gives n t to the n minus one, times h. Every other choice takes h at least twice, so it carries h squared.

@words text="quotient = n·tⁿ⁻¹ + (terms with h)"
Subtract t to the n, divide by h, and the constant term is n t to the n minus one. For a constant, the top is c minus c, so every quotient is zero.

@chapter Term by term
@math heading="Two more facts" items="(p + q)′ = p′ + q′@of a sum;;(c·p)′ = c·p′@a constant factor;;(c·tⁿ)′ = n·c·tⁿ⁻¹@term by term"
Two more facts handle a whole polynomial. The derivative of a sum is the sum of the derivatives. And a constant factor comes through unchanged. Together, c t to the n becomes n c t to the n minus one, term by term.

@chapter A cubic
@math heading="p(t) = t³ − 6t² + 9t" items="p′(t) = 3t² − 12t + 9@three t squared;;= 3(t² − 4t + 3)@Factor out three;;= 3(t − 1)(t − 3)@t minus one;;zeros:  t = 1,  t = 3@the zeros"
Take t cubed minus six t squared plus nine t. The three terms give three t squared, minus twelve t, and nine. Factor out three, then factor again, and you get three times t minus one, times t minus three. So the zeros are at one and three.

@chapter Reading the sign
@math heading="One test point in each region" items="t = 0:  3·(−1)·(−3) = 9    rising@At zero;;t = 2:  3·1·(−1) = −3    falling@At two;;t = 4:  3·3·1 = 9    rising@At four"
Now test one point in each region. At zero, the derivative is three times minus one times minus three, which is nine, positive. At two, it's minus three, negative. At four, it's nine again.

@art sign-strip
Positive means rising, negative means falling, and zero means the tangent is level for a moment. A zero alone doesn't say which way the graph goes on either side, so you test between the zeros. Here, the graph rises until one, falls until three, then rises again.

@art cubic-shape
That's exactly what this cubic does. It climbs to a height of four at one, drops to zero at three, and rises for ever after. The derivative told you the shape without plotting a single point.

@art derivative-below
Stack the two graphs, one above the other, and you can see it. Where the derivative sits above its axis, the cubic climbs. Where it dips below, the cubic falls. And the derivative's two zeros line up with the hump and the valley.

@chapter Where people slip
@list heading="Common slips" items="(t³)′ = t²  ✗   it's 3t²@forgetting the coefficient|(5)′ = 1  ✗   it's 0@a constant|Differentiating each factor of a product@the factors"
The first slip is forgetting the coefficient. The derivative of t cubed is three t squared, not t squared. The second is giving a constant a rate. The derivative of five is zero, not one. The third is differentiating the factors of a product separately. That isn't this rule. Expand first.

@art height-vs-direction
And don't read a positive derivative as a positive function. For t squared minus four t at three, the derivative is two, so the graph is rising. But the height there is minus three, below the axis. The derivative answers direction, not height.

@chapter Try it
@words text="p(t) = t² − 4t" sub="p′(t) = 2t − 4,  zero at t = 2"
Your turn. Differentiate t squared minus four t. You should get two t minus four, with its zero at two. Test the sign on each side, and say what shape the graph has to be.

@end text="Read the shape from the sign"
You can type a polynomial and see its derivative, its zeros, and where it rises and falls, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: differential-equations-and-eulers-method/what-a-differential-equation-is
title: What a differential equation is, and how to check an answer
thumb: The answer is a function
---

@chapter A new kind of equation
@title text="What a Differential Equation Is" sub="Differential Equations and Euler's Method" art=thumb
An equation in algebra asks for a number. Three x plus one equals seven, so x is two. A differential equation asks for something bigger: a whole function.

@art number-vs-function
It doesn't say what the unknown is. It says what the unknown does: how fast it changes. Your job is to find a function that behaves that way, at every moment at once.

@words text="y′ = 2t" sub="the rate of change of y at time t is 2t"
Take the smallest example. Y prime equals two t says the rate of change of y at time t is two t. Zero at the start, two at time one, four at time two.

@chapter Order and solution
@list heading="Three words" items="Differential equation: the unknown is a function, and its derivatives appear@A differential equation|Order: the highest derivative present@Its order|Solution: true for every t in some interval@a solution"
A differential equation is one whose unknown is a function, and which involves that function's derivatives. Its order is the highest derivative that appears. And a solution is a function that makes the equation true for every t in some interval. The word every carries the weight.

@art order-steps
Y prime equals two t is first order. Y double prime plus y equals zero is second order. And y prime equals y squared is still first order, square and all. The order comes from the highest derivative, and nothing else.

@chapter The residual test
@math heading="residual = left side − right side" items="y = t²:   y′ = 2t,   residual 2t − 2t = 0@T squared;;y = t² + 3:   y′ = 2t,   residual 0@plus three;;y = t³:   y′ = 3t²,   residual 3t² − 2t@T cubed"
To check a candidate, substitute it and read the residual: the left side minus the right. T squared has derivative two t, so the residual is zero. T squared plus three has the same derivative, so it works too. T cubed has derivative three t squared, and the residual is three t squared minus two t.

@art residual-flat
A residual of zero for every t means a solution. The lab works this out symbolically. Nothing is tried at sample points, so the verdict is about every t at once. The curve it draws is another matter. That's made with ordinary floating point numbers, to look at, not to trust for a digit.

@chapter Zero at a point is not enough
@art residual-curve
T cubed's residual factors as t times three t minus two. It vanishes at zero and at two thirds. That doesn't rescue it. A solution needs the residual to be zero at every t, not at two of them.

@math heading="y′ = 2t,  candidate y = 2t" items="y′ = 2@Its derivative;;residual:  −2t + 2@the residual;;zero only at t = 1@only at one"
Here's another. Try y equals two t. Its derivative is two, so the residual is minus two t plus two. That's zero only at one, and nowhere else.

@art line-crosses-once
Agreeing at a point means you've satisfied one instance of the equation, and no more. One instance of agreement is exactly what the residual test refuses to accept.

@chapter One equation, many answers
@art family-shifted
Now the first surprise. T squared and t squared plus three are both solutions. Add any constant C to t squared, and the derivative stays two t. So t squared plus C is a solution for every C: a whole family of curves, the same shape shifted up or down.

@words text="y′ = y" sub="a rate that depends on the unknown itself"
You met y prime equals two t before, as the question of which function has this rate, and the answer was an antiderivative. But a differential equation can have a rate that depends on the unknown itself, like y prime equals y. Then an antiderivative alone won't answer it.

@chapter Where people slip
@list heading="Common slips" items="Expecting a number for an answer@The first|Reading the order from exponents or terms@The second|Testing at one value of t@the third"
The first slip is expecting a number for an answer. The answer is a function, and here there are infinitely many. The second is reading the order from the exponents, or the number of terms. And the third is testing a candidate at one value of t, and stopping.

@chapter Try it
@words text="y′ = 2t" sub="test y = t² − 7"
Your turn. Test y equals t squared minus seven against y prime equals two t. Differentiate it, subtract two t, and simplify. Then say where it sits in the family. Then try y equals two t again, and find the one value of t where its residual happens to vanish.

@end text="Substitute, subtract, read the residual"
You can type an equation and a candidate, and see the exact residual, on Learn. That's learn dot get er done dot I O.

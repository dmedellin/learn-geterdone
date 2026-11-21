---
format: long
lesson: rates-of-change-and-the-derivative/the-second-derivative
title: The second derivative: which way a graph bends
thumb: The rate of the rate
---

@chapter The rate of the rate
@title text="The Second Derivative" sub="Rates of Change and the Derivative" art=thumb
The derivative of a polynomial is another polynomial. So it has a derivative of its own. That's the second derivative, and it tells you something the first one can't: which way the graph bends.

@words text="p″ = (p′)′" sub="position → velocity → acceleration"
Write it p double prime. It's the derivative of p prime, the rate at which the slope is changing. If p is a position, then p prime is a velocity, and p double prime is an acceleration. To find it, apply the power rule a second time. T cubed gives three t squared, and then six t.

@chapter Its sign is the bend
@art cup-and-cap
Where p double prime is positive, the slopes get larger as t grows, and the graph bends up, like a cup. That's called concave up. Where it's negative, the slopes get smaller, and the graph bends down, like a cap. Concave down.

@art tangent-below-cup
A tangent line lies below a graph that bends up. That's why the tangent estimates for t squared, a few lessons back, always fell short.

@chapter A cubic with an S in it
@math heading="p(t) = t³ − 3t²" items="p′(t) = 3t² − 6t@three t squared minus six t;;p″ = 6t − 6 = 6(t − 1)@six t minus six;;t < 1:  p″ < 0,  bends down@Below one;;t > 1:  p″ > 0,  bends up@Above one"
Take t cubed minus three t squared. Its derivative is three t squared minus six t, and differentiating again gives six t minus six, which is six times t minus one. Below one, that's negative, so the graph bends down. Above one, it's positive, so it bends up.

@art s-curve
So at one, the graph changes its bend. A place where p double prime changes sign is called an inflection point.

@math heading="The slope, p′ = 3t² − 6t" items="t = 0:  0@At zero;;t = 1:  −3@at one;;t = 2:  0@at two;;t = 3:  9@at three"
You can see it in the slopes. At zero the slope is zero, at one it's minus three, at two it's zero again, and at three it's nine. The slope falls until one, then rises. It bottoms out exactly where p double prime is zero.

@chapter An inflection is not a turn
@math heading="Three special places" items="turns, p′ = 3t(t − 2) = 0:  t = 0 max,  t = 2 min@The turns;;inflection, p″ changes sign:  t = 1@The inflection;;at t = 1:  p′ = −3,  not 0@And there"
The turns of this graph are at the zeros of p prime, three t times t minus two. That's zero, a maximum, and two, a minimum. The inflection is between them, at one. And there, p prime is minus three, not zero. The graph is falling steeply as it passes through.

@art slopes-bottom-out
So you have two different questions. Where does the graph turn? Read p prime. Where does it change its bend? Read p double prime.

@chapter Bend is not direction
@art falling-cup
And concave up doesn't mean rising. The parabola t squared has p double prime equal to two, positive everywhere. Yet it falls for every negative t. A cup can be descending into its bottom as well as climbing out of it.

@chapter Two inflections
@math heading="p(t) = t⁴ − 6t²" items="p′ = 4t³ − 12t@four t cubed;;p″ = 12t² − 12 = 12(t − 1)(t + 1)@twelve t squared;;inflections:  t = −1,  t = 1@two inflection points"
For t to the fourth minus six t squared, p prime is four t cubed minus twelve t, and p double prime is twelve t squared minus twelve. That's twelve times t minus one, times t plus one: positive, then negative, then positive. So there are two inflection points, at minus one and one.

@art w-shape
The graph is a W, with its middle hump bending down. A parabola is the plainest case of all. T squared has p double prime equal to two, which never changes sign, so it bends up everywhere and has no inflection.

@chapter Where people slip
@list heading="Common slips" items="Looking for inflections where p′ = 0@The first|Reading concave up as rising@The second|Calling every zero of p″ an inflection@the third"
The first slip is looking for an inflection where p prime is zero. Those are the turns. The second is reading concave up as rising. And the third is calling every zero of p double prime an inflection. As with turns, the zero is only a place to look. The sign on each side decides.

@chapter Try it
@words text="p(t) = t⁴" sub="p″ = 12t²"
Your turn. The second derivative of t to the fourth is twelve t squared. It's zero at zero, and positive on both sides. Is zero an inflection point? Decide from the sign on each side, not from the zero itself.

@end text="Turns read p′, bends read p″"
You can see a polynomial's second derivative and its inflection points beside its turns, on Learn. That's learn dot get er done dot I O.

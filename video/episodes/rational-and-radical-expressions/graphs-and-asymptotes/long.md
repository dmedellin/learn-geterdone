---
format: long
lesson: rational-and-radical-expressions/graphs-and-asymptotes
title: Holes, asymptotes and zeros: read the graph from the factors
thumb: Hole or asymptote?
---

@chapter The question
@title text="Graphs and Asymptotes" sub="Rational and Radical Expressions" art=thumb
Every feature of a rational function's graph is already written in its factored form. A factor that cancels gives a hole. A factor left in the denominator gives a vertical asymptote. And the two degrees give the end behaviour.

@math heading="Rational function" items="f(x) = p(x) / q(x)@f of x;;domain: every real x except the zeros of the original q@except the zeros"
A rational function is f of x equals p of x over q of x, two polynomials, with q not the zero polynomial. Its domain is every real number except the zeros of q, and that means the original q, before any cancelling.

@words text="x = 3 excluded, then (x − 3) cancels" sub="so what does the graph do at 3?"
Suppose three is excluded, and then the factor x minus three cancels. What does the graph do at three? Something quite specific, and it isn't what happens at a zero of the denominator that survives.

@chapter Asymptote or hole
@art vertical-asymptote
If, after cancelling every common factor, x minus a still divides the denominator and not the numerator, then the line x equals a is a vertical asymptote. As x gets close to a, the values of f grow without bound, one way or the other.

@art hole-curve
But if every copy of x minus a in the bottom cancels, a is still outside the domain, while the reduced function has an ordinary value there. The graph is the reduced graph with that one point removed. A hole.

@words text="Cancelling does not put the point back"
That hole is the honest picture of what cancelling did. The reduced expression agrees with f everywhere f exists, and is defined at one point more. Two functions that differ at one point are different functions.

@chapter End behaviour
@math heading="Horizontal asymptote, by degree" items="n < m:  y = 0@smaller;;n = m:  y = a/b@equal;;n > m:  none@bigger"
Let n be the degree of the top and m the degree of the bottom, with leading coefficients a and b. If n is smaller, the horizontal asymptote is y equals zero. If they're equal, it's y equals a over b. If n is bigger, there's no horizontal asymptote.

@art horizontal-asymptote
That's not a rule to memorise. Divide top and bottom by x to the larger degree. For large x, every term with x underneath shrinks to zero, and what survives is exactly that comparison.

@math heading="Three end behaviours" items="(2x + 1)/(x² − 4):  1 < 2,  y = 0@two x plus one;;(3x² + 1)/(x² − 4):  tie,  y = 3/1 = 3@three x squared;;(x² + 1)/(x − 1):  2 > 1,  none@x squared plus one"
Two x plus one, over x squared minus four, has one less than two, so y equals zero. Three x squared plus one, over x squared minus four, is a tie, so y equals three over one, which is three. And x squared plus one, over x minus one, has two greater than one, so no horizontal asymptote at all.

@art slant-asymptote
In that last one, long division gives x plus one, plus two over x minus one, and the graph approaches the line y equals x plus one. That's a slant asymptote. This course mentions it and doesn't pursue it.

@chapter One function, every feature
@math heading="f(x) = (x² − x − 6)/(x² − 2x − 3)" items="= (x − 3)(x + 2) / [(x − 3)(x + 1)]@factor;;domain: x ≠ 3,  x ≠ −1@before cancelling;;reduced: (x + 2)/(x + 1)@cancel"
Now read one function completely. x squared minus x minus six, over x squared minus two x minus three. First, factor: x minus three times x plus two, over x minus three times x plus one. Record the domain before cancelling: three and minus one are out. Then cancel, leaving x plus two over x plus one.

@math items="hole at (3, 5/4):  (3 + 2)/(3 + 1)@a hole;;vertical asymptote x = −1:  top is 1 ≠ 0@vertical asymptote;;zero at x = −2@is a zero;;horizontal asymptote y = 1@horizontal asymptote"
x minus three cancelled, so there's a hole at three, at height three plus two over three plus one, five quarters. x plus one survives with a top of one, so minus one is a vertical asymptote. Minus two is a zero. And the degrees tie, leading coefficients one and one, so the horizontal asymptote is y equals one.

@art full-picture
A zero needs the top to be zero and the point to be in the domain. Three makes this numerator zero, but three was never in the domain, so it's a hole, not a zero. Near minus one the values run off to infinity. Near three, they close in on five quarters.

@chapter Where people slip
@list heading="Common slips" items="Taking the domain from the cancelled form@The first|Finding a hole's height in the original@The second|Thinking a graph never crosses its horizontal asymptote@the third"
The first slip is taking the domain from the cancelled form. The second is substituting into the original to find a hole's height. That gives zero over zero, which isn't a height. Cancel first, then substitute. And the third is assuming the graph never crosses its horizontal asymptote.

@art crossing-asymptote
It can. A horizontal asymptote only describes large x, and near the origin the graph may cross it as often as it likes. The vertical asymptote is the one it can never touch.

@chapter Try it
@words text="g(x) = (x² − 1)/(x² + x − 2)" sub="= (x − 1)(x + 1) / [(x − 1)(x + 2)]"
Your turn. g of x is x squared minus one, over x squared plus x minus two, which factors as x minus one times x plus one, over x minus one times x plus two. Find the original domain, the reduced rule, the hole and its height, the vertical asymptote, the zero, and the horizontal asymptote.

@end text="Factor, then read the graph"
You can practise reading holes and asymptotes from factors on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: rational-and-radical-expressions/rational-expressions-and-their-domains
title: Rational expressions: where the bottom is zero, nothing exists
thumb: Exclude from the original
---

@chapter The question
@title text="Rational Expressions and Their Domains" sub="Rational and Radical Expressions" art=thumb
Take x squared minus four, over x minus two. What is it worth when x is two? Most people say four. The real answer is that it isn't worth anything at all.

@art fraction-bar
A rational expression is one polynomial over another. It's the algebra version of a fraction, and it follows the same rules for the same reasons. Which means it breaks in the same place: wherever the bottom is zero.

@math heading="Rational expression" items="P(x) / Q(x)@P of x over Q of x;;Q is not the zero polynomial@not the zero polynomial"
In symbols, it's P of x over Q of x, where both are polynomials and Q is not the zero polynomial. That condition is about the polynomial, not about x. Q of x equals x minus two is a perfectly good denominator, even though it hits zero somewhere.

@chapter The domain
@art number-line-gaps
The domain is every real number x where Q of x is not zero. A number that makes the bottom zero is an excluded value. The expression simply assigns nothing to it, so on a number line, it's a gap.

@words text="Factor the bottom. Set each factor to zero." sub="the real solutions are the exclusions"
For the denominators in this course, finding the domain starts as a factoring problem. Factor the bottom, set each factor to zero, and collect the real solutions. An unfactored denominator hides the answer.

@chapter Two exclusions
@math heading="(x + 1) / (x² − x − 6)" items="x² − x − 6 = (x − 3)(x + 2)@factor the bottom;;x − 3 = 0  ⟹  x = 3@x equals three;;x + 2 = 0  ⟹  x = −2@minus two;;domain: all real x, x ≠ 3, x ≠ −2@every real number except"
Here's one. x plus one, over x squared minus x minus six. First, factor the bottom: it's x minus three, times x plus two. That's zero when x equals three, and when x is minus two. So the domain is every real number except those two.

@art zero-on-top
What about x equals minus one? It makes the top zero. But a zero on top is fine. The bottom there is one plus one minus six, which is minus four, and zero over minus four is just zero. An ordinary value at an ordinary point.

@chapter The hole
@math heading="(x² − 4) / (x − 2)" items="excluded: x = 2@two is excluded;;= (x − 2)(x + 2) / (x − 2)@factor the top;;= x + 2,  for x ≠ 2@for every x;;at x = 2:  0/0@zero over zero"
Now the case that gives this lesson its point. x squared minus four, over x minus two. The bottom is zero at two, so two is excluded. Factor the top, and for every x other than two, this equals x plus two. But at two itself, substituting gives zero over zero.

@math heading="Near x = 2" items="1.9 → 3.9@one point nine;;1.99 → 3.99@one point nine nine;;2 → no value@at two;;2.01 → 4.01@two point oh one;;2.1 → 4.1@two point one"
Look at the values nearby. One point nine gives three point nine. One point nine nine gives three point nine nine. At two, nothing. Then two point oh one gives four point oh one, and two point one gives four point one.

@art approach-arrows
The values close in on four from both sides, and the expression still has no value at two.

@art hole-graph
That gap is called a hole. Picture the line y equals x plus two with a single point missing, right above two. A later lesson, Graphs and Asymptotes, draws it properly.

@art two-lines
Here's what matters now. x plus two, the simplified answer, carries no record of the gap. Two expressions are equal when they agree everywhere both are defined. So the equation holds for x not equal to two, and written without that condition it's false at one point. The exclusion is a fact about where you started.

@chapter Undefined is not a value
@words text="0/0 is not 0, not 1, not ∞" sub="no number times 0 gives 4 · every number times 0 gives 0"
Why not just call zero over zero something? Division is the inverse of multiplication. No number times zero gives four, so four over zero has no answer. And every number times zero gives zero, so zero over zero has too many. Neither case gives you a value.

@chapter Where people slip
@list heading="Common slips" items="Excluding where the top is zero@The first|Reading the domain off the simplified form@The second|Treating 0/0 as a number@the third"
The first slip is excluding values that make the top zero. Only the bottom can destroy the expression. The second is reading the domain off the simplified form. Simplifying changes the formula, not the expression you were asked about. And the third is treating zero over zero as a number.

@chapter Try it
@words text="(2x − 1) / (x² + x − 12)" sub="x² + x − 12 = (x + 4)(x − 3)"
Your turn. Take two x minus one, over x squared plus x minus twelve. The bottom factors as x plus four, times x minus three. Write the domain. Then decide whether one half, where the top is zero, is allowed. Ask only where division fails.

@end text="Find every excluded value"
You can practise finding excluded values, one factor at a time, on Learn. That's learn dot get er done dot I O.

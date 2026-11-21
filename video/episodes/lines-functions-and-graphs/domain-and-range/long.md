---
format: long
lesson: lines-functions-and-graphs/domain-and-range
title: Domain and range: what goes in, what comes out
thumb: What goes in, what comes out
---

@chapter The idea
@title text="Domain and Range" sub="Lines, Functions and Graphs" art=thumb
Every function has two sets attached to it. What it accepts, and what it actually gives back. The first is easy to read off a formula. The second takes an argument.

@art input-output-axes
The domain is the set of inputs a function is defined on. The range is the set of outputs it produces: every y that some input in the domain actually reaches. Not values that look allowed. Values that really come out.

@words text="natural domain" sub="every real x that gives a real value"
When a formula arrives with no domain stated, you use the natural domain: every real number for which the formula gives a real value. That's a convention, the largest sensible default. A problem is free to name a smaller set.

@chapter Two exclusions
@art zero-denominator
With the formulas so far, only two things can go wrong. The first is a zero denominator. Set every denominator equal to zero, solve, and exclude those inputs. For x plus two, over x minus two times x minus three, the excluded inputs are two and three.

@math heading="g(x) = √(2x − 7)" items="2x − 7 ≥ 0@at least zero;;x ≥ 7/2@seven halves;;domain  [7/2, ∞)@exact fraction"
The second is an even root of a negative. The square root of two x minus seven needs two x minus seven to be at least zero. So x is at least seven halves. Write the exact fraction, not three point five. Cube roots are fine, though. The cube root of minus eight is minus two.

@math heading="h(x) = √(x + 4) / (x − 1)" items="x ≥ −4@at least minus four;;x ≠ 1@can't be one;;[−4, 1) ∪ (1, ∞)@So the domain"
When both appear, both conditions must hold. The square root of x plus four, over x minus one. The top needs x at least minus four. The bottom says x can't be one. So the domain is minus four to one, joined with one to infinity.

@art root-start
Notice minus four is included, with a square bracket. The square root of zero is zero, a perfectly good output. It's the denominator, not the root, that makes an open end.

@chapter A trap with squares
@math heading="k(x) = √(9 − x²)" items="9 − x² ≥ 0@nine minus x squared;;x² ≤ 9@x squared is at most nine;;−3 ≤ x ≤ 3@between minus three and three;;✗  x ≤ 3@just x is at most three"
Now the square root of nine minus x squared. You need nine minus x squared at least zero, so x squared is at most nine. That means x is between minus three and three, inclusive. If you root both sides and write just x is at most three, you lose the whole left half.

@chapter Why the range is harder
@words text="Range needs an argument" sub="three tools"
The domain is about which inputs the formula chokes on. The range is about behaviour across the whole domain, and there's no checklist. But three tools cover most cases.

@art parabola-floor
First, non negativity. x squared is never below zero, and it equals zero at zero, so its range is zero to infinity. Likewise, the absolute value of x, minus two, has range minus two to infinity.

@art semicircle
Second, track the outer operation. The square root of nine minus x squared takes the root of something running from zero up to nine, so the outputs run from zero to three.

@words text="y = 2x − 3  →  x = (y + 3)/2" sub="every real y is reached"
Third, solve for the input. If y equals two x minus three, then x equals y plus three, over two. That exists for every real y, so the line reaches every real output.

@art missing-point
One more. Take q of x equals two x plus one, with x not equal to three. Removing the input three removes the point three, seven, so the range is missing seven, not three. An excluded input removes an output, not its own number.

@chapter Writing it down
@list heading="Interval notation" items="[ ] includes the endpoint@square bracket|( ) excludes it@round bracket|∞ always takes ( )@infinity|∪ joins the pieces@join the pieces"
Write the answer in interval notation. A square bracket includes the endpoint, and a round bracket excludes it. Infinity always gets a round bracket, because it's never attained. And use a union to join the pieces, in increasing order. Then test a value at each end. At minus four, h gives zero, and at one, it divides by zero.

@chapter Where people slip
@list heading="Common slips" items="Copying a missing input into the range@The first|Opening an end a root leaves closed@The second|Losing half of a squared inequality@the third"
The first slip is copying a missing input into the range. The second is opening an endpoint that a root leaves closed. And the third is losing half of a squared inequality.

@chapter Try it
@words text="s(x) = √(x + 2) / (x − 4)" sub="root condition given: x ≥ −2"
Try the square root of x plus two, over x minus four. The root condition is given: x is at least minus two. Find the denominator exclusion, combine the conditions, write the intervals, and test both minus two and four.

@end text="Find the domain yourself"
The full lesson is on Learn. That's learn dot get er done dot I O.

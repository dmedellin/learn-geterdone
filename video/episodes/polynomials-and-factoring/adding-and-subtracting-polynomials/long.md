---
format: long
lesson: polynomials-and-factoring/adding-and-subtracting-polynomials
title: Adding and subtracting polynomials without sign errors
thumb: The minus reaches every term
---

@chapter The question
@title text="Adding and Subtracting Polynomials" sub="Polynomials and Factoring" art=thumb
Adding two polynomials sounds easy, and mostly it is. Subtracting them is where the wrong answers live. Here's the one habit that removes nearly all of them.

@art like-terms
Start with like terms. Two terms are like terms when their variable parts are identical: the same variables, raised to the same exponents.

@words text="5x²y and −2x²y: like · 5x²y and 5xy²: not" sub="coefficients play no part"
Five x squared y and minus two x squared y are like terms. Five x squared y and five x y squared are not. The coefficients play no part in deciding. A hundred x cubed and x cubed are like terms. x cubed and x squared are not, however close they look.

@chapter Why like terms combine
@math heading="The distributive law" items="axⁿ + bxⁿ = (a + b)xⁿ@a x to the n;;ac + bc = (a + b)c,  c = xⁿ@with c equal to"
For any numbers a and b, a x to the n plus b x to the n is a plus b, times x to the n. That's just the distributive law, a c plus b c equals a plus b times c, with c equal to x to the n. It isn't a special rule for polynomials, and that's exactly why it's safe.

@art no-common-piece
Turn it around and you see why x squared plus x cubed can't be collected. Pulling out x squared gives x squared times one plus x. That's a product, not a shorter sum. It's factoring, which is a legitimate move, but it isn't addition.

@chapter Adding in one line
@art sorted-sum
Here's the sum: three x cubed minus five x plus two, plus x cubed plus four x squared minus five.

@math heading="(3x³ − 5x + 2) + (x³ + 4x² − 5)" items="x³: 3x³ + x³ = 4x³@the x cubed terms;;x²: 4x²@only one x squared;;x: −5x@only one x term;;1: 2 − 5 = −3@the constants;;4x³ + 4x² − 5x − 3@result"
Work one power at a time. The x cubed terms give four x cubed. There's only one x squared term, four x squared, and only one x term, minus five x. The constants give two minus five, minus three. The result is four x cubed plus four x squared minus five x minus three.

@art power-columns
Working by power, highest first, rather than left to right, is what stops you using a term twice or skipping one.

@chapter Subtraction
@math heading="Negate every term" items="−(x² − 5x − 2) = −x² + 5x + 2@every sign flipped;;✗  −x² − 5x − 2@not"
Subtracting a polynomial means adding its negative, and the negative has every sign flipped. Minus, x squared minus five x minus two, is minus x squared plus five x plus two. It is not minus x squared minus five x minus two.

@art sign-flip-row
That's the distributive law with minus one. Nothing is being remembered here, every sign is computed. The safest habit is to write the negated polynomial out on its own line before you add anything. It costs one line.

@chapter One subtraction, in full
@math heading="(4x² − 3x + 6) − (x² − 5x − 2)" items="−(x² − 5x − 2) = −x² + 5x + 2@negate;;(4x² − 3x + 6) + (−x² + 5x + 2)@an addition;;x²: 4 + (−1) = 3@four plus minus one;;x: −3 + 5 = 2@minus three plus five;;1: 6 + 2 = 8@six plus two;;3x² + 2x + 8@the answer"
Four x squared minus three x plus six, minus x squared minus five x minus two. First negate: minus x squared plus five x plus two. Now it's an addition. Four plus minus one is three. Minus three plus five is two. Six plus two is eight. So the answer is three x squared plus two x plus eight.

@words text="Check at x = 1: 13 and 13" sub="7 − (−6) = 13 · 3 + 2 + 8 = 13"
Check by substituting a number. At x equals one the original is seven minus minus six, thirteen. The answer is three plus two plus eight, also thirteen. One substitution catches nearly every sign error.

@chapter What happens to the degree
@art cancelling-leaders
The degree of a sum is at most the larger of the two degrees. Usually it equals it, but if the leading terms cancel, it drops.

@math items="(5x⁴ − 2x² + x) + (−5x⁴ + 2x² + 3) = x + 3@five x to the fourth;;degree 4 + degree 4 → degree 1@degree four"
Five x to the fourth minus two x squared plus x, plus minus five x to the fourth plus two x squared plus three, is x plus three. Degree four plus degree four gives degree one. Addition can lower a degree. It can never raise one.

@chapter Where people slip
@list heading="Common slips" items="Distributing the minus to the first term only@The first|Adding the exponents@The second|Forcing unlike terms together@The third"
The first slip is distributing the minus sign to the first term only, which is the most common single error in the course. The second is adding exponents when you add like terms. Three x squared plus five x squared is eight x squared, not eight x to the fourth. The third is forcing unlike terms together. x squared plus x cubed is already finished.

@chapter Try it
@words text="(3x³ − 2x + 4) − (−x³ + 5x − 6)" sub="negation: +x³ − 5x + 6"
Your turn. Three x cubed minus two x plus four, minus, minus x cubed plus five x minus six. The negation is x cubed minus five x plus six. Collect the three powers, and check at x equals one.

@math items="4x³ − 7x + 10@four x cubed;;at x = 1: both give 7@give seven"
You should get four x cubed minus seven x plus ten, and at x equals one both the original and the answer give seven. A middle term of plus three x means the five x wasn't negated.

@end text="Negate on its own line"
You can add and subtract any two polynomials and see the negation step written out, on Learn. That's learn dot get er done dot I O.

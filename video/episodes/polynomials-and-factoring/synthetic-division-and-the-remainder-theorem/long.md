---
format: long
lesson: polynomials-and-factoring/synthetic-division-and-the-remainder-theorem
title: Synthetic division, and why the remainder is f of c
thumb: The remainder is f(c)
---

@chapter The question
@title text="Synthetic Division and the Remainder Theorem" sub="Polynomials and Factoring" art=thumb
Dividing by x minus c with long division, you write the same powers of x on every line. They carry no information. Strip them out, and the whole division fits in one row of numbers.

@art stripped-columns
Because the divisor is x minus c, and its leading coefficient is one, each quotient coefficient is just the leading number on the line before. And each subtraction becomes an addition, once you flip the sign of c.

@chapter The method
@list heading="Synthetic division" items="Write c, then every coefficient@write c|Bring down the first@bring down|Multiply by c, add to the next@multiply it by c|Last number: the remainder@the remainder"
Here's the method. Write c, then the coefficients of f in descending order, with zeros for any missing powers. Bring down the first coefficient. Multiply it by c, add that to the next coefficient, and repeat. The final number is the remainder. The others are the quotient.

@chapter A worked row
@art multiply-add-row
Divide two x cubed minus five x squared plus three x minus seven by x minus three. So c is three, and the row is two, minus five, three, minus seven.

@math heading="3 │ 2  −5  3  −7" items="bring down 2@bring down two;;2 · 3 = 6,  −5 + 6 = 1@two times three;;1 · 3 = 3,  3 + 3 = 6@one times three;;6 · 3 = 18,  −7 + 18 = 11@six times three"
Bring down two. Two times three is six, and minus five plus six is one. One times three is three, and three plus three is six. Six times three is eighteen, and minus seven plus eighteen is eleven.

@math items="quotient 2x² + x + 6@the quotient;;remainder 11@the remainder"
So the quotient is two x squared plus x plus six, and the remainder is eleven.

@art one-degree-down
The quotient drops exactly one degree, because a cubic divided by a linear polynomial is a quadratic. If your quotient has the same degree as f, you've kept one number too many. The last one is the remainder.

@chapter The sign of c
@words text="x + 4 = x − (−4)   →   c = −4"
The divisor must be written as x minus c, so c is what's being subtracted. For x minus three, c is three. For x plus four, write it as x minus minus four, so c is minus four.

@art wrong-divisor
Use plus four there, and you've divided by x minus four, a different polynomial. You get a wrong answer that looks perfectly well formed, which is the argument for always checking.

@math heading="(x³ + 2x² − 5x + 1) ÷ (x + 4)" items="c = −4 │ 1  2  −5  1@minus four;;1 · (−4) = −4,  2 + (−4) = −2@two plus minus four;;(−2)(−4) = 8,  −5 + 8 = 3@minus five plus eight;;3 · (−4) = −12,  1 + (−12) = −11@minus eleven"
With c equal to minus four, the row is one, two, minus five, one. Bring down one. Two plus minus four is minus two. Minus two times minus four is eight, and minus five plus eight is three. Three times minus four is minus twelve, leaving minus eleven. Quotient x squared minus two x plus three, remainder minus eleven.

@chapter The remainder theorem
@math heading="The remainder is f(c)" items="f(x) = (x − c)q(x) + r@f of x equals;;f(c) = (c − c)q(c) + r@at x equals c;;= 0 · q(c) + r = r@zero times"
Now the remarkable part. Dividing f by x minus c gives f of x equals x minus c, times q of x, plus r, and r is a constant. That holds for every x, so it holds at x equals c. Then the first part is zero times q of c, which leaves r.

@math heading="Check" items="f(3) = 54 − 45 + 9 − 7 = 11@f of three;;g(−4) = −64 + 32 + 20 + 1 = −11@g of minus four"
Check it. f of three is fifty-four minus forty-five plus nine minus seven, which is eleven, the remainder we found. And for the second, g of minus four is minus sixty-four plus thirty-two plus twenty plus one, minus eleven. Again, the remainder.

@art two-directions
That points two ways. It's a fast way to evaluate a polynomial, three multiplications and three additions for a cubic. And a remainder of zero means f of c is zero. That's where the factor theorem begins.

@chapter Where people slip
@list heading="Common slips" items="Using the sign printed in the divisor@The first|Leaving out zero coefficients@The second|Reading the remainder as part of the quotient@The third"
The first slip is using the sign printed in the divisor. The second is leaving out zero coefficients. x cubed minus eight must go in as one, zero, zero, minus eight. And the third is reading the remainder as part of the quotient, which makes the quotient a degree too high.

@chapter Try it
@words text="(x³ − 4x² + x + 6) ÷ (x − 2)" sub="2 │ 1  −4  1  6"
Your turn. Divide x cubed minus four x squared plus x plus six by x minus two. The setup is two, then one, minus four, one, six. Complete the row, name the quotient, and check the last number against f of two.

@math items="1, −2, −3, 0@the bottom row;;q = x² − 2x − 3,  remainder 0@the remainder is zero"
The bottom row is one, minus two, minus three, zero. So the quotient is x squared minus two x minus three, and the remainder is zero. If you used minus two as c, you divided by something else.

@end text="Watch the row compute f(c)"
You can build the row one step at a time and watch it agree with f of c, on Learn. That's learn dot get er done dot I O.

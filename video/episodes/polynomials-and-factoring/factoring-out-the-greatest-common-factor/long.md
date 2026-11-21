---
format: long
lesson: polynomials-and-factoring/factoring-out-the-greatest-common-factor
title: Factoring out the greatest common factor, and checking it
thumb: The poorest term decides
---

@chapter The question
@title text="Factoring Out the Greatest Common Factor" sub="Polynomials and Factoring" art=thumb
Factoring is multiplication run backwards. And the first move, every single time, is to pull out whatever every term shares. That's the greatest common factor.

@math heading="The distributive law, backwards" items="ab + ac = a(b + c)@a b plus a c;;x² + 5x = x(x + 5)@x squared plus five x"
To factor a polynomial is to write it as a product. The licence is the distributive law read right to left: a b plus a c equals a times b plus c. So x squared plus five x is x times x plus five.

@art product-is-zero
That isn't simpler to look at. It's more useful. A product tells you when the whole thing is zero, and a sum doesn't.

@chapter What the GCF is
@art shared-core
For terms with integer coefficients, the greatest common factor is the largest monomial that divides all of them. Its coefficient is the greatest common divisor of the coefficients. And each variable appears to the lowest power it has in every term.

@words text="lowest power, in every term" sub="a missing variable is missing from the GCF"
The word to hold on to is lowest. A term with only three x's can't supply four. And a variable that's missing from even one term is missing from the GCF entirely.

@chapter A worked example
@math heading="12x⁴y − 18x³y² + 6x³y" items="gcd(12, 18, 6) = 6@twelve, eighteen and six;;x: powers 4, 3, 3 → x³@four, three, three;;y: powers 1, 2, 1 → y@one, two, one;;GCF = 6x³y@six x cubed y"
Take twelve x to the fourth y, minus eighteen x cubed y squared, plus six x cubed y. The coefficients are twelve, eighteen and six, with greatest common divisor six. The x powers are four, three, three, so x cubed. The y powers are one, two, one, so y. The GCF is six x cubed y.

@math heading="Divide each term by 6x³y" items="12x⁴y ÷ 6x³y = 2x@two x;;−18x³y² ÷ 6x³y = −3y@minus three y;;6x³y ÷ 6x³y = 1@leaves one;;6x³y(2x − 3y + 1)@the answer"
Now divide each term by it. The first gives two x. The second gives minus three y. And the third is the GCF itself, so it leaves one. The answer is six x cubed y times two x minus three y plus one.

@art leftover-one
Three terms went in, so three terms come out in the bracket. That count is the fastest check that nothing was dropped. Write the one. Five x squared plus five x is five x times x plus one, not five x times x.

@math heading="Check by expanding" items="6x³y · 2x = 12x⁴y@times two x;;6x³y · (−3y) = −18x³y²@times minus three y;;6x³y · 1 = 6x³y@times one"
Then expand to check. Six x cubed y times two x, times minus three y, and times one gives back all three terms. This is the one topic where checking is faster than producing the answer.

@chapter Negatives and greatest
@math heading="Take the minus out too" items="−4x³ + 8x² − 12x = −4x(x² − 2x + 3)@minus four x"
When the leading coefficient is negative, take the minus out with the GCF. Minus four x cubed plus eight x squared minus twelve x is minus four x times x squared minus two x plus three. Every sign in the bracket flips.

@art still-shared
And it has to be the greatest. Twelve x squared plus eighteen x equals two x times six x plus nine. That's true, but incomplete, because six x plus nine still has a three in it. The full answer is six x times two x plus three.

@words text="6x³ + 9x² + 4x = x(6x² + 9x + 4)" sub="gcd(6, 9, 4) = 1"
A factor shared by two terms out of three isn't common. In six x cubed plus nine x squared plus four x, the gcd is one, and the last term has only x. So the GCF is just x, and that's all you can take.

@chapter Where people slip
@list heading="Common slips" items="Dropping the 1@The first|Taking out a factor missing from one term@The second|Stopping at a factor that isn't the greatest@The third"
The first slip is dropping the one when a term is the GCF. The second is taking out a factor missing from one term. Pull x squared out of that last example and you're left with x to the minus one. And the third is stopping at a factor that isn't the greatest. Always look at the bracket again.

@art first-step
Take it out first, always. Every later technique assumes the easy factor is gone, and skipping it leaves you searching numbers far too large.

@chapter Try it
@words text="−18x⁴ + 30x³ − 12x²" sub="take the negative out"
Your turn. Minus eighteen x to the fourth, plus thirty x cubed, minus twelve x squared. Take the negative out so the bracket starts positive. Find the gcd and the lowest power of x, divide all three terms, then expand.

@math items="−6x²(3x² − 5x + 2)@minus six x squared"
You should get minus six x squared, times three x squared minus five x plus two. If your bracket has only two terms, you dropped the two from the last one.

@end text="Find it, take it, expand it"
You can type any polynomial and watch the GCF found, taken out and expanded back, on Learn. That's learn dot get er done dot I O.

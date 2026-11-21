---
format: long
lesson: rational-and-radical-expressions/simplifying-rational-expressions
title: Simplifying rational expressions: cancel factors, never terms
thumb: Factors cancel. Terms don't.
---

@chapter One rule
@title text="Simplifying Rational Expressions" sub="Rational and Radical Expressions" art=thumb
Simplifying a rational expression comes down to one rule. A factor shared by the top and the bottom may be removed. A term may not. The gap between those two words causes more lost marks than almost anything else in school algebra.

@math heading="The fundamental principle" items="(P·K) / (Q·K) = P / Q@P K over Q K;;Q ≠ 0,  K ≠ 0@as long as"
Here's the rule. P K over Q K equals P over Q, as long as Q and K aren't zero. It works because K over K is one, and multiplying by one changes nothing. That's also why K can't be zero: zero over zero is not one.

@art factor-vs-term
K multiplies P, and K multiplies Q. Nothing in that rule lets you remove something that's added to P. A factor is joined to the rest by multiplication. A term is joined by addition. Two x over two y cancels to x over y. Two plus x, over two plus y, cancels to nothing.

@chapter The method
@list heading="The method" items="Factor the top completely@Factor the numerator|Factor the bottom completely@factor the denominator|Record the excluded values@record the excluded|Cancel the shared factors@strike out"
So factoring isn't optional. Factor the numerator completely, factor the denominator completely, record the excluded values, and then strike out the factors that appear in both.

@art strike-out
You can't cancel what you can't see. In x squared minus nine, over x squared plus x minus twelve, a common factor is there, but it's hidden until both lines are factored.

@art lowest-terms
And when nothing is left to strike, the top and bottom share no factor except a constant. That's what lowest terms means.

@chapter A legal cancellation
@math heading="(x² − 9) / (x² + x − 12)" items="= (x − 3)(x + 3) / ((x + 4)(x − 3))@factors as;;excluded: x ≠ 3,  x ≠ −4@both are excluded;;= (x + 3) / (x + 4),  x ≠ 3,  x ≠ −4@removing it"
Take x squared minus nine, over x squared plus x minus twelve. It factors as x minus three times x plus three, over x plus four times x minus three. The bottom is zero at three and at minus four, so both are excluded. x minus three is common, and removing it leaves x plus three over x plus four.

@math heading="Check" items="x = 0:  −9/−12 = 3/4  and  3/4  ✓@at zero;;x = 1:  −8/−10 = 4/5  and  4/5  ✓@at one;;x = 3:  original undefined,  reduced 6/7@at three"
Check it. At zero, minus nine over minus twelve is three quarters, and so is the answer. At one, both give four fifths. But at three, the original is undefined, while x plus three over x plus four is happy to give six sevenths.

@art missing-point
That's why the exclusion is written twice. The two expressions agree everywhere except that single point, where one exists and the other doesn't. Nothing about six sevenths tells you it shouldn't be there. Only the condition you carried does.

@chapter Opposite factors
@art opposite-arrows
Some pairs look different but share a factor. a minus b and b minus a differ only by a sign. a minus b is minus, b minus a. So when the top and bottom look like opposites, their quotient is minus one.

@math heading="(3 − x) / (x − 3)" items="3 − x = −(x − 3)@write the top;;= −(x − 3) / (x − 3) = −1,  x ≠ 3@becomes;;x = 0:  3/(−3) = −1  ✓@checking at zero"
Take three minus x, over x minus three. Write the top as minus, x minus three. The expression becomes minus one, for every x except three. Checking at zero gives three over minus three, which is minus one. It agrees.

@chapter The tempting mistake
@words text="(x + 3) / x" sub="already in lowest terms"
Now the error the whole lesson is aimed at. In x plus three, over x, the x on the bottom is a factor of the denominator, but only a term of the numerator. Nothing cancels. The expression is already in lowest terms, and the answer is not three.

@art spot-check
One number catches it. At x equals one, x plus three over x is four over one, which is four. At x equals three, it's six over three, which is two. Neither is three. A simplification is an identity, and an identity that fails at x equals one is not an identity.

@chapter Where people slip
@list heading="Common slips" items="Cancelling a term on both lines@The first|Dropping the exclusions@The second|Missing an opposite pair@the third"
The first slip is cancelling a term because it's on both lines. x plus three over x plus four isn't three quarters; at one it's four fifths. The second is dropping the exclusions on the way. And the third is missing an opposite pair: four minus x squared, over x minus two, is minus, x plus two.

@chapter Try it
@words text="(x² − 16) / (x² + x − 20)" sub="factor first, record the exclusions, then cancel"
Your turn. Simplify x squared minus sixteen, over x squared plus x minus twenty. Factor both lines before you cancel, write down where the original bottom is zero, cancel one factor, and check your answer at x equals zero.

@end text="Factor first, then cancel"
You can practise spotting factors you're allowed to cancel on Learn. That's learn dot get er done dot I O.

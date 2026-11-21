---
format: long
lesson: algebra-foundations/scientific-notation
title: Scientific notation: huge and tiny numbers, made readable
thumb: Replace the zeros with a number
---

@chapter The problem
@title text="Scientific Notation" sub="Algebra Foundations" art=thumb
Try reading six hundred two, followed by twenty one zeros. You can't, not reliably. Nobody counts twenty one zeros without slipping, so the notation itself causes errors. Scientific notation replaces the zeros with a number.

@art long-zeros
Very big and very small numbers share the same problem. A long string of placeholders, and all the meaning is in how many there are.

@chapter The form
@words text="a × 10ⁿ" sub="1 ≤ |a| < 10,   n an integer"
A number is in scientific notation when it's written a times ten to the n, where the size of a is at least one and less than ten, and n is an integer. a is the mantissa, and n is the exponent.

@words text="12.5 × 10³ = 1.25 × 10⁴" sub="right value, wrong form"
Every real number except zero has exactly one such form. Twelve point five times ten cubed is a correct way to write twelve thousand five hundred. It just isn't scientific notation, because twelve point five isn't below ten. Renormalised, it's one point two five times ten to the fourth.

@art magnitude-ladder
The form lets you compare at a glance. Compare exponents first, and mantissas only if the exponents tie. So eight point nine times ten to the minus five is smaller than one point two times ten to the minus four.

@chapter Converting
@art point-left
To convert, move the decimal point until exactly one nonzero digit stands in front of it. Count the places you moved. That count is the exponent.

@math items="93000 → 9.3 × 10⁴@ninety three thousand;;0.00072 → 7.2 × 10⁻⁴@zero point zero zero zero seven two"
Ninety three thousand: the point moves four places left, so it's nine point three times ten to the fourth. Zero point zero zero zero seven two: the point moves four places right, so it's seven point two times ten to the minus four.

@art point-right
Then check the sign by the size of the number, not by your count. A size of at least one means the exponent is zero or more. A size below one means it's negative. That even covers minus ninety three thousand, whose exponent is positive.

@words text="9.3 × 10⁵ = 930000" sub="count places moved, not zeros"
And don't count zeros. Nine times ten to the fifth is nine with five zeros, so the shortcut looks safe. But nine point three times ten to the fifth is nine hundred thirty thousand: ninety three, followed by four zeros.

@chapter Multiplying and dividing
@math items="(3 × 10⁸)(2 × 10⁻³) = 6 × 10⁵@three times ten to the eighth;;(9.9 × 10³) / (2 × 10²) = 4.95 × 10¹@nine point nine"
To multiply, multiply the mantissas and add the exponents. Three times ten to the eighth, times two times ten to the minus three, is six times ten to the fifth. To divide, divide the mantissas and subtract the exponents. Nine point nine over two is four point nine five, and three minus two is one.

@art seesaw
The result might not be normalised, and that's expected. If the mantissa reaches ten, move the point one place left and add one to the exponent. If it falls below one, move it right and subtract one. The mantissa's move is always paid for by the exponent.

@math heading="(6.4 × 10⁵)(5 × 10⁻⁸)" items="6.4 · 5 = 32@six point four times five;;5 + (−8) = −3@five plus minus eight;;32 × 10⁻³ = 3.2 × 10⁻²@renormalise"
Here's the first worked example. Six point four times five is thirty two. Five plus minus eight is minus three. Thirty two times ten to the minus three is the right value, but the mantissa's too big. Renormalise, and it's three point two times ten to the minus two.

@math heading="(1.5 × 10³) / (6 × 10⁷)" items="1.5 / 6 = 0.25@one point five over six;;3 − 7 = −4@three minus seven;;0.25 × 10⁻⁴ = 2.5 × 10⁻⁵@too small"
And the other direction. One point five over six is zero point two five. Three minus seven is minus four. Now the mantissa is too small, so the point moves right, the exponent drops by one, and you get two point five times ten to the minus five.

@chapter Adding
@art align-stacks
Addition is the operation this form doesn't make easy. Before you touch the mantissas, both numbers need the same power of ten. It's the same move as finding a common denominator, and it's the step people skip.

@math heading="1.2 × 10⁵ + 3.4 × 10⁴" items="= 1.2 × 10⁵ + 0.34 × 10⁵@zero point three four;;= (1.2 + 0.34) × 10⁵@add the mantissas;;= 1.54 × 10⁵@one point five four"
So rewrite three point four times ten to the fourth as zero point three four times ten to the fifth. That line isn't in the form, and it doesn't need to be. Now add the mantissas, and you get one point five four times ten to the fifth.

@chapter Where people slip
@list heading="Common slips" items="Counting zeros instead of moving the point@counting zeros|Renormalising the mantissa only@renormalising|Adding mantissas with different exponents@adding the mantissas"
Three slips. Counting zeros instead of moving the point. Renormalising the mantissa and leaving the exponent alone: twelve times ten to the fourth is one point two times ten to the fifth, not the fourth. And adding the mantissas while the exponents differ.

@chapter Try it
@words text="(2.5 × 10⁻³)(4 × 10⁶)"
Try two point five times ten to the minus three, times four times ten to the sixth. Multiply the mantissas and add the exponents first. You'll get ten times ten cubed. Then normalise, to one times ten to the fourth.

@end text="Two numbers, one operation"
You can pick two numbers and an operation, and predict the exponent before you see it, on Learn. That's learn dot get er done dot I O.

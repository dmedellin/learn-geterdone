---
format: long
lesson: algebra-foundations/integer-exponents
title: Integer exponents: the laws are just counting
thumb: The laws are just counting
---

@chapter The idea
@title text="Integer Exponents" sub="Algebra Foundations" art=thumb
Exponent laws look like rules to memorise. They're not. Each one is just counting factors. And once you see that, zero and negative exponents stop being mysterious too.

@words text="xⁿ = x · x · … · x" sub="n factors of x"
For a whole number n, one or more, x to the n means n factors of x, multiplied together. x is the base and n is the exponent, and x to the one is just x. Notice this says nothing about zero or negative n. Those come later.

@chapter Three laws by counting
@art factor-blocks
The product law: x to the m, times x to the n, is x to the m plus n. Why? x to the m is m factors, and x to the n is n factors, so the product has m plus n factors.

@art cancel-pairs
The quotient law: x to the m over x to the n is x to the m minus n, when x isn't zero and m is bigger than n. Each of the n factors below cancels one above, which leaves m minus n.

@art power-groups
And the power law: x to the m, all to the n, is x to the m n. That's n copies of a block of m factors, so m times n factors in all.

@math items="x² · x³ = (x·x)(x·x·x) = x⁵@x squared times x cubed;;x⁵ / x² = x³@x to the fifth over x squared;;(x²)³ = x⁶@x squared, cubed"
So x squared times x cubed is x to the fifth. x to the fifth over x squared is x cubed. And x squared, cubed, is x to the sixth. If you forget which law adds and which multiplies, write out the factors for a small case.

@chapter Over products, not sums
@words text="(xy)ⁿ = xⁿyⁿ" sub="but (x + y)² ≠ x² + y²"
An exponent distributes over a product, and over a quotient. It doesn't distribute over a sum. At x equals one and y equals three, x plus y, squared, is sixteen, while x squared plus y squared is ten.

@chapter Zero and negative exponents
@math heading="What would the laws need?" items="x³ / x³ = x³⁻³ = x⁰@if the quotient law;;x³ / x³ = 1@arithmetic says;;so x⁰ = 1@so x to the zero"
Those laws were proved for positive exponents. So ask what they'd need if we extended them. If the quotient law holds when the exponents are equal, x cubed over x cubed is x to the zero. Arithmetic says it's one. So x to the zero must be one.

@math items="x³ · x⁻³ = x⁰ = 1@x cubed times;;so x⁻³ = 1 / x³@one over x cubed"
The same idea works with the product law. x cubed times x to the minus three is x to the zero, which is one. So x to the minus three must be one over x cubed.

@art halving-steps
These are definitions, not consequences. They're the only values that keep the laws true for every integer exponent, which is why they were chosen. Both need x not to be zero, so zero to the zero is left undefined here.

@words text="2⁻³ = 1/8" sub="a positive number"
A negative exponent doesn't make the value negative. Two to the minus three is one eighth, a positive number. The exponent's sign says which side of the fraction bar the power belongs on. The value's sign comes from the base.

@art cross-bar
That gives you a handy move. A factor may cross the fraction bar if its exponent changes sign. x to the minus two, over y to the minus three, is y cubed over x squared. That's not a new rule. It's the definition, used twice.

@chapter Every law at once
@math heading="(2x³y⁻²)⁻² · (4x⁻¹y³)" items="2⁻² = 1/4,    (x³)⁻² = x⁻⁶,    (y⁻²)⁻² = y⁴@the outer exponent"
Here's the worked example, with x and y not zero. First, the outer exponent goes onto every factor in the bracket. Two to the minus two is a quarter. x cubed becomes x to the minus six. And y to the minus two becomes y to the fourth.

@math items="(1/4) · 4 = 1@a quarter times four;;x⁻⁶ · x⁻¹ = x⁻⁷@x to the minus six;;y⁴ · y³ = y⁷@y to the fourth;;answer:   y⁷ / x⁷@so the answer"
Now collect one base at a time. A quarter times four is one. x to the minus six times x to the minus one is x to the minus seven. y to the fourth times y cubed is y to the seventh. So the answer is y to the seventh over x to the seventh.

@chapter Where people slip
@list heading="Common slips" items="Multiplying exponents when bases multiply@multiplying the exponents|Combining different bases@two different bases|Reading a negative exponent as negative@reading a negative exponent"
Three slips. Multiplying the exponents when you multiply powers: x squared times x cubed is x to the fifth, not the sixth. Combining two different bases. And reading a negative exponent as a negative value.

@art different-bases
Every one of these laws starts with a single base. Two cubed times three squared is eight times nine, which is seventy two, and no law turns that into one power. Different bases stay apart.

@chapter Try it
@words text="(3x⁻²)² · x⁵" sub="with x ≠ 0"
Try three x to the minus two, squared, times x to the fifth. The bracket gives nine x to the minus four. Then minus four plus five is one, so the answer is nine x. If you got three x, you forgot the square applies to the three as well.

@end text="Each law, computed twice"
You can check every law against the powers written out as products, on Learn. That's learn dot get er done dot I O.

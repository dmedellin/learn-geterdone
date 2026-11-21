---
format: long
lesson: laplace-transforms/partial-fractions-exactly
title: Partial fractions for Laplace: one term for every power
thumb: Every power gets a term
---

@chapter The question
@title text="Partial Fractions, Exactly" sub="Laplace Transforms" art=thumb
Solving by transform leaves you with a fraction in s that isn't in the table. Partial fractions takes it apart into pieces that are. The trick is knowing which pieces to write before you compute anything.

@chapter The shape comes first
@art factor-tree
The denominator decides the shape. So factor it first, into linear pieces, and any quadratics that won't factor over the reals.

@list heading="The form" items="(s − a):  A/(s − a)@distinct linear factor|(s − a)^m:  m terms, powers 1 to m@repeated|irreducible quadratic q:  (B·s + C)/q@irreducible quadratic"
Each distinct linear factor gets one term, A over s minus a. A factor repeated m times gets m terms, one for every power from one up to m. And each irreducible quadratic gets a two-part numerator, B s plus C, over the quadratic.

@art pieces
The numerator has to be of lower degree than the denominator. Then the job is finding numbers for a form that's already written down.

@chapter Distinct factors
@math heading="(s + 3)/((s + 1)(s + 2))" items="s + 3 = A·(s + 2) + B·(s + 1)@Multiply through;;s = −1:  2 = A@At s equals minus one;;s = −2:  1 = −B@At s equals minus two"
Write A over s plus one, plus B over s plus two. Multiply through by the whole denominator, and s plus three equals A times s plus two, plus B times s plus one. That holds for every s. At s equals minus one, the B term vanishes, so A is two. At s equals minus two, the A term vanishes, so B is minus one.

@art clear-denominators
That identity is the key move every time. Once the denominators are cleared, you're comparing two polynomials in s, and they must agree at every value of s and in every power.

@chapter A repeated factor
@math heading="1/(s·(s + 1)²)" items="= A/s + B/(s + 1) + C/(s + 1)²@three terms;;1 = A·(s + 1)² + B·s·(s + 1) + C·s@clear;;s = 0:  A = 1    s = −1:  C = −1@At s equals zero;;s² terms:  0 = A + B,  B = −1@compare the s squared"
Here s appears once and s plus one twice, so there are three terms. Clear the denominators. At s equals zero, A is one. At s equals minus one, one equals minus C, so C is minus one. No value of s isolates B, so compare the s squared terms on both sides: zero equals A plus B, so B is minus one.

@math heading="invert" items="F = 1/s − 1/(s + 1) − 1/(s + 1)²@F is one over s;;f = 1 − e^(−t) − t·e^(−t)@one minus e;;s = 1:  1/4 = 1 − 1/2 − 1/4  ✓@Spot check"
So F is one over s, minus one over s plus one, minus one over s plus one squared. Inverting, f is one minus e to the minus t, minus t e to the minus t. Spot check at s equals one: the left side is a quarter, and the right is one minus a half minus a quarter, also a quarter.

@art t-times-decay
That t e to the minus t is what the repeated factor buys. A single s plus one would give only e to the minus t. The square gives that, and the same exponential times t.

@chapter Why every power
@art missing-term
Suppose you wrote only A over s plus C over s plus one squared. Clearing gives one equals A times s plus one squared, plus C s. The s squared coefficient is A, which must be zero. But s equals zero says A is one. That's a contradiction, so no such A and C exist. The middle term supplies the missing s squared.

@chapter An irreducible quadratic
@math heading="1/(s·(s² + 2s + 5))" items="2² − 4·5 = −16 < 0@no real roots;;= A/s + (B·s + C)/(s² + 2s + 5)@B s plus C;;A = 1/5,   B = −1/5,   C = −2/5@one fifth"
Now one over s times s squared plus two s plus five. That quadratic has no real roots, since two squared minus four times five is minus sixteen. So write A over s, plus B s plus C over the quadratic. At s equals zero, one equals five A, so A is one fifth. The s squared terms give B as minus one fifth, and the s terms give C as minus two fifths.

@math heading="s² + 2s + 5 = (s + 1)² + 4" items="s + 2 = (s + 1) + 1@split the numerator;;f = 1/5 − (1/5)·e^(−t)·cos(2t) − (1/10)·e^(−t)·sin(2t)@one fifth minus"
To invert, complete the square: s plus one, squared, plus four. Then split the numerator s plus two as s plus one, plus one. The first part is the shifted cosine. The leftover one is half the sine entry. So f is one fifth, minus a fifth e to the minus t cos two t, minus a tenth e to the minus t sine two t.

@art shifted-wave
Each term is a table entry read backwards. Finding the coefficients is the arithmetic. Inverting is just reading from right to left.

@chapter Where people slip
@list heading="Common slips" items="Only the highest power of a repeated factor@The first|A bare constant over a quadratic@The second|Inverting s + 2 as a pure cosine@And the third"
The first slip is writing only the highest power of a repeated factor. The second is putting a bare constant over an irreducible quadratic. That's too few unknowns, and the equations can't be met. And the third is inverting s plus two over the quadratic as a pure shifted cosine, which loses the sine term.

@chapter Try it
@words text="1/(s·(s + 1)²)" sub="write the form, then find A, B, C"
Your turn. Rebuild the repeated-factor example yourself. Write the three-term form, clear the denominators, substitute both roots, compare the s squared terms for the last coefficient, and invert. Then spot check at s equals one.

@end text="Take a fraction apart exactly"
You can decompose your own fractions, in exact arithmetic, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: sequences-and-series/the-general-term-of-an-expansion
title: Finding one term of a binomial expansion, or proving it isn't there
thumb: Solve for k
---

@chapter One term, not all of them
@title text="The General Term of an Expansion" sub="Sequences and Series" art=thumb
Most questions about an expansion want just one term. The term in x to the fifth, the constant term, the middle term. You don't need to expand the whole thing to find it.

@math heading="The general term" items="C(n, k) aⁿ⁻ᵏ bᵏ,   k = 0, 1, …, n@C of n, k;;it is term number k + 1@term number k plus one"
In the expansion of a plus b to the n, the general term is C of n, k, times a to the n minus k, times b to the k. Since k starts at zero, that's term number k plus one.

@art one-card
Some books number the terms differently, so the safe habit is to describe a term by the power it contains, not its position. Choose k, and everything else is settled: the coefficient, both powers, and the sign.

@chapter Collect the powers of x
@math heading="(x + 2/x)⁶" items="C(6, k) x⁶⁻ᵏ (2/x)ᵏ@C of six, k;;= C(6, k) · 2ᵏ · x⁶⁻²ᵏ@collect"
When a and b carry powers of x, both contribute. In x plus two over x, to the sixth, the general term is C of six, k, times x to the six minus k, times two over x to the k. Collect the powers, and the term holds x to the six minus two k.

@math heading="The constant term" items="6 − 2k = 0  →  k = 3@six minus two k;;C(6, 3) · 2³ = 20 · 8 = 160@one hundred and sixty"
For the constant term, set six minus two k equal to zero. So k is three, and the term is C of six, three times two cubed. That's twenty times eight, one hundred and sixty. Six of the seven terms never had to be computed.

@art ladder-hit
That's the whole method. Collect the power of x, set it equal to the power you want, and solve for k. Then k must pass two tests: it has to be a whole number, and it has to lie between zero and n.

@chapter When there's no such term
@math heading="(x² + 1/x)⁸" items="C(8, k) x¹⁶⁻³ᵏ@sixteen minus three k;;16 − 3k = 0  →  k = 16/3@sixteen thirds"
Try x squared plus one over x, to the eighth. The term holds x to the sixteen minus three k. Setting that to zero gives k equals sixteen thirds, which isn't a whole number.

@art ladder-miss
The powers run sixteen, thirteen, ten, seven, four, one, minus two, minus five, minus eight. They step right over zero. So the expansion has no constant term, and that is the answer. Don't round k: rounding just finds some other term.

@chapter A harder one
@math heading="Constant term of (2x² − 3/x)⁹" items="power of x:  2(9 − k) − k = 18 − 3k@the power of x;;18 − 3k = 0  →  k = 6@k is six"
Now two x squared minus three over x, to the ninth. The first part contributes two times nine minus k to the power of x, and the second contributes minus k. Together, eighteen minus three k, so k is six.

@math heading="k = 6" items="C(9, 6) · 2³ · (−3)⁶ = 84 · 8 · 729@eighty four;;= 489888@four hundred"
The term is C of nine, six, eighty four, times two cubed, times minus three to the sixth. That's four hundred and eighty nine thousand, eight hundred and eighty eight.

@art two-pulls
Check it by recomputing the exponent from the two factors separately. Two x squared, cubed, is eight x to the sixth. Minus three over x, to the sixth, is seven hundred twenty nine over x to the sixth. They cancel, so the term really is constant.

@chapter Middle terms
@art middle-pair
An expansion to the n has n plus one terms. For odd n there are two middle terms, with equal coefficients. In two x minus one, to the seventh, they're k equals three and four, and C of seven, three equals C of seven, four, thirty five.

@math heading="(2x − 1)⁷" items="k = 3:   35(2x)⁴(−1)³ = −560x⁴@minus five hundred and sixty;;k = 4:   35(2x)³(−1)⁴ = 280x³@two hundred and eighty"
But the terms aren't equal. At k equals three, it's minus five hundred and sixty x to the fourth. At k equals four, it's two hundred and eighty x cubed. The symmetry belongs to C of n, k, and the powers of two x and minus one break it.

@chapter Common slips
@list heading="Common slips" items="Taking the power of x from one part only@First|Rounding a fractional k@Second|Swapping the exponents of a and b@Third"
First, taking the power of x from only one part. In the last example, forgetting the minus k gives a constant term at k equals nine, which is really minus nineteen thousand six hundred eighty three over x to the ninth. Second, rounding a fractional k. Third, putting k on a and n minus k on b.

@art mirror-swap
That swap gives the mirror term. In x plus three, to the tenth, the coefficient of x to the seventh is three thousand two hundred forty. Swap the exponents and you get two hundred sixty two thousand four hundred forty, which belongs to x cubed.

@chapter Try it
@words text="constant term of (x³ − 2/x)⁸" sub="a = x³,  b = −2/x,  n = 8"
Your turn. Find the constant term of x cubed minus two over x, to the eighth. Write the general term, collect both contributions to the power of x, solve for k, and check it's a whole number in range. Then recompute the exponent from the two factors separately.

@end text="One term, both ways"
You can build one term from the general term and check it against the full expansion, on Learn. That's learn dot get er done dot I O.

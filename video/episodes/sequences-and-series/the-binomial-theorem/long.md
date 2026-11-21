---
format: long
lesson: sequences-and-series/the-binomial-theorem
title: The binomial theorem: expand any power without multiplying it out
thumb: The coefficients count
---

@chapter Too many brackets
@title text="The Binomial Theorem" sub="Sequences and Series" art=thumb
You can multiply out a plus b, squared, or cubed, by hand. To the fifth, with patience. But a plus b to the twelfth?

@art branching-tree
Multiplying out twelve brackets means two to the twelfth, four thousand and ninety six products, before you've collected anything. The binomial theorem skips all of it, and writes down the answer directly.

@chapter The pattern
@math heading="Small powers" items="(a + b)² = a² + 2ab + b²@squared;;(a + b)³ = a³ + 3a²b + 3ab² + b³@cubed;;(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴@to the fourth"
Look at the small cases. Squared: a squared plus two a b plus b squared. Cubed: a cubed plus three a squared b, plus three a b squared, plus b cubed. To the fourth, the coefficients are one, four, six, four, one.

@art exponent-balance
In every line, the power of a falls as the power of b rises, and the two always add up to the exponent outside. So a cubed b cubed can never appear in a plus b to the fifth.

@art triangle-row
Strip out the coefficients and you get Pascal's triangle. Row n holds the coefficients of a plus b to the n.

@chapter A formula for the coefficients
@math heading="n choose k" items="C(n, k) = n! / (k!(n − k)!)@C of n, k equals"
You don't have to build the triangle. C of n, k equals n factorial, over k factorial times n minus k factorial. It's read n choose k, and zero factorial is one.

@math heading="C(9, 4)" items="= 9! / (4! 5!)@nine factorial;;= (9·8·7·6) / (4·3·2·1)@the five factorial cancels;;= 3024 / 24 = 126@one hundred and twenty six"
Take C of nine, four: nine factorial over four factorial times five factorial. The five factorial cancels most of the top, leaving nine times eight times seven times six, over four times three times two times one. That's three thousand and twenty four over twenty four, one hundred and twenty six. No need to write nine factorial down at all.

@chapter The theorem
@math heading="The binomial theorem" items="(a + b)ⁿ = Σ C(n, k) aⁿ⁻ᵏ bᵏ,   k from 0 to n@a plus b to the n"
So a plus b to the n is the sum, for k from zero to n, of C of n, k, times a to the n minus k, times b to the k. That's n plus one terms.

@art bracket-choices
Why those coefficients? Expanding n brackets means picking a or b from each one and multiplying. You get a to the n minus k, b to the k exactly when b came from k of the brackets. The number of ways to choose which k is C of n, k.

@chapter Signs
@math heading="(a − b)⁴" items="= a⁴ − 4a³b + 6a²b² − 4ab³ + b⁴@a minus b"
For a minus b, treat it as a plus minus b. The coefficients are row four, unchanged. The signs come from minus b to the k, so the terms with odd k are negative. The last term is plus b to the fourth.

@art alternating-signs
That one surprises people, who expect it to be negative. Odd powers of a minus b end negative, and even powers end positive. Compute minus b to the k, and you never have to guess.

@chapter A worked expansion
@math heading="(2x − 3)⁴:   a = 2x,  b = −3" items="1·(2x)⁴ = 16x⁴@sixteen x;;4·(2x)³(−3) = −96x³@minus ninety six;;6·(2x)²(−3)² = 216x²@two hundred and sixteen x squared;;4·(2x)(−3)³ = −216x@minus two hundred and sixteen x;;1·(−3)⁴ = 81@eighty one"
Now two x minus three, to the fourth. Here a is two x, and b is minus three. Using row four: sixteen x to the fourth, minus ninety six x cubed, plus two hundred and sixteen x squared, minus two hundred and sixteen x, plus eighty one.

@words text="x = 1:   (2 − 3)⁴ = 1      16 − 96 + 216 − 216 + 81 = 1  ✓" sub="the sum of the coefficients"
Check by putting x equals one. The left side is minus one to the fourth, which is one. The right side is sixteen minus ninety six plus two sixteen minus two sixteen plus eighty one, also one.

@chapter Common slips
@art missing-middle
The worst slip is dropping the middle terms, as if a plus b to the n were a to the n plus b to the n. Put a and b equal to one: the left side is two to the n, the shortcut gives only two.

@list heading="Two more slips" items="Writing 2x³ for (2x)³@raising only part|Alternating signs by habit@guessing the signs"
The other two: raising only part of a term to the power, writing two x cubed for two x, all cubed, which is eight x cubed. And guessing the signs by habit instead of computing minus b to the k.

@chapter Try it
@words text="(x − 2)⁵" sub="a = x,  b = −2 ·  row 5: 1 5 10 10 5 1"
Your turn. Expand x minus two, to the fifth. Here a is x, b is minus two, and row five is one, five, ten, ten, five, one. Write all six terms before simplifying, then check by putting x equals one into both sides.

@end text="One row at a time"
You can build the triangle row by row and expand any power beside it, on Learn. That's learn dot get er done dot I O.

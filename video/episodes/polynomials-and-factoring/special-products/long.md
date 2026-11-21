---
format: long
lesson: polynomials-and-factoring/special-products
title: Special products: the patterns worth knowing by sight
thumb: Don't drop the 2ab
---

@chapter The question
@title text="Special Products" sub="Polynomials and Factoring" art=thumb
Some products turn up so often that it pays to know them on sight. They're ordinary multiplications, nothing new. They're singled out because each one runs backwards later, when you factor, and there recognition is the whole method.

@chapter Difference of squares
@math heading="(a + b)(a − b)" items="a² − ab + ba − b²@four products;;−ab + ba = 0@cancel;;= a² − b²@leaving"
Start with a plus b, times a minus b. Distribute the four products: a squared, minus a b, plus b a, minus b squared. The middle terms are like terms with opposite signs, so they cancel, leaving a squared minus b squared.

@art cancelling-middle
That cancellation is the whole content. It happens because the two brackets differ in only one sign. Three terms collapse to two.

@chapter Square of a binomial
@math heading="(a + b)²" items="(a + b)(a + b) = a² + ab + ba + b²@a plus b times a plus b;;= a² + 2ab + b²@two a b;;(a − b)² = a² − 2ab + b²@a minus b, all squared"
Now a plus b, all squared. That's a plus b times a plus b, which gives a squared plus a b plus b a plus b squared, so a squared plus two a b plus b squared. And a minus b, all squared, is a squared minus two a b plus b squared.

@art square-tiles
The two forms are really one result. The last term is always positive, because it's a square. Only the middle sign follows the sign in the bracket.

@words text="(a + b)² ≠ a² + b²" sub="a = 1, b = 3:  (1 + 3)² = 16 · 1 + 9 = 10"
Here's the claim to kill. a plus b, squared, is not a squared plus b squared. One number settles it. At a equals one and b equals three, the left side is sixteen and the right side is ten. A single counterexample is a complete disproof.

@art missing-piece
Squaring distributes over multiplication, but never over addition. The missing two a b is the most persistent error in school algebra.

@chapter Recognition in practice
@art pattern-match
When you meet a product, ask which pattern it matches. Are the two brackets identical except for one sign? Is it a bracket squared? If nothing matches, just distribute. The patterns are shortcuts, not obligations.

@math heading="Name the pattern, then substitute" items="(3x + 5)(3x − 5):  a = 3x, b = 5@same terms;;= 9x² − 25@nine x squared;;(2x − 7)²:  a = 2x, b = 7@a square;;= 4x² − 28x + 49@four x squared"
Remember, a and b stand for whole expressions. Three x plus five times three x minus five: same terms, opposite signs, so a is three x and b is five. That's nine x squared minus twenty-five. Two x minus seven, squared, is a square with a equal to two x and b equal to seven. That gives four x squared minus twenty-eight x plus forty-nine.

@words text="2 · (2x) · 7 = 28x" sub="not 14x"
The middle term is two times two x times seven, twenty-eight x, subtracted. Not fourteen x. Both a and b go in, and so does the two.

@chapter The cube patterns
@math heading="Sum and difference of cubes" items="(a + b)(a² − ab + b²) = a³ + b³@a plus b;;(a − b)(a² + ab + b²) = a³ − b³@a minus b"
Two more, used mainly when you factor. a plus b times a squared minus a b plus b squared is a cubed plus b cubed. And a minus b times a squared plus a b plus b squared is a cubed minus b cubed.

@art opposite-signs
Distribute the first and the a squared b terms cancel, and so do the a b squared terms. Note the signs. The binomial carries the same sign as the answer, and the middle of the trinomial carries the opposite one.

@words text="(x + 2)(x² − 2x + 4) = x³ + 8" sub="a = x, b = 2"
For example, x plus two times x squared minus two x plus four is a sum of cubes, with a equal to x and b equal to two. It's x cubed plus eight.

@chapter Where people slip
@list heading="Common slips" items="Writing (a + b)² = a² + b²@The first|Halving or dropping the 2@The second|Expecting a² + ab + b² to be a perfect square@The third"
The first slip is writing a plus b, squared, as a squared plus b squared. The second is halving or dropping the two in the middle term. And the third is expecting a squared plus a b plus b squared to be a perfect square. It isn't. A square has two a b.

@art test-numbers
Whenever you doubt an identity, test it on small numbers, or simply expand it. The derivation is shorter than the doubt.

@chapter Try it
@words text="(3x + 2)²" sub="a = 3x, b = 2 · outer terms: 9x² and 4"
Your turn. Three x plus two, squared. a is three x and b is two, so the outer terms are nine x squared and four. Recover the middle term, then test at x equals one.

@math items="9x² + 12x + 4@nine x squared plus twelve x;;at x = 1: both give 25@give twenty-five"
You should get nine x squared plus twelve x plus four, and both forms give twenty-five at x equals one. If you got six x in the middle, you used a b where the identity needs two a b.

@end text="Choose a and b, watch the middle"
You can pick a pattern, choose a and b, and watch which middle terms cancel and which double, on Learn. That's learn dot get er done dot I O.

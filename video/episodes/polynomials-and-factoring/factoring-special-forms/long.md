---
format: long
lesson: polynomials-and-factoring/factoring-special-forms
title: Factoring special forms: squares, perfect squares and cubes
thumb: A sum of squares stops
---

@chapter The question
@title text="Factoring Special Forms" sub="Polynomials and Factoring" art=thumb
Some polynomials factor in one line, if you recognise their shape. There are four shapes to know. Each is a special product run backwards, and for the cubes, the general methods won't find the answer at all.

@art four-stencils
So the job is recognition. Look at the shape first, name the pattern, and only then substitute.

@chapter Difference of squares
@math heading="a² − b² = (a − b)(a + b)" items="9x² − 25 = (3x)² − 5²@nine x squared;;= (3x − 5)(3x + 5)@three x minus five"
One perfect square minus another factors as a minus b, times a plus b. Nine x squared minus twenty-five is three x, squared, minus five squared. So it's three x minus five, times three x plus five.

@art conjugate-pair
Expand the right side and the middle terms cancel, a b and minus a b. That's the whole reason the pattern works.

@chapter A sum of squares
@words text="x² + 4 ≠ (x + 2)(x + 2)" sub="(x + 2)² = x² + 4x + 4"
Now the most common invented law in this lesson. There's no such pattern for a sum. x squared plus four is not x plus two times x plus two. Expand that and you get x squared plus four x plus four.

@art always-above
For every real x, x squared plus four is greater than zero. So it has no real root, and therefore no real linear factor. It stops there.

@chapter Perfect square trinomials
@words text="a² ± 2ab + b² = (a ± b)²" sub="outer terms square · middle term 2ab"
A trinomial is a perfect square exactly when the outer terms are perfect squares and the middle term is twice the product of their roots, up to sign.

@math items="x² + 12x + 36:  2 · x · 6 = 12x  ✓@twice x times six;;= (x + 6)²@x plus six;;25x² − 20x + 4:  2 · 5x · 2 = 20x  ✓@twice five x times two;;= (5x − 2)²@five x minus two"
x squared plus twelve x plus thirty-six: twice x times six is twelve x, so it's x plus six, squared. Twenty-five x squared minus twenty x plus four: twice five x times two is twenty x, so it's five x minus two, squared.

@art middle-test
The middle term test is what makes this a theorem, not a guess. x squared plus thirteen x plus thirty-six has square outer terms too. But twice x times six is twelve x, not thirteen x, so it's not a perfect square. It happens to factor as x plus four times x plus nine.

@chapter Sums and differences of cubes
@math heading="Cubes" items="a³ − b³ = (a − b)(a² + ab + b²)@a cubed minus b cubed;;a³ + b³ = (a + b)(a² − ab + b²)@a cubed plus b cubed"
Unlike squares, a sum of cubes does factor. a cubed minus b cubed is a minus b, times a squared plus a b plus b squared. And a cubed plus b cubed is a plus b, times a squared minus a b plus b squared.

@art cube-signs
The signs are what people misremember. The binomial carries the sign of the original. The middle of the trinomial carries the opposite sign. And the last term, b squared, is positive in both.

@math heading="Two examples" items="8x³ − 27 = (2x − 3)(4x² + 6x + 9)@eight x cubed;;27x³ + 64 = (3x + 4)(9x² − 12x + 16)@twenty-seven x cubed"
Eight x cubed minus twenty-seven is two x, cubed, minus three cubed. That's two x minus three, times four x squared plus six x plus nine. Twenty-seven x cubed plus sixty-four is three x plus four, times nine x squared minus twelve x plus sixteen.

@chapter Factor completely
@math heading="x⁴ − 16" items="(x²)² − 4²@x squared, squared;;(x² − 4)(x² + 4)@x squared minus four, times;;(x − 2)(x + 2)(x² + 4)@factor it again"
Take x to the fourth minus sixteen. It's x squared, squared, minus four squared. So it's x squared minus four, times x squared plus four. But x squared minus four is a difference of squares too, so factor it again: x minus two, times x plus two, times x squared plus four.

@art pattern-twice
Two different claims finish that. That it multiplies back is checked by expanding. That x squared plus four goes no further is a separate claim, and the reason is that it stays positive, not that nothing came to mind.

@words text="2x² − 50 = 2(x² − 25) = 2(x − 5)(x + 5)"
And take out the common factor first. Two x squared minus fifty doesn't match, because two x squared isn't a perfect square. As two times x squared minus twenty-five, it does.

@chapter Where people slip
@list heading="Common slips" items="Factoring a sum of squares@The first|Skipping the middle-term test@The second|Wrong signs in the cubes trinomial@The third"
The first slip is factoring a sum of squares. The second is skipping the middle term test. Four x squared plus ten x plus twenty-five has square outer terms, but it needs twenty x, so it isn't two x plus five, squared. The third is wrong signs in the cubes trinomial. Expand to check.

@chapter Try it
@words text="16x⁴ − 81 = (4x²)² − 9²"
Your turn. Sixteen x to the fourth minus eighty-one is four x squared, squared, minus nine squared. Apply the pattern, retest both factors, and expand to check.

@math items="(2x − 3)(2x + 3)(4x² + 9)@two x minus three"
The complete answer is two x minus three, times two x plus three, times four x squared plus nine. If you stopped at four x squared minus nine, there's a second difference of squares waiting.

@end text="Match the pattern, then check it"
You can type an expression and see which special form it matches, or that it matches none, on Learn. That's learn dot get er done dot I O.

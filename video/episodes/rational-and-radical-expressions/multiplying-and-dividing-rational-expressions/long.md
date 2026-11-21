---
format: long
lesson: rational-and-radical-expressions/multiplying-and-dividing-rational-expressions
title: Dividing rational expressions: the exclusion that hides
thumb: Flip it, and write it down
---

@chapter Nothing new, almost
@title text="Multiplying and Dividing Rational Expressions" sub="Rational and Radical Expressions" art=thumb
Multiplying algebraic fractions works exactly like multiplying number fractions. Dividing is multiplying by the reciprocal. The one genuinely new thing is that dividing forbids more values than it seems to.

@art across-product
Start with the product. a over b, times c over d, is a c over b d. Across the top, across the bottom, no adjustment at all. The product excludes every zero of b and every zero of d.

@math heading="Quotient rule" items="a/b ÷ c/d = a/b · d/c = ad / bc@a over b divided by;;b ≠ 0,  d ≠ 0,  c ≠ 0@three conditions"
Division turns into that product. a over b divided by c over d is a over b times d over c, which is a d over b c. There are three conditions: b, d and c are all non zero. Each one is doing work, and the third is the easy one to lose.

@art flip-divisor
Why can't c be zero? Because you're dividing by the number c over d, and that number is zero exactly when c is zero. Dividing by zero is undefined, whether the zero shows up as a plain zero or as a fraction with zero on top.

@chapter The hidden exclusion
@math heading="(x² − 4)/(x² + 6x + 9)  ÷  (x − 2)/(x + 3)" items="denominators (x + 3)² and x + 3:  x ≠ −3@the visible denominators;;divisor (x − 2)/(x + 3) is 0 at x = 2:  x ≠ 2@the divisor"
Here's the example. x squared minus four over x squared plus six x plus nine, divided by x minus two over x plus three. The visible denominators, x plus three squared and x plus three, forbid minus three. But the divisor is zero when x is two, so two is forbidden too.

@art hidden-zero
After you flip, x minus two sits in a denominator, where you can finally see it. That's the general pattern. Flipping turns the divisor's top into a bottom. So record the exclusion the moment you flip, because that factor is about to cancel and vanish.

@chapter Working it through
@math items="= (x² − 4)/(x² + 6x + 9) · (x + 3)/(x − 2)@flip the divisor;;= (x − 2)(x + 2)(x + 3) / ((x + 3)²(x − 2))@factor everything;;= (x + 2)/(x + 3),   x ≠ −3,  x ≠ 2@what's left"
With the exclusions safely written down, the mechanical part is short. Flip the divisor. Factor everything: x squared minus four is x minus two times x plus two, and the first bottom is x plus three squared. x minus two cancels, one x plus three cancels, and what's left is x plus two over x plus three.

@math heading="Check at x = 0" items="(−4/9) ÷ (−2/3) = (−4/9)(−3/2) = 2/3@minus four ninths;;(x + 2)/(x + 3) = 2/3  ✓@the answer gives"
Check at zero. The original is minus four ninths divided by minus two thirds, which is minus four ninths times minus three halves, two thirds. And the answer gives two thirds. They match.

@words text="at x = 2, the answer says 4/5" sub="the original asks you to divide by 0"
But notice. Every trace of why two isn't allowed has gone. Plug two into the answer and you get four fifths, a number the original can't produce, because at two it asks you to divide by zero.

@chapter Cancel before you multiply
@art cancel-across
Now a product. x plus one over x minus five, times x minus five over x plus two. x minus five is on the bottom of the first and the top of the second, so it cancels. The answer is x plus one over x plus two, with x not five and not minus two.

@art tangled-expansion
Multiplying first would give x squared minus four x minus five, over x squared minus three x minus ten, and the same cancellation, only harder. The factors are visible before you multiply and buried afterwards.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the divisor can be zero@The first|Looking for a common denominator@The second|Multiplying out before cancelling@the third"
The first slip is forgetting that the divisor may be zero. Write those values down when you flip. The second is looking for a common denominator. Products and quotients never need one. And the third is multiplying everything out before cancelling.

@art detour-path
That second one deserves a word. Building a common denominator here is extra work that can't help, and worse, it invites you to add the numerators out of habit.

@chapter Try it
@words text="(x² − 1)/(x² + 3x + 2) ÷ (x − 1)/(x + 2)" sub="flip, and add x ≠ 1 straight away"
Your turn. Simplify x squared minus one over x squared plus three x plus two, divided by x minus one over x plus two. Flip the divisor, and immediately add x not equal to one to your exclusions. Then factor, cancel, and record the two zeros of the original denominators yourself.

@end text="Three sources of exclusions"
You can practise catching every exclusion in a division on Learn. That's learn dot get er done dot I O.

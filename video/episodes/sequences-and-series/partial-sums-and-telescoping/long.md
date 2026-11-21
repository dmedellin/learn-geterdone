---
format: long
lesson: sequences-and-series/partial-sums-and-telescoping
title: Partial sums and telescoping: sums that collapse to two ends
thumb: Everything between cancels
---

@chapter Stop anywhere
@title text="Partial Sums and Telescoping" sub="Sequences and Series" art=thumb
Stop adding a series after one term, then after two, then after three. Each stopping place gives a number, and those numbers make a sequence of their own.

@art running-total
These are the partial sums. S one is a one, S two is a one plus a two, and S n is the sum of the first n terms. Every question about a series, how big does it get, does it settle, is really a question about this sequence.

@math heading="A recursion for the sums" items="S₁ = a₁@S one equals;;Sₙ = Sₙ₋₁ + aₙ@S n equals"
They have a recursion, and it's the cheap way to build a table. S one equals a one, and S n equals the previous sum plus the next term. Each new partial sum costs one addition, not n of them.

@chapter The terms come back
@math heading="The odd numbers" items="aₙ:   1, 3, 5, 7, 9, 11@one, three, five;;Sₙ:   1, 4, 9, 16, 25, 36@one, four, nine;;Sₙ − Sₙ₋₁:   3, 5, 7, 9, 11@subtract"
Take the odd numbers, one, three, five, seven. Their partial sums are one, four, nine, sixteen, the squares. Now subtract each sum from the next, and you get three, five, seven, nine, eleven. The terms come back.

@art difference-back
That always works. S n is the previous sum plus one extra term, so a n equals S n minus S n minus one, for n at least two. The restriction isn't fussiness: there is no S zero to subtract.

@art odd-first-term
So the first term needs its own check. Take S n equals n squared plus five. Subtracting gives two n minus one for n at least two. But a one is S one, which is six. The sequence is six, three, five, seven, nine, with a genuinely exceptional first term.

@chapter Telescoping
@math heading="A telescoping sum" items="(b₁ − b₂) + (b₂ − b₃) + … + (bₙ − bₙ₊₁)@Write out the sum;;= b₁ − bₙ₊₁@It collapses"
Now suppose every term is a difference of consecutive members of some other sequence: b k minus b k plus one. Write out the sum. It collapses to b one minus b n plus one.

@art cancel-pairs
Here's why. b two appears with a minus, then with a plus. So does b three, and every one up to b n. Only the first and the last have no partner.

@art telescope
That's why it's called telescoping. The sum closes up on itself, and only the two ends stay showing. The sequence b can be anything at all. The only thing used is that a finite sum can be regrouped freely.

@chapter A worked telescope
@math heading="Σ 1/(k(k + 1)),  k from 1 to n" items="1/k − 1/(k + 1) = 1/(k(k + 1))  ✓@check the split;;bₖ = 1/k@b k is one over k;;= 1 − 1/(n + 1) = n/(n + 1)@n over n plus one"
Take one over k times k plus one. First check the split: one over k, minus one over k plus one, recombines to exactly that. So b k is one over k, and the sum is one minus one over n plus one, which is n over n plus one.

@art climb-below-line
For n equals one, two, three and four, that predicts a half, two thirds, three quarters and four fifths. Adding the terms by hand gives the same four numbers. And every one of those sums sits below one.

@chapter Telescopes in disguise
@words text="Sₙ − rSₙ was a telescope" sub="bₖ = a₁rᵏ⁻¹"
The geometric sum formula was a telescope all along. Put b k equal to the k-th geometric term. Then b k minus b k plus one is that term times one minus r, and the collapse gives the same line you got by multiplying by r and subtracting.

@words text="bₖ = (k − 1)²" sub="bₖ₊₁ − bₖ = 2k − 1, so 1 + 3 + … + (2n − 1) = n²"
Or take b k equal to k minus one, squared. Then b k plus one minus b k is two k minus one, the odd numbers. So the first n odd numbers add up to n squared minus zero: n squared, a second route to the pairing result.

@chapter Common slips
@list heading="Common slips" items="Using aₙ = Sₙ − Sₙ₋₁ at n = 1@First|Ending on bₙ instead of bₙ₊₁@Second|Assuming every fraction telescopes@Third"
First, using the subtraction at n equals one without checking S one. Second, leaving b n at the far end instead of b n plus one. Test at n equals one: the sum is a half, and the wrong form gives zero. Third, assuming a sum telescopes because its terms are fractions. One over k squared doesn't. Always recombine the split.

@chapter Try it
@words text="Σ 2/((2k − 1)(2k + 1)),  k from 1 to 5" sub="split:  1/(2k − 1) − 1/(2k + 1)"
Your turn. Sum two over two k minus one times two k plus one, for k from one to five. The split is one over two k minus one, minus one over two k plus one. Recombine it first, write all five brackets, find the two survivors, and compare with the five fractions added directly.

@end text="Terms, sums, and the differences back"
You can enter a term and a partner, and watch the lab test your split before it collapses, on Learn. That's learn dot get er done dot I O.

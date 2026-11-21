---
format: long
lesson: sequences-and-series/sigma-notation
title: Sigma notation: read it, write it, shift it
thumb: A rule and a range
---

@chapter The idea
@title text="Sigma Notation" sub="Sequences and Series" art=thumb
Long sums are a pain to write out. Sigma notation packs one into a single symbol, by storing two separate things: a rule for the terms, and a range for the index.

@math heading="Sigma" items="Σ aₖ,  k from m to n@sigma of a k;;= aₘ + aₘ₊₁ + … + aₙ@means a m"
Sigma of a k, with k running from m to n, means a m plus a m plus one, and so on, up to a n. The letter k is the index, m and n are the lower and upper limits, and the expression being added is the summand.

@words text="upper limit < lower limit  →  sum = 0" sub="no terms at all"
One edge case. If the upper limit is below the lower one, there are no terms, and the sum is zero. That's the number you have when you've added nothing.

@chapter Reading one
@art expand-row
When you meet a sigma you don't know, expand it. Put in each value of the index in turn and add. It's slow, but it's the definition, so it can never be wrong.

@math heading="Σ k²,  k from 1 to 5" items="1² + 2² + 3² + 4² + 5²@one squared;;= 1 + 4 + 9 + 16 + 25@one plus four;;= 55@fifty five"
The sum of k squared, for k from one to five, is one squared plus two squared, up to five squared. That's one plus four plus nine plus sixteen plus twenty five, which is fifty five.

@chapter Three surprises
@art constant-row
The summand doesn't have to mention the index. The sum of seven, for k from one to four, is seven plus seven plus seven plus seven, twenty eight. The limits alone decide how many terms.

@math heading="Two more" items="Σ 2ᵏ,  k from 0 to 3  =  1 + 2 + 4 + 8 = 15@two to the k;;Σ (−1)ᵏ k,  k from 2 to 5  =  2 − 3 + 4 − 5 = −2@minus one to the k"
And the lower limit doesn't have to be one. The sum of two to the k, from zero to three, is one plus two plus four plus eight, fifteen. Its first term is one, not two. And minus one to the k, times k, from two to five, gives two minus three plus four minus five, minus two.

@chapter Counting the terms
@art fence-posts
How many terms run from k equals m to k equals n? It's n minus m plus one, because both ends are included. Subtracting the limits counts the gaps, not the posts.

@words text="k = 4 to k = 11:  8 terms" sub="11 − 4 + 1, not 11 − 4"
From four to eleven is eight terms, not seven. And that slip is silent. The expansion looks fine, and every formula you apply afterwards inherits the wrong count.

@chapter Writing one
@math heading="3 + 5 + 7 + 9 + 11 = 35" items="Σ (2k + 1),  k from 1 to 5@two k plus one;;Σ (2k + 3),  k from 0 to 4@two k plus three;;Σ (2k − 3),  k from 3 to 7@two k minus three"
Going the other way, a sum has no single correct sigma. Three plus five plus seven plus nine plus eleven is thirty five, and all of these produce it: two k plus one from one to five, two k plus three from zero to four, and two k minus three from three to seven. The only difference is where you started counting.

@chapter What passes through
@art split-sum
Some things pass through a sigma. A constant factor comes out. A sum of two sequences splits into two sums. And a constant summand adds up to the term count times the constant.

@math heading="k = 1, 2,   aₖ = bₖ = k" items="Σ aₖbₖ = 1 + 4 = 5@one plus four;;(Σ aₖ)(Σ bₖ) = 3 · 3 = 9@three times three"
Products don't. Take k equals one and two, with a k and b k both equal to k. The sum of the products is one plus four, five. The product of the sums is three times three, nine. Sigma abbreviates addition, and that's all that passes through.

@chapter Shifting the index
@math heading="Σ (k − 2),  k from 3 to 7  =  15" items="put k = j + 2@put k equals;;limits:  3 → 1,   7 → 5@three becomes one;;summand:  (j + 2) − 2 = j@becomes j;;Σ j,  j from 1 to 5  =  15@still fifteen"
Sometimes you need a sum to start somewhere else. Take k minus two, from three to seven, which is fifteen. Put k equals j plus two. The limits move down by two: three becomes one, seven becomes five. And the summand becomes j. The sum of j from one to five is still fifteen.

@art shift-slide
That's the whole rule. The limits move one way and the index inside moves the other, both together. Expand the first term of each form and compare. That's your check.

@art wrong-shift
The classic slip is moving only the limits. The sum of k plus four, from one to six, is forty five. Change the range to zero to five and keep k plus four, and you get thirty nine.

@chapter Try it
@words text="Σ (4k + 1),  k from 3 to 7" sub="5 terms ·  put k = j + 2"
Your turn. Take four k plus one, from three to seven. That's seven minus three plus one, five terms. Rewrite it to start at j equals one using k equals j plus two. Then expand both forms, and check the first term, the last term and the total.

@end text="Expand it, then shift it"
You can expand any sigma term by term, and turn a dial to shift it, on Learn. That's learn dot get er done dot I O.

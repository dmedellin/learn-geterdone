---
format: long
lesson: randomised-algorithms/the-cost-is-a-distribution
title: Randomised quicksort: the cost is a distribution, not a number
thumb: Always, expected, measured
---

@chapter Three numbers
@title text="The Cost Is a Distribution" sub="Randomised Algorithms" art=thumb
How many comparisons does quicksort make on eight sorted keys? With a fixed pivot, twenty eight. With a random pivot, there isn't one answer. There's a distribution, and three different kinds of number describe it.

@chapter The fixed pivot
@art fixed-pivot
Quicksort picks a pivot, partitions a block of length L against it for L minus one comparisons, and recurses on the two pieces. The fixed rule always takes the last element. On a sorted array, every pivot is the largest key left, so every split is as lopsided as it can be.

@math heading="Fixed pivot, sorted, n = 8" items="7 + 6 + 5 + 4 + 3 + 2 + 1 = 28@seven plus six;;= n(n − 1)/2@n times n minus one"
That's seven plus six plus five, down to one, which is twenty eight, n times n minus one over two. Reversed, also twenty eight. Alternating high and low, sixteen. One rule, three inputs, three counts, each fixed forever.

@chapter The random pivot
@art random-pivot
Now pick the pivot uniformly at random, at every call, independently.

@art distribution-bars
On the same sorted array, the comparison count can be anything from thirteen to twenty eight. The lab draws all sixteen probabilities as bars, and checks they add to one.

@math heading="The recursion over sizes" items="D(k) = (k − 1) + average over i of D(i) ⊛ D(k − 1 − i)@D of k"
It computes them exactly, with a recursion over sizes. D of k is k minus one, plus the average, over where the pivot lands, of the convolution of the two pieces' distributions. No seeds, no runs. It only depends on how the pivots split the blocks.

@chapter What the bars say
@math heading="n = 8" items="most likely:  C = 16,  P = 73/360@sixteen;;mean:  E[C] = 2369/140 ≈ 16.92@the mean;;P(17) = 29/840@seventeen"
The most likely count is sixteen, with probability seventy three over three sixty. The mean is two three six nine over one forty, about sixteen point nine two. So the mean isn't the typical cost. And seventeen has less than a fifth of sixteen's probability. It's jagged.

@words text="jagged is real"
That jaggedness is real. A comparison count is a sum of block lengths minus one, and at small n some totals have many ways to arise and some have few. Nothing about the expectation requires the shape around it to be smooth.

@chapter Two checks
@words text="2(n + 1)Hₙ − 4n = 2369/140" sub="H₈ = 761/280"
The closed form for the expectation is two, times n plus one, times the n th harmonic number, minus four n. With H eight equal to seven six one over two eighty, it gives the same two three six nine over one forty. The panel prints agrees beside it.

@art all-orders
At small n, there's a third route. Run the fixed pivot on every input order. At n equals five that's a hundred and twenty runs, and the distribution matches, with expectation thirty seven fifths. Randomising the pivot on a fixed input is the same experiment as fixing the pivot on a random input. Each run is also checked to be sorted.

@chapter The measured column
@math heading="Mean over 120 seeds" items="sorted:  415/24 ≈ 17.29@sorted array;;reversed:  1031/60@reversed;;alternating:  1003/60@alternating"
Over seeds one to a hundred and twenty, the sorted array averaged four fifteen over twenty four, about seventeen point two nine. The reversed array gave ten thirty one over sixty, and alternating gave ten oh three over sixty, below the expectation.

@art measured-dots
The observed range on the sorted array was thirteen to twenty seven. The true support is thirteen to twenty eight. The seeds that never hit twenty eight don't make it impossible.

@art same-shape
Three measured means. One expectation. The exact distribution is identical for all three inputs, because a random pivot position picks a random rank whatever order the keys came in. The randomness is the algorithm's, not the data's. And the one claim that's always true: every run costs at most twenty eight.

@chapter Where people slip
@list heading="Common slips" items="Calling the average the expectation@The first|Treating the expectation as typical@The second|Pitting a worst case against an expectation@And the third"
The first slip is calling an average over runs the expectation. The second is treating the expectation as the typical cost. And the third is pitting twenty eight against the expectation, as if they compete. Twenty eight holds on every run, with probability one over three fifteen of being hit.

@end text="Always, expected, measured"
Move the seed slider and watch which numbers move, on Learn. That's learn dot get er done dot I O.

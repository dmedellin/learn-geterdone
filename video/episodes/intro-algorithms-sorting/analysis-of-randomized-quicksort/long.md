---
format: long
lesson: intro-algorithms-sorting/analysis-of-randomized-quicksort
title: Randomized quicksort: counting comparisons pair by pair
thumb: Two over j minus i plus one
---

@chapter No bad inputs
@title text="Randomized Quicksort" sub="Introduction to Algorithms, Sections 7.3 and 7.4" art=thumb
Quicksort's average behaviour assumed every ordering of the input was equally likely. The book doesn't let that assumption stand.

@quote text="In an engineering situation, however, we cannot always expect this assumption to hold." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 7.3"
In an engineering situation, however, we cannot always expect this assumption to hold. So section seven point three stops assuming anything about the input, and puts the randomness inside the algorithm.

@art random-pivot
The change is two lines. Before partitioning, swap the last element with one chosen at random from the subarray. Now every key is equally likely to be the pivot, and a sorted array is exactly as likely to split well as any other.

@chapter The worst case remains
@art worst-run
Does randomness remove the worst case? No. An unlucky run of pivot choices makes the same splits a sorted input does, and section seven point four point one proves the worst case is still theta of n squared. At seven keys, the worst run still makes twenty one comparisons. What's gone is any input's power to force it.

@chapter Count pairs, not calls
@art pair-arcs
Now for the expected comparisons. Rather than count call by call, the authors count pair by pair. Every comparison is between a pivot and another key, and a pivot never appears in a later call. So each pair of keys is compared at most once.

@math items="X = Σ Xᵢⱼ  over all pairs i < j@X is the sum;;E[X] = Σ Pr{zᵢ is compared to zⱼ}@linearity"
Name the keys z one to z n, in sorted order. Let X i j be the indicator that z i and z j are compared. X is the sum over all pairs, and by linearity, its expectation is the sum of the probabilities.

@chapter When two keys meet
@art between-set
Look at the keys from z i to z j, a set of j minus i plus one keys. Until a pivot is chosen from that set, it all stays together in one subarray, because any earlier pivot sends the whole set to the same side.

@art split-apart
If the first pivot from the set lands strictly between z i and z j, they go to different sides, and never meet. If it's z i or z j itself, that key is compared with everything in its call, including the other one.

@math heading="The key probability" items="Pr{zᵢ meets zⱼ} = 2 / (j − i + 1)@two over j minus i plus one"
Each of the j minus i plus one keys is equally likely to be first, and two of them cause a comparison. So the probability is two over j minus i plus one.

@chapter Adding it up
@math heading="n = 7, by distance d" items="d = 1: 6 pairs × 1 = 6@six pairs;;d = 2: 5 × 2/3 = 10/3@ten thirds;;d = 3: 4 × 1/2 = 2,  d = 4: 3 × 2/5 = 6/5@six fifths;;d = 5: 2 × 1/3,  d = 6: 1 × 2/7@two sevenths;;E[X] = 472/35 ≈ 13.4857@four hundred and seventy two"
At seven keys, group the pairs by distance. Six pairs at distance one, each certain, give six. Five at distance two give ten thirds. Then two, then six fifths, then two thirds, then two sevenths. In total, four hundred and seventy two over thirty five, about thirteen point four nine.

@math heading="In general" items="E[X] = 2·(n + 1)·Hₙ − 4n@two times n plus one;;= O(n lg n)@O of n log n"
The book bounds the sum with the harmonic series to get O of n log n. The exact total is two times n plus one times H n, minus four n. Together with the best case, the expected time is theta of n log n.

@art same-fraction
Here's the striking part. Average over all four hundred and twenty nine pivot sequences on the shuffled array, and you get four hundred and seventy two over thirty five. On the sorted array, the reversed one, and one built to beat median of three, you get the same fraction.

@words text="200 seeds: 13.7150" sub="a sample, not all 429"
Two hundred random runs average thirteen point seven one five, a little above, because they're a sample of the possibilities, not all of them.

@chapter Common slips
@list heading="Common slips" items="Reading it as an average over inputs@The first|Believing randomness removes the worst case@The second|Thinking linearity needs independence@the third"
The first slip is reading the expectation as an average over inputs. It's over the pivots, for every input. The second is believing randomization removes the worst case. And the third is thinking linearity needs independent indicators. These indicators are strongly dependent.

@chapter Try it
@words text="n = 5" sub="group the pairs by distance"
Your turn. At five keys, compute the expected comparisons by grouping the pairs by distance, as the table did at seven. Check your fraction against the closed form, then compare with the lab.

@end text="Count it three ways"
You can see the expectation reached three ways, on every input, on Learn. That's learn dot get er done dot I O.

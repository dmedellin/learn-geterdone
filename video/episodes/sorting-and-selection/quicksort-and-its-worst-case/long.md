---
format: long
lesson: sorting-and-selection/quicksort-and-its-worst-case
title: Every quicksort pivot rule has an input that kills it
thumb: Build the killer input
---

@chapter The question
@title text="Quicksort and Its Worst Case" sub="Sorting and Selection" art=thumb
Quicksort is famous for being fast. It's also quadratic in the worst case. Which is it? Both, and the pivot rule decides when. Better still, for any fixed rule, you can build the input that beats it.

@chapter Where the cost lives
@art recursion-split
To quicksort a range: if it holds fewer than two elements, stop. Otherwise partition around a pivot, then quicksort the left part and the right part. There's no merge step, and the pivot is never looked at again.

@words text="cost = Σ (range length − 1)"
A partition of length m costs m minus one comparisons. So a whole run costs the sum, over every call, of its length minus one. The splits decide everything.

@math heading="The recurrence" items="T(n) = T(k) + T(n − k − 1) + (n − 1)@T of n;;k = n/2:  Θ(n log n)@about half;;k = 0:  n(n − 1)/2@k is zero"
In symbols, T of n is T of k plus T of n minus k minus one, plus n minus one, where k is how many keys fall below the pivot. If k is about half every time, that's Theta of n log n. If k is zero every time, it's n times n minus one, over two.

@chapter The obvious bad case
@art lopsided
Use the first element as the pivot, on sorted input. The pivot is the smallest key, so the left side is empty and the right side has n minus one. Then it happens again, and again.

@math heading="First-element pivot, sorted input, n = 32" items="comparisons:  496@four hundred and ninety six;;n(n − 1)/2 = 496@met exactly;;depth:  31@thirty one"
At thirty two keys, the lab measures four hundred and ninety six comparisons, with a recursion depth of thirty one. That's the worst case of the recurrence, met exactly. And sorted input is the commonest input there is.

@chapter Building a killer
@art adversary
Median of three fixes sorted input. So build a bad input for it. The lab runs the rule on items whose values aren't decided yet. Whenever the rule compares two of them, it freezes one at the next smallest value, choosing so the pivot keeps landing near the bottom.

@words text="a real permutation of 1 … n"
Every answer stays consistent with the final values, so what comes out is a genuine permutation of one to n, not a trick. Then the ordinary quicksort runs on it, and counts. It's the same move as the lower bound arguments later on: answer the questions so the bad case stays alive. Aimed at one rule, it gives an input rather than a bound.

@math heading="Median of three, its own killer" items="n = 32:  304 comparisons,  depth 16@three hundred and four;;n log₂ n = 160@a hundred and sixty;;n = 16:  88 · ratio 3.45@eighty eight"
At thirty two keys, quicksort spends three hundred and four comparisons and recurses sixteen deep, where a balanced split would be about six deep, and n log two n is a hundred and sixty. Halve the length to sixteen, and it's eighty eight. Doubling n multiplied the work by three point four five.

@art growth-two-sizes
A count that roughly quadruples when n doubles is behaving quadratically. The lab reads that from integer counts at two sizes, not from a drawn curve.

@chapter Each rule, its own killer
@art rule-specific
Here's the twist. The array built against median of three costs a first element pivot only a hundred and forty three. The one built against a first element pivot costs a middle element pivot a hundred and three. Each rule has its own bad input. The flaw is in the rule.

@art equal-keys
And one input beats them all. Twenty four equal keys cost every rule two hundred and seventy six, n times n minus one over two again, because Lomuto sends every key equal to the pivot to one side.

@words text="Deterministic rule: Θ(n²)" sub="on one input: whatever you measured"
So what is quicksort's cost? On the input in front of you, whatever the lab measured. As a claim about all inputs under a deterministic rule, Theta of n squared, because the killer exists. Randomised quicksort changes the question by moving where the randomness lives.

@chapter Where people slip
@list heading="Common slips" items="Turning a worst case into a speed verdict@The first|Thinking a better rule removes the worst case@The second|Reading the verdict off a drawn curve@And the third"
The first slip is saying quadratic, so slower than merge sort. That mixes two questions, and comparisons aren't time anyway. The second is thinking a cleverer rule removes the worst case. Every deterministic rule is a function of the array, so every one has a killer. And the third is reading the verdict off a drawn curve.

@chapter Try it
@words text="Pick a pivot rule, build its killer" sub="count at n = 16 and n = 32"
Your turn. Choose a pivot rule, build the input that defeats it, and count quicksort's comparisons at sixteen and thirty two keys. Place the ratio in the recurrence.

@end text="Build a killer input"
You can build the input that defeats any pivot rule and count what it costs, on Learn. That's learn dot get er done dot I O.

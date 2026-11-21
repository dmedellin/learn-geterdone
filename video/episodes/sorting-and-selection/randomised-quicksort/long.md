---
format: long
lesson: sorting-and-selection/randomised-quicksort
title: Randomised quicksort: the exact expected count, on every input
thumb: Same answer on every array
---

@chapter The question
@title text="Randomised Quicksort" sub="Sorting and Selection" art=thumb
Every fixed pivot rule has an input that kills it. So pick the pivot at random. Then the expected cost isn't about the input at all. And you can work it out exactly, in three lines.

@chapter The one change
@art random-pivot
Randomised quicksort changes one thing. Each call picks its pivot uniformly at random from its own range. The input isn't shuffled, and nothing is assumed about it. Two runs on the same array can cost different amounts.

@words text="z₁ < z₂ < … < zₙ" sub="Xᵢⱼ = 1 if zᵢ and zⱼ are ever compared"
Rename the keys by rank, z one the smallest up to z n the largest. The algorithm never sees these names. Now let X i j be one if z i and z j are compared at some point, and zero if not. The total comparisons, X, is the sum of all of them.

@chapter When two keys meet
@art stretch
Look at the stretch of sorted order from z i to z j. All of it starts in the same call. Now think about the first pivot drawn from that stretch.

@list heading="The first pivot from zᵢ … zⱼ" items="Strictly between: they're separated for ever@strictly between|zᵢ or zⱼ: they're compared, once@z i or z j"
If it's something strictly between them, z i goes left, z j goes right, and they're never in the same call again. So they're never compared. But if it's z i or z j itself, that one is the pivot of a call containing the other, and they're compared, exactly then.

@art separated
That's the key fact. A comparison only ever happens between a pivot and something in its own call. Once a key between them is drawn, z i and z j are split up for good.

@math heading="The probability" items="j − i + 1 keys in the stretch@j minus i plus one;;P(Xᵢⱼ = 1) = 2/(j − i + 1)@two over"
Every key in the stretch is equally likely to be drawn first. There are j minus i plus one of them, and two give a comparison. So the probability is two over j minus i plus one.

@chapter Adding it up
@math heading="Linearity of expectation" items="E[X] = Σ E[Xᵢⱼ]@the expected value;;= Σᵢ Σ_d 2/(d + 1)@d equal;;= 2(n + 1)Hₙ − 4n@two times n plus one;;< 2n ln n@less than"
The expected value of X is the sum of the expected indicators. Let d equal j minus i, and each inner sum is a tail of the harmonic series. Collect the terms, and you get two times n plus one times H n, minus four n. That's less than two n ln n.

@art dependent
And here's the thing people get stuck on. These indicators aren't independent. Knowing one pair was compared tells you about which pivots were drawn. Linearity doesn't care. The expectation of a sum is the sum of the expectations, for any random variables at all.

@chapter Nine keys, three ways
@math heading="n = 9" items="H₉ = 7129/2520@H nine;;E[X] = 2593/126 ≈ 20.5794@two five nine three"
At nine keys, H nine is seven one two nine over two five two oh. So the expected count is two five nine three over a hundred and twenty six, about twenty point five seven nine four. The lab gets that fraction three ways.

@list heading="One fraction, three ways" items="The closed form@closed form|The recurrence, solved bottom up@recurrence|Every one of 4 862 pivot sequences@every one"
The closed form. The recurrence, solved from the bottom, which has no harmonic number in it. And by averaging over every one of the four thousand eight hundred and sixty two possible pivot sequences on the array. That last one isn't a sample. It's every run there is.

@art five-arrays
Run that enumeration on a sorted array, a reversed one, an up then down one, a shuffle, and the median of three killer. All five give two five nine three over a hundred and twenty six. The expectation doesn't know which array it was handed.

@words text="120 seeds on the killer: 20.6583" sub="a sample: 120 of 4 862 runs"
Beside that, the lab prints a mean over a hundred and twenty seeds, and that one is a sample. On the killer it's twenty point six five eight three, a little above. Move the seed and it moves. Nothing above it does.

@chapter The hypothesis
@art equal-pile
The derivation assumed distinct keys. On twenty four equal keys, Lomuto sends everything to one side under every seed. The cost is two hundred and seventy six, where the formula says ninety two point eight. The formula isn't beaten. It was never about that array.

@chapter Where people slip
@list heading="Common slips" items="Hearing expected as on a typical input@The first|Looking for independence first@The second|Applying the formula to ties@And the third"
The first slip is hearing expected as on a typical input. This average is over the algorithm's own coin flips, so it holds for each input separately. The second is looking for independence before using linearity. And the third is applying the formula to an array with ties.

@chapter Try it
@words text="Derive P(Xᵢⱼ = 1) for n = 4" sub="then add up all six pairs"
Your turn. Take four keys. For each of the six pairs, write the probability they're compared, add them, and check your answer against the closed form.

@end text="Average over every run"
You can enumerate every pivot sequence and watch the expectation stay put, on Learn. That's learn dot get er done dot I O.

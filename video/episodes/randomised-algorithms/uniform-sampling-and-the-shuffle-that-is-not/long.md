---
format: long
lesson: randomised-algorithms/uniform-sampling-and-the-shuffle-that-is-not
title: The shuffle everyone writes is wrong, and one division proves it
thumb: 24 doesn't divide 256
---

@chapter Two shuffles
@title text="Uniform Sampling, and the Shuffle That Is Not" sub="Randomised Algorithms" art=thumb
Here's a shuffle that looks right, and people write it from memory. It's wrong. And you can prove it's wrong with one division, without running it even once.

@list heading="Two shuffles" items="Fisher–Yates: i from n − 1 down, j uniform in 0..i@Fisher Yates|Naive swap: i from 0 up, j uniform in 0..n − 1@the naive swap"
Both start from the identity and walk the array once, swapping positions i and j. Fisher Yates goes down from the end, and draws j from zero up to i. The naive swap goes up from zero, and draws j from the whole array, every time.

@art swap-arrows
That one change, drawing from the whole array instead of from what's left, is the whole difference.

@chapter Count the tapes
@art tape
Fix the input. The only thing that can still vary is the sequence of random draws. Call that sequence a tape. Every draw is uniform and independent, so every tape is equally likely.

@words text="P(output) = tapes giving it ÷ all tapes"
So the probability of an output is the number of tapes that produce it, divided by the number of tapes. Both are integers, so it's an exact fraction. A probability question becomes a counting question.

@chapter Fisher–Yates is exact
@art bijection
Fisher Yates makes one choice out of n, then one out of n minus one, and so on. That's n factorial tapes. Two different tapes give two different permutations, and there are n factorial permutations. So the match is one to one.

@words text="P(σ) = 1/n!" sub="n = 4: 1/24 in every row"
Every permutation has probability exactly one over n factorial. The lab prints one over twenty four in every row at n equals four, and a distance from uniform of exactly zero.

@chapter The naive swap fails
@math heading="n = 4" items="tapes: 4⁴ = 256@four to the four;;permutations: 4! = 24@four factorial;;256 = 24 × 10 + 16@ten, with sixteen"
The naive swap makes n draws from n values, so n to the n tapes. At n equals four, that's four to the four, two hundred and fifty six tapes, and four factorial, twenty four permutations. If it were uniform, every permutation would get the same number of tapes. But two hundred and fifty six over twenty four is ten, with sixteen left over.

@art unequal-piles
There's no way to deal two hundred and fifty six tapes into twenty four equal piles. So the shuffle isn't uniform, and nothing about that argument needed a sample.

@words text="n! ∤ nⁿ  for every n ≥ 3"
It fails for every n of three or more. Take a prime p between n over two and n. It divides n factorial, but it doesn't divide n, so it can't divide n to the n. The lab just prints the remainders: three, sixteen and five, at n equals three, four and five.

@chapter How wrong is it?
@math heading="Naive swap, n = 4" items="most likely: 1032, 15 tapes = 15/256@fifteen tapes;;least likely: 8 tapes = 1/32@eight tapes;;total variation from uniform: 25/384@twenty five over"
Divisibility says it's wrong, not how wrong. The enumeration does that. At n equals four, the most likely permutation is one zero three two, with fifteen tapes. The least likely have eight tapes, one over thirty two. The favoured outcome is almost twice as likely. The total variation distance from uniform is twenty five over three hundred and eighty four.

@art growing-bias
It's the largest amount the two distributions can disagree about any event.

@words text="1/18 → 25/384 → 3157/37500" sub="n = 3, 4, 5"
And more swaps don't wash it out. The distance is one eighteenth at n equals three, about point zero five six. Then about point zero six five at four, and about point zero eight four at five. The bias grows.

@chapter Why sampling won't tell you
@art sample-bars
Shuffling a lot and looking at the counts doesn't work. Fisher Yates over one hundred and twenty seeds at n equals four reached only twenty three of the twenty four permutations, and it's provably uniform. A sample from a uniform distribution is uneven. Refuting uniformity by sampling is expensive. By counting, it costs one division.

@chapter Where people slip
@list heading="Common slips" items="Testing uniformity by counting outputs@The first|Reading the bias off the output@The second|Thinking more randomness is fairer@And the third"
The first slip is testing uniformity by shuffling and counting. The second is reading the bias off the output. Nobody can look at one zero three two and see why. And the third is thinking more randomness is fairer. The naive swap uses more draws, and it's the one that's wrong.

@end text="Count the tapes, not the outputs"
You can enumerate every tape of both shuffles on Learn. That's learn dot get er done dot I O.

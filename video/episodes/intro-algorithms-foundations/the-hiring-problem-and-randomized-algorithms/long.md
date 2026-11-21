---
format: long
lesson: intro-algorithms-foundations/the-hiring-problem-and-randomized-algorithms
title: The hiring problem: why you only expect about ln n hires
thumb: Shuffle first, then expect ln n
---

@chapter An odd story
@title text="The Hiring Problem" sub="Introduction to Algorithms, Chapter 5" art=thumb
Chapter five tells a story about an employment agency. It seems an odd thing for an algorithms book, until you see what it's really about.

@quote text="The hiring problem models how often we update our notion of which element is currently winning." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 5.1"
The authors explain: the hiring problem models how often we update our notion of which element is currently winning. Keeping a running maximum is everywhere.

@chapter The procedure
@art candidate-line
An agency sends you one candidate a day. You interview each one, and whenever a candidate is better than your current assistant, you fire the assistant and hire the candidate. Interviewing costs a small amount, c i. Hiring costs a large amount, c h.

@math heading="Cost of m hires" items="O(cᵢ·n + c_h·m)@O of c i n"
So with m hires out of n candidates, the cost is O of c i n plus c h m. The interviews always cost the same, so the question is m.

@art increasing-worst
In the worst case, candidates arrive in increasing order of quality, and you hire every single one. That's n hires.

@chapter Random order
@words text="All n! orders equally likely" sub="a uniform random permutation"
To say anything about the average, you need an assumption about the input. Give each candidate a distinct rank, and assume each of the n factorial orders is equally likely. That's a uniform random permutation.

@art indicator-switch
The tool is the indicator random variable. For an event A, it's one if A happens, and zero if not. And its expected value is just the probability of A. Toss a fair coin n times, add up the indicators, and you expect n over two heads.

@math heading="Lemma 5.2" items="Xᵢ = I{candidate i is hired}@X i;;E[Xᵢ] = 1/i@one over i;;E[X] = 1 + 1/2 + … + 1/n = Hₙ@the harmonic number;;= ln n + O(1)@natural log of n"
Let X i be the indicator that candidate i is hired. That happens exactly when candidate i is the best of the first i, and in a random order each of those is equally likely to be best. So the expectation is one over i. Add them up, and the expected hires are H n, the harmonic number, which is the natural log of n plus a constant.

@art harmonic-shrink
Notice what the proof never did. It never worked out the probability of exactly m hires. Linearity of expectation needs no independence at all. And the answer is small. With a thousand candidates in random order, you expect to hire about seven and a half.

@chapter A worked order
@math heading="[3, 6, 2, 7, 1, 8, 5, 4]" items="hires at positions 1, 2, 4, 6@positions one, two, four and six;;cost 8 + 4·10 = 48@forty eight;;average over 40,320 orders: 761/280 ≈ 2.72 = H₈@forty thousand"
Take three, six, two, seven, one, eight, five, four. You hire at positions one, two, four and six. With c i one and c h ten, the cost is forty eight. Averaged over all forty thousand three hundred and twenty orders, the hires are seven hundred and sixty one over two hundred and eighty, about two point seven two. That's exactly H eight.

@words text="Increasing: 8 hires · Best first: 1 hire" sub="the average stays 2.72"
In increasing order, you hire all eight, at cost eighty eight. With the best candidate first, you hire once, at cost eighteen. The average doesn't move, because it's over all orders, not this one.

@chapter Make it a guarantee
@art shuffle
That average assumed something about the agency. Section five point three removes the assumption. Shuffle the list at random first, then run the same loop. Now the expected cost holds for every input, averaged over the algorithm's own coin flips. A rival who knows your code can't pick a bad order.

@list heading="Shuffling uniformly" items="Permute by sorting: random priorities, then sort@by sorting|Randomize in place: swap A[i] with a random A[i..n]@in place"
How do you shuffle? Permute by sorting gives each element a random priority and sorts by it. Randomize in place is better: O of n time, no extra array.

@art permute-in-place
At each step i, it swaps A of i with an element chosen uniformly from A i to n. The book warns that making each element equally likely to land in each position isn't enough. Every whole arrangement has to be equally likely.

@chapter Common slips
@list heading="Common slips" items="Treating an average as a guarantee@The first|Thinking you need the full distribution@The second|Believing linearity needs independence@the third"
The first slip is treating an average over inputs as a guarantee for your input. The second is thinking you need the full distribution of the count. And the third is believing linearity of expectation needs independence. It doesn't.

@chapter Try it
@words text="[5, 2, 7, 4, 8, 1, 6, 3]" sub="hires, cost, then E[X₃] and E[X₈]"
Your turn. For five, two, seven, four, eight, one, six, three, list the hires and the cost, with c i one and c h ten. Then work out the chance that the third, and the eighth, candidates are hired on a random order.

@end text="Average every order yourself"
You can average the hires over every order of eight or nine candidates, on Learn. That's learn dot get er done dot I O.

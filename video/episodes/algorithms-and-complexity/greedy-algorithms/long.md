---
format: long
lesson: algorithms-and-complexity/greedy-algorithms
title: When is greedy optimal? Only when you can prove it
thumb: Greedy needs a proof
---

@chapter The idea
@title text="Greedy Algorithms" sub="Algorithms and Complexity" art=thumb
A greedy algorithm takes the best looking choice at every step, and never goes back. Sometimes that's provably optimal. Usually it isn't. So with greedy, the proof is the whole story.

@chapter Interval scheduling
@art interval-bars
Here's a case where it works. You're given intervals, each with a start and a finish time, and you want as many as possible with no two overlapping. The greedy rule: keep taking the interval that finishes earliest, among those that fit with what you've already chosen.

@list heading="Why earliest finish is optimal" items="Greedy g₁, g₂, … and optimal o₁, o₂, …, by finish time@Line up|g₁ finishes no later than o₁@For the first|If gᵢ ≤ oᵢ, then o₍ᵢ₊₁₎ is still available@For the step"
Line up the greedy choices and an optimal set, both in order of finish time. By induction, each greedy interval finishes no later than the matching optimal one. For the first, greedy took the earliest finish of all. For the step, the next optimal interval is still available to greedy, so greedy's next finishes no later.

@words text="Greedy stays ahead" sub="so the sizes are equal"
If the optimum had more intervals, its next one would still fit with everything greedy chose, so greedy wouldn't have stopped. So the two sets have the same size, and greedy is optimal.

@art short-trap
Other sensible rules fail. Shortest interval first fails when a short interval overlaps two long ones that don't overlap each other. Taking it blocks both.

@art long-first
And earliest start first fails when one very long interval begins first, and blocks everything else. Only earliest finish is optimal, and you can't see that without the proof.

@chapter Where greedy fails
@math heading="Coin change" items="{1, 5, 10, 25}:  largest first is always optimal@one, five;;{1, 3, 4},  amount 6:  greedy  4 + 1 + 1  →  3 coins@one, three and four;;but  3 + 3  →  2 coins@three plus three"
Coin change is the classic trap. With coins of one, five, ten and twenty five, taking the largest coin first is optimal for every amount. But with one, three and four, try making six. Greedy takes four, then one, then one, three coins. But three plus three uses two.

@art coin-piles
So greedy works for coin change is a property of the coin system, not of the strategy. And nothing in the algorithm warns you when it fails.

@art tsp-tour
It can be far worse. Building a travelling salesman tour by always going to the nearest city can be arbitrarily bad. There are instances where it exceeds the best tour by any factor you like. You get a tour quickly, with no guarantee at all.

@chapter The exchange argument
@list heading="The exchange argument" items="Take an optimal solution that differs from greedy@Assume|Find the first place they differ@Find the first|Change the optimum to agree there, no worse@Show you can|Repeat until it is the greedy solution@Repeat"
So how do you prove greedy is right? The standard tool is the exchange argument. Assume an optimal solution that differs from the greedy one. Find the first place they differ. Show you can change the optimum to agree with greedy there, without making it worse. Repeat, and the optimum turns into the greedy solution.

@words text="Swap the heavier edge for the lighter one" sub="the cut property of minimum spanning trees"
It's exactly the argument behind minimum spanning trees. Swapping a heavier edge for a lighter one never increases the total. Wherever greedy is correct, the technique is the same.

@chapter Huffman coding
@art huffman-merge
One more success. To build a Huffman code, repeatedly merge the two least frequent symbols into one combined node. That gives a prefix free binary code of minimum expected length, and it's the compression method behind several standard formats.

@words text="Merge the two rarest" sub="an optimal tree can make them deepest siblings"
Again the proof is an exchange argument. It shows an optimal tree can always put the two rarest symbols together, as siblings at the deepest level. It's a genuine theorem, not an observation.

@chapter Where people slip
@list heading="Common slips" items="Assuming greedy is optimal because it seems reasonable@The first|Testing instead of proving@The second|Not saying which you have@The third"
The first slip is assuming greedy is optimal because it seems reasonable. Three sensible rules for intervals, and only one is right. The second is testing instead of proving. And the third is not saying which you have. Optimal by an exchange argument and a heuristic are both respectable. Passing off the second as the first is not.

@chapter Try it
@words text="Break the wrong rules" sub="shortest first · earliest start"
Try building the counterexamples yourself. Draw a few intervals where shortest first picks fewer than the best possible. Then draw a set where earliest start does. In each case, check that earliest finish gets the maximum.

@end text="Prove it, or call it a heuristic"
The full lesson on greedy algorithms is on Learn. That's learn dot get er done dot I O.

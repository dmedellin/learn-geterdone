---
format: long
lesson: greedy-and-matroids/greedy-for-every-weighting
title: Greedy works for every weighting exactly when it's a matroid
thumb: Every weighting, or it fails
---

@chapter The question
@title text="Greedy for Every Weighting" sub="Greedy Algorithms and Matroids" art=thumb
When does greedy give the best answer? Not on one input, but whatever weights you put on the elements. There's an exact answer, and it goes in both directions.

@art sorted-weights
Here's greedy on an independence system. Sort the elements from heaviest to lightest, walk the list once, and add each element if the set stays independent. You always end with a maximal set. The question is whether it's the heaviest one.

@words text="Rado and Edmonds" sub="greedy optimal for every weighting  ⟺  matroid"
The theorem, due to Rado and Edmonds, says greedy returns a maximum weight independent set for every non negative weighting if and only if the family is a matroid.

@chapter Matroid means greedy wins
@art two-bases
Suppose it's a matroid. Greedy's answer and the best answer are both bases, so they have the same size. List each from heaviest to lightest, and compare them position by position.

@math heading="Position by position" items="claim: w(gᵢ) ≥ w(oᵢ) for every i@The claim;;least i with w(gᵢ) < w(oᵢ)?@take the first;;A = {g₁ … g_(i−1)},  B = {o₁ … oᵢ}@Let A;;exchange: x ∈ B \ A,  w(x) > w(gᵢ)  ✗@exchange gives"
The claim is that greedy's i th element weighs at least the optimum's, for every i. If not, take the first position where it's lighter. Let A be greedy's first i minus one choices, and B the optimum's first i. Exchange gives an x in B that can join A, heavier than greedy's choice.

@words text="greedy would have taken x first" sub="contradiction"
But greedy, having chosen A, would have reached x before its own i th choice, and taken it. That's a contradiction. So greedy is never lighter, position by position, and its total is the best.

@chapter Not a matroid means greedy loses
@math heading="Build the bad weighting" items="exchange fails for A, B with |A| = a@exchange fails;;A: weight a + 2  ·  B \ A: weight a + 1  ·  rest: 0@a plus two;;greedy ≤ a(a + 2)  <  (a + 1)² ≤ w(B)@a times a plus two"
The converse is constructive. Take a pair where exchange fails, with A of size a. Give A's elements weight a plus two, the rest of B weight a plus one, and everything else zero. Greedy takes all of A, then nothing from B. It collects at most a times a plus two, less than a plus one squared, which B alone reaches.

@art path-weights
On the matchings of a three edge path, A is the middle edge and B is the two ends. The recipe gives the middle weight three and the ends two each.

@art balance
Greedy grabs the middle, for three, and then neither end can join it. But the two ends together are worth four.

@words text="weights 2 3 2" sub="greedy 3 · best 4"
That's exactly the weighting the lab ships as this family's default: two, three, two. So you meet a counterexample before you even read the proof that guarantees one.

@chapter The search
@art weight-cube
Then the panel goes further than the proof. It walks every weighting in one, two, three to the n, in a fixed order, and stops at the first one where greedy loses. For three elements, that's twenty seven weightings, and it stops at the thirteenth.

@words text="1 2 2" sub="greedy takes the middle: 2 · the ends: 3"
The thirteenth is one, two, two. Greedy takes the middle edge, worth two. The two ends together are worth three. Thirteen says nothing about the family. It's just where that walk order happens to find it, and relabelling moves it.

@words text="tie: 2 and 2" sub="the tie-break is part of the algorithm"
And notice the tie. The middle and one end both weigh two. Greedy's fixed tie break takes the middle. Break the tie the other way, and greedy takes both ends and reaches three. A counterexample can depend on the tie break.

@chapter The other direction, swept
@list heading="All 243 weightings in {1, 2, 3}⁵" items="Uniform: greedy never beaten@uniform|Graphic: greedy never beaten@graphic|Partition: greedy never beaten@partition"
On the three matroids, the panel walks the whole space, all two hundred and forty three weightings of five elements. Greedy is never beaten, on the uniform, graphic or partition family.

@art sweep-grid
The panel says it tried all of them, because no counterexample found and the whole space was searched are different sentences. But it's still a sample. The theorem covers every weighting, and the sweep catches code that's drifted from the theorem.

@chapter Where people slip
@list heading="Common slips" items="Testing greedy on the weighting you happen to have@The first|Reading the thirteen as meaningful@The second|Forgetting the sweep is a sample@The third"
The first slip is testing greedy on the weighting you happen to have. On the non matroid, twelve weightings in a row let greedy win. The second is reading the thirteen as meaningful. The third is forgetting that two hundred and forty three weightings is a sample of infinitely many.

@chapter Try it
@words text="matchings of a path · weights 3 1 3"
Your turn. On the three edge path, try weights three, one, three. Does greedy win here? Then explain why that run, on its own, tells you nothing about whether the family is a matroid.

@end text="Search for the weighting that beats greedy"
You can sweep every weighting and find the one that beats greedy, on Learn. That's learn dot get er done dot I O.

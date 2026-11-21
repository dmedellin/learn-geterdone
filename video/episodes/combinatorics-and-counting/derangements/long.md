---
format: long
lesson: combinatorics-and-counting/derangements
title: Derangements: the hat-check problem and the surprise of 1/e
thumb: Nobody gets their own hat
---

@chapter Nobody gets their own hat
@title text="Derangements" sub="Combinatorics and Counting" art=thumb
A group of people check their hats, and the hats come back at random. What's the chance that nobody gets their own?

@art hat-check
You might guess that with more people, someone is bound to get their own hat. But the answer barely depends on how many people there are, and it settles almost at once.

@art no-fixed-point
A derangement of one to n is a permutation that moves every element. Nothing stays in its own place. We write D n for the number of them.

@art fixed-point
A permutation that leaves even one element where it was isn't a derangement. That element is called a fixed point.

@chapter Counting by inclusion–exclusion
@words text="Aᵢ = permutations that fix i"
Let A i be the set of permutations that fix element i. A derangement is in none of the A i, so D n is n factorial minus the size of their union.

@math heading="Dₙ by inclusion–exclusion" items="each k-fold intersection: (n − k)!@n minus k factorial;;there are C(n, k) of them@C of n, k of them;;Dₙ = Σ (−1)ᵏ C(n, k)(n − k)!@So D n;;= n! Σ (−1)ᵏ / k!@n factorial times"
Fixing k chosen elements leaves the others free, so each such intersection has n minus k factorial members, and there are C of n, k of them. So D n is the alternating sum of those. That simplifies to n factorial times the sum of minus one to the k, over k factorial.

@math heading="Dₙ = n!(1 − 1/1! + 1/2! − ⋯)" items="D₄ = 24(1 − 1 + 1/2 − 1/6 + 1/24) = 9@twenty four"
For four people: twenty four, times one minus one, plus a half, minus a sixth, plus one twenty fourth. That's nine.

@chapter The surprising limit
@math heading="Dₙ for small n" items="D₁ = 0,  D₂ = 1,  D₃ = 2@zero, one, two;;D₄ = 9,  D₅ = 44,  D₆ = 265@nine, forty four;;D₇ = 1854,  D₈ = 14833@one thousand eight hundred and fifty four"
The first few are zero, one, two, then nine, forty four, two hundred and sixty five. Then one thousand eight hundred and fifty four, and fourteen thousand eight hundred and thirty three.

@art converging-zigzag
Now divide by n factorial, to get the fraction of all permutations that are derangements. It goes a half, a third, then point three seven five, point three six six seven, and it settles down almost at once.

@words text="Dₙ / n! → 1/e ≈ 0.3679"
The limit is one over e, about point three six seven nine. The formula's sum is the alternating series for one over e, and its terms shrink so fast that the fraction is right to four places by n equals seven.

@words text="10 people or 10 million: ≈ 0.3679"
So the chance that nobody gets their own hat is essentially the same for ten people as for ten million. Extra people bring extra ways to be mismatched. And D n is always the nearest whole number to n factorial over e.

@chapter A recurrence
@art recurrence-split
There's a second route. In a derangement, element one goes to some position j, with n minus one choices. If j goes to position one, the other n minus two form a derangement: D n minus two ways. If not, the remaining n minus one form one of their own: D n minus one ways.

@math heading="Recurrence" items="Dₙ = (n − 1)(Dₙ₋₁ + Dₙ₋₂)@D n equals;;D₄ = 3(D₃ + D₂) = 3(2 + 1) = 9@three times"
So D n equals n minus one, times D n minus one plus D n minus two. Check it: D four is three times two plus one, which is nine. Two different methods, the same numbers.

@chapter Exactly k fixed points
@art choose-then-derange
Out of six people, how many outcomes give exactly two of them their own hat? First choose which two: C of six, two, fifteen ways. Then derange the other four so none is fixed: D four, nine ways.

@math heading="Six people, exactly two fixed" items="C(6, 2) · D₄ = 15 · 9 = 135@Fifteen times nine;;Σₖ C(6, k) · D₆₋ₖ = 720 = 6!@sum over every k"
Fifteen times nine is a hundred and thirty five. Now check it. Every permutation has one definite number of fixed points, so the sum over every k of C of six, k times D six minus k must be six factorial, seven hundred and twenty. And it is, as long as D zero is one.

@chapter Where people slip
@list heading="Common slips" items="Forgetting D₀ = 1@The first|Unequal forbidden positions@The second|Expecting the proportion to vary with n@And the third"
The first slip is forgetting that D zero is one; the empty permutation has no fixed points. The second is using derangements when each element doesn't have exactly one forbidden position. And the third is expecting the proportion to change with n. It doesn't.

@chapter Try it
@words text="7 elements, exactly three fixed points" sub="then sum over every k: 7! = 5040"
Your turn. Count the permutations of seven elements with exactly three fixed points. Then check that summing your formula over every k from zero to seven gives seven factorial, five thousand and forty.

@end text="Watch Dₙ / n! settle on 1/e"
You can step n up and watch the fraction settle on one over e, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: combinatorics-and-counting/generalized-pigeonhole
title: The pigeonhole principle: the simple idea behind surprising proofs
thumb: The hard part is the boxes
---

@chapter Some box has at least
@title text="The Pigeonhole Principle" sub="the generalised version" art=thumb
Put n objects into k boxes, and some box must hold at least n over k, rounded up. That's the generalised pigeonhole principle. It's almost too simple to state. The hard part is choosing the boxes.

@art pigeon-boxes
Here's why it's true. If every box held at most one less than that bound, the total would come out smaller than n. But all n objects were placed. So some box must reach the bound.

@math heading="Some box has at least ⌈n/k⌉" items="100 people, 12 months: ⌈100/12⌉ = 9@a hundred people;;10 integers, 2 parities: ⌈10/2⌉ = 5@ten integers;;50 objects, 7 boxes: ⌈50/7⌉ = 8@fifty objects"
Among a hundred people, at least nine share a birth month. In any ten integers, at least five share a parity. And fifty objects in seven boxes puts at least eight in some box. Each is one division.

@art month-boxes
Always round up. Fifty over seven is about seven point one four, so the guarantee is eight. Rounding down to seven is true, but weaker than what holds. And nine would be false: seven boxes holding eight, then seven in each of the other six, account for all fifty.

@chapter Monotone subsequences
@art zigzag-sequence
Now a real theorem. Erdos and Szekeres showed that any sequence of n squared plus one distinct numbers has a monotone subsequence of length n plus one, increasing or decreasing. You can't avoid it.

@words text="at each position i: (aᵢ, bᵢ)" sub="longest increasing, longest decreasing, ending at i"
At each position i, record two numbers: a i, the length of the longest increasing subsequence ending there, and b i, the length of the longest decreasing one ending there.

@art pair-grid
Suppose there's no monotone subsequence of length n plus one. Then every a and every b is between one and n, so the pair takes one of n squared values. With n squared plus one positions, two positions must share a pair.

@math heading="Two positions i < j can't share a pair" items="xᵢ < xⱼ ⟹ aⱼ > aᵢ@If x i is less;;xᵢ > xⱼ ⟹ bⱼ > bᵢ@If x i is greater"
But that's impossible. If x i is less than x j, the increasing run ending at i extends to j, so a j is bigger. If x i is greater, then b j is bigger. Either way, the pairs differ.

@words text="inventing the boxes is the proof"
The boxes are the n squared possible pairs, and inventing them is the entire proof. Once the classification is chosen, pigeonhole does the rest in one line.

@chapter Six people
@art six-points-graph
Among any six people, three are mutual acquaintances, or three are mutual strangers. Take one person, P. Each of the other five is an acquaintance or a stranger, so at least three of them, five over two rounded up, fall in one class. Say three acquaintances.

@words text="R(3, 3) = 6"
If any two of those three know each other, they and P are three mutual acquaintances. If no two do, those three are mutual strangers. Either way, there's a triangle.

@art five-cycle
And five people aren't enough. Put five in a circle where each knows exactly their two neighbours, and there's no triangle of either kind. That construction is what makes the answer exactly six, not just at most six.

@words text="R(4, 4) = 18 · 43 ≤ R(5, 5) ≤ 46"
These Ramsey numbers grow ferociously, and almost all of them are unknown. R of four, four is eighteen. R of five, five is only known to lie between forty three and forty six, despite decades of effort.

@chapter A block that sums to a multiple
@math heading="Any n integers: some block sums to a multiple of n" items="partial sums s₁, s₂, …, sₙ, mod n@partial sums;;some sⱼ ≡ 0: done@remainder zero;;else n sums, n − 1 remainders@n minus one;;sⱼ − sᵢ = aᵢ₊₁ + ⋯ + aⱼ ≡ 0@difference"
One more. Take any n integers, and their partial sums, and look at the remainders mod n. If some partial sum has remainder zero, you're done. If none does, n sums share n minus one remainders, so two match. Their difference, a consecutive block, is a multiple of n.

@chapter Where people slip
@list heading="Common slips" items="Rounding the bound down@The first|More boxes than objects@The second|Proving only the upper bound@And the third"
The first slip is rounding the bound down. The second is choosing more boxes than objects. A finer classification proves less, and with too many boxes nothing follows. And the third is proving only the upper bound of a Ramsey type result, without the construction.

@chapter Try it
@words text="5 points in a unit square" sub="two are within √2 / 2 of each other"
Your turn. Show that among any five points in a unit square, two are within root two over two of each other. Then try a finer partition, and see what it costs you in the number of points.

@end text="See the triangles the proof ranges over"
You can list the twenty triangles among six people that the proof ranges over, on Learn. That's learn dot get er done dot I O.

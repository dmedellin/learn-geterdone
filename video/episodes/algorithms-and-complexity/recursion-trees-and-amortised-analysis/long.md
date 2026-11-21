---
format: long
lesson: algorithms-and-complexity/recursion-trees-and-amortised-analysis
title: Recursion trees, and why a doubling array is fast
thumb: Rare and expensive is cheap
---

@chapter Two new questions
@title text="Recursion Trees and Amortised Analysis" sub="Algorithms and Complexity" art=thumb
The master theorem handles even splits. But what about a split that isn't even? And what about an operation that's usually cheap, but now and then very expensive? This lesson answers both.

@chapter Recursion trees
@art uneven-tree
Draw the recursion as a tree. The root does the top level combining work, its children are the subproblems, and so on down to the base cases. The total cost is the work at every node, and it's easiest to add it up level by level.

@math heading="T(n) = T(n/3) + T(2n/3) + n" items="each level: sizes sum to n  →  n work@each level;;depth: log₃⸝₂ n@the depth;;total: Θ(n log n)@the total"
Take T of n over three plus T of two n over three, plus n. At each level the sizes still add up to n, so each level does n work. The deepest branch shrinks to two thirds each time, so the depth is log base three halves of n. The total is Theta of n log n, just like an even split.

@words text="Any constant-fraction split → log depth"
That's why quicksort survives an imperfect pivot. Any constant fraction split gives logarithmic depth. Only a consistently extreme pivot, splitting off one element at a time, gives the quadratic worst case.

@math heading="T(n) = 2T(n/2) + n²" items="level i:  2ⁱ · (n/2ⁱ)² = n²/2ⁱ@level i;;total:  n² Σ 1/2ⁱ < 2n²@the total;;T(n) = Θ(n²)@Theta of n squared"
Now a tree with unequal levels: two T of n over two, plus n squared. Level i has two to the i subproblems of size n over two to the i, doing n squared over two to the i work. The total is less than two n squared, so T of n is Theta of n squared.

@art shrinking-levels
Here the root dominates. And the master theorem agrees, since log two of two is one, which is less than d equals two.

@chapter Amortised cost
@words text="Amortised cost = total cost of m operations ÷ m" sub="for a worst-case sequence"
Now the second question. The amortised cost of an operation is the total cost of a worst case sequence of m operations, divided by m. It's a guarantee about sequences, not about any single operation.

@art doubling-array
Here's the classic example. A dynamic array doubles its capacity whenever it fills up, copying every element across. A single insertion can cost Theta of n. But insertion is Theta of one, amortised.

@math heading="n insertions from capacity 1" items="copies at sizes 1, 2, 4, 8, …@the size reaches;;1 + 2 + 4 + ⋯ + 2^⌊log₂ n⌋ < 2n@less than two n;;+ n insertions:  total < 3n@under three n"
Start from capacity one and insert n elements. The copies happen when the size reaches one, two, four, eight, and so on. They cost less than two n element moves in total. Add the n insertions themselves, and the total is under three n. So each insertion costs under three, a constant.

@art cost-spikes
The geometric series is doing the work. The expensive operations are rare, and their cost grows exactly as fast as the gaps between them.

@art fixed-steps
And doubling is essential. Grow by a fixed amount c instead, and the copies happen at c, two c, three c, and so on. That totals Theta of n squared moves, Theta of n per insertion. The two policies differ by a whole class.

@chapter Three methods
@list heading="Three methods" items="Aggregate: total ÷ m@aggregate|Accounting: overcharge cheap ops, save credit@accounting|Potential: actual cost + ΔΦ@potential"
There are three ways to do this. The aggregate method takes the total cost and divides by m. The accounting method charges cheap operations extra and saves the credit. And the potential method defines a potential function on the data structure, and adds its change to the actual cost.

@art credit-coins
Here's accounting on the doubling array. Charge three units per insertion. One pays for the insertion. One is saved to copy this element later. And one is saved to copy an older element. When the array doubles, every element has exactly the credit its move needs.

@chapter Not average case
@words text="Amortised ≠ average case" sub="no probability, every sequence"
Amortised is not the same as average case. Average case assumes a distribution over inputs. Amortised assumes nothing, and bounds the total for any sequence at all. That's a strictly stronger guarantee.

@chapter Where people slip
@list heading="Common slips" items="Confusing amortised with average case@The first|Summing a recursion tree by branch@The second|Assuming any growth policy works@The third"
The first slip is confusing amortised with average case. The second is summing a recursion tree by branch instead of by level. Levels are what make the sums simple. And the third is assuming any growth policy gives amortised constant time. Only geometric growth does.

@chapter Try it
@words text="Grow by c:  c + 2c + 3c + ⋯" sub="why is that Θ(n²)?"
Try the fixed increment policy yourself. Write the copy costs as a sum, c plus two c plus three c, up to about n, and use the summation formula to see why it's Theta of n squared.

@end text="Rare and expensive can still be cheap"
The full lesson on recursion trees and amortised analysis is on Learn. That's learn dot get er done dot I O.

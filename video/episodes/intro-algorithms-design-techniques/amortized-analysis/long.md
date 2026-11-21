---
format: long
lesson: intro-algorithms-design-techniques/amortized-analysis
title: Amortized analysis: aggregate, accounting and potential
thumb: Cheap ones pay for the big one
---

@chapter Not an average over inputs
@title text="Amortized Analysis and Dynamic Tables" sub="Introduction to Algorithms, Chapter 17" art=thumb
Some operations are usually cheap and occasionally very expensive. Amortized analysis bounds the total cost of a whole sequence, so the rare expensive ones are paid for by the many cheap ones.

@quote text="an amortized analysis guarantees the average performance of each operation in the worst case." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 17"
The chapter separates this from average case analysis, because no probability enters it. An amortized analysis guarantees the average performance of each operation in the worst case. The average is over a sequence, and it holds for every sequence.

@chapter Aggregate analysis
@art multipop-stack
Start with a stack that has push, pop, and multipop, which pops up to k objects at once. One multipop can cost O of n, so a careless bound on n operations is O of n squared. But an object can be popped at most once for each time it was pushed. So all the pops together are at most the pushes, and n operations cost O of n.

@art binary-counter
Next, a binary counter, where incrementing costs the bits it flips. One increment can flip every bit. But bit zero flips every time, bit one every second time, bit two every fourth. So n increments flip fewer than n times one plus a half plus a quarter and so on, which is two n.

@chapter The accounting method
@art credit-coins
The accounting method charges each operation an amortized cost, and stores any excess as credit on objects. For the stack, charge two per push: one pays for the push, and one sits on the object to pay for popping it later. Pop and multipop are charged nothing. The one rule: credit must never go negative.

@chapter The potential method
@math heading="Potential" items="ĉᵢ = cᵢ + Φ(Dᵢ) − Φ(Dᵢ₋₁)@actual cost plus;;Σ ĉᵢ = Σ cᵢ + Φ(Dₙ) − Φ(D₀)@the middle terms cancel"
The potential method stores the prepaid work in the structure as a whole, as a function phi. An operation's amortized cost is its actual cost plus the change in phi. Add them up, and the middle terms cancel, so if phi never drops below where it started, the amortized total bounds the actual total.

@art potential-level
For the stack, let phi be the number of objects. A push costs two, amortized. A multipop of k objects costs zero. For the counter, let phi be the number of one bits, and every increment costs at most two.

@math heading="4-bit counter, 10 increments" items="flips: 10 + 5 + 2 + 1 = 18@ten, five, two and one;;Φ₀ = 0,  Φ₁₀ = ones in 1010 = 2@one zero one zero;;amortized 18 + 2 = 20 = 2 per increment@exactly two"
Increment a four bit counter ten times from zero. The bits flip ten, five, two and one times, eighteen in all, under twenty. Phi starts at zero and ends at the ones in one zero one zero, which is two. So the amortized total is twenty, exactly two per increment.

@chapter Dynamic tables
@art table-doubling
Now a table that grows. When it's full, double it and copy every item across. One insertion can cost a lot, but n insertions cost less than three n. Charge three: one to insert the item, one to move it at the next expansion, and one to move an item that's already moved once.

@math items="Φ = 2·num − size@two times num minus size"
The potential is two times num minus size. It's zero just after an expansion, and equals num just before one, exactly enough to pay for the copying.

@art thrash-boundary
Deletions bring a trap. Halve the table whenever it's under half full, and a sequence of inserts and deletes at the boundary expands and contracts over and over, copying everything each time. The fix is to halve only below a quarter full.

@math heading="The boundary sequence, 20 operations" items="quarter rule: 35  (bound 54)@the quarter rule;;half rule: 24 + 19 + 19 + 10 = 72@the half rule"
In the lab's boundary sequence, twenty operations cost thirty five under the quarter rule, against a bound of fifty four. Worked by hand under the half rule, the same sequence costs seventy two. Each round of delete, delete, insert, insert costs nineteen instead of four.

@chapter Common slips
@list heading="Common slips" items="Reading amortized as average-case@The first|Thinking every operation is cheap@The second|Letting credit or potential go negative@the third"
The first slip is reading amortized cost as average case cost. Nothing is random. The second is thinking a cheap amortized cost means every operation is cheap. One expansion of thirty two items costs thirty three. And the third is letting the credit, or the potential, go negative.

@chapter Try it
@words text="3-bit counter from 110, 5 increments" sub="check 2n − bₙ + b₀"
Your turn. A three bit counter starts at six, one one zero, and is incremented five times, wrapping past seven to zero. Count the bits flipped by each increment, and check the total against two n minus b n plus b nought. Then explain why the bound needs b nought.

@end text="Price a table yourself"
You can price a growing and shrinking table, operation by operation, on Learn. That's learn dot get er done dot I O.

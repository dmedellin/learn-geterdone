---
format: long
lesson: dynamic-programming/the-fill-order-is-part-of-the-algorithm
title: The fill order is part of the algorithm: matrix chains done wrong
thumb: Right recurrence, wrong order
---

@chapter The question
@title text="The Fill Order Is Part of the Algorithm" sub="Dynamic Programming and Optimal Substructure" art=thumb
A dynamic program has three parts: a table, a recurrence, and an order to fill the table in. The recurrence is the part people check. The order is the part that quietly goes wrong, and when it does, nothing crashes.

@art chain-bracketing
Here's the problem. You have a chain of matrices to multiply, in a fixed order. Multiplying a p by q matrix with a q by r matrix costs p times q times r scalar multiplications. The product is the same however you bracket the chain, but the cost isn't.

@words text="30 35 15 5 10 20 25" sub="seven dimensions · six matrices"
Seven numbers describe six matrices. The lab loads thirty, thirty five, fifteen, five, ten, twenty, twenty five. So the first matrix is thirty by thirty five, the second is thirty five by fifteen, and so on.

@chapter The recurrence
@math heading="Matrix chain" items="cost(i, i) = 0@cost of i, i;;cost(i, j) = min over i ≤ k < j of@for i less than j;;cost(i, k) + cost(k+1, j) + p(i)·p(k+1)·p(j+1)@the two halves"
Let cost of i, j be the fewest multiplications for matrices i through j. Cost of i, i is zero. And for i less than j, it's the minimum over split points k, of the two halves, plus p of i, times p of k plus one, times p of j plus one, for the final join.

@art last-split
Why is that right? Every bracketing has a last multiplication, joining i through k with k plus one through j. The join's cost depends only on i, k and j. And if either half could be done more cheaply, you'd swap it in. That's optimal substructure.

@chapter The order it forces
@art diagonal-fill
Now look at what each cell reads. Cost of i, j reads two strictly shorter intervals. So you have to fill by interval length: every length zero interval, then length one, and so on. That's a diagonal sweep, twenty one cells of the thirty six.

@art row-fill
But the order everyone writes, because every other table is filled that way, is row by row. Row major crosses the whole first row before it fills one cell of the second. And cell zero, two needs cell one, two, which is in the second row. It reads it anyway.

@chapter The cell that goes wrong
@math heading="Correct: cost(0, 2)" items="min(0 + 2625 + 30·35·5,  15750 + 0 + 30·15·5)@the minimum of;;= min(0 + 2625 + 5250,  15750 + 0 + 2250)@five thousand two hundred and fifty;;= 7875@seven thousand eight hundred"
Done correctly, cost of zero, two is the minimum of two options. Zero plus two thousand six hundred and twenty five plus five thousand two hundred and fifty, or fifteen thousand seven hundred and fifty plus zero plus two thousand two hundred and fifty. That's seven thousand eight hundred and seventy five.

@math heading="Row major: cost(0, 2)" items="cell (1, 2) not written yet  →  reads as 0@has been written;;0 + 0 + 5250 = 5250@zero plus zero;;5250 < 18 000  →  stores 5250@stores it"
Row major reaches cell zero, two before cell one, two has been written. The missing cell reads as nothing, which acts like zero. So the first option is zero plus zero plus five thousand two hundred and fifty. That beats eighteen thousand, so it stores it. No bracketing of those three matrices costs that.

@words text="by length: 15 125 · row major: 9 000" sub="35 reads hit unwritten cells"
The damage spreads to every cell that reads it. By interval length, the corner says fifteen thousand one hundred and twenty five, and all forty two bracketings confirm it. Row major says nine thousand. Thirty five reads landed on unwritten cells.

@art full-table
And the wrong order does more work. Row major writes all thirty six cells, against twenty one. Both make the same seventy reads. It produces a fuller looking table, with a cheaper looking answer, and every cell's arithmetic checks out against what was there at the time.

@chapter What is proved
@math heading="Costs" items="table: Θ(n²) cells × O(n) each = Θ(n³)@Theta of n squared;;bracketings: Catalan(n − 1)@Catalan;;6 → 42 · 7 → 132 · 9 → 1 430@forty two"
The table has Theta of n squared meaningful cells, each taking order n work, so filling it is Theta of n cubed. Enumerating bracketings grows like the Catalan numbers: forty two at six matrices, a hundred and thirty two at seven, fourteen hundred and thirty at nine.

@art catalan-growth
The enumeration is the only reason we know fifteen thousand one hundred and twenty five is right. And it's also the first thing to become unrunnable as the chain grows.

@chapter Where people slip
@list heading="Common slips" items="Treating the fill order as a presentation detail@The first|Expecting a wrong order to fail loudly@The second|Checking the recurrence and trusting the table@The third"
The first slip is treating the fill order as a detail. It's a third of the algorithm, so write it down beside the recurrence. The second is expecting a wrong order to fail loudly. It can't. The third is checking the recurrence and concluding the table is right. The recurrence was right in both runs.

@chapter Try it
@words text="cost(1, 3)" sub="which cells must exist first?"
Your turn. For the chain thirty, thirty five, fifteen, five, ten, twenty, twenty five, write out the options for cost of one, three. Which cells does it read, and does row by row fill them in time?

@end text="Watch the fill order go wrong"
You can fill the table both ways and see every early read painted red, on Learn. That's learn dot get er done dot I O.

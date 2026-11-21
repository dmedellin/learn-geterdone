---
format: long
lesson: intro-algorithms-design-techniques/matrix-chain-multiplication
title: Matrix-chain multiplication: the order that saves the work
thumb: Same product, half the work
---

@chapter Order matters
@title text="Matrix-Chain Multiplication" sub="Introduction to Algorithms, Section 15.2" art=thumb
Multiplying matrices is associative. Every way of bracketing a chain gives the same product. But not at the same cost, and the difference can be enormous.

@quote text="Note that in the matrix-chain multiplication problem, we are not actually multiplying matrices." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 15.2"
The authors make one thing clear early. Note that in the matrix chain multiplication problem, we are not actually multiplying matrices. The output is an order of operations, and the time spent finding it is repaid when the multiplying is finally done.

@chapter The cost
@art matrix-shapes
A p by q matrix times a q by r matrix takes p times q times r scalar multiplications, and gives a p by r result. So for a chain A one to A n, with matrix A i of size p i minus one by p i, the problem is to bracket it with the fewest multiplications.

@art catalan-growth
Can you just try every bracketing? No. The last multiplication splits the chain somewhere, and each side is bracketed independently. The counts are the Catalan numbers: one, one, two, five, fourteen, forty two, a hundred and thirty two, growing exponentially.

@chapter Optimal substructure
@art split-point
Suppose the best bracketing of A i to A j splits after A k. Then its bracketing of the left part must itself be the best for that part. If a cheaper one existed, you could paste it in and lower the total. The same goes for the right part.

@math heading="The recurrence" items="m[i, i] = 0@m of i i;;m[i, j] = min over i ≤ k < j of@for i less than j;;m[i, k] + m[k + 1, j] + pᵢ₋₁·pₖ·pⱼ@the cost of multiplying"
So m of i i is zero. And for i less than j, m of i j is the minimum over every split k of the left cost, plus the right cost, plus the cost of multiplying the two results, p i minus one times p k times p j. The split that wins goes in a second table, s.

@chapter The fill order
@art diagonal-fill
Each entry reads only shorter subchains. So the table is filled by chain length: all chains of length two, then three, up to the whole chain. There are theta of n squared entries, each trying up to n splits, so it's O of n cubed time.

@math heading="Dimensions 3 5 2 6 4" items="m[1,2] = 30,  m[2,3] = 60,  m[3,4] = 48@thirty, sixty;;m[1,3] = min(150, 66) = 66@sixty six;;m[2,4] = min(88, 180) = 88@eighty eight;;m[1,4] = min(148, 102, 138) = 102@a hundred and two"
Take four matrices with dimensions three, five, two, six, four. The pairs cost thirty, sixty and forty eight. For one to three, the splits cost a hundred and fifty or sixty six, so sixty six. For two to four, eighty eight. And the whole chain tries a hundred and forty eight, a hundred and two, and a hundred and thirty eight, so a hundred and two.

@art two-orders
The best split is after A two, so the answer is A one A two, times A three A four. That pairs the left two and the right two, a shape no left to right evaluation would find. The worst of the five bracketings costs two hundred and forty, more than twice as much.

@chapter Filling it wrong
@math heading="6 2 10 4 8 3" items="by chain length: 228@two hundred and twenty eight;;all 14 bracketings agree: 228@fourteen;;row by row: 36  ✗@row by row"
In the lab, take five matrices, six, two, ten, four, eight, three. Filled by chain length, the answer is two hundred and twenty eight, and checking all fourteen bracketings finds the same minimum. Now fill it row by row instead, and the table finishes with thirty six, a number no bracketing achieves.

@art wrong-order
Some cells were read before they were written. Nothing crashed, and the number looked plausible. That's why the fill order has to be argued from the recurrence, not trusted to look right.

@chapter Common slips
@list heading="Common slips" items="Thinking the order doesn't matter much@The first|Filling the table in the order it's drawn@The second|Picking the cheapest final product first@the third"
The first slip is thinking the multiplication order doesn't matter much. The best and worst on five matrices are two hundred and twenty eight and one thousand and sixty four. The second is filling the table in the order it's drawn. And the third is picking the split that makes the final multiplication cheapest, a greedy rule that can fail.

@chapter Try it
@words text="6 2 10 4 8 3" sub="fill m and s by chain length"
Your turn. Fill the m and s tables by hand for six, two, ten, four, eight, three, by chain length. Check that the whole chain costs two hundred and twenty eight, print the bracketing from s, and list the cells a row by row fill would read too early.

@end text="Fill it in two orders"
You can fill a chain's table in two orders and check it against every bracketing, on Learn. That's learn dot get er done dot I O.

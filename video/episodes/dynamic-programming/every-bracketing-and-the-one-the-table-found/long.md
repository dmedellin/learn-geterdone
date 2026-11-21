---
format: long
lesson: dynamic-programming/every-bracketing-and-the-one-the-table-found
title: Every bracketing, and getting the tree back from the table
thumb: The number is not the tree
---

@chapter The question
@title text="Every Bracketing, and the One the Table Found" sub="Dynamic Programming and Optimal Substructure" art=thumb
A dynamic programming table gives you a number, the cheapest cost. But usually you want the thing itself, the actual bracketing. Getting that back is a separate claim, and it deserves its own check.

@art bracket-tree
A bracketing is really a binary tree. Its leaves are the matrices in order, and each internal node is one multiplication. Its cost is the sum, over the internal nodes, of p times q times r, where the left child is p by q and the right child is q by r.

@chapter How many are there?
@math heading="Counting bracketings" items="c(1) = 1@c of one;;c(n) = Σ over k of c(k) · c(n − k)@c of n;;c(n) = C(n − 1),  the Catalan numbers@Catalan"
Every bracketing has a last multiplication, splitting the chain after some matrix k. The left part and the right part are bracketed independently. So the count c of n is the sum over k, of c of k times c of n minus k, with c of one equal to one. That's the Catalan recurrence, shifted by one.

@list heading="Catalan(n − 1)" items="4 matrices: 5@four matrices|6 matrices: 42@forty two at six|7 matrices: 132@seven|9 matrices: 1 430@nine"
That gives five bracketings at four matrices, forty two at six, and a hundred and thirty two at seven. By nine, it's fourteen hundred and thirty, and the growth never lets up.

@art many-trees
The lab's enumeration builds every one of those trees, using the same recursion with the trees kept instead of counted. And it returns exactly those counts.

@art split-reuse
Notice that split. It's exactly the split the table's recurrence minimises over. The recurrence is the enumeration, with the sub answers stored instead of rebuilt. That's what dynamic programming is.

@chapter Following the pointers back
@art pointer-walk
Each cell records which split k won. To get the tree back, start at the cell for the whole chain and read its split. That gives two intervals, each with its own recorded split. Keep going until you reach single matrices.

@words text="((A1A2)(((A3A4)(A5A6))A7))" sub="dimensions 5 10 3 12 5 50 6 4"
On the lab's seven matrices, with dimensions five, ten, three, twelve, five, fifty, six, four, the walk returns this tree. A one A two together, then A three A four and A five A six, joined, then with A seven.

@chapter Three routes, one answer
@list heading="Three checks" items="Table: 2052 after 28 cells@The table|All 132 bracketings: best 2052, worst 14 060@enumeration|Tree re-costed from the dimensions: 2052@re costing"
The table reports two thousand and fifty two after filling twenty eight cells. The enumeration walks all a hundred and thirty two bracketings, with no table, and finds a best of two thousand and fifty two. And re costing the tree from the dimensions alone also gives two thousand and fifty two.

@art wrong-pointer
Why the third check? Because following a wrong pointer doesn't give an error. It gives a different bracketing, still a valid tree, still printable, still looking like an answer. The only cheap way to catch it is to cost the tree independently, and compare.

@chapter What the counts say
@words text="7 matrices: 28 cells vs 132 · 4 matrices: 10 cells vs 5"
On seven matrices, the table fills twenty eight cells against a hundred and thirty two bracketings, about five times fewer. But at four matrices, it's ten cells against five bracketings, and the table is behind.

@math heading="Proved growth" items="table: Θ(n³)@Theta of n cubed;;enumeration: Catalan(n − 1) ≈ 4ⁿ / n^(3/2)@four to the n"
The proved statements are Theta of n cubed for the table, against Catalan of n minus one for enumeration, which grows like four to the n over n to the three halves. So the gap widens without bound. But the small counts tell you that on four matrices, the asymptotically better method is slower.

@art worst-vs-best
The enumeration buys one more thing, the worst bracketing. Here it costs fourteen thousand and sixty, about six point nine times the optimum. The table only ever keeps minima, so it can't tell you what optimising was worth.

@chapter Where people slip
@list heading="Common slips" items="Treating the value and the object as one answer@The first|Relying on an enumeration you can't run@The second|Reading the optimum as the value of optimising@The third"
The first slip is treating the value and the tree as one answer. The table can be right about one and the walk wrong about the other. The second is relying on an enumeration you can't run at the size you care about. The lab refuses nine matrices. The third is reading the optimum's cost as what optimising is worth.

@chapter Try it
@words text="((A1A2)(((A3A4)(A5A6))A7))" sub="5 10 3 12 5 50 6 4"
Your turn. Re cost this tree by hand from the dimensions. Work out each multiplication from the spans of its two children, add them up, and check you get two thousand and fifty two.

@end text="Walk the pointers yourself"
You can enumerate every bracketing and re cost the table's tree, on Learn. That's learn dot get er done dot I O.

---
format: long
lesson: greedy-and-matroids/why-huffman-is-optimal
title: Why no prefix code beats Huffman: two lemmas and an induction
thumb: Two lemmas close the gap
---

@chapter The question
@title text="Why Huffman Is Optimal" sub="Greedy Algorithms and Matroids" art=thumb
You can measure that Huffman's code is short. But the claim that no prefix code is shorter is a claim about codes nobody built. On six symbols, that's forty two tree shapes and thirty thousand, two hundred and forty placements. Looking at one code can't settle it.

@math heading="Cost of a tree" items="B(T) = Σ wᵢ · dᵢ@B of T;;dᵢ = depth of symbol i@d i is"
So write the cost of a tree as B of T, the sum of each weight times its depth, where d i is the depth of symbol i.

@art tree-cost
That's the total bit count of the code, so deep leaves cost more, and heavy deep leaves cost most. Minimising the code means minimising B over every tree, and every way of putting symbols on its leaves.

@chapter Lemma one
@art deepest-siblings
The first lemma says some optimal tree has the two lightest symbols, x and y, as sibling leaves at the very bottom. Take any optimal tree. Because it's full, its deepest leaf has a sibling, a and b, both at maximum depth.

@math heading="Swap a with x" items="change = (w_a − w_x)(d_x − d_a)@the cost changes by;;w_a − w_x ≥ 0  ·  d_x − d_a ≤ 0@Since x is lightest;;change ≤ 0@at most zero"
Swap a with x. The cost changes by w a minus w x, times d x minus d a. Since x is lightest, the first factor is at least zero. Since a is deepest, the second is at most zero. So the change is at most zero.

@art downhill-swap
The tree was already optimal, so the cost can't go down either. It stays put. Do the same with b and y, and now x and y are deepest siblings. It's the exchange argument again, moving symbols between positions in a tree instead of in a schedule.

@chapter Lemma two
@art merge-leaf
The second lemma handles the merge. Replace x and y with one new symbol z, whose weight is their sum. Take an optimal tree for that smaller alphabet, and expand z back into a node with children x and y.

@math heading="The costs differ by a constant" items="B(T) = B(T′) + w_x + w_y@B of T equals;;if B(U) < B(T),  contract x, y  →  U′@Suppose some tree U;;B(U′) < B(T′)  ✗@smaller than B of T prime"
Since x and y sit one level below z, B of T equals B of T prime, plus w x plus w y. Suppose some tree U for the full alphabet were cheaper. By lemma one, x and y can be siblings in U, so contract them. That tree is smaller than B of T prime, which was optimal. A contradiction.

@chapter The induction
@art induction-ladder
Now the induction is immediate. With two symbols, the only tree gives each a one bit code, and that's optimal. For n symbols, Huffman's first merge takes the two lightest. The rest of the run is Huffman on the smaller alphabet, optimal by induction, and lemma two lifts that back up.

@chapter Checking every tree
@math heading="Shapes × assignments" items="4 leaves: 5 shapes · 120 pairs@four leaves;;5 leaves: 14 shapes · 1680 pairs@five leaves;;6 leaves: 42 shapes · 30 240 pairs@six leaves"
The lab checks the conclusion by brute force. The number of shapes follows the Catalan numbers, and each shape has n factorial assignments. Four leaves give five shapes and a hundred and twenty pairs. Five leaves give fourteen and sixteen hundred and eighty. Six leaves give forty two, and thirty thousand, two hundred and forty.

@list heading="Best found = Huffman" items="a:10 b:10 c:10 d:10 → 80 bits@four equal weights|six-symbol alphabet → 224 bits@six symbol|skewed → 170 · Fibonacci → 25@skewed and Fibonacci"
On four equal weights, the best of a hundred and twenty is eighty bits, and Huffman's costs eighty. On the six symbol alphabet, the best is two hundred and twenty four, again Huffman's. On the skewed and Fibonacci alphabets, a hundred and seventy and twenty five bits. Matched every time.

@art every-shape
The search tries every assignment, not just heaviest on shallowest. That would assume the swap inequality from lemma one, and check the proof against itself. Seven leaves means a hundred and thirty two shapes and five thousand and forty assignments each, so the panel refuses, and says so.

@chapter Where people slip
@list heading="Common slips" items="Confusing the shortest code found with no shorter code@The first|Reading the enumeration as the proof@The second|Expecting the search to grow gently@The third"
The first slip is confusing the shortest code you found with the claim that none is shorter. The second is reading the enumeration as the proof. It's four alphabets. A disagreement would be conclusive, but agreement isn't. The third is expecting the search to grow gently. Catalan times factorial explodes fast.

@chapter Try it
@words text="a:1  b:1  c:2  d:3  e:5"
Your turn. Take weights one, one, two, three and five. Run Huffman and find each depth. Then pick a tree where a heavier symbol sits deeper than a lighter one, swap them, and work out the change in cost from lemma one's formula.

@end text="Search every tree yourself"
You can check Huffman against every tree and every assignment, on Learn. That's learn dot get er done dot I O.

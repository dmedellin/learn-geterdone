---
format: long
lesson: intro-algorithms-advanced-structures/fibonacci-heaps
title: Fibonacci heaps: put off the work, then pay for it
thumb: Lazy now, tidy later
---

@chapter The bargain
@title text="Fibonacci Heaps" sub="Introduction to Algorithms, Sections 19.1–19.2" art=thumb
Chapter nineteen builds a heap that does almost nothing when you add to it, and catches up later.

@quote text="The mergeable-heap operations on Fibonacci heaps delay work as long as possible." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 19.2"
That sentence opens section nineteen point two: the mergeable heap operations on Fibonacci heaps delay work as long as possible. The chapter is an account of what that delay buys, and who pays for it.

@chapter Why bother
@math heading="Binary heap vs Fibonacci heap" items="binary: insert, extract, decrease-key Θ(lg n)@a binary heap;;binary: union Θ(n)@uniting two;;Fibonacci: insert, union, decrease-key Θ(1) amortized@a Fibonacci heap;;Fibonacci: extract-min O(lg n) amortized@extracts"
A binary heap inserts, extracts and decreases keys in theta of log n time. But uniting two of them means rebuilding, theta of n. A Fibonacci heap inserts, unites and decreases a key in constant amortized time, and extracts in O of log n amortized.

@words text="“predominantly of theoretical interest”" sub="amortized bounds · large constants"
The authors add two cautions. These are amortized bounds, not per operation ones. And the constant factors make the structure, in their words, predominantly of theoretical interest. It shines where extractions are few, as in graph algorithms that may decrease a key once per edge.

@chapter What it's made of
@art root-list
A Fibonacci heap is a collection of trees, each one min heap ordered. Their roots sit in one circular, doubly linked list, the root list. A pointer, H dot min, marks the root with the least key. Every other root is unordered.

@math heading="The potential" items="Φ(H) = t(H) + 2m(H)@the potential is;;here every mark is false@every mark is false"
For the analysis, the potential is t of H plus two m of H: the number of trees, plus twice the number of marked nodes. The marks matter in the next lesson. Here every mark is false, so the potential is just the number of roots.

@chapter Three lazy operations
@art insert-a-root
Insert makes the new key a one node tree, drops it into the root list beside the minimum, and updates the minimum if it's smaller. The number of trees rises by one, so the amortized cost is the actual cost plus one.

@art splice-lists
Union splices two root lists together and keeps the smaller minimum. The trees and marks are just the two heaps' together, so the potential doesn't change. None of these operations ever looks at a tree's shape.

@chapter Extract-min does the work
@art consolidate
Extract min removes the minimum, moves its children into the root list, and then consolidates. It takes the roots one at a time, with an array indexed by degree. When two roots share a degree d, it links them, the larger key becoming a child of the smaller, to make one tree of degree d plus one.

@art one-per-degree
At the end, no two roots share a degree. So at most D of n plus one roots are left, where D of n bounds the largest degree. The amortized cost of extraction is O of D of n.

@chapter The numbers
@art potential-ledger
In the lab, each step costs one, and each root carries one unit of potential. Insert eight keys and stop. Nothing's tidied, so each insertion spends one and stores one.

@math heading="The lab's unit costs" items="8 inserts: actual 8, amortized 16, Φ = 8@eight inserts;;then extract: actual 8, Φ 8 → 3, amortized 3@one extract min;;totals: 16 actual, 19 amortized@the totals"
Eight inserts: actual cost eight, amortized sixteen, potential eight. Then one extract min scans seven roots, for an actual cost of eight, and links them into three trees. The potential falls from eight to three, so its amortized cost is three. The totals are sixteen actual and nineteen amortized.

@words text="17 inserts, then one extract" sub="actual 17 · Φ 17 → 1 · amortized 1"
Seventeen inserts and one extraction is starker. The extraction costs seventeen actual steps and links all sixteen survivors into one tree of degree four. The potential falls from seventeen to one, so its amortized cost is one. The units the insertions stored paid for the roots scanned.

@chapter Where people slip
@list heading="Common slips" items="Reading constant amortized as cheap every time@The first|Expecting the root list to stay short@The second|Linking any two roots@And the third"
The first slip is reading a constant amortized bound as cheap every time. One extraction can cost seventeen steps. The second is expecting the root list to stay short. Only extraction tidies it. And the third is linking any two roots. Consolidate links only equal degrees, and that's what keeps degrees small.

@chapter Try it
@words text="insert 6, 2, 9, 4, 7, 1, 8 · extract" sub="root list · actual cost · ΔΦ · amortized"
Your turn. On an empty heap, insert six, two, nine, four, seven, one and eight, then extract. Write the root list afterwards, and the extraction's actual cost, change in potential, and amortized cost.

@end text="Price every heap operation"
You can watch every operation charged its actual cost and its change in potential, on Learn. That's learn dot get er done dot I O.

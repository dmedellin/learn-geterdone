---
format: long
lesson: intro-algorithms-foundations/merge-sort-and-divide-and-conquer
title: Merge sort and the recursion tree, explained
thumb: Halve it, merge it, n log n
---

@chapter A different design
@title text="Merge Sort and Divide-and-Conquer" sub="Introduction to Algorithms, Section 2.3" art=thumb
Insertion sort was incremental. It sorted a prefix, then added one more element. Merge sort takes a completely different approach, and gets a different order of growth.

@list heading="Divide-and-conquer" items="Divide into subproblems@divide|Conquer them recursively@conquer|Combine the solutions@combine"
It's divide and conquer, in three steps at every level. Divide the problem into smaller subproblems. Conquer them recursively. Then combine their solutions.

@art divide-combine
For merge sort, divide the array into two halves, sort each half by merge sort, and merge them. One element is already sorted, so the recursion stops there. The array splits in half, and in half again, down to single elements. Then everything merges back up, pairs of one into runs of two, runs of two into runs of four, until two halves become the sorted array.

@chapter Merging
@quote text="The key operation of the merge sort algorithm is the merging of two sorted sequences in the ‘combine’ step." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 2.3"
The book is clear about where the work is. The key operation of the merge sort algorithm is the merging of two sorted sequences in the combine step.

@art two-piles
Picture two face up piles of cards, each sorted with the smallest on top. Take the smaller of the two top cards and put it face down on an output pile. Repeat. When one pile is empty, move the other one over whole.

@art sentinel
The book adds a twist. A sentinel card holding infinity sits at the bottom of each pile, so no step ever has to ask whether a pile is empty. Each step is constant work, so merging n elements costs theta of n. And like insertion sort, it's proved correct by a loop invariant.

@chapter The recurrence
@math heading="Merge sort's recurrence" items="T(n) = 2T(n/2) + Θ(n)@T of n equals;;T(1) = Θ(1)@T of one"
Dividing costs constant time. Conquering costs two T of n over two. Merging costs theta of n. So T of n equals two T of n over two, plus theta of n, with T of one constant.

@art recursion-tree
To solve it, draw the recursion tree. The root costs c times n, and has two children of size n over two. Expand those, and keep going until the subproblems have size one.

@art level-sums
Now add across each level. The number of nodes doubles as their size halves, so every level costs c times n. For n a power of two, there are log n plus one levels.

@math items="T(n) = c·n·lg n + c·n@c n log n plus c n;;= Θ(n lg n)@theta of n log n"
So T of n is c n log n plus c n, which is theta of n log n.

@chapter Counting comparisons
@art merge-levels
The lab counts comparisons instead of time. A merge of m elements makes at most m minus one comparisons, because it stops when one half runs out.

@math heading="[6, 1, 8, 3, 7, 2, 5, 4]" items="level 3: 4 merges of 2  →  4@four merges of two;;level 2: 2 merges of 4  →  6@two merges of four;;level 1: 1 merge of 8  →  7@one merge of eight;;total 17, the worst case for n = 8@seventeen"
On six, one, eight, three, seven, two, five, four: four merges of two make four comparisons. Two merges of four make six. One merge of eight makes seven. That's seventeen, exactly the worst case for eight keys.

@words text="Merge sort: 12 to 17" sub="insertion sort: 7 to 28, at n = 8"
Insertion sort made twenty one. On a sorted or reversed array, merge sort falls to twelve. At eight keys, merge sort's count only moves between twelve and seventeen, where insertion sort's moved between seven and twenty eight.

@words text="12 keys: 31 comparisons" sub="4 levels · worst case 33"
And the algorithm never needed a power of two. Twelve keys take four levels, making eleven, nine, seven and four comparisons. That's thirty one, against a worst case of thirty three.

@words text="Insertion sort inside merge sort" sub="Problem 2-1"
So theta of n log n beats theta of n squared for large n, while insertion sort wins on small arrays. The book's problem two one combines them, sorting short runs by insertion sort inside merge sort.

@chapter Common slips
@list heading="Common slips" items="Crediting the split, not the cheap merge@The first|Counting lg n levels, not lg n + 1@The second|Thinking n must be a power of 2@the third"
The first slip is crediting the speed to the splitting. Combine in quadratic time and you're back to theta of n squared. The second is counting log n levels instead of log n plus one, forgetting the leaves. And the third is thinking n must be a power of two. Only the tidy analysis needed that.

@chapter Try it
@words text="[2, 4, 9, 7, 1, 3, 8, 6]" sub="runs and comparisons at each level"
Your turn. Run merge sort by hand on two, four, nine, seven, one, three, eight, six. Write the runs after each level, and the comparisons each merge makes. Total them, and compare with the worst case for eight keys.

@end text="Count merges level by level"
You can count merge sort's comparisons level by level on Learn. That's learn dot get er done dot I O.

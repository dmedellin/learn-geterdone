---
format: long
lesson: data-structures/choosing-a-structure
title: How to choose a data structure: the dashes decide
thumb: The mix decides, not the data
---

@chapter The question
@title text="Choosing a Structure" sub="Data Structures" art=thumb
You've got a million integers. Which data structure should hold them? That question can't be answered, because it asks about the data. What decides is what you'll do with them.

@words text="The operation mix decides"
The questions that matter are these. Which operations happen, and in what proportion. Does anything need the keys in order. And does the set change, or is it built once.

@art toolbox
This course has built eight structures and proved a bound for each. Choosing between them is mostly a matter of putting the useful five in one table.

@chapter One table
@art cost-grid
The instrument is a cost table. Operations as columns, structures as rows, and in each cell the bound this course already proved. Nothing in it is new. Every entry came from an earlier lesson.

@math heading="search · insert · delete · min" items="sorted array:  log n · n · n · 1@sorted array;;hash table:  1 · 1 · 1 · n  (expected)@hash table;;AVL tree:  log n · log n · log n · log n@AVL tree;;binary heap:  n · log n · log n · 1@binary heap"
A sorted array: search log n, insert and delete n, min one. A hash table: one, one, one, expected, and min costs n. An AVL tree: log n across the board. A binary heap: search n, insert and delete log n, and min one.

@list heading="Three entries to say out loud" items="Hash table's 1s are expected, Θ(n) worst@The hash table's|Heap: min is 1, search is n@The heap's|Union–find: dashes all the way@And union"
Three of those deserve saying out loud. The hash table's ones are expected, under an assumption about the keys, with a Theta of n worst case. The heap's min is one but its search is n, since siblings have no order. And union find's row is dashes all the way across. It isn't a container at all.

@chapter The refusals
@art dash-cells
Now the columns most people forget: predecessor, range, and walking the keys in order. The AVL tree and the sorted array do all three. The hash table and the heap get dashes. Not supported, at any speed.

@art scrambled
That's not slowness. Hashing deliberately destroys the order, and that's how it gets its constant. So a dash is the right entry. A big number in that cell would be a lie, because it suggests the table could do it at some price.

@words text="Hash index vs B-tree" sub="wins the point lookup 1 I/O to 3 · loses the mix by ≈ 170×"
System design meets the same mistake with a disk attached. Price a hash index and a B tree on nine hundred point lookups and a hundred small ranges a second. The hash index wins the lookup, one I O to three, and loses the mix by a factor of nearly a hundred and seventy.

@chapter One mix, executed
@math heading="n = 32:  12 search, 2 index, 2 delete, 2 min" items="sorted array:  108@a hundred and eight;;dynamic array:  478@four seventy eight;;doubly-linked list:  513@five thirteen;;stack, queue:  —@can't run"
The lab costs a mix by running it, on five sequence structures. A lookup heavy mix of thirty two elements: twelve searches, two indexes, two deletes, two mins. The sorted array costs a hundred and eight. The dynamic array four seventy eight. The linked list five thirteen. The stack and the queue can't run it at all.

@math heading="n = 32:  insert at one end, remove at the other, 8 + 8" items="doubly-linked list:  168@a hundred and sixty eight;;dynamic array:  440@four forty;;sorted array:  —@cannot be told"
Now insert at one end and remove at the other, eight of each. The linked list wins with a hundred and sixty eight. The dynamic array pays four forty, shifting on every front insert. And the sorted array cannot be told where to insert, so it can't run this mix at all.

@art two-rankings
The winner changed, and the refusals changed with it. The sorted array was four to five times cheaper on the first mix, and impossible on the second. That's what a real choice usually looks like, much more often than a factor of two on a shared operation.

@chapter Where people slip
@list heading="Common slips" items="Believing a hash table is always fastest@The first|Choosing from the data, not the mix@The second|Reading one ranking as general@And the third"
The first slip is believing a hash table is always the fastest map. The second is choosing from the data. The same million integers want a sorted array if they never change, an AVL tree if they do, a heap if you only want the smallest. And the third is reading one measured ranking as a general result.

@art bound-and-count
A hundred and eight against five thirteen is one mix at one size. Change the proportions, or n, and the order moves. So the honest report uses both. The table of bounds says what will happen, and the count shows it happening.

@chapter Try it
@words text="Write your own mix" sub="cost it on every structure · name what the winner can't answer"
Your turn. Write down a mix of operations from something you've built. Cost it on every structure in the table, rank them, and then name what the winner can't answer at all.

@end text="Cost a mix on everything"
You can run your own mix on every structure at once, on Learn. That's learn dot get er done dot I O.

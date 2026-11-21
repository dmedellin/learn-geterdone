---
format: long
lesson: intro-algorithms-data-structures/stacks-queues-and-linked-lists
title: Stacks, queues and linked lists: what each one costs
thumb: Cheap here, costly there
---

@chapter Dynamic sets
@title text="Stacks, Queues and Linked Lists" sub="Introduction to Algorithms, Chapter 10" art=thumb
Part three of the book is about data structures, and it opens with vocabulary. A dynamic set is one that grows, shrinks and gets queried while an algorithm runs.

@list heading="Seven operations" items="SEARCH, INSERT, DELETE@search, insert and delete|MINIMUM, MAXIMUM@minimum and maximum|SUCCESSOR, PREDECESSOR@successor and predecessor"
The authors list seven operations: search, insert and delete, minimum and maximum, successor and predecessor. Every structure in this course is judged by which of those it does quickly. And the cost belongs to the representation, not the set.

@chapter Stacks and queues
@art stack-column
A stack in an array needs one index, the top. Push increments it and stores. Pop decrements it and returns the element above. Both cost constant time. A stack removes the newest element, last in, first out.

@art circular-queue
A queue removes the oldest. It needs two indices, the head, the next to leave, and the tail, the slot the next arrival takes. Both move right and wrap around, so the array is used as a ring.

@math heading="Q[1..n]" items="empty:  head = tail@empty;;full:  tail one step behind head@full;;holds at most n − 1@n minus one"
Here's the catch. The queue is empty when head equals tail. So full has to look different: the tail one step behind the head. That's why one slot is always left unused, and a queue in n slots holds at most n minus one elements.

@chapter Linked lists
@art linked-list
A doubly linked list replaces index order with pointer order. Every element points to its successor and its predecessor, and the list's head points to the first.

@list heading="List costs" items="SEARCH: Θ(n) worst case@search|INSERT at the front: O(1)@insert|DELETE given a pointer: O(1)@delete"
Search walks from the head, theta of n in the worst case. Insert splices a new element in at the front in constant time. And delete splices one out in constant time, but only if you're handed a pointer to it. Delete by key means searching first.

@chapter The sentinel
@quote text="A sentinel is a dummy object that allows us to simplify boundary conditions." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 10.2"
Then the authors add a device. A sentinel is a dummy object that allows us to simplify boundary conditions.

@art sentinel-ring
Every pointer that would point to nothing points to the sentinel instead. The list becomes a ring, with the sentinel between tail and head. An empty list is the sentinel pointing to itself. Insert and delete lose their tests for the ends.

@words text="Clearer code, same bound" sub="one extra object per list"
What does it buy? It rarely changes an asymptotic bound. Mostly it makes code clearer. And it costs one extra object per list, which adds up across many short lists.

@chapter Without pointers, and trees
@art free-list
In a language without pointers, use arrays. Three arrays, next, key and prev, hold one field each, and an object is just an index. Unused objects sit on a free list, worked as a stack, so allocating and freeing are constant time.

@art child-sibling
And for trees whose nodes can have any number of children, each node keeps just two pointers: its leftmost child, and its next sibling to the right. That stores any rooted tree in linear space.

@chapter Pricing a sequence
@math heading="Array vs list" items="four-operations: 122 vs 92@a hundred and twenty two;;front insertions: 370 vs 78@three seventy;;random access: 16 vs 250@random access"
The lab prices one sequence of operations on an array and on a linked list. A mixed sequence costs a hundred and twenty two on the array and ninety two on the list. Front insertions cost three seventy against seventy eight, and random access flips it, sixteen against two fifty.

@words text="Both must walk: 212 vs 216" sub="the representation hardly matters"
Mix in searches and deletes, so that both must walk, and it's two twelve against two sixteen. The representation hardly matters. A count is a fact about one sequence, while the chapter's bounds hold for every list.

@chapter Common slips
@list heading="Common slips" items="List insert is O(1), without saying where@The first|Filling every slot of a circular queue@The second|Expecting a sentinel to improve the bound@the third"
The first slip is saying a list inserts in constant time without saying where. The splice is cheap. Reaching the place is what costs. The second is filling every slot of a circular queue. And the third is expecting a sentinel to improve the bound.

@chapter Try it
@words text="front-insertions · 8 elements · halfway" sub="price each operation by hand"
Your turn. In the lab, choose front insertions, starting size eight, one round, position halfway. Price each operation on both representations by hand first. Then move the position to the back, and say which total changes and why.

@end text="Price a sequence yourself"
You can price one operation sequence on an array and a linked list, on Learn. That's learn dot get er done dot I O.

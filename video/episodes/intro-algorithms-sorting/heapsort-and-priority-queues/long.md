---
format: long
lesson: intro-algorithms-sorting/heapsort-and-priority-queues
title: Heapsort and priority queues, from one heap
thumb: Take the root, n − 1 times
---

@chapter Two careers for one heap
@title text="Heapsort and Priority Queues" sub="Introduction to Algorithms, Sections 6.4 and 6.5" art=thumb
A max heap keeps its largest key at the root. Use that once, and you get a sort. Use it again and again, and you get a queue that always serves the biggest key first.

@chapter Heapsort
@art root-to-end
Heapsort is short, because building the heap did most of the work. The largest key is at A one, and it belongs at A n. So swap them, and shrink the heap by one, which takes the placed key out of the heap.

@art shrinking-heap
The new root may break the property. But both of its subtrees are still heaps, which is exactly what max heapify needs. One call restores the heap on the first n minus one elements. Repeat, and the sorted part grows from the right as the heap shrinks from the left, in the same array.

@math heading="Heapsort's cost" items="BUILD-MAX-HEAP: O(n)@build;;n − 1 calls of MAX-HEAPIFY: O(lg n) each@n minus one;;total O(n lg n), constant extra space@n log n"
The build is O of n. Then n minus one calls of max heapify cost O of log n apiece. So heapsort runs in O of n log n, with only constant storage outside the array. That's merge sort's bound, with insertion sort's frugality.

@chapter What it doesn't promise
@art unstable
What heapsort doesn't promise matters just as much. Its long jump, from root to end, carries a key past others equal to it. So equal keys can leave in a different order from the one they came in. Heapsort is not stable.

@words text="Sorted input: 85 comparisons" sub="a shuffle of the same 16 keys: 80"
And it doesn't get cheaper on input that's already sorted. The build rearranges an increasing array almost completely. In the lab, sixteen keys already in order cost eighty five comparisons, more than a shuffle's eighty.

@chapter Counting comparisons
@math heading="16 shuffled keys" items="heapsort: 80 = 22 build + 58 extract@eighty comparisons;;merge sort: 48@forty eight;;ratio 5/3, extra memory 0@five thirds"
On one fixed shuffle of sixteen keys, heapsort makes eighty comparisons, twenty two building the heap and fifty eight in the extractions. Merge sort makes forty eight, a ratio of five thirds. But heapsort uses no extra memory at all.

@words text="Lower bound: ⌈lg 16!⌉ = 45" sub="about the worst input, not every input"
Every comparison sort needs at least forty five comparisons in the worst case on sixteen keys, a bound chapter eight proves. Merge sort's thirty two on sorted input is below that, and it breaks nothing. The lower bound is about each sort's worst input.

@quote text="Heapsort is an excellent algorithm, but a good implementation of quicksort, presented in Chapter 7, usually beats it in practice." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 6.5"
The authors are candid. Heapsort is an excellent algorithm, but a good implementation of quicksort, presented in chapter seven, usually beats it in practice.

@chapter Priority queues
@art job-queue
So the heap gets a second career. A max priority queue keeps a set, and lets you insert an element, read the maximum, extract the maximum, and increase a key. A shared computer uses one to pick its highest priority job. A simulation uses the min version to process the earliest event next.

@art increase-key
Extracting the max moves the last element to the root and sifts it down. Increasing a key works the other way. A key that rises can only break the property with its parent, so swap it with its parent while the parent is smaller. That's a walk up a path of at most log n edges.

@art insert-slot
And insert is a neat trick. Add a slot at the end holding a key smaller than every key, then increase it to the new key. So it costs what increase key costs.

@math heading="On an n-element heap" items="HEAP-MAXIMUM: Θ(1)@maximum;;EXTRACT-MAX, INCREASE-KEY, INSERT: O(lg n)@the other three"
Reading the maximum is constant time. The other three are each O of log n.

@chapter Common slips
@list heading="Common slips" items="Expecting heapsort to be stable@The first|Expecting sorted input to be cheap@The second|Thinking a priority queue is sorted@the third"
The first slip is expecting heapsort to keep equal keys in order, like merge sort. The second is expecting sorted input to be cheap. And the third is thinking a priority queue keeps its elements sorted. It only keeps the heap property, which is enough.

@chapter Try it
@words text="[15, 12, 14, 11, 9, 1, 3, 8, 6, 2]" sub="EXTRACT-MAX, then INSERT 13"
Your turn. Start from fifteen, twelve, fourteen, eleven, nine, one, three, eight, six, two. Extract the max, then insert thirteen. Write the array after each, and count the swaps.

@end text="Race heapsort and merge sort"
You can count heapsort's comparisons beside merge sort's on the same array, on Learn. That's learn dot get er done dot I O.

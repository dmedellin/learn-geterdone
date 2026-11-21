---
format: long
lesson: intro-algorithms-sorting/heaps
title: Heaps, and why building one takes linear time
thumb: Build a heap in O(n)
---

@chapter A new technique
@title text="Heaps and Building a Heap" sub="Introduction to Algorithms, Sections 6.1 to 6.3" art=thumb
Heapsort runs in n log n time like merge sort, and sorts in place like insertion sort. It also brings a new design idea: let a data structure manage the information your algorithm needs. That structure is the heap.

@chapter A tree in an array
@art array-as-tree
A binary heap is an array, read as a nearly complete binary tree. Every level is full except perhaps the lowest, which fills from the left. The root is A one, and no pointers are stored at all.

@math heading="Node i" items="parent(i) = ⌊i/2⌋@its parent;;left(i) = 2i@left child;;right(i) = 2i + 1@right child"
Node i finds its parent at the floor of i over two, its left child at two i, and its right child at two i plus one. Each is just a shift.

@art heap-tree
In a max heap, every node other than the root is no larger than its parent. So the largest value sits at the root. Notice what that doesn't say. Siblings can be in either order, and nodes on different branches aren't compared at all. A heap is rarely sorted.

@chapter Max-heapify
@art sift-down
Everything is built on one procedure, max heapify. It's called on a node whose two subtrees are already heaps, but whose own value may be too small. It finds the largest of the node and its children. If that's a child, it swaps them, and carries on from the child's position. The value sinks until it's big enough, or reaches a leaf.

@math items="T(n) ≤ T(2n/3) + Θ(1)@T of two n over three;;= O(lg n),  or O(h) at height h@O of log n"
Each level costs a constant, and a child's subtree holds at most two thirds of the nodes. So T of n is at most T of two n over three plus a constant, which is O of log n, or O of h for a node of height h.

@chapter Building a heap
@art build-order
To build a heap from any array, notice the leaves are already one element heaps. They're the second half of the array. So call max heapify on the internal nodes only, from the floor of n over two back down to one.

@words text="Every node above i is a heap root" sub="the loop invariant"
That order is the correctness argument. Before each call, every node numbered above i is the root of a heap. Node i's children are numbered above i, so they're heap roots, and max heapify's precondition holds.

@chapter Why it's linear
@quote text="This upper bound, though correct, is not asymptotically tight." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 6.3"
The obvious price is about n over two calls, each costing up to log n, so O of n log n. The authors say: this upper bound, though correct, is not asymptotically tight.

@art height-layers
The trick is that a call costs the height of its own node, and most nodes are low. Half the nodes are leaves and cost nothing, a quarter are at height one, an eighth at height two, and only the root is at the top. The count halves at each level while the cost grows by one, and a halving beats an increment.

@math heading="n = 20" items="h = 0: 10 nodes → 0@ten nodes;;h = 1: 5 → 5,  h = 2: 3 → 6@five at height one;;h = 3: 2 → 6,  h = 4: 1 → 4@two at height three;;sum 21  vs  n·⌊lg n⌋ = 80@twenty one"
At twenty keys, there are at most ten nodes at height zero, five at height one costing five, three at height two costing six, two at height three costing six, and one at height four costing four. That's twenty one, against eighty for the loose bound.

@math items="Σ h/2ʰ = 2@converges to two;;BUILD-MAX-HEAP = O(n)@O of n"
In general, the sum becomes n times the sum of h over two to the h, and that series converges to two. So building a heap is O of n.

@chapter In the lab
@art loose-vs-tight
The lab builds min heaps, the mirror image, with every count the same. With thirty one keys in decreasing order, the build makes twenty six swaps, exactly the sum. Inserting the keys one at a time instead makes ninety eight.

@chapter Common slips
@list heading="Common slips" items="Pricing the build at n lg n@The first|Reading the heap property as sorted order@The second|Heapifying a node whose subtrees aren't heaps@the third"
The first slip is pricing the build at n log n, which is correct but not tight. The second is reading the heap property as sorted order. And the third is calling max heapify on a node whose subtrees aren't heaps yet. It only fixes one path.

@chapter Try it
@words text="[3, 8, 10, 1, 12, 6, 4, 7]" sub="array after each MAX-HEAPIFY"
Your turn. Build a max heap by hand from three, eight, ten, one, twelve, six, four, seven. Write the array after each call, count the swaps, and compare with the sum over heights at eight keys.

@end text="Count the build yourself"
You can count a heap build's swaps beside the exact sum, on Learn. That's learn dot get er done dot I O.

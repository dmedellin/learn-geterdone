---
format: long
lesson: data-structures/building-a-heap-in-linear-time
title: Why building a heap is linear, not n log n
thumb: Half the nodes do nothing
---

@chapter The question
@title text="Building a Heap in Linear Time" sub="Data Structures" art=thumb
You have n keys and you want a heap. Insert them one at a time, and each insert can cost log n, so you'd guess n log n. But there's a way that costs less than two n. The trick is noticing where the height actually is.

@chapter Bottom up
@art leaves-are-heaps
Start from a plain array, in any order. Every position past the floor of n over two is a leaf. And a leaf on its own is already a heap, with nothing to fix.

@math heading="Floyd's build-heap" items="for i = ⌊n/2⌋ down to 1@from the floor of n over two;;    sift-down(i)@sift down"
So go backwards. For i from the floor of n over two, down to one, sift down at position i. That's the whole algorithm, and the loop only touches internal nodes.

@art subtrees-ready
The order is what makes it correct. When the pass reaches node i, everything below it has already been processed. Both of its subtrees are heaps, so one sift down puts i where it belongs.

@chapter Counting the cost
@art height-layers
A node at height h sifts at most h levels. But how many nodes are that high? About half the nodes are leaves, at height zero. About a quarter are at height one, an eighth at height two. The count halves as the cost goes up.

@math heading="The bound" items="Σ ⌈n/2ʰ⁺¹⌉ · h@the sum over h;;≤ n · Σ h/2ʰ⁺¹@at most n times;;Σ h/2ʰ = 2  ⟹  under 2n@converges to two"
So the total is the sum over h of the ceiling of n over two to the h plus one, times h. Drop the ceilings and it's at most n times the sum of h over two to the h plus one. And the sum of h over two to the h converges to two. So the whole thing is under two n.

@words text="Θ(n)" sub="no logarithm anywhere"
Linear in the number of keys, with no logarithm in it at all. That sum is the one piece of analysis being imported. Differentiate the geometric series, or notice that S equals S over two plus one.

@chapter The sum at n = 31
@math heading="n = 31: nodes × height" items="h = 0:  16 × 0 = 0@sixteen leaves;;h = 1:  8 × 1 = 8@height one;;h = 2:  4 × 2 = 8@height two;;h = 3:  2 × 3 = 6@height three;;h = 4:  1 × 4 = 4@the root;;total 26  ·  2n = 62@twenty six"
Here it is for thirty one keys. Sixteen leaves, contributing nothing. Eight nodes at height one give eight. Four at height two give eight. Two at height three give six. And the root, alone, gives four. Total, twenty six, against two n of sixty two.

@words text="31 × 4 = 124" sub="charging every node the root's height"
Now compare n log n. Thirty one times four is a hundred and twenty four, nearly five times as much. The whole error is charging every node the root's height, when only one node has it.

@chapter Both methods, measured
@math heading="n = 31, keys arriving 31, 30, … 1" items="Floyd's build:  26 swaps,  52 comparisons@Floyd's build;;n inserts:  98 swaps,  98 comparisons@one at a time"
Now feed both methods the keys thirty one down to one. That's the worst case for insertion, since every new key sifts all the way to the root. Floyd's build swaps twenty six times, exactly the sum. Inserting one at a time swaps ninety eight times.

@art swap-bars
Twenty six against ninety eight is a factor of three point eight, on exactly the same keys. And the saving isn't a trick of implementation. Sifting up from the top down would just be insertion in disguise. It's a different order of operations.

@art insert-vs-build
Two things to be careful about. The sum bounds swaps, not comparisons. Floyd makes fifty two comparisons, because each level compares the two children first. And on a shuffled input, Floyd swaps twenty one, below the sum, because not every node sifts its full height.

@chapter Where people slip
@list heading="Common slips" items="Charging every node the tree's height@The first|Reading the sum as a comparison count@The second|Judging from one input@And the third"
The first slip is charging every node the height of the tree. Write the distribution down before you multiply. The second is quoting the sum as a comparison count, which is off by about two. And the third is judging from one input.

@art same-heap
On keys already in increasing order, both methods swap zero times and make the same thirty comparisons, and build the same heap. That measurement is real, and it says nothing. The difference between linear and n log n is about all inputs.

@chapter Try it
@words text="Evaluate Σ ⌈n/2ʰ⁺¹⌉·h for your own n"
Your turn. Pick a size, list how many nodes sit at each height, multiply by the height, and add. Check it's under two n. Then say in one sentence why n inserts cost more.

@end text="Race the two builds"
You can run both builds on the same keys and watch the swaps, on Learn. That's learn dot get er done dot I O.

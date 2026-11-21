---
format: short
lesson: greedy-and-matroids/why-huffman-is-optimal
title: The one swap behind Huffman's proof
---

@art downhill-swap
Why can't any prefix code beat Huffman? It starts with one swap.

@words text="heavier symbol deeper than a lighter one?"
Suppose a heavier symbol sits deeper in the tree than a lighter one.

@math items="change = (w_heavy − w_light)(d_shallow − d_deep) ≤ 0@the cost changes by"
Swap them. The cost changes by the weight difference, which is positive, times the depth difference, which is negative. So the swap can never make the code longer.

@end text="Full lesson on Learn"
The two lemmas and the full proof are on Learn.

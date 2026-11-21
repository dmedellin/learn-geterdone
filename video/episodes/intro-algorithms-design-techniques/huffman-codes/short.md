---
format: short
lesson: intro-algorithms-design-techniques/huffman-codes
title: A Huffman code's cost is just the sum of its merges
---

@art merge-step
Here's a neat shortcut. A Huffman code's total cost is just its merges added up.

@math items="merges: 9, 15, 24, 36, 60@nine, fifteen;;9 + 15 + 24 + 36 + 60 = 144 bits@a hundred and forty four"
Six letters, merged two at a time, make nodes of nine, fifteen, twenty four, thirty six and sixty. Add them, and you get a hundred and forty four bits.

@art code-tree
Each merge pushes every leaf below it one level deeper, adding one bit per character.

@end text="Full lesson on Learn"
Build a code yourself in the full lesson on Learn.

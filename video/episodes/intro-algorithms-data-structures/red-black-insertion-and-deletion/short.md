---
format: short
lesson: intro-algorithms-data-structures/red-black-insertion-and-deletion
title: A red-black insert never rotates more than twice
---

@art red-uncle
However big a red black tree gets, an insert rotates at most twice.

@art black-uncle-rotate
If the new node's uncle is red, you just recolour and move up. That can climb the tree, but it never rotates. If the uncle is black, one or two rotations finish the job, and the loop stops.

@words text="Recolouring climbs; rotations stop"
So recolouring may take O of log n steps, but rotations are capped at two.

@end text="Full lesson on Learn"
Count every case in the full lesson on Learn.

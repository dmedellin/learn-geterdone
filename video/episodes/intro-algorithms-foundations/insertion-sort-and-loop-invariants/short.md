---
format: short
lesson: intro-algorithms-foundations/insertion-sort-and-loop-invariants
title: The three-part proof behind every loop
---

@art invariant-three-parts
Your tests passed. That still doesn't prove your loop is correct.

@list items="Initialisation@true before the first|Maintenance@each iteration keeps it|Termination@when the loop stops"
A loop invariant does. Show it's true before the first iteration, that each iteration keeps it true, and that when the loop stops, it gives you the answer.

@art sorted-prefix
For insertion sort, the invariant is that the prefix holds its original elements, now sorted. At the end, the prefix is the whole array.

@end text="Full lesson on Learn"
Check the invariant pass by pass in the full lesson on Learn.

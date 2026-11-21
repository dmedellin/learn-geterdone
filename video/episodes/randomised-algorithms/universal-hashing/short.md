---
format: short
lesson: randomised-algorithms/universal-hashing
title: How to stop someone wrecking your hash table
---

@art one-slot-pile
See someone's hash function, and you can pile every key into one slot.

@art random-function
So don't fix the function. Draw it at random from a universal family, where any two keys collide with probability at most one over m.

@words text="k mod 4: 1 and 5 collide, P = 1" sub="family, p = 11: 2/11"
With k mod four, the keys one and five always collide. Against a random function from the family at p equals eleven, a pair collides two elevenths of the time.

@end text="Full lesson on Learn"
The full lesson is on Learn.

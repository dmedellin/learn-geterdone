---
format: short
lesson: intro-algorithms-design-techniques/rod-cutting
title: A million calls, or 211
---

@art recursion-explosion
A twenty inch rod: over a million recursive calls, or two hundred and eleven.

@words text="2ⁿ calls · only n + 1 subproblems"
The plain recursion makes two to the n calls, because every length asks about every shorter length again and again. But there are only twenty one distinct lengths.

@art table-fill
So solve each length once and store it. That's dynamic programming, and the cost drops to n squared.

@end text="Full lesson on Learn"
Count the calls yourself in the full lesson on Learn.

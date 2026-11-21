---
format: short
lesson: strings-and-pattern-matching/the-text-where-nothing-is-skipped
title: When the skipping algorithm loses five to one
---

@art right-match-then-fail
The famous skipping algorithm can lose to naive search, five to one.

@words text="30 a's · pattern baaaa"
Search thirty a's for b a a a a. Horspool compares from the right, matches four a's, then fails on the b. Every time. And it can only shift by one.

@words text="Horspool 130 · naive 26"
That's a hundred and thirty comparisons. Naive checks the b first, and makes twenty six. Flip the pattern, and they swap.

@end text="Full lesson on Learn"
Try it on Learn.

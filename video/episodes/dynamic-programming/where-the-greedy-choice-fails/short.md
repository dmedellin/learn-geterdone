---
format: short
lesson: dynamic-programming/where-the-greedy-choice-fails
title: Largest coin first gives the wrong change
---

@art greedy-commit
Taking the biggest coin first can give you the wrong change.

@math items="coins 1, 3, 4  ·  amount 6@one, three and four;;4 + 1 + 1  →  3 coins@four plus one plus one;;3 + 3  →  2 coins@three plus three"
Use coins one, three and four, and make six. Largest first gives four plus one plus one, three coins. But three plus three is just two.

@words text="Try every first coin, keep the best"
The fix isn't a better rule. It's a recurrence that tries every first coin and keeps the best.

@end text="Full lesson on Learn"
Try your own coins on Learn.

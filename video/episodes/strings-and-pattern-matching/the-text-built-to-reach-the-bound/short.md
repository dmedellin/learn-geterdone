---
format: short
lesson: strings-and-pattern-matching/the-text-built-to-reach-the-bound
title: A steep line is not a quadratic
---

@art steep-line
Your string search got much slower. That still doesn't make it quadratic.

@words text="100, 220, 340, 460, 580, 700"
Search twenty four a's for a a a a b, then repeat the text. The counts climb by a hundred and twenty each time. That's a straight line.

@words text="per character: m/2" sub="only when m grows with n"
With the pattern fixed, the bound is linear too. You only get a quadratic when the pattern grows with the text.

@end text="Full lesson on Learn"
See both tables on Learn.

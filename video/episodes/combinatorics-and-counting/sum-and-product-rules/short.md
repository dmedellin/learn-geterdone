---
format: short
lesson: combinatorics-and-counting/sum-and-product-rules
title: When "or" does not mean add
---

@art overlapping-circles
Or usually means add. Here's a question where adding gives the wrong answer.

@math items="starts with a vowel: 3380@start with a vowel;;ends in z: 676@end in z;;✗  3380 + 676 = 4056@four thousand and fifty six"
Three letter strings that start with a vowel: three thousand three hundred and eighty. Strings that end in z: six hundred and seventy six. Add them, and you get four thousand and fifty six. Wrong.

@math items="both: 130@a hundred and thirty;;3380 + 676 − 130 = 3926@three thousand nine hundred and twenty six"
A hundred and thirty strings do both, so they were counted twice. Subtract them once: three thousand nine hundred and twenty six.

@words text="Add only when nothing is in both"
The sum rule needs disjoint sets. Check that before you add.

@end text="Full lesson on Learn"
The full lesson, with the product rule too, is on Learn.

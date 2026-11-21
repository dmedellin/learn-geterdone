---
format: short
lesson: strings-and-pattern-matching/borders-and-the-failure-function
title: The one idea behind KMP: borders
---

@art border-overlap
The whole trick of Knuth Morris Pratt is a prefix that's also a suffix.

@words text="ababa → border aba"
In a b a b a, the start a b a is also the end. That's a border.

@words text="slide so the border lines up"
So when a match fails after a b a b a, you don't start over. Slide the pattern so that border lines up, and three characters already match. The text pointer never moves back.

@end text="Full lesson on Learn"
Build the table on Learn.

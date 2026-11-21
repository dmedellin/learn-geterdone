---
format: short
lesson: intro-algorithms-strings-geometry-hardness/automata-and-knuth-morris-pratt
title: Why KMP never reads a text character twice
---

@art fallback
When a match fails, you already know the text's last few characters.

@art border
They're the pattern's. So Knuth Morris Pratt slides the pattern to its longest border: a prefix of what matched that's also a suffix of it.

@math items="abaabab: π = 0, 0, 1, 1, 2, 3, 2@a b a a b a b;;19 comparisons vs 35@nineteen"
For the pattern a b a a b a b, that's pi. On the lesson's text, KMP makes nineteen comparisons where the naive matcher makes thirty five.

@end text="Full lesson on Learn"
Build the table yourself in the full lesson on Learn.

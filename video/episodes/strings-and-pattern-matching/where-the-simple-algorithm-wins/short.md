---
format: short
lesson: strings-and-pattern-matching/where-the-simple-algorithm-wins
title: The text where naive search beats KMP
---

@art one-per-alignment
Here's a text where the naive matcher beats Knuth Morris Pratt every time.

@words text="search for zebra" sub="no z in the text"
Search for zebra in a text with no z. Every naive alignment fails on its first comparison. KMP still reads every character.

@math items="naive: n − m + 1@naive;;KMP: n@KMP;;gap: m − 1@gap"
Naive makes n minus m plus one comparisons. KMP makes n. The gap is m minus one, every time. KMP's guarantee is about the worst case, not this one.

@end text="Full lesson on Learn"
Race them on Learn.

---
format: short
lesson: strings-and-pattern-matching/the-matcher-as-a-machine
title: Search a text without comparing a single character
---

@art table-grid
You can find a pattern in a text without making a single comparison.

@words text="one state per characters matched"
Build a machine whose state is how much of the pattern is matched so far. Work out, in advance, where every state goes on every letter.

@words text="n characters → n lookups"
Then the search is one table lookup per character, whatever the text says. The cost moves into the table, which grows with the alphabet.

@end text="Full lesson on Learn"
Build one on Learn.

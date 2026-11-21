---
format: short
lesson: intro-algorithms-strings-geometry-hardness/naive-and-rabin-karp-matching
title: Same text, same pattern, eight false matches
---

@art collision
Change one number, and the hash finds eight matches that aren't there.

@math items="mod 17: 0 spurious hits@seventeen;;mod 13: 8 spurious hits@thirteen"
Search a banana and a bandana in a cabana for a n a. At modulus seventeen, Rabin Karp has no spurious hits. At thirteen, eight.

@words text="Equal hashes are a hint, not a match"
Equal hashes are a hint, not a match. That's why every hash match is checked, character by character.

@end text="Full lesson on Learn"
Sweep the modulus yourself in the full lesson on Learn.

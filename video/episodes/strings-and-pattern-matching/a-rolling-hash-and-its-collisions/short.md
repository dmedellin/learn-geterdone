---
format: short
lesson: strings-and-pattern-matching/a-rolling-hash-and-its-collisions
title: Two strings, nothing in common, same hash
---

@art collision-pair
Two strings with no letters in common, and exactly the same hash.

@words text="base 256 · modulus 41" sub="' th' → 36 · 'ain' → 36"
Read each as a number in base two hundred and fifty six, and take it mod forty one. Both leave thirty six.

@words text="7 candidates · 4 matches · 3 collisions"
So in the rain in spain, seven windows match the pattern's hash, but only four are real. Rabin Karp has to check the characters every time.

@end text="Full lesson on Learn"
Check them on Learn.

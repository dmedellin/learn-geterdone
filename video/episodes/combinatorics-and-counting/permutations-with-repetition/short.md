---
format: short
lesson: combinatorics-and-counting/permutations-with-repetition
title: How many ways to spell MISSISSIPPI?
---

@art letter-tiles
MISSISSIPPI has eleven letters, but far fewer than eleven factorial arrangements. Why?

@art swap-identical
Swap two of the S's, and the word doesn't change. So eleven factorial counts every real arrangement many times over.

@math items="11! / (1! · 4! · 4! · 2!)@divide;;= 34 650@thirty four thousand six hundred and fifty"
For each letter, divide by the factorial of how often it repeats: one M, four I's, four S's and two P's. That leaves thirty four thousand six hundred and fifty.

@end text="Full lesson on Learn"
The full lesson, with the BANANA gap trick, is on Learn.

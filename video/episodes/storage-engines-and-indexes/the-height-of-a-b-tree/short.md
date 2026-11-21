---
format: short
lesson: storage-engines-and-indexes/the-height-of-a-b-tree
title: A billion keys is only four levels deep
---

@art wide-tree
A billion keys in a B-tree. How many levels deep? Four.

@math items="500 → 250 000 → 125 000 000 → 62 500 000 000@five hundred"
With five hundred entries a page, every level multiplies by five hundred. Five hundred, two hundred and fifty thousand, a hundred and twenty five million, sixty two and a half billion. Four levels.

@art cached-top
And the top two levels are only about two megabytes, so they stay in memory. A lookup costs two disk reads.

@end text="Full lesson on Learn"
The full lesson, with the fanout on a slider, is on Learn.

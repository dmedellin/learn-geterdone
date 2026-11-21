---
format: short
lesson: storage-engines-and-indexes/the-rum-trade-off
title: There is no best storage engine
---

@art rum-triangle
Which storage engine is best? None. Every one pays somewhere.

@math items="tiered:  update 5,  read 50,  memory 10@writes each byte;;levelled:  update 25,  read 5@levelled tree"
A tiered tree writes each byte only five times, but probes fifty runs on a lookup and keeps ten copies. A levelled tree gets reads down to five, by writing twenty five times.

@words text="Choose two. Pay in the third."
Merging less means keeping more, and keeping more means searching more.

@end text="Full lesson on Learn"
The full lesson, with the B-tree corner too, is on Learn.

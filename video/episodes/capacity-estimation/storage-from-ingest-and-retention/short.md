---
format: short
lesson: capacity-estimation/storage-from-ingest-and-retention
title: Half a terabyte a day for 90 days is not 45 terabytes
---

@art growing-staircase
Half a terabyte a day, kept ninety days. Forty five terabytes? Not even close.

@math items="15.00 + 15.75 + 16.54 = 47.29 TB@growing five percent;;× 3 copies = 141.86 TB@three copies"
With the ingest growing five percent a month, the three monthly blocks add up to forty seven point two nine terabytes. Keep three copies and it's a hundred and forty one point eight six.

@words text="Storage is a sum, then × copies"
Storage is a sum over the window. Then the copies multiply it.

@end text="Full lesson on Learn"
The full lesson, with the growth on a slider, is on Learn.

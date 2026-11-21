---
format: short
lesson: storage-engines-and-indexes/row-vs-column-storage
title: Columnar is faster, until you want the whole row
---

@art column-layout
A three column scan over a billion rows. Row store, a hundred seconds. Column store, six.

@math items="row: 100.00 GB@a hundred gigabytes;;column: 6.00 GB@six"
The row store reads whole rows, a hundred gigabytes. The column store reads only the three named columns, and compresses them better, six gigabytes.

@art whole-row-fetch
But fetch one whole row by key, and it flips. One page read in the row store. Twenty in the column store.

@end text="Full lesson on Learn"
The full lesson, with the crossover worked out, is on Learn.

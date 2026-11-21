---
format: short
lesson: enterprise-patterns-distribution/data-transfer-object
title: Sending too much data can be faster
---

@art getter-per-field
Sending four thousand bytes nobody reads can make your screen almost four times faster.

@math items="5 getters: ≈ 102.07 ms@five getter calls;;one transfer object: ≈ 26.07 ms@one object"
Five getter calls at twenty milliseconds each take about a hundred and two milliseconds. One object carrying every field, wasted notes and all, takes about twenty six.

@words text="A round trip costs more than the bytes"
The four saved round trips could have carried eighty thousand bytes. That's why Fowler would rather send too much.

@end text="Full lesson on Learn"
The full lesson, with a lab that weighs it, is on Learn.

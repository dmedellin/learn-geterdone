---
format: short
lesson: scaling-laws-and-cost/move-the-data-or-the-compute
title: A faster network won't fix this
---

@art same-pipe
Moving two terabytes to your job takes four hours. Moving the job to the data takes forty milliseconds.

@math items="(code + result)/bw < D/bw@code plus result;;code + result < D@bandwidth cancels out"
Both plans cross the same link, so the bandwidth cancels out. The decision is just code plus result against the dataset. Bytes against bytes.

@words text="A faster link makes the winner faster. It never changes the winner."
Ship the code, not the table, and only the small result comes back.

@end text="Full lesson on Learn"
The full lesson, with the tie worked out, is on Learn.

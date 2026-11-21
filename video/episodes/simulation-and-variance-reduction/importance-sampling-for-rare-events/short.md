---
format: short
lesson: simulation-and-variance-reduction/importance-sampling-for-rare-events
title: The rare event estimate that's stable, unbiased, and zero
---

@art huge-weight
This estimator is unbiased, perfectly stable, and returns zero.

@words text="P(10 heads) = 1/1024"
Sample ten coins weighted toward tails, one fifth heads, and reweight each draw. Ten heads becomes one in ten million, with a weight of about nine thousand five hundred.

@math items="2000 draws:  0 hits → 0@two thousand;;variance × ≈ 9546@multiplied"
Two thousand draws, no hits, estimate zero. The variance was multiplied by about nine and a half thousand. Only that number shows anything went wrong.

@end text="Full lesson on Learn"
The full lesson, with a good proposal too, is on Learn.

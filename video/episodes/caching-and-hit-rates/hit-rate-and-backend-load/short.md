---
format: short
lesson: caching-and-hit-rates/hit-rate-and-backend-load
title: Ninety to ninety-nine percent is not a nine point gain
---

@art shrinking-misses
Your hit rate went from ninety to ninety nine percent. Your database just got ten times quieter.

@math items="90%:  (1/10)(10 000) = 1 000 rps@ninety percent;;99%:  (1/100)(10 000) = 100 rps@ninety nine"
At ten thousand requests a second, ninety percent sends a thousand to the backend. Ninety nine percent sends a hundred.

@words text="The backend sees 1 − h" sub="compare miss rates as a ratio"
The backend only sees the misses, so compare the miss rates, and compare them as a ratio.

@end text="Full lesson on Learn"
The full lesson, with a hit rate slider, is on Learn.

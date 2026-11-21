---
format: short
lesson: caching-and-hit-rates/cache-size-and-hit-rate
title: Ninety percent costs five keys. Ninety-nine costs twenty-eight.
---

@art stretched-gap
One more nine of hit rate can cost you five times the memory.

@math items="90%  →  C = 5@ninety percent;;99%  →  C = 28@ninety nine"
With fifty keys and a Zipf exponent of two, ninety percent needs the top five keys. Ninety nine percent needs the top twenty eight.

@words text="28/5 = 5.6× the cache" sub="for a tenfold cut in backend load"
That's five point six times the cache, for a tenfold cut in backend load. Choose the target first, then read the size off the curve.

@end text="Full lesson on Learn"
The full lesson, with the curve to drag, is on Learn.

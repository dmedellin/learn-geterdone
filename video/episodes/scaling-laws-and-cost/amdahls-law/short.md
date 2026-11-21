---
format: short
lesson: scaling-laws-and-cost/amdahls-law
title: Why five percent serial work caps you at 20x
---

@art ceiling-curve
Five percent of your job can't run in parallel. So no number of machines gets you past twenty times faster.

@math items="S(n) = 1 / ((1 − p) + p/n)@one over;;S(∞) = 1/(1 − p) = 1/(1/20) = 20×@One over one twentieth"
Machines shrink the parallel part and leave the serial part alone. So the speedup climbs toward one over the serial fraction. One over one twentieth is twenty.

@words text="32 machines: 12.549×"
Thirty two machines get you twelve and a half.

@end text="Full lesson on Learn"
The full lesson, with the efficiency too, is on Learn.

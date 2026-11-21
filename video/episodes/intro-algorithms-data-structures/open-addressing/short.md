---
format: short
lesson: intro-algorithms-data-structures/open-addressing
title: Why a nearly full hash table crawls
---

@art bound-curve
A hash table seven eighths full needs about eight probes per miss.

@math items="1 + α + α² + … = 1/(1 − α)@adds up to"
With open addressing, you always probe once, again about alpha of the time, again about alpha squared. That adds up to one over one minus alpha.

@words text="α = 7/8 → 8 probes"
At seven eighths, that's eight. And as the table fills, it grows without limit. So keep alpha well away from one.

@end text="Full lesson on Learn"
Count the probes yourself in the full lesson on Learn.

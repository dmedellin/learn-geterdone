---
format: short
lesson: capacity-estimation/read-write-ratio
title: 100 to 1 reads to writes is not 1% writes
---

@art split-bar
A hundred reads for every write. So one percent of the traffic is writes, right?

@math items="W = T/(r + 1)@r plus one;;10 000/101 = 99.01 writes/s@ninety nine point zero one"
Not quite. The total includes the writes, so you divide by r plus one. At ten thousand requests a second, that's ninety nine point zero one writes, not a hundred.

@words text="100 and 9 900 make 99:1"
Check it: a hundred writes against nine thousand nine hundred reads is ninety nine to one.

@end text="Full lesson on Learn"
The full lesson, with the ratio on a slider, is on Learn.

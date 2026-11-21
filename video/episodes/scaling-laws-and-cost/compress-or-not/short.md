---
format: short
lesson: scaling-laws-and-cost/compress-or-not
title: Compressing made our transfer five times slower
---

@art fast-link
Ten gigabytes. On a gigabit link, compressing saves time. On ten gigabits, it costs five times as much.

@math items="bw* = rate · (k − 1)/k = 187.5 MB/s@one eighty seven point five"
Set the two times equal, and the file size cancels out. Above a link speed of rate times k minus one over k, sending raw is faster. For this compressor, that's one eighty seven point five megabytes a second.

@words text="Decide per link, not per file"
The file never mattered.

@end text="Full lesson on Learn"
The full lesson, with the break-even worked out, is on Learn.

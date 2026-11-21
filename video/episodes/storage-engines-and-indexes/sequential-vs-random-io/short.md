---
format: short
lesson: storage-engines-and-indexes/sequential-vs-random-io
title: Ten seconds or forty two minutes, same gigabyte
---

@art many-seeks
Same gigabyte, same disk. Ten seconds, or forty two minutes.

@math items="one sweep:  10 ms + 10 s = 10.01 s@one sweep;;4 kB chunks:  250 000 × 10 ms + 10 s ≈ 41.8 min@four kilobytes at a time"
One sweep costs one ten millisecond seek, plus ten seconds of bytes. Four kilobytes at a time costs two hundred and fifty thousand seeks, plus the same ten seconds.

@words text="The bytes never changed. The seeks did."
Every extra minute is the arm moving, a quarter of a million times, while nothing is transferred.

@end text="Full lesson on Learn"
The full lesson, with three devices to compare, is on Learn.

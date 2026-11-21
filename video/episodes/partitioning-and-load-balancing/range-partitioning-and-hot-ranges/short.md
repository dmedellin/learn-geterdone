---
format: short
lesson: partitioning-and-load-balancing/range-partitioning-and-hot-ranges
title: Your shard chart is flat, and one shard is at 100%
---

@art flat-histogram
Your writes per shard chart is perfectly flat. One shard is taking every write.

@art write-pointer
Key by a timestamp, and the next write always goes to the range holding the top of the key space. Right now, one range of eight takes a hundred percent.

@words text="Over the run: 12.50% each" sub="right now: 100% on one"
Over the whole run, the hot range moves along, and every range ends at an equal twelve and a half percent. So look at the last few minutes.

@end text="Full lesson on Learn"
The full lesson, with three key designs side by side, is on Learn.

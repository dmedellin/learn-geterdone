---
format: short
lesson: partitioning-and-load-balancing/hot-keys-and-salting
title: Sixty four times the shards, thirty one percent better
---

@art hot-key-shard
One key takes twelve percent of your traffic. Will more shards help?

@math items="N = 16:  hottest 17 500 /s@seventeen thousand five hundred;;N = 1 024:  hottest 12 086 /s@twelve thousand and eighty six"
Barely. At sixteen shards the hottest takes seventeen thousand five hundred a second. At a thousand and twenty four, still twelve thousand and eighty six. One key always lands on one shard.

@art salt-split
Split the key into eight salted pieces instead, and the hottest shard drops to seven thousand.

@end text="Full lesson on Learn"
The full lesson, with the read cost of salting, is on Learn.

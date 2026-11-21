---
format: short
lesson: partitioning-and-load-balancing/rehashing-when-n-changes
title: Adding one shard moves 87.5% of your keys
---

@art mod-n-shuffle
Seven shards, add one. You'd guess about a seventh of the keys move. It's seven eighths.

@math items="mod N moves 7/8 = 87.50%@seven eighths;;ring moves 1/8 = 12.50%@one eighth;;7/8 + 1/8 = 1@add up to one"
Under mod N, seven eighths of the keys change shard. On a consistent hash ring, only one eighth move. And the two add up to one.

@words text="One moves all but a sliver. The other moves the sliver."
That's the whole case for consistent hashing.

@end text="Full lesson on Learn"
The full lesson, with the count done both ways, is on Learn.

---
format: short
lesson: data-structures/choosing-a-structure
title: Why a hash table can't find the next key down
---

@art dash-cells
Ask a hash table for the largest key below k. It isn't slow. It simply can't.

@words text="predecessor · range · in order:  —"
Hashing scrambles the order on purpose. That's how it gets constant lookups. So predecessor, range queries and walking the keys in order aren't supported, at any speed.

@words text="The dashes decide"
Those dashes decide more structure choices than the numbers do.

@end text="Full lesson on Learn"
The full lesson, with every structure costed at once, is on Learn.

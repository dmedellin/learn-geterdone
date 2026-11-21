---
format: short
lesson: data-structures/open-addressing-and-linear-probing
title: Delete one key, lose another
---

@art cut-chain
In a probing hash table, deleting one key can make a different key disappear.

@words text="search stops at the first empty slot"
A search stops at the first empty slot. So if you empty a slot in the middle of a key's probe sequence, the search stops early, and the key past it is never found.

@art tombstone
The fix is a tombstone. Mark the slot dead. Searches walk past it, inserts can reuse it.

@end text="Full lesson on Learn"
The full lesson, with the lost keys named, is on Learn.

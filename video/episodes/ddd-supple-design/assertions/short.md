---
format: short
lesson: ddd-supple-design/assertions
title: Bikes created out of nothing, and how to catch it
---

@art bikes-from-nothing
A bike transfer can create bikes out of nothing, and its name won't tell you.

@words text="removed = 3 and added = 3" sub="the post-condition"
Dock a sends three bikes to dock b. The post condition says three are removed and three are added.

@math items="transfer-one-sided: removed = 0@forgot;;first false clause: removed = 3@first false"
One implementation forgot to take them out of a. Removed is zero, and the first false clause is removed equals three.

@words text="Trust the guarantee"
State what a command guarantees, and checking it is easy.

@end text="Full lesson on Learn"
Check three states clause by clause in the full lesson on Learn.

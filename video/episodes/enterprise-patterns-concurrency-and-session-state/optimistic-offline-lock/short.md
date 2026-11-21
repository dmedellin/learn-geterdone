---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/optimistic-offline-lock
title: Your version check misses this conflict
---

@art read-dependency
Your version check passes. Your quote is still wrong. Here's why.

@words text="You checked what you wrote"
Kim builds a quote from a discount. Lee changes the discount and commits. Kim saves the quote. The quote's version never changed, so the check passes.

@math items="reads unchecked: both commit@both commit;;read checked: Kim conflicts@Kim conflicts"
With reads unchecked, both commit, on a discount that no longer exists. Check the discount's version too, and Kim conflicts, as she should.

@end text="Full lesson on Learn"
The full lesson, with a lab that replays it, is on Learn.

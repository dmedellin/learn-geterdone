---
format: short
lesson: algorithmic-and-automated-trading/signal-engine-and-strategy-state
title: Twelve true events should make one entry
---

@art twelve-vs-one
Your buy condition is true twelve times in a row. How many buys?

@math items="stateless: 12 entries@twelve entries;;stateful: 1@just one"
A stateless engine emits twelve entries, eleven of them duplicates. A stateful one emits just one: the transition into long.

@words text="Signal on the change, not the condition"
After that, the strategy is already long. A condition that stays true isn't a new event, so there's nothing new to signal.

@end text="Full lesson on Learn"
Toggle state in the full lesson on Learn.

---
format: short
lesson: gof-behavioral-objects/state
title: Fourteen branches, or seven classes?
---

@art switch-tangle
The same switch on a status field, in method after method. There's a pattern for that.

@art connection-states
Give each state a class. The object hands every request to its current state, and swaps it when the state changes.

@words text="14 branches · 7 classes"
A library copy with five states and nine transitions needs fourteen branches as one conditional, or seven classes as State.

@end text="Full lesson on Learn"
It's not smaller. But a new state is a new class. The full lesson is on Learn.

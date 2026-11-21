---
format: short
lesson: gof-structural/bridge
title: Why your class count multiplies
---

@art window-subclasses
Three kinds of guide, on three players. Why does that cost ten classes?

@math items="3 × 3 + 1 = 10@three times three;;(3 + 1) + (3 + 1) = 8@two hierarchies"
One subclass per pairing is three times three, plus one: ten. Split it into two hierarchies, guides and players, and it's eight.

@art two-hierarchies
Each guide holds a reference to its player. That reference is the bridge.

@words text="New player: +3 or +1"
Add a fourth player. Subclassing adds three classes. The bridge adds one.

@end text="Full lesson on Learn"
The full lesson, and when not to bother, is on Learn.

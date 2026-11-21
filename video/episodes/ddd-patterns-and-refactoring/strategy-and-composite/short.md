---
format: short
lesson: ddd-patterns-and-refactoring/strategy-and-composite
title: A Strategy doesn't remove the decision
---

@art choice-moved
Seven decisions become two. But the choice didn't disappear.

@math items="plan tests:  7 decision points@seven;;pricing policies:  2 decision points@two"
A bike share tests the rider's plan in every method, seven decision points. Give each plan its own pricing policy, and the count falls to two.

@words text="Chosen once, not everywhere"
Which plan applies is now decided once, where a ride is given its policy. And riders already talk about plans, so it's a domain pattern.

@end text="Full lesson on Learn"
Count the decisions yourself in the full lesson on Learn.

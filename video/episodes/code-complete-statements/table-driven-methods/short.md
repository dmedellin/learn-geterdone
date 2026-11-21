---
format: short
lesson: code-complete-statements/table-driven-methods
title: Same table, same key, two different fees
---

@art endpoint-rule
A book sixty days late pays twenty, or ten. Same table, same key.

@words text="under 60 days → 10 · under 365 → 20"
The library charges ten under sixty days, and twenty under three hundred and sixty five. So what about exactly sixty?

@math items="below 60?  no → 20@not below;;at or below 60?  yes → 10@at or below"
If the rule is below, sixty is not below sixty, so it pays twenty. If it's at or below, it pays ten. The table holds no logic. The endpoint rule does, so state it.

@end text="Full lesson on Learn"
The full lesson, with a stair step lab, is on Learn.

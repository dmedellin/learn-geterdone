---
format: short
lesson: linear-programming-models/multiperiod-planning-and-balance-constraints
title: The cheaper plan that misses fifty units
---

@art unmet-demand
This plan costs a hundred less, and leaves fifty units of demand unmet.

@math items="P₁ + P₂ + P₃ + P₄ ≥ 105@one row;;make 0, 0, 45, 60  →  675@six hundred and seventy five;;unmet: 15 + 35 = 50@fifty units"
Replace four balance rows with one row about total production. The plan makes nothing until period three, for six hundred and seventy five instead of seven seventy five. And fifty units of earlier demand go unserved.

@words text="One balance row per period"
Only a balance row per period says when a unit has to exist.

@end text="Full lesson on Learn"
The full lesson, with both plans side by side, is on Learn.

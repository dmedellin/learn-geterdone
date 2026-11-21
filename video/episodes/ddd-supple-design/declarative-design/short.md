---
format: short
lesson: ddd-supple-design/declarative-design
title: No counter-example is not a proof
---

@art sixth-lot
Five stored lots, no counter example. The rule still doesn't subsume the old one.

@math items="B: (moisture ≤ 6 and sealed) or temp ≤ −25@with an or;;lotF: sealed, moisture 4, 0 degrees@lot F"
Take a storage rule with an or in it. Every lot that passes it also passes the old rule. But add lot F, sealed, moisture four, at zero degrees. It passes the new rule and fails the old.

@words text="Checking candidates proves nothing on its own"
One separating candidate disproves subsumption. None among the ones you have proves nothing.

@end text="Full lesson on Learn"
Compare seed bank rules in the full lesson on Learn.

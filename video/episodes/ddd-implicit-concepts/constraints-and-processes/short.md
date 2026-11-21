---
format: short
lesson: ddd-implicit-concepts/constraints-and-processes
title: Factoring a rule removes zero decisions
---

@words text="4 decisions before · 4 after"
Moving a business rule into its own class removes exactly zero decisions.

@art moved-decisions
A theatre's sales limit had four decisions inline. Named SalesLimit, it still has four: three in the constraint, one in the caller.

@art constraint-object
What changed is that the rule is now a thing with a name, one the team can find, discuss, and grow.

@end text="Full lesson on Learn"
Count the decisions yourself in the full lesson on Learn.

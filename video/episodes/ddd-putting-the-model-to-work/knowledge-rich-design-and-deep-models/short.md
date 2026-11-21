---
format: short
lesson: ddd-putting-the-model-to-work/knowledge-rich-design-and-deep-models
title: Your business rule is hiding in an if
---

@art buried-guard
Your most important business rule might be hiding in one if statement.

@words text="No expert can read it."
A guard clause enforces the rule, but no business expert could check it, and a new developer can't trace it to the requirement.

@art policy-object
Evans lifts it into its own policy object, with a method for each clause, named the way the business names it.

@art named-refusal
Same answers. But now a refusal says which part of the rule refused.

@end text="Full lesson on Learn"
Check a clinic's bookings clause by clause in the full lesson on Learn.

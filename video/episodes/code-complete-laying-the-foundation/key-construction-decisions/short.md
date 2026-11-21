---
format: short
lesson: code-complete-laying-the-foundation/key-construction-decisions
title: Your language is missing a feature. Now what?
---

@art separated-layers
Your language lacks a feature you need. Does that mean you can't have it?

@words text="Program into the language, not in it"
No. Steve McConnell's advice is to program into your language, not in it. Decide what you want to express first, then work out how.

@code block=1 lines=3-7 label=Java focus="3@named constant|5-7@forwards"
Java has no default arguments. So write the default once, as a named constant, and give the shorter version one job. It forwards.

@end text="Full lesson on Learn"
The full lesson, with the whole convention, is on Learn.

---
format: short
lesson: code-complete-variables/declaring-and-initializing-variables
title: Every initialization bug comes down to one thing
---

@art read-before-set
Every initialisation bug comes down to one thing. Which one?

@words text="A value you didn't expect"
A variable holding an initial value you didn't expect. It was never assigned, or it's out of date, or only part of it was set.

@art proximity
So give each variable its value where you declare it, close to where it's first used. Steve McConnell calls that cheap insurance.

@end text="Full lesson on Learn"
The full lesson, with a lab that finds reads before sets, is on Learn.

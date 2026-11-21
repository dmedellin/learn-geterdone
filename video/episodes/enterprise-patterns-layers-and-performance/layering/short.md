---
format: short
lesson: enterprise-patterns-layers-and-performance/layering
title: The test that finds business logic in your UI
---

@art two-presentations
Is there business logic hiding in your web page? Add a command line.

@code block=1 lines=1-15 label=Java focus="3-5@three lines|11-13@copied"
Fowler's test: imagine a second, radically different presentation. Here, a page and a command line both decide whether sales rose more than ten percent. Those three lines get copied.

@words text="What you'd copy is domain logic"
Whatever you'd have to duplicate belongs in the domain, where both can ask it.

@end text="Full lesson on Learn"
The full lesson, with a lab that finds the copies, is on Learn.

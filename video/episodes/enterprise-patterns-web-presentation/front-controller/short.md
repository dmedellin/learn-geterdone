---
format: short
lesson: enterprise-patterns-web-presentation/front-controller
title: You don't need a Front Controller to remove duplication
---

@art many-pages-repeat
Two pages repeat six lines. Do you need a Front Controller to fix it?

@math items="two page controllers: 1 block, 6 lines@six lines;;superclass: 0 lines@superclass;;front handler: 0 lines@one handler"
Two page controllers share one block of six lines. Move them into a superclass, and the copies drop to zero. Move them into one handler, and it's zero too.

@words text="One config · dynamic commands · fresh command · decorators"
So the count can't choose. Fowler's real reasons are one configuration, dynamic commands, a fresh command per request, and decorators.

@end text="Full lesson on Learn"
The full lesson, with a lab that finds the copies, is on Learn.

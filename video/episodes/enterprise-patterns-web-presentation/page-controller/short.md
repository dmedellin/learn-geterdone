---
format: short
lesson: enterprise-patterns-web-presentation/page-controller
title: Moving a decision out doesn't remove it
---

@art branching-controller
Your controller went from five decision points to one. Where did the other four go?

@math items="concert-page: 1 + if 3 + && 1 = 5@five decision points;;concert-page-split: 1@just one"
A page controller that picks one of four views has five decision points. Move the choice of view to a helper, and the controller has just one.

@art helper-split
The four branches moved to the helper. The gain is a place to test them, with no request and no web server.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts them, is on Learn.

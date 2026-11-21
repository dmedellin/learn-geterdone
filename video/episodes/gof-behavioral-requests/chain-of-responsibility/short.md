---
format: short
lesson: gof-behavioral-requests/chain-of-responsibility
title: Who takes the request?
---

@art chain-click-help
You click for help on a button. Who should answer it?

@art chain-handlers
Line up everyone who might. Each one handles the request, or passes it to the next. The sender only knows the first.

@words text="Rewire, don't rewrite."
That's Chain of Responsibility. Add a handler, or reorder them, without touching the sender.

@art chain-falls-off
The catch? Nobody has to take it. A request can fall off the end, unhandled.

@end text="Full lesson on Learn"
The full lesson, with a lab to run the chain, is on Learn.

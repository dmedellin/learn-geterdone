---
format: short
lesson: code-complete-system-considerations/programming-tools
title: Why editing one header rebuilds everything
---

@art header-ripple
You changed one header. Why did the whole program rebuild?

@code block=1 lines=1-3 label=make focus="2-3@main dot o and util dot o|1@app"
Both main dot o and util dot o list util dot h, so both are remade. And app is linked from both, so it's remade too.

@words text="A build redoes what depends on the change"
A build tool doesn't rebuild what you edited. It rebuilds everything that depends on it, through every chain.

@end text="Full lesson on Learn"
The full lesson, with a build lab, is on Learn.

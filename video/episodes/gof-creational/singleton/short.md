---
format: short
lesson: gof-creational/singleton
title: Why a global variable isn't a singleton
---

@art global-vs-singleton
A global variable makes one object easy to reach. It doesn't stop anyone making a second.

@code block=1 lines=2-14 focus="5@hides its constructor|9-14@first time"
A singleton hides its constructor, keeps its one instance itself, and makes it the first time anyone asks.

@math items="fresh: 5 × 50 = 250@five requests;;lazy: 50@made once"
In the lesson's locker network, five requests making their own registry cost two hundred and fifty. Made once and shared, fifty.

@end text="Full lesson on Learn"
The full lesson, and the costs the book admits, is on Learn.

---
format: short
lesson: availability-and-failure/correlated-failure
title: A one in a thousand shared failure makes your pair eleven times worse
---

@art shared-cause
Your two replicas share a rack. That one fact can wipe out most of what the second machine bought you.

@math items="independent:  p² = 0.0001@independently;;c = 1/1000:  0.0010999@one in a thousand"
Each is down a hundredth of the time, so independently they're both down one time in ten thousand. Add a one in a thousand chance of an event that takes both, and it's eleven times worse.

@words text="Another replica doesn't touch c" sub="separate the failure domains"
Another replica in that rack won't help. Moving one to another rack will.

@end text="Full lesson on Learn"
The full lesson, with the common cause to move, is on Learn.

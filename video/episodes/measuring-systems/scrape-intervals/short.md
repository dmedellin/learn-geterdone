---
format: short
lesson: measuring-systems/scrape-intervals
title: A 14 second outage your graph will never show
---

@art spike-between
Scrape every fifteen seconds, and a fourteen second outage can vanish completely.

@math items="P(caught) = min(1, d/I)@d over I;;3 s spike,  15 s interval:  1/5@one time in five"
A gauge is read at instants. A spike is caught only if a read lands inside it, with chance d over I. A three second spike at a fifteen second interval is seen one time in five.

@words text="A flat graph is a fact about the reads"
Not about your system.

@end text="Full lesson on Learn"
The full lesson, with counter resets too, is on Learn.

---
format: short
lesson: availability-and-failure/retries-and-request-amplification
title: Your retry policy triples your load on the worst day
---

@art cost-and-benefit
Two retries cost you eleven percent extra load. Until the day they cost you a hundred and seventy one.

@math items="p = 0.1:  1.11 attempts · 99.9% success@ten percent;;p = 0.9:  2.71 attempts · 27.1% success@ninety percent"
At a ten percent failure rate, two retries mean one point one one attempts per request. At ninety percent, two point seven one, and only twenty seven percent succeed.

@words text="Most expensive when least useful"
Retries are cheapest when you don't need them.

@end text="Full lesson on Learn"
The full lesson, with the failure rate to drag, is on Learn.

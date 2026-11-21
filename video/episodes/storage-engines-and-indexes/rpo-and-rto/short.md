---
format: short
lesson: storage-engines-and-indexes/rpo-and-rto
title: The restore time no backup schedule can shorten
---

@art floor-line
Back up every hour instead of every day. Your restore still can't beat this floor.

@math items="copy = 2.00 TB / 200 MB/s = 2.78 h@two point seven eight;;24 h interval:  RTO 12.38 h@daily;;1 h interval:  RTO 3.18 h@hourly"
Copying two terabytes back at two hundred megabytes a second takes two point seven eight hours. A shorter interval cuts the log to replay. Daily, recovery is twelve point three eight hours. Hourly, three point one eight.

@words text="The copy is the floor"
Below that, it's about bandwidth.

@end text="Full lesson on Learn"
The full lesson, with the target run backwards, is on Learn.

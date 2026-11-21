---
format: long
lesson: storage-engines-and-indexes/rpo-and-rto
title: We have backups is not an answer: RPO and RTO
thumb: Bytes lost, hours down
---

@chapter Two questions, two units
@title text="RPO and RTO" sub="Storage Engines and Indexes" art=thumb
Ask a team how they'd recover from losing a database, and you'll often hear, we have backups. That's not a number of bytes, and it's not a number of hours. So it doesn't answer either of the two real questions.

@list heading="Two objectives" items="RPO: how much is lost, in bytes@how much work is lost|RTO: how long you're down, in hours@how long you're down"
The recovery point objective asks how much work is lost, measured in bytes. The recovery time objective asks how long you're down, measured in hours. They're controlled by different things. The first by the schedule, the second by bandwidth.

@chapter Bytes at risk
@art interval-at-risk
A failure loses whatever was written since the last backup. The worst case is a failure just before the next one, a whole interval of writes.

@math heading="Daily backup,  20 MB/s of writes" items="RPO worst = 86 400 s × 20 MB/s = 1.73 TB@one point seven three;;RPO expected = 864.00 GB@eight hundred and sixty four"
A day is eighty six thousand four hundred seconds. At twenty megabytes a second, that's one point seven three terabytes at risk. A failure at a random moment loses half that on average, eight hundred and sixty four gigabytes.

@art expected-half
Keep both. The worst case is what a commitment has to survive. The expected case is what you'll typically pay. Put the expected figure in a contract and you understate the exposure by two.

@chapter Hours to be back
@math heading="2.00 TB,  restore 200 MB/s,  replay 50 MB/s" items="copy = 2.00 TB / 200 MB/s = 10 000 s = 2.78 h@two point seven eight;;replay = 1.73 TB / 50 MB/s = 34 560 s = 9.60 h@nine point six;;RTO = 2.78 + 9.60 = 12.38 h@twelve point three eight"
Recovery time is two parts. Copy two terabytes back at two hundred megabytes a second, and that's ten thousand seconds, two point seven eight hours. Then replay the surviving log, one point seven three terabytes at fifty megabytes a second, nine point six hours. Twelve point three eight hours in all.

@art copy-and-replay
Look at what dominates. Most of the outage is replaying a day of log, not copying. So the fastest lever here is the backup interval, not the restore path. Leave the replay out, and you've quoted the smaller term.

@chapter A shorter interval
@math heading="Four intervals" items="1 h:  72.00 GB,  RTO 3.18 h@one hour;;6 h:  432.00 GB,  RTO 5.18 h@six hours;;12 h:  864.00 GB,  RTO 7.58 h@twelve hours;;24 h:  1.73 TB,  RTO 12.38 h@twenty four"
A shorter interval buys twice. One hour gives seventy two gigabytes at risk and a recovery of three point one eight hours. Six hours, four hundred and thirty two gigabytes and five point one eight. Twelve hours, eight hundred and sixty four and seven point five eight. Twenty four, one point seven three terabytes and twelve point three eight.

@art floor-line
But the copy never moves. Two point seven eight hours sits under every row. No backup schedule makes a restore faster than moving the data. An aggressive recovery target is really a statement about bandwidth and dataset size.

@art rto-line
So recovery time is a straight line in the interval, starting at that floor. Past an hourly backup, more frequent backups buy almost nothing.

@chapter Run it backwards
@math heading="Target: RTO ≤ 4 h" items="4 h − 2.78 h = 1.22 h of replay@one point two two;;1.22 h × 50 MB/s ≈ 220 GB of log@two hundred and twenty;;220 GB / 20 MB/s  →  interval ≤ 3.06 h@three point oh six"
Turn a target into a schedule. A four hour target leaves one point two two hours for replay. At fifty megabytes a second, that's about two hundred and twenty gigabytes of log. At twenty megabytes a second of writes, that's three point oh six hours. So back up at least every three hours.

@art untested-restore
And if the copy alone took more than four hours, no schedule could reach it. One caveat. Restore bandwidth has to be measured on a real restore. A backup that's never been restored is a forecast. And real outages also include detection and the decision to restore.

@chapter Where people slip
@list heading="Common slips" items="Offering “we have backups” as an answer@The first|Mixing worst case and expected loss@The second|Leaving out the log replay@the third"
The first slip is offering we have backups as a recovery claim. The second is quoting the worst case and the expected loss as if they were one number. And the third is leaving the log replay out of the recovery time.

@chapter Try it
@words text="Daily backup,  restore 400 MB/s" sub="first move: copy falls to 1.39 h"
Your turn. Keep the daily schedule and double the restore bandwidth to four hundred. The copy falls to one point three nine hours. Work out the new recovery time, then what a four hour target allows as an interval, and why that moved so much further.

@end text="Bytes lost, hours down"
You can move the interval and the bandwidth and watch both objectives, on Learn. That's learn dot get er done dot I O.

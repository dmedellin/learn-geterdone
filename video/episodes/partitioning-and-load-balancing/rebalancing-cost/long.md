---
format: long
lesson: partitioning-and-load-balancing/rebalancing-cost
title: Rebalancing: the seventeen hours nobody prices properly
thumb: Hours, and the latency during
---

@chapter What a rebalance is
@title text="Rebalancing Cost" sub="Partitioning and Load Balancing" art=thumb
Every structural change to a partitioned system ends the same way. Some data has to move. How long does that take, and what happens to the fleet while it does?

@art data-moving
A rebalance moves a fraction m of the stored data between nodes. Maybe the shard count changed, a node was added or lost, or the placement got uneven. The throttle, B, is the bandwidth the copy is allowed to use. It's a deliberate limit, because the node has other work to do.

@chapter The window
@math heading="m = 25%,  D = 48 TB,  B = 200 MB/s" items="bytes = 0.25 × 48 TB = 12.00 TB@twelve terabytes;;duration = 12 × 10¹² / (200 × 10⁶)@two hundred times ten;;= 60 000 s = 16 h 40 min@sixty thousand seconds"
Move a quarter of forty eight terabytes, and that's twelve terabytes. At two hundred megabytes a second, divide twelve times ten to the twelve by two hundred times ten to the six. That's sixty thousand seconds, sixteen hours and forty minutes.

@chapter The fleet while it moves
@art budget-split
That isn't idle time. Each node has a transfer budget, say eight hundred megabytes a second, and the copy is holding two hundred of it, a quarter. Whatever the copy takes isn't available for serving requests.

@math heading="λ = 5 000 /s,  μ = 8 000 /s" items="service during = 8 000 × 3/4 = 6 000 /s@six thousand;;ρ before = 5 000/8 000 = 62.50%@sixty two and a half;;ρ during = 5 000/6 000 = 83.33%@eighty three point three three"
So a node that served eight thousand requests a second now serves six thousand. Arrivals are still five thousand. Utilisation goes from sixty two and a half percent to eighty three point three three percent, and stays there until the copy finishes.

@math heading="M/M/1 wait,  W = 1/(μ − λ)" items="before = 1/(8 000 − 5 000) = 0.333 ms@point three three three;;during = 1/(6 000 − 5 000) = 1.000 ms@one millisecond;;3.00×@three times"
And the queueing wait. Before, one over three thousand, point three three three milliseconds. During, one over a thousand, one millisecond. Three times the wait.

@art knee-curve
Why does a twenty one point rise in utilisation triple the wait? That's the knee. Response time rises without bound as utilisation approaches one, so equal steps in utilisation aren't equal steps in latency. A rebalance is a decision to sit further up that curve for a measured number of hours.

@chapter Turning the throttle
@art throttle-trade
The throttle moves the two costs in opposite directions. At fifty megabytes a second, the move takes two days, eighteen hours and forty minutes, at sixty six point six seven percent. At two hundred, sixteen hours forty, at eighty three point three three.

@art overflow-queue
Now try four hundred, to halve the window to eight hours twenty. The copy takes half the budget, so the node serves four thousand a second against five thousand arriving. That isn't slower. It's a queue that grows for as long as the copy runs. The throttle's ceiling is set by the workload, not the network.

@art utilisation-gauge
So say it properly. Not about seventeen hours. Say, for sixteen hours and forty minutes, every node runs at eighty three point three three percent with three times the wait. That's the sentence to check against a latency objective.

@chapter Where m comes from
@math heading="Growing 7 shards to 8, 48 TB at 200 MB/s" items="mod N moves 7/8 = 42 TB:  2 d 10 h 20 min@forty two terabytes;;ring moves 1/8 = 6 TB:  8 h 20 min@six terabytes"
The fraction m comes from the design. Growing seven shards to eight under mod N moves seven eighths, forty two terabytes, which at two hundred megabytes a second is two days, ten hours and twenty minutes. On a ring, one eighth, six terabytes, eight hours twenty.

@words text="7/8 + 1/8 = 1" sub="counted in days of elevated latency"
So the identity from rehashing is, in the end, a statement about how many days of elevated latency a growth step costs.

@chapter Where people slip
@list heading="Common slips" items="Reporting the duration, not the utilisation@The first|Raising the throttle without checking ρ@The second|Taking the moved fraction as 1/N@the third"
The first slip is reporting the duration and not the utilisation. The second is raising the throttle to shorten the window without checking utilisation. And the third is taking the moved fraction as one over N out of habit.

@chapter Try it
@words text="D = 96 TB" sub="first move: 24.00 TB to move"
Your turn. Keep everything else and take the dataset to ninety six terabytes. That's twenty four terabytes to move. Work out the duration at two hundred megabytes a second, say what happens to utilisation during the move, then find the throttle that brings the window back to sixteen hours forty, and whether it's usable.

@end text="Price the window and the load"
You can move the throttle and watch the window and the utilisation trade, on Learn. That's learn dot get er done dot I O.

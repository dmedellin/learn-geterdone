---
format: long
lesson: replication-and-consistency/replication-lag-and-stale-reads
title: Replication lag: why waiting the average still gives stale reads
thumb: Wait the mean, one in five stale
---

@chapter The question
@title text="Replication Lag and Stale Reads" sub="Replication and Consistency" art=thumb
You write to the leader, then read from a follower. How long should you wait to be sure the read sees the write? The average lag sounds like a safe answer. At the average, one read in five is still wrong.

@art lag-gap
Replication lag is the delay between a write committing on the leader and becoming visible on a follower. A read of that follower is stale if it returns the value from before the write.

@chapter A tail, and nothing else
@math heading="Stale at delay t" items="stale  ⟺  lag > t@exactly when;;P(stale at t) = P(lag > t)@the probability"
A read issued t after the write is stale exactly when the lag exceeds t. So the probability of a stale read is the probability that the lag is more than t. A tail, and nothing else.

@art long-tail
And lag isn't a constant. It's a distribution with a long right tail, made by whatever the follower is occasionally busy with. A compaction. A slow disk. A network hiccup. A burst of writes it's still applying.

@chapter A measured lag
@list heading="Lag (ms : weight of 1000)" items="10 : 500@ten milliseconds|25 : 300@twenty five|50 : 120@fifty|120 : 60 · 250 : 15 · 400 : 5@a hundred and twenty"
Here's a day of measured lag. Half the time it's ten milliseconds. Three hundred in a thousand, twenty five. A hundred and twenty, fifty milliseconds. Then sixty at a hundred and twenty, fifteen at two fifty, and five at four hundred.

@math heading="The tail past each delay" items="P(lag > 10) = 1/2@past ten;;P(lag > 25) = 1/5@past twenty five;;P(lag > 50) = 2/25 = 8%@past fifty;;P(lag > 250) = 1/200@two fifty"
Every figure is a sum of weights over a thousand. Past ten milliseconds, a half. Past twenty five, a fifth. Past fifty, two twenty fifths, eight percent. Past two fifty, one in two hundred. No model, no fitting. Just a column of the table.

@chapter Why the mean fails
@math heading="The mean lag" items="(10·500 + 25·300 + 50·120 + 120·60 + 250·15 + 400·5)/1000@the mean;;= 31 450/1000 = 629/20 = 31.45 ms@thirty one point four five;;P(lag > 31.45) = 200/1000 = 1/5@two hundred parts"
Weight each lag and add them up, and the mean is thirty one thousand four hundred and fifty over a thousand, thirty one point four five milliseconds. But the mass above that is two hundred parts in a thousand. Wait for the mean, and one read in five is stale.

@art balance-point
A mean is a balance point, not a deadline. Half the mass sits at ten milliseconds and pulls the average down, while the hundred and twenty, two fifty and four hundred millisecond events, the ones that cause complaints, sit far above it. Ninety nine percent fresh needs two fifty, eight times the mean.

@chapter What eight percent costs
@math heading="12 000 follower reads a second" items="12 000 × 2/25 = 960 stale reads/s@nine hundred and sixty"
At twelve thousand follower reads a second and a fifty millisecond delay, that's twelve thousand times two twenty fifths, nine hundred and sixty stale reads every second. It's not intermittent. It's eight percent, all day.

@chapter Two guarantees
@art read-your-writes
Two named guarantees fail on exactly this mass. Read your writes says a client that wrote sees its own write. It fails when that client's next read lands on a follower still in the tail.

@art monotonic
Monotonic reads says time never goes backwards for a client. It fails when a client moves from a caught up follower to a lagging one, and sees a value, then an older value, with no write in between. That's the incident nobody can reproduce.

@art version-wait
The repairs all make the read wait, or send it where the data is. Route a client's reads to the leader for a while after it writes. Pin a session to one follower. Or carry the write's version, and have the follower wait until it reaches it.

@chapter Where people slip
@list heading="Common slips" items="Using the mean lag as a freshness delay@The first|Quoting the probability without the read rate@The second|Assuming a stale read is the only failure@The third"
The first slip is using the mean lag as a freshness delay. The second is quoting the probability without the read rate. Eight percent sounds like rounding. Nine hundred and sixty a second doesn't. The third is assuming a stale read is the only failure, when monotonic reads breaks in the same tail.

@chapter Try it
@words text="delay = 120 ms" sub="12 000 reads/s"
Your turn. The team can't wait two hundred and fifty milliseconds and proposes a hundred and twenty. Read the tail past a hundred and twenty off the table, convert it to stale reads a second, and say which guarantee a user would report the failure as.

@end text="Pick a delay, read the tail"
You can set the read delay against a measured lag distribution and count the stale reads, on Learn. That's learn dot get er done dot I O.

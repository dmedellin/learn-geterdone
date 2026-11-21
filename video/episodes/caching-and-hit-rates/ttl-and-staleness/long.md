---
format: long
lesson: caching-and-hit-rates/ttl-and-staleness
title: TTL and staleness: what a shorter TTL really costs
thumb: Half the staleness, twice the misses
---

@chapter The question
@title text="TTL and Staleness" sub="Caching and Hit Rates" art=thumb
Your cache serves stale data, so somebody says, shorten the TTL. It's half of a good idea. The other half is a bill, and this video works out both.

@art ttl-window
A cache entry written at time t, with a time to live of T, is served until t plus T, then thrown away. If the real value changes inside that window, the entry is stale from the change until the window ends.

@words text="A TTL bounds staleness" sub="it never prevents it"
So a TTL doesn't keep data fresh. It caps how long it can be wrong. We cache for sixty seconds and we serve data up to sixty seconds wrong are the same sentence.

@chapter Two assumptions
@art two-clocks
To get a formula, assume the value updates every U seconds, and that the refresh lands at a time unrelated to the updates. That's a uniform phase. Neither is true of a real system, and the lesson keeps both visible.

@chapter Where the two branches come from
@math heading="G uniform on [0, U)" items="stale time = max(0, T − G)@stale for;;T ≤ U:  E = T²/(2U),  fraction = T/(2U)@shorter than;;T ≥ U:  E = T − U/2,  fraction = 1 − U/(2T)@longer;;T = U:  both give 1/2@both give a half"
Let G be the time from the start of a window to the next update. The entry is stale for T minus G, or zero. When the TTL is shorter than the update interval, the stale fraction averages to T over two U. When it's longer, it's one minus U over two T. At T equals U, both give a half.

@math heading="U = 60 s" items="T = 10 s:  10/120 = 1/12 = 8.33%@A ten second;;T = 30 s:  1/4 = 25.00%@thirty;;T = 60 s:  1/2 = 50.00%@sixty;;T = 120 s:  3/4 = 75.00%@a hundred and twenty"
Take a value that changes once a minute. A ten second TTL gives ten over a hundred and twenty, a twelfth, eight point three three percent. Thirty seconds gives a quarter. Sixty gives a half. And a hundred and twenty uses the other branch, three quarters.

@art stale-climb
So a TTL twice the update interval means three quarters of the time you're serving something wrong. Below U, staleness grows in a straight line. Above it, it climbs toward one and never quite gets there.

@chapter The other direction
@math heading="Miss rate of one key" items="one miss per key per TTL@expires once;;miss rate = 1/(λ_key·T)@one over"
Now shorten the TTL. A key read lambda key times a second expires once every T seconds, and one read in each window pays for the refill. So its miss rate is one over lambda key times T.

@art expiry-ticks
Short windows mean many refills, and long windows mean few. Once lambda key times T drops to one or less, the key expires between reads, and every read is a miss.

@math heading="5 reads a second" items="T = 10 s:  stale 1/12 · miss 1/50 = 2.00%@ten seconds;;T = 1 s:  stale 1/120 = 0.83% · miss 1/5 = 20.00%@one second;;T = 240 s:  stale 7/8 = 87.50% · miss 1/1200 = 0.08%@two hundred and forty"
At five reads a second and ten seconds, the stale fraction is a twelfth and the miss rate is one in fifty. Drop to one second, and staleness falls to a hundred and twentieth, but misses rise to one in five. At two hundred and forty seconds, it's seven eighths stale, and almost no misses.

@art seesaw
Every factor of ten you take off the staleness, you put back on the backend. A price display can be a minute wrong. A permission check can't be wrong, but it's read rarely, so a short TTL costs little. The formula prices both options in the same units.

@chapter One run versus the average
@art phase-runs
The formula is an expectation over the phase. Fix the phase at thirty percent of U, with sixty and ten seconds, and one run measures a thirtieth stale, not a twelfth. Average twenty four phases, and it lands back on a twelfth. Use it to compare TTLs, not to report last week.

@chapter Where people slip
@list heading="Common slips" items="Believing a shorter TTL fixes staleness for free@The first|Using the wrong branch@The second|Reading the formula as one run's prediction@The third"
The first slip is believing a shorter TTL fixes staleness for free. Quote both numbers. The second is using the wrong branch. At T equals two U, T over two U gives one, but the right answer is three quarters. The third is reading the formula as a prediction about a particular run.

@chapter Try it
@words text="U = 10 s · 200 reads/s · T = 60 s" sub="branch: 1 − U/(2T)"
Your turn. A key changes every ten seconds and is read two hundred times a second. With a sixty second TTL, use one minus U over two T. Find the stale fraction and miss rate, then a TTL under ten percent stale, and say which number this key can afford.

@end text="Move the TTL, watch both numbers"
You can drag the TTL and the phase and watch staleness and misses trade places, on Learn. That's learn dot get er done dot I O.

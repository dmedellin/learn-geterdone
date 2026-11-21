---
format: long
lesson: availability-and-failure/mtbf-and-mttr
title: MTBF and MTTR: why the machine that breaks more can be more available
thumb: Fix it faster
---

@chapter The question
@title text="MTBF and MTTR" sub="Availability and Failure" art=thumb
Two machines. One fails once a year. The other fails every hundred hours. Which would you rather run? By the end of this video, you'll probably pick the one that breaks eighty seven times as often.

@art run-repair-cycle
A machine's life is a cycle. It runs for a while, it fails, it's repaired, and it runs again. MTBF is the mean length of a working stretch. MTTR is the mean length of a repair.

@chapter The formula
@math heading="Steady-state availability" items="one cycle = MTBF + MTTR@One full cycle;;A = MTBF / (MTBF + MTTR)@the availability"
One full cycle lasts MTBF plus MTTR, and the service is up for MTBF of it. So the availability is MTBF over MTBF plus MTTR.

@art wear-curve
This course takes the failure rate as constant. A machine that's run for a year is no likelier to fail in the next hour than a new one. That's wrong for anything that wears out, but it's what lets MTBF be one number.

@chapter A worked example
@math heading="M = 1000 h, R = 60 min" items="A = 3 600 000 / 3 603 600 = 1000/1001@a thousand over;;= 99.90010%  ·  three nines@ninety nine point nine;;8 h 45 min 4.50 s down a year@eight hours"
A thousand hours between failures and an hour to repair gives a thousand over a thousand and one. That's ninety nine point nine oh oh one oh percent, three nines, and eight hours forty five minutes four and a half seconds down a year.

@chapter Two levers, one lever
@math heading="Halve R or double M" items="A(2M, R) = 2M/(2M + R)@double the time;;= M/(M + R/2) = A(M, R/2)@divide top and bottom"
Double the time between failures, and A is two M over two M plus R. Divide top and bottom by two, and it's M over M plus R over two. That's exactly what you get by halving the repair. It's an identity, true for any sizes.

@art equal-bars
So halve the repair to thirty minutes, and A becomes two thousand over two thousand and one. Double the time between failures instead, and it's two thousand over two thousand and one, to the digit. Which lever to pull is a question of cost, and faster repair is usually cheaper.

@chapter What a target demands
@math heading="Four nines, M = 1000 h" items="MTTR = M(1 − A)/A@rearrange;;= 3 600 000 × (1/10000) / (9999/10000)@three million six hundred thousand;;= 3 600 000/9999 = 360.036 s = 6 min 0.04 s@six minutes"
Rearrange and the target tells you the repair time it allows. MTTR is M times one minus A, over A. For four nines on a thousand hour machine, that's three million six hundred thousand over nine nine nine nine seconds. Six minutes, every time.

@art stopwatch
Stated that way, four nines is a claim about paging, automation and rollback, not hardware. The alternative, at the current one hour repair, is running nine thousand nine hundred and ninety nine hours between failures. That's a different and much slower project.

@chapter Why the unreliable machine wins
@math heading="Two machines" items="A: fails yearly, 1 day to fix  →  365/366 = 99.72678%@Machine A;;B: every 100 h, 6 min to fix  →  1000/1001 = 99.90010%@Machine B"
Machine A fails once a year and takes a day to fix. That's three sixty five over three sixty six, two nines, almost a full day down a year. Machine B fails every hundred hours, but is back in six minutes. A thousand over a thousand and one, three nines, eight hours forty five a year.

@art rare-vs-frequent
Machine B breaks eighty seven times as often and is down a third as long. Availability doesn't count failures. It counts seconds. And the user experiences seconds.

@chapter Where people slip
@list heading="Common slips" items="Reading an MTBF as one outage a year@The first|Mixing hours and minutes@The second|Treating reliability as the thing being bought@The third"
The first slip is reading an MTBF of a year as one outage a year. A mean isn't a schedule. The second is mixing units. A thousand and sixty with no units gives ninety four point three percent, wrong by over fifty times in the downtime. The third is treating reliability as the thing being bought.

@art unit-mixup
So convert both lifetimes to seconds before you divide, every time. And remember the cheaper half of the equation. Buying only reliability leaves the repair time untouched, and the user feels both.

@chapter Try it
@words text="MTBF = 730 h · target 99.99%" sub="1 − A falls tenfold; M doesn't move"
Your turn. A database fails once a month. Three nines needs every failure fixed in forty three minutes fifty seconds. Now ask for four nines. Find the required repair time. Then, at a repair time your team could actually hold, what MTBF would it demand?

@end text="Pull both levers yourself"
You can set the time between failures and the repair time and watch the two levers match, on Learn. That's learn dot get er done dot I O.

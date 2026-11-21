---
format: long
lesson: latency-and-the-tail/latency-is-not-throughput
title: Latency is not throughput: which one is your transfer paying?
thumb: A bigger pipe, the same distance
---

@chapter The question
@title text="Latency Is Not Throughput" sub="Latency and the Tail" art=thumb
Your page is slow, so you buy a faster link. And nothing changes. That's not bad luck. It's what happens when you mix up two different numbers.

@art pipe-length-width
Latency is how long one round trip takes. Bandwidth is how many bits a second the link carries once data is flowing. One is a duration, the other is a rate. A connection can be enormous and slow, or tiny and immediate.

@chapter The bandwidth-delay product
@math heading="100 Mbit/s, 80 ms round trip" items="100 Mbit/s = 10⁸ bit/s = 1.25 × 10⁷ B/s@a hundred megabits;;BDP = 1.25 × 10⁷ × 0.08 s@Multiply by eighty;;= 10⁶ B = 1 MB@one megabyte"
Multiply the two and you get the bandwidth delay product. A hundred megabits a second is ten to the eight bits, or one point two five times ten to the seven bytes, a second. Multiply by eighty milliseconds, and that's ten to the six bytes, one megabyte.

@art bytes-in-flight
A rate times a time is a quantity. So that megabyte is how much data can be on the wire at once, sent and not yet acknowledged. The link has a megabyte of road on it. And because it's in bytes, you can compare it directly with the size of a transfer.

@chapter Two terms
@math heading="Time for one transfer" items="t = RTT + size/bandwidth@one waiting term;;64 kB: send = 64 000 × 8 / (100 × 1000) = 5.12 ms@sixty four kilobytes;;t = 80 + 5.12 = 85.12 ms  (94.0% waiting)@eighty five point one two"
The time for a transfer is one round trip plus the size over the bandwidth: one waiting term and one sending term. Send sixty four kilobytes, and the sending term is five point one two milliseconds. So the total is eighty five point one two, and ninety four percent of it is waiting.

@art small-transfer
The sending term is the smaller number by a factor of more than fifteen. And it's the only one bandwidth touches. This transfer finishes long before the pipe is full.

@chapter Price both upgrades
@math heading="64 kB: which upgrade?" items="double bandwidth → saves 2.560 ms@double the bandwidth;;halve RTT → saves 40 ms@halve the round trip"
Now price both upgrades on that same transfer. Double the bandwidth, and the sending term halves, saving two point five six milliseconds. Halve the round trip instead, and you save forty. That's about sixteen times as much, and no amount of extra bandwidth closes that gap.

@art crossover
The two terms are equal at exactly one size, where the size over the bandwidth equals the round trip. Rearrange that and the size is bandwidth times round trip. It's the bandwidth delay product again. The BDP isn't just a capacity. It's the crossover.

@chapter The other side
@math heading="4 MB on the same link" items="send = 320 ms,  t = 400 ms  (20.0% waiting)@three hundred and twenty;;double bandwidth → saves 160 ms@doubling the link;;halve RTT → saves 40 ms@halving the round trip"
Now send four megabytes on the same link. It spends three hundred and twenty milliseconds sending and eighty waiting, four hundred in all. This one's past the crossover, so it's bandwidth bound. Doubling the link saves a hundred and sixty milliseconds, and halving the round trip saves forty.

@art same-forty
Notice that halving the round trip saves forty milliseconds in both cases. The round trip term doesn't know how big the payload is. That's why it dominates small transfers, and vanishes into the noise on large ones.

@chapter A faster link
@art wide-pipe-same-wait
Here's the misconception. A faster link doesn't lower the round trip. The round trip is set by how far the signal travels and how many devices it passes through. A page that makes four sequential requests over an eighty millisecond link can move to a gigabit connection and measure no change at all.

@words text="Shorten the distance, or remove a trip"
What does move the round trip is shortening the distance, or removing a trip altogether. The speed of light puts a hard floor under the first. The second is usually the one you can change.

@chapter Where people slip
@list heading="Common slips" items="One quality called speed@The first|Dividing by eight wrongly@The second|Thinking a faster link cuts the RTT@The third"
The first slip is treating bandwidth and latency as one quality called speed. The second is dividing by eight in the wrong direction, or not at all. A hundred megabits a second is twelve point five megabytes a second. And the third is assuming a faster link lowers the round trip.

@chapter Try it
@words text="20 Mbit/s · 200 ms round trip · 300 kB" sub="20 Mbit/s = 2.5 × 10⁶ B/s"
Your turn. A satellite hop: twenty megabits a second, a two hundred millisecond round trip. Twenty megabits is two point five times ten to the six bytes a second. Compute the bandwidth delay product, decide what a three hundred kilobyte transfer is bound by, and price both upgrades.

@end text="Find your side of the crossover"
You can change the size, the bandwidth and the round trip and watch which term wins, on Learn. That's learn dot get er done dot I O.

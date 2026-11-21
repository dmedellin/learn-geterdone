---
format: long
lesson: latency-and-the-tail/round-trips-not-bytes
title: Round trips, not bytes: count the conversation
thumb: Count the round trips
---

@chapter The question
@title text="Round Trips, Not Bytes" sub="Latency and the Tail" art=thumb
Your page is slow on first load, so someone proposes halving the HTML. It saves five point six milliseconds. Removing one handshake would save eighty. The question isn't how many bytes the response is. It's how many times the conversation went back and forth.

@art handshake-chain
A first connection pays for a DNS lookup, then a TCP handshake, then a TLS handshake, and then the request itself. None of them can start until the one before has finished. So they add.

@words text="k = sequential round trips" sub="only exchanges on the critical path"
The round trip count, k, is the number of exchanges that must complete in sequence before the response can begin to arrive. Work that happens in parallel with something else doesn't add to k.

@chapter The formula
@math heading="Time for a request" items="t = k·RTT + bytes/bandwidth@k times the round trip;;k = 1 DNS + 1 TCP + 2 TLS 1.2 + 1 request = 5@five"
The time is k times the round trip, plus the bytes over the bandwidth. Count the lab's preset: one for DNS, one for TCP, two for TLS one point two, and one for the request. That's five.

@math heading="80 ms round trip, 14 kB at 10 Mbit/s" items="TTFB = 5 × 80 = 400.0 ms@four hundred;;bytes = 14 000 × 8 / (10 × 1000) = 11.2 ms@eleven point two;;total = 411.2 ms@four hundred and eleven;;ratio = 400 / 11.2 = 35.7×@thirty five point seven"
At an eighty millisecond round trip, the time to first byte is four hundred milliseconds. Fourteen kilobytes at ten megabits a second costs eleven point two. The total is four hundred and eleven point two, and the round trips cost thirty five point seven times what the bytes do.

@art waiting-bar
That ratio settles the argument. Halving the HTML saves five point six milliseconds, about one and a third percent. Removing a single handshake saves eighty, or nineteen percent. And time to first byte isn't a share of the total. It's the delay before the total even starts.

@chapter The crossover payload
@art crossover-scale
So when do the bytes start to matter? There's one payload where the two sides balance exactly.

@math heading="When bytes equal round trips" items="bytes/bandwidth = k·RTT@the bytes cost;;crossover = k × bandwidth × RTT = 5 × 100 kB = 500 kB@five hundred kilobytes"
The bytes cost as much as the round trips when bytes over bandwidth equals k times the round trip. So the crossover payload is k times the bandwidth delay product. Here that's five times a hundred kilobytes, five hundred kilobytes. Fourteen kilobytes is a thirty fifth of the way there.

@art video-segment
A four megabyte video segment on the same connection is eight times past the crossover, and for that one the bytes are the whole story. At k equals one, the crossover is exactly the bandwidth delay product. It's one fact, counted once, then k times.

@chapter Warm connections
@list heading="What each costs" items="DNS: 1, or 0 once cached@DNS|TCP: 1, or 0 when reused@TCP|TLS: 2 in 1.2, 1 in 1.3, 0 resumed@TLS|Request: always 1@the request"
DNS costs one round trip, and zero once the answer is cached. TCP costs one, and zero when an open connection is reused. TLS costs two in version one point two, one in one point three, and zero on a resumed session. And the request is always one. It's the only one that carries your data.

@art cached-shortcuts
Every entry in that list except the last is overhead that a well configured client and server pay once, and then stop paying.

@math heading="The same request, warm" items="k = 1:  TTFB = 80 ms@k equals one;;total = 91.2 ms@ninety one point two;;saving 411.2 − 91.2 = 320 ms@three hundred and twenty"
Cache the DNS answer, reuse the connection, and only the request is left. k equals one. Time to first byte falls to eighty, and the total to ninety one point two. That's a saving of three hundred and twenty milliseconds, four round trips exactly, with nothing changed about the payload or the link.

@art first-and-second
That's why a site feels slow on the first page and fast on the second. And it's why the measurement to trust is the cold one.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the request is a round trip@The first|Counting messages, not exchanges@The second|Shaving bytes when round trips dominate@The third"
The first slip is forgetting that the request itself is a round trip. A warm connection still has to ask. The second is counting messages from a packet capture instead of sequential exchanges. And the third is optimising bytes when the ratio says round trips. Compute the ratio first, and let it choose the work.

@chapter Try it
@words text="150 ms · 5 Mbit/s · 40 kB · cold TLS 1.3, DNS uncached" sub="k = 1 + 1 + 1 + 1 = 4"
Your turn. A mobile connection, a hundred and fifty millisecond round trip, five megabits a second, a forty kilobyte JSON response, over a cold TLS one point three connection with no cached DNS. The count is four. Compute the time to first byte, the byte term, the total and the ratio.

@end text="Remove a round trip"
You can switch each handshake on and off and watch the time to first byte, on Learn. That's learn dot get er done dot I O.
